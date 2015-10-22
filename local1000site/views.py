from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import PicRepertory, PicInstance
from django.shortcuts import get_object_or_404
from django.utils import timezone
from datetime import datetime, time
import json
import codecs
import http
import pdb
import os
# Create your views here.
def index(requeset):
    # return HttpResponse("this is local1000/index")
    pic_repertories = PicRepertory.objects.all()
    template = loader.get_template('local1000site/index.html')
    context = RequestContext(requeset, {
        'pic_repertories': pic_repertories,
    })
    return HttpResponse(template.render(context))

def pic_index_ajax(request):
    time_stamp = request.GET.get("time_stamp")
    if time_stamp is not None and time_stamp != "":
        dt_temp = datetime.strptime(time_stamp, "%Y-%m-%d %H:%M:%S")
        dt = datetime(dt_temp.year, dt_temp.month, dt_temp.day, dt_temp.hour, dt_temp.minute, dt_temp.second)
    else:
        dt = datetime(2000, 01, 01, 00, 00, 00)
    pic_repertories = PicRepertory.objects.filter(pub_date__gte=dt)
    pic_repertory_list = []
    for pic_repertory in pic_repertories:
        name = pic_repertory.rep_name
        mtime = pic_repertory.pub_date
        index = pic_repertory.id
        pic_repertory_list.append({"name": name, "mtime": str(mtime), "index": index})
    result_body = json.dumps(pic_repertory_list, ensure_ascii=False, indent=2)
    return HttpResponse(result_body)


def pic_content_ajax(request):
    rep_id = request.GET.get("id")
    r = get_object_or_404(PicRepertory, pk=rep_id)
    pic_instances = PicInstance.objects.filter(repertory=r)
    pic_names = []
    for pic_instance in pic_instances:
        pic_names.append(pic_instance.pic_name)

    result_obj = {
        "dirName": r.rep_name,
        "picpage": rep_id,
        "pics": pic_names,
    }
    result_body = json.dumps(result_obj, ensure_ascii=False, indent=2)
    return HttpResponse(result_body)

RootDir = 'D:/Python27/testdir/testsubdir/linux1000/'

def urls1000(request):
    request_body = request.body.decode('utf-8')
    request_obj = json.loads(request_body, 'uft-8')
    title = request_obj["title"]
    request_body_fmt = json.dumps(request_obj, ensure_ascii=False, indent=2)
    img_src_array = request_obj["imgSrcArray"]
    print img_src_array
    print request_body_fmt
    dir = RootDir + title + '/'
    os.mkdir(dir)
    pic_repertory = PicRepertory(rep_name=title, pub_date=timezone.now())
    pic_repertory.save()
    for url in img_src_array:
        img_name = http.download(url, dir)
        PicInstance(pic_name=img_name, repertory=pic_repertory).save()
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



