from django.core.mail import send_mail
from django.conf import settings

from django.shortcuts import render


from search.forms import SearchForm


def home(request):
    title = "Welcome"
    form = SearchForm(request.POST or None)

    context = {
        "title": title,
        "form": form
    }

    if form.is_valid():
        form.save()
        context = {
            "title": "Thank you",
        }

        subject = 'Search results for: ' + form.cleaned_data.get('searching_text')
        message = "For %s: search results" % subject
        from_email = settings.EMAIL_HOST_USER
        to_email = form.cleaned_data.get('email')
        send_mail(subject,
                  message,
                  from_email,
                  [to_email],
                  fail_silently=False)

        # mail.send(
        #     'pellia@ukr.net',  # List of email addresses also accepted
        #     'mybesttestmail@gmail.com',
        #     subject='My email',
        #     message='H1',
        # )

    return render(request, "home.html", context)
