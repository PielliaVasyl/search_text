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

    return render(request, "home.html", context)
