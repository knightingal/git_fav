import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
from local1000site.models import PicRepertory, PicInstance

django.setup()


def main():
    pic_repertorise = PicRepertory.objects.all()
    for pic_repertory in pic_repertorise:
        print("process pic_repertory " + pic_repertory.rep_name)
        pic_instances = PicInstance.objects.filter(repertory=pic_repertory)
        pic_instance = pic_instances[0]
        pic_instance.is_cover = 1
        pic_instance.save()
        pic_repertory.cover = pic_instance.pic_name
        pic_repertory.save()


if __name__ == "__main__":
    main()
