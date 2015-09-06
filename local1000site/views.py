from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import PicRepertory, PicInstance
from django.shortcuts import get_object_or_404
import json
import codecs
import http
import pdb
# Create your views here.
def index(requeset):
    # return HttpResponse("this is local1000/index")
    pic_repertories = PicRepertory.objects.all()
    template = loader.get_template('local1000site/index.html')
    context = RequestContext(requeset, {
        'pic_repertories': pic_repertories,
    })
    return HttpResponse(template.render(context))

def urls1000(request):
    request_body = request.body.decode('utf-8')

    request_obj = json.loads(request_body, 'uft-8')
    # pdb.set_trace()

    title = request_obj["title"]
    request_body_fmt = json.dumps(request_obj, ensure_ascii=False, indent=2)
    img_src_array = request_obj["imgSrcArray"]
    print img_src_array
    print request_body_fmt
    for url in img_src_array:
        http.download(url)
    return HttpResponse("111")

def repertory(request, rep_id):
    r = get_object_or_404(PicRepertory, pk=rep_id)
    pic_instances = PicInstance.objects.filter(repertory=r)
    str_pic_instances = ""
    for pic_instance in pic_instances:
        str_pic_instances += str(pic_instance)
    template = loader.get_template('local1000site/repertory.html')
    context = RequestContext(request, {
        'pic_repertory': r,
        'pic_instances': pic_instances
    })
    return HttpResponse(template.render(context))



