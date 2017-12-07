#! /usr/bin/env python
# -*- coding:utf-8 -*-

"""
File: app.py
Author: Johnson
Date: 2017-12-07 11:50
"""
import os
import urllib.request
import json
from datetime import datetime
import time
from wxpy import *
from wechat_sender import *

print('登录微信')
bot = Bot()
pid = os.fork()
if pid == 0:
    url = "http://flights.ctrip.com/domesticsearch/search/SearchFirstRouteFlights?DCity1=ZUH&ACity1=HRB&SearchType=S&DDate1=2017-12-24"
    req = urllib.request.Request(url)
    req.add_header(
        'Cookie', '_abtest_userid=5233fed8-9321-46d3-b5e9-a740129c1db4; _fpacid=09031074310985375271; GUID=09031074310985375271; DomesticUserHostCity=ZUH|%d6%e9%ba%a3; corpid=; corpname=; CtripUserInfo=VipGrade=0&UserName=&NoReadMessageCount=1&U=300EA3FA507AD43BBF95D8E9875BE7CD; AHeadUserInfo=VipGrade=0&UserName=&NoReadMessageCount=1&U=300EA3FA507AD43BBF95D8E9875BE7CD; Union=AllianceID=2549&SID=1274523&OUID=; Session=SmartLinkCode=U1274523&SmartLinkKeyWord=&SmartLinkQuary=&SmartLinkHost=&SmartLinkLanguage=zh; LoginStatus=1%7c; cticket=56DB214D66C7B179609756965DC1CD91B0BDF2888C4496A154251EE26E2C1D35; DUID=u=0A809E4AF31F947EACC37C8897FB04FE&v=0; IsNonUser=F; ticket_ctrip=uoeOwviAJ6VQEgTNwLuTqSV9j/bS+aOP3Riia1P+kyQbgkQZsD2giZETWT58uWhA+M5G0hccO37JNV8FE5BG6bmxYh1nYExx37RD4A046r3xPlLnX2XS8m26VMSagtHyjchFkMzWDTqK1OXjLo+tWDvCTTK2WfMTw9mi8CJvUjzRzPAnhEfkh+SKBDyf7eK4pwOF6yrK6Kd6wNmUpVS1ngVX8wvNzBfAKJaYCIENkJLmBfv2CRZ7biEX0u4zmCbyH0MKDNHWqT+yd9g2a6tQwu8fQxWoj6BP0uXTLwVT0NLjWkDYAfaJMA==; login_uid=FE5C5051829BC1324F2AB3201A6A49AE; login_type=0; login_cardType=0; FD_SearchHistorty={"type":"S","data":"S%24%u73E0%u6D77%28ZUH%29%24ZUH%242017-12-24%24%u54C8%u5C14%u6EE8%28HRB%29%24HRB"}; ASP.NET_SessionId=syo0gt0zqcxrnyok2nybedel; ASP.NET_SessionSvc=MTAuMTUuMTI4LjM3fDkwOTB8b3V5YW5nfHwxNTEwNzM5NzM2MDYw; appFloatCnt=14; _bfa=1.1494819956636.2upbci.1.1512605141488.1512615140033.33.188; page_time=1512605151600%2C1512605165044%2C1512605165271%2C1512605234574%2C1512605234895%2C1512605443003%2C1512605457829%2C1512605458076%2C1512605474312%2C1512605498310%2C1512605505175%2C1512605506796%2C1512605517235%2C1512605528418%2C1512605601167%2C1512605601396%2C1512605691960%2C1512605692201%2C1512605726681%2C1512605726917%2C1512605978658%2C1512606033463%2C1512606033711%2C1512615141451%2C1512615141702; _RF1=113.74.124.161; _RSG=XE4o4_DNruAxvelPIwLYW8; _RDG=28c175e90a300d2984185eb7138059405c; _RGUID=ae355cdf-c4c8-43a1-8822-57a499be8e7b; Mkt_UnionRecord=%5B%7B%22aid%22%3A%222549%22%2C%22timestamp%22%3A1512615143242%7D%5D; __zpspc=9.27.1512615143.1512615143.1%233%7Cwww.google.com%7C%7C%7C%7C%23; _jzqco=%7C%7C%7C%7C1512023648268%7C1.531103271.1494819958489.1512606035232.1512615143287.1512606035232.1512615143287.undefined.0.0.108.108; MKT_Pagesource=PC; _bfi=p1%3D101027%26p2%3D101027%26v1%3D188%26v2%3D187')
    while True:
        print('获取数据')
        with urllib.request.urlopen(req) as url:
            print('获取数据成功')
            data = json.loads(url.read().decode('gbk'))
            for t in data['tf']:
                if t['Routes'][0]['tcn'] == '西安':
                    Sender().send(datetime.now().strftime( "%H:%M") + ' 价格%d元' % t['p'])
                    break
        time.sleep(3)
else:
    listen(bot)
