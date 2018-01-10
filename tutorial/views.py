from django.shortcuts import render
from .models import Person,Test
from django_tables2 import RequestConfig
from .tables import PersonTable


def people(request):
    table = PersonTable(Person.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'people.html', {'table': table})
#   return render(request, 'people.html', {'people': Person.objects.all()})

def games(request):
    table = PersonTable(Test.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'games.html', {'table': table})


#    return render(request, 'games.html', {'games': Test.objects.all()})
