import django_tables2 as tables
from .models import Person,Test

class PersonTable(tables.Table):
    class Meta:
        model = Person
        model = Test
        template = 'django_tables2/bootstrap.html'
