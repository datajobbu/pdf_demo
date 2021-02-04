import xhtml2pdf.pisa as pisa

from io import BytesIO

from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template

from .models import Report 


def index(request):
    articles = Report.objects.order_by('code').values()
    context = {'articles': articles}
    return render(request, 'table.html', context)


def detail(request, code):
    article = Report.objects.filter(code=code).values()
    context = {'article': article}

    template = get_template('pdf.html')
    html = template.render(context)
    response = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), response)

    if not pdf.err:
        return HttpResponse(response.getvalue(), content_type='application/pdf')

    else:
        return HttpResponse("Error Rendering PDF", status=400)
    
    return render(request, 'pdf.html', context)