from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import PicRepertory
import json
import codecs
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
    request_body = request.body.decode('utf-8')
    request_obj = json.loads(request_body, 'uft-8')
    title = request_obj["title"]
    request_body_fmt = json.dumps(request_obj, ensure_ascii=False, indent=2)
    print request_body_fmt
    # print title
    fp = codecs.open(title, 'w',  'utf-8')
    fp.write(title)
    fp.close()
    return HttpResponse("get urls1000")