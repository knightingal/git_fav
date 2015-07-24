from django.http import HttpResponse
from .models import WebPage
import json
import codecs
def index(request):
    web_page_list = WebPage.objects.all()
    web_page_json_array = []
    for web_page in web_page_list:
        web_page_json_array.append({"page_name": web_page.page_name, "page_url": web_page.page_url})
    web_page_json = json.dumps(web_page_json_array, ensure_ascii=False, indent=2)
    print web_page_json
    fd = codecs.open("web_page.json", 'w', 'utf-8')
    fd.write(web_page_json)
    fd.close()
    return HttpResponse("Hello, world. You're at the polls index.\n" + web_page_json)