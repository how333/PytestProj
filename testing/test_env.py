#!/usr/bin/env python
# -*- coding: utf-8 -*-


def test_env(cmdoption):
    print('测试环境验证')
    env, datas = cmdoption
    print(f'环境：{env}, 数据：{datas}')
    ip = datas['env']['ip']
    port = datas['env']['port']
    url = 'http://' + ip + ':' + str(port)
    print(url)
