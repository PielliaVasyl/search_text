import datetime
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone

from django.shortcuts import render
import logging

from search.forms import SearchForm

from whoosh.index import open_dir
from whoosh.fields import *
from whoosh.qparser import QueryParser
from whoosh.collectors import TimeLimitCollector, TimeLimit


ix = open_dir("Whoosh_index")


def home(request):
    title = "Search text"
    form = SearchForm(request.POST or None)

    context = {
        "title": title,
        "form": form
    }

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()

        message = "You will get search results for: %s via %s soon" % (instance.searching_text, instance.email)
        context = {
            "title": "Thank you",
            "message": message,
        }

        with ix.searcher() as searcher:
            query = QueryParser("text", ix.schema).parse(instance.searching_text)
            # Get a collector object
            c = searcher.collector(limit=None)
            # Wrap it in a TimeLimitedCollector and set the time limit to 10 seconds
            tlc = TimeLimitCollector(c, timelimit=instance.t_limit)
            # Try searching
            try:
                searcher.search_with_collector(query, tlc)
            except TimeLimit:
                pass
            # You can still get partial results from the collector
            results = tlc.results()
            lst = []
            for i in range(0, len(results)):
                st = ''
                st += 'Book: '
                st += results[i]["book"]
                st += ', chapter: '
                st += results[i]["chapter"]
                st += ', page: '
                st += str(results[i]["page"])
                lst.append(st)



        # with ix.searcher() as searcher:
        #     query = QueryParser("text", ix.schema).parse(instance.searching_text)
        #     results = searcher.search(query)
        #     lst = []
        #     for i in range(0, len(results)):
        #         st = ''
        #         st += 'Book: '
        #         st += results[i]["book"]
        #         st += ', chapter: '
        #         st += results[i]["chapter"]
        #         st += ', page: '
        #         st += str(results[i]["page"])
        #         lst.append(st)

        logging.basicConfig(format=u'%(levelname)-8s [%(asctime)s] %(message)s', level=logging.DEBUG,
                            filename=u'mylog.log')
        time_diff = datetime.datetime.now(timezone.utc) - instance.timestamp
        logging.info(time_diff.total_seconds())

        subject = 'Search results for: ' + form.cleaned_data.get('searching_text')
        message = 'Search results for: ' + form.cleaned_data.get('searching_text') + '\n'
        for i in range(0, len(lst)):
            message += str(i+1)+') '
            message += lst[i]
            message += '\n'
        from_email = settings.EMAIL_HOST_USER
        to_email = form.cleaned_data.get('email')
        send_mail(subject,
                  message,
                  from_email,
                  [to_email],
                  fail_silently=True)
    return render(request, "home.html", context)


