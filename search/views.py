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
        with ix.searcher() as searcher:
            query = QueryParser("text", ix.schema).parse(instance.searching_text)
            results = searcher.search(query)
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

        message = "You will get search results for: %s via %s soon" % (instance.searching_text, instance.email)
        context = {
            "title": "Thank you",
            "message": message,
        }

        subject = 'Search results for: ' + form.cleaned_data.get('searching_text')
        message = 'Search results for: ' + form.cleaned_data.get('searching_text') + '\n'
        for i in range(0, len(lst)):
            message += str(i+1)+') '
            message += lst[i]
            message += '\n'
        logging.basicConfig(format=u'%(levelname)-8s [%(asctime)s] %(message)s', level=logging.DEBUG,
                            filename=u'mylog.log')
        time_diff = datetime.datetime.now(timezone.utc) - instance.timestamp
        logging.info(time_diff.total_seconds())

        from_email = settings.EMAIL_HOST_USER
        to_email = form.cleaned_data.get('email')

        send_mail(subject,
                  message,
                  from_email,
                  [to_email],
                  fail_silently=False)
    return render(request, "home.html", context)


