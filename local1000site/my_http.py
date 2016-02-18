import sys
if sys.version_info.major == 3:
    import http.client as http_client
else:
    import httplib as http_client
import re


def parse_img_url(url):
    re_ret = re.search(r'^http://(.+?)(/.+)$', url)
    path = re_ret.group(2)
    re_ret = re.search(r'^.+/(.+)$', path)
    img_name = re_ret.group(1)
    return img_name


def parse_img_name(img_name):
    re_ret = re.search(r'^.+\.(.+)$', img_name)
    img_type = re_ret.group(1)
    return img_type

def download(url, dir):
    # http://www.baidu.com/201507/027/2.jpg
    # print "downloading " + url
    re_ret = re.search(r'^http://(.+?)(/.+)$', url)
    host = re_ret.group(1)
    path = re_ret.group(2)

    re_ret = re.search(r'^.+/(.+)$', path)
    img_name = re_ret.group(1)
    while True:
        # conn = http.client.HTTPConnection(host)
        conn = http_client.HTTPConnection(host)
        conn.request("GET", path, headers={
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Host": host,
            "Pragma": "no-cache",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:39.0) Gecko/20100101 Firefox/39.0",
        })

        resp = conn.getresponse()
        if resp.status == 200:
            img_content = resp.read()
            fp = open(dir + img_name, "wb")
            fp.write(img_content)
            fp.close()
            break
        # print "download " + url + " failed, try again"
    return img_name


def post_body_to_node(url, body):
    # url = "http://127.0.0.1:8081/navy/donwLoadNavy"
    re_ret = re.search(r'^http://(.+?)(/.+)$', url)
    host = re_ret.group(1)
    path = re_ret.group(2)

    conn = http_client.HTTPConnection(host)
    conn.request("POST", path, body=body, headers={
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "Host": host,
        "Pragma": "no-cache",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:39.0) Gecko/20100101 Firefox/39.0",
    })
    response = conn.getresponse()
    ret_body = response.read()
    conn.close()
    return ret_body


if __name__ == "__main__":
    download("http://www-file.huawei.com/~/media/CORPORATE/Images/home/small-banner/%E5%BE%90%E6%80%BB11-13.jpg", "./")


