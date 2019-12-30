from django.shortcuts import render,redirect
from resumeapp.forms import resumeform
from django.http import HttpResponse
from resumeapp.models import resumedetails
from django.views.generic import view
from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa
# from reportlab.pdfgen import canvas  
# from django.http import HttpResponse  
# from django.template.loader import get_template

# Create your views here.
def resume(request):
    if request.method=='POST':
        form=resumeform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            # return redirect(success)
    else:
        form=resumeform
    return render(request,"resumeapp/resume.html",{'form':form})
def display(request):
    resumes=resumedetails.objects.all()
    return render(request,"resumeapp/display.html",{'form':resumes})


def render_to_pdf(template_src,context_dict={}):
    template=get_template(template_src)
    html=template.render(context_dict)
    result=BytesIO()
    pdf=pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")),result)
    if not pdf.error:
        return HttpResponse(result.getvalue(),context_dict='application/pdf')
        return None

class pdf(view):
    def get(self,request,*args,**kwargs):
        template=get_template('resumeapp/display.html')
        context={}
        html=template.render(context)
        pdf=render_to_pdf('resumeapp/display.html',context)
        if pdf:
            response=HttpResponse(pdf,content_type='application/pdf')
            filename = 'mypdf.pdf'
            content="inline;filename='%s'"%(filename)
            download=request.GET.get("download")
            if download:
                content="attachment;filename='%s'"%(filename)
            response['Content-Disposition']=content
            return response
        return HttpResponse("Not Found")


















# from django.core.files.storage import FileSystemStorage
# from django.http import HttpResponse, HttpResponseNotFound

# def pdf_view(request):
#     fs = FileSystemStorage()
#     filename = 'mypdf.pdf'
#     if fs.exists(filename):
#         with fs.open(filename) as pdf:
#             response = HttpResponse(pdf, content_type='application/pdf')
#             response['Content-Disposition'] = 'attachment; filename="mypdf.pdf"'
#             return response
#     else:
#         return HttpResponseNotFound('The requested pdf was not found in our server.')
  
# def write_pdf_view(request):
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'inline; filename="mypdf.pdf"'

#     buffer = BytesIO()
#     p = canvas.Canvas(buffer)

#     # Start writing the PDF here
#     p.drawString(100, 100, 'Hello world.')
#     # End writing

#     p.showPage()
#     p.save()

#     pdf = buffer.getvalue()
#     buffer.close()
#     response.write(pdf)

#     return response