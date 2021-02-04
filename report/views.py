from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Report 


def index(request):
    articles = Report.objects.order_by('code').values()
    context = {'articles': articles}
    return render(request, 'table.html', context)