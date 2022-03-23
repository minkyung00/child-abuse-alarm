from urllib.parse import unquote
import requests
from bs4 import BeautifulSoup

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
import django
django.setup()

from center.serializers import CenterAllSerializer

serviceKey = "6689d861c52a42458eb12ac3c601ce78"
serviceKeyDecoded = unquote(serviceKey, 'UTF-8')

def get_center_list(arcode):
    baseUrl = "http://api.childcare.go.kr/mediate/rest/cpmsapi021/cpmsapi021/request?key="
    url = baseUrl + serviceKey + '&arcode=' + arcode

    res = requests.get(url)
    xml = res.text
    soup = BeautifulSoup(xml, 'html.parser')

    result = []
    for tag in soup.find_all('item'):
        center_obj = {
            "name": tag.crname.text,
            "address": tag.craddr.text,
            "code": tag.stcode.text,
            "homepage": tag.crhome.text,
            "telephone": tag.crtel.text
        }

        result.append(center_obj)

    return result

if __name__=='__main__':
    arcode = ["11110", "11140", "11170", "11200", "11215", "11230", "11260", "11290", "11305", "11320", "11350", "11380", "11410", "11440", "11470", "11500", "11530", "11545", "11560", "11590", "11620", "11650", "11680", "11710", "11740"]
    for code in arcode:
        centers = get_center_list(code)
        for data in centers:
            serializer = CenterAllSerializer(data=data)
            if serializer.is_valid():
                serializer.save()