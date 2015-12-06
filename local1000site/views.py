from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import PicRepertory, PicInstance, ShipRepertory, ShipPic
from django.shortcuts import get_object_or_404
from django.utils import timezone
from datetime import datetime
import json
import http
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
        dt_temp = datetime.strptime(time_stamp, "%Y%m%d%H%M%S")
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


def navy(request):
    request_body = request.body.decode('utf-8')
    request_obj = json.loads(request_body, 'uft-8')
    # request_body_fmt = json.dumps(request_obj, ensure_ascii=False, indent=2)
    # print request_obj

    title = request_obj["title"]
    dir_name = title.replace(' ', '_')
    ship_repertory = ShipRepertory(ship_name=title, dir_name=dir_name)
    ship_repertory.save()

    full_dir = RootDir + dir_name + '/'
    os.mkdir(full_dir)
    img_array = request_obj["imgArray"]
    ship_pic_list = []
    for img in img_array:
        pic_url = img["imrSrc"]
        pic_description = img["description"]
        pic_copyright = img["copyright"]
        ship = ship_repertory
        ship_pic_list.append(ShipPic(pic_name="",
                                     pic_url=pic_url, pic_description=pic_description, pic_copyright=pic_copyright,
                                     ship=ship))
        img_name = http.download(pic_url, dir)

    ShipPic.objects.bulk_create(ship_pic_list)

    return HttpResponse("111")


def urls1000(request):
    title = http.post_body_to_node(request.body)

    request_body = request.body.decode('utf-8')

    request_obj = json.loads(request_body, 'uft-8')
    # title = request_obj["title"]
    d = datetime.now()
    tz_now = timezone.now()
    # title = d.strftime('%Y%m%d%H%M%S') + title
    request_body_fmt = json.dumps(request_obj, ensure_ascii=False, indent=2)
    img_src_array = request_obj["imgSrcArray"]
    print img_src_array
    print request_body_fmt
    full_dir = RootDir + title + '/'
    # os.mkdir(full_dir)

    pic_instance_list = []
    for url in img_src_array:
        # img_name = http.download(url, dir)
        img_name = http.parse_img_name(url)
        pic_instance_list.append(PicInstance(pic_name=img_name))

    pic_repertory = PicRepertory(rep_name=title, pub_date=tz_now)
    pic_repertory.save()

    for pic_instance in pic_instance_list:
        pic_instance.repertory = pic_repertory

    PicInstance.objects.bulk_create(pic_instance_list)

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
