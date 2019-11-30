#!/usr/bin/env python
# encoding: utf-8

import time
import random
import string
import requests
import contextlib

import ssl

ssl._create_default_https_context = ssl._create_unverified_context


def get_random_only_letter(k):
    return ''.join(random.choices(string.ascii_letters, k=k))


def get_random_str(k):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=k))


def request_get(url, params=None, headers={}, allow_redirects=True):
    try:
        with contextlib.closing(
                requests.get(url, params=params, headers=headers, timeout=30, allow_redirects=allow_redirects)) as req:
            data = req.json()
        # print("[{}]\nurl:{}\nparams:{}\nresult:{}".format(now(), url, json.dumps(params, ensure_ascii=False),
        #                                                   json.dumps(data, ensure_ascii=False)))
        return "succ", data
    except Exception as e:
        print(e)
        return "fail", {}


def request_get_content(url, params=None, headers={}, allow_redirects=True):
    try:
        with contextlib.closing(
                requests.get(url, params=params, headers=headers, timeout=30, allow_redirects=allow_redirects)) as req:
            data = req.content
        return "succ", data
    except Exception as e:
        print(e)
        return "fail", ""


def request_get_text(url, params=None, headers={}, allow_redirects=True):
    try:
        with contextlib.closing(
                requests.get(url, params=params, headers=headers, timeout=30, allow_redirects=allow_redirects)) as req:
            data = req.text
        return "succ", data
    except Exception as e:
        print(e)
        return "fail", ""


def request_post(url, data=None, files=None, headers={}):
    try:
        with contextlib.closing(requests.post(url, data=data, files=files, headers=headers, timeout=30)) as req:
            data = req.text
        return "succ", data
    except Exception as e:
        print(e)
        return "fail", {}


def filter_map(params):
    for k in list(params.keys()):
        if not params.get(k, ''):
            params.pop(k)


def now():
    '''
    获取当前时间
    :return: str 2019-10-13 12:00:00
    '''
    return time.strftime("%Y-%m-%d %X")
