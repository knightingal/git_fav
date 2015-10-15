import json
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
import django
from django.utils import timezone
django.setup()
from local1000site.models import PicRepertory, PicInstance

def main():
    fd = open("local1000site_picrepertory.json", 'r')
    rep_content = fd.read()
    fd.close()

    fd = open("local1000site_picinstance.json", 'r')
    instance_content = fd.read()
    fd.close()

    rep_obj_list = json.loads(rep_content)
    instance_obj = json.loads(instance_content)

    for rep_obj in rep_obj_list:
        rep_name = rep_obj["rep_name"]
        rep_id = rep_obj["id"]
        print rep_name
        filted_instance_obj = filter(lambda instance: instance['repertory_id'] == rep_id, instance_obj)
        pic_repertory = PicRepertory(rep_name=rep_name, pub_date=timezone.now())
        pic_repertory.save()

        pic_instance_list = []
        for instance in filted_instance_obj:
            pic_instance_list.append(PicInstance(pic_name=instance['pic_name'], repertory=pic_repertory))

        PicInstance.objects.bulk_create(pic_instance_list)


if __name__ == "__main__":
    main()