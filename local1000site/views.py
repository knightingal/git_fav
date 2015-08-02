from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import PicRepertory
# Create your views here.
def index(requeset):
    # return HttpResponse("this is local1000/index")
    pic_repertories = PicRepertory.objects.all();
    template = loader.get_template('local1000site/index.html')
    context = RequestContext(requeset, {
        'pic_repertories': pic_repertories,
    })
    return HttpResponse(template.render(context))

def urls1000(request):
    print request.get_full_path()
    return HttpResponse("get urls1000")