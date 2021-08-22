from django.shortcuts import render
import datetime

# Create your views here.


def index(request):
    time = datetime.datetime.now()
    return render(request, "newyear/index.html", {
        # newyear is valiable
        "newyear": time.month == 1 and time.day == 1,
        "newYearTrue": True
    })
