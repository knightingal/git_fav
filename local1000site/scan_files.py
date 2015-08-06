import os
import re
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
import django
from django.utils import timezone
django.setup()
from local1000site.models import PicRepertory, PicInstance

def main():
    for root, dirs, files in os.walk("D:/Python27/testdir/testsubdir/linux1000"):
        print root
        img_files = filter(lambda x: re.search(r'\.[j|J][p|P][g|G]|[p|P][n|N][g|G]$', x) is not None, files)
        if len(img_files) != 0:
            rep_name = unicode(re.split(r'[\\|/]', root)[-1], 'gbk')
            print rep_name
            pic_repertory = PicRepertory(rep_name=rep_name, pub_date=timezone.now())
            pic_repertory.save()
            for img_file in img_files:
                PicInstance(pic_name=img_file, repertory=pic_repertory).save()

if __name__ == "__main__":
    main()