#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib.func_txy import request_get
from lib.func_txy import request_post
from lib.func_txy import get_random_str


class TaoBao(object):
    def __init__(self, cookie):
        self.url = "https://s.taobao.com/image"
        self.cookie = cookie
        self._headers()

    def _headers(self):
        self.headers = {
            'Origin': "https://s.taobao.com",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:85.0) Gecko/20100101 Firefox/85.0",
            "Accept": "*/*",
            "Referer": "https://s.taobao.com",
            "cookie": self.cookie
        }

    def upload(self, filename):
        name = get_random_str(5)
        bytestream = open(filename, "rb").read()

        files = {
            "imgfile": (name, bytestream, 'image/jpeg')
        }

        status, res = request_post(self.url, files=files, headers=self.headers)
        return status, res

    def run(self,filename):
        pass


if __name__ == '__main__':
    cookie = """t=ec7d6e1b7c687aeb2c3a07f9d4c5756f; tfstk=c1gRBgVS7IC-HEObI0KcdVABgCRcZCJLh_whJCxBrdbMCjbOijuiWxZWVWNYjIC..; cna=ka+iGA2ZtHoCAd+mDTsyy1ty; isg=BC4udAm1wiH14DbFSRcaFKwDfILwL_IpH1tjUVj38jHsO8-VwLuiOZl99yfX-OpB; l=eBSSs3MnjMLluLkABOfaKurza77tlIObYuPzaNbMiOCPOafp5E2CW6g95X89Cn1VH6y2R3ryTLzHBvYRjP5-6NEUE3k_J_fi3dC..; sgcookie=E100LidiNBglA8K%2FSY3HVJ3jvKNUSXkbtdWCUenMwT6QEQvjKtZ%2FX7l6f4o%2FExOZqnymYciRgsb3ys%2FEhZLUj9lP%2BQ%3D%3D; uc3=lg2=UtASsssmOIJ0bQ%3D%3D&nk2=D8rzH4x218aIdKb0JwU%3D&id2=Uone8R3kdMWx%2BA%3D%3D&vt3=F8dCuASu8bi%2FEGqwsgs%3D; lgc=liukang1315548; uc4=id4=0%40UOE0C9w4vvLerT2nRGhTFGMNOoK5&nk4=0%40DenJvbcRU2AUYUs1%2BtUEYlrtVSvkm9VTQw%3D%3D; tracknick=liukang1315548; _cc_=URm48syIZQ%3D%3D; mt=ci=22_1; thw=cn; _m_h5_tk=07ea7280f32d9f0bb6749269092a2ae8_1614340052386; _m_h5_tk_enc=cbbc43b28f97537441a7d2ff4ee43008; uc1=cookie21=UIHiLt3xThH8t7YQoFNq&existShop=false&cookie15=WqG3DMC9VAQiUQ%3D%3D&cookie16=U%2BGCWk%2F74Mx5tgzv3dWpnhjPaQ%3D%3D&pas=0&cookie14=Uoe1hgVrOlbNpg%3D%3D; _tb_token_=36aa77075e5ee; xlly_s=1; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; cookie2=1647f1622fef40b9731cee6f169e010c; _samesite_flag_=true; unb=1851761146; csg=8b79ad64; cookie17=Uone8R3kdMWx%2BA%3D%3D; dnk=liukang1315548; skt=53aa49495c5bca18; existShop=MTYxNDMzMjI3Nw%3D%3D; _l_g_=Ug%3D%3D; sg=86f; _nk_=liukang1315548; cookie1=BvHRhuQY3RxrjUjxWd4SmiE8hsnjazyeAo5KJX2lrAQ%3D; enc=IKvtEmT%2BIGLHbirF3ChTkNweOHeYyH6IS48WVVXcHFzQqv2IuVV%2F6Jh5dCm4qjmkn%2FB%2BILhCNnh8PREyAvHX7A%3D%3D; JSESSIONID=C2A6D9014B1BB581A0A56ED54D895D6B; hng=CN%7Czh-CN%7CCNY%7C156"""
    filename = "../data/下载.jpeg"
    taobao = TaoBao(cookie)
    data = taobao.upload(filename)
    print(data)
