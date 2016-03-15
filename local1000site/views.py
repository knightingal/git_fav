from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import PicRepertory, PicInstance, ShipRepertory, ShipPic
from django.shortcuts import get_object_or_404
from django.utils import timezone
from datetime import datetime
import json
from .my_http import post_body_to_node, parse_img_url, parse_img_name


# Create your views here.
def index(request):
    pic_repertories = PicRepertory.objects.all()
    template = loader.get_template('local1000site/index.html')
    context = RequestContext(request, {
        'pic_repertories': pic_repertories,
    })
    return HttpResponse(template.render(context))


def pic_index_ajax(request):
    time_stamp = request.GET.get("time_stamp")
    if time_stamp is not None and time_stamp != "":
        dt_temp = datetime.strptime(time_stamp, "%Y%m%d%H%M%S")
        dt = datetime(dt_temp.year, dt_temp.month, dt_temp.day, dt_temp.hour, dt_temp.minute, dt_temp.second)
    else:
        dt = datetime(2000, 1, 1, 00, 00, 00)
    pic_repertories = PicRepertory.objects.filter(pub_date__gte=dt)
    pic_repertory_list = []
    for pic_repertory in pic_repertories:
        name = pic_repertory.rep_name
        mtime = pic_repertory.pub_date
        repertory_index = pic_repertory.id
        pic_repertory_list.append({"name": name, "mtime": str(mtime), "index": repertory_index})
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

    img_array = request_obj["imgArray"]
    ship_pic_list = []
    ship_pic_url_list = []
    i = 0
    for img in img_array:
        pic_url = img["imrSrc"]
        pic_description = img["description"]
        pic_copyright = img["copyright"]
        ship = ship_repertory
        pic_name = str(i) + '-' + parse_img_url(pic_url)
        pic_type = parse_img_name(pic_name)
        ship_pic_list.append(ShipPic(pic_name=pic_name, pic_type=pic_type,
                                     pic_url=pic_url, pic_description=pic_description, pic_copyright=pic_copyright,
                                     ship=ship))
        ship_pic_url_list.append(pic_url)
        i += 1

    ShipPic.objects.bulk_create(ship_pic_list)

    ship_info = {
        "name": dir_name,
        "ship_pic_url_list": ship_pic_url_list,
    }

    ship_info_json = json.dumps(ship_info, indent=2)
    print(ship_info_json)
    dir_name = post_body_to_node("http://127.0.0.1:8081/navy/donwLoadNavy", ship_info_json)

    ship_repertory.dir_name = dir_name
    ship_repertory.save()

    return HttpResponse("111")


def urls1000(request):
    title = post_body_to_node("http://127.0.0.1:8081/startDownload/", request.body)

    request_body = request.body.decode('utf-8')

    request_obj = json.loads(request_body, 'uft-8')
    tz_now = timezone.now()
    request_body_fmt = json.dumps(request_obj, ensure_ascii=False, indent=2)
    img_src_array = request_obj["imgSrcArray"]
    print(img_src_array)
    print(request_body_fmt)

    pic_instance_list = []
    for url in img_src_array:
        # img_name = http.download(url, dir)
        img_name = parse_img_url(url)
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
