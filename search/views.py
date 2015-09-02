from datetime import time, datetime
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone
from django.utils.timesince import timesince
from django.shortcuts import render
import logging
from django.utils.timezone import utc

from search.forms import SearchForm


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

        subject = 'Search results for: ' + form.cleaned_data.get('searching_text')
        message = "For %s: search results" % subject
        from_email = settings.EMAIL_HOST_USER
        to_email = form.cleaned_data.get('email')

        logging.basicConfig(format=u'%(levelname)-8s [%(asctime)s] %(message)s', level=logging.DEBUG,
                            filename=u'mylog.log')

        time_diff = datetime.now(timezone.utc) - instance.timestamp

        logging.info(time_diff.total_seconds())

        send_mail(subject,
                  message,
                  from_email,
                  [to_email],
                  fail_silently=False)
    return render(request, "home.html", context)


