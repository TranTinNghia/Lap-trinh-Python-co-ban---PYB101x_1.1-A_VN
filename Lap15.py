import urllib.request
import json
import ssl
def tinh_tong_so_comment():
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    url_json = "http://py4e-data.dr-chuck.net/comments_1430672.json"
    url_json_read = urllib.request.urlopen(url_json, context = ctx).read()
    data_json = json.loads(url_json_read)
    sum_result = 0
    for i in data_json["comments"]:
        a = i["count"]
        sum_result = sum_result + int(a)
    return sum_result
print("Tổng của số comment toàn bộ User = " + str(tinh_tong_so_comment()))