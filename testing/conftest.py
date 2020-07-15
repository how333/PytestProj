#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import yaml


def pytest_addoption(parser):
    mygroup = parser.getgroup('hogwarts')
    mygroup.addoption("--env",
                      default='test',
                      dest='env',
                      help='set your run env'
                      )


@pytest.fixture(scope='session')
def cmdoption(request):
    datapath = ''
    myenv = request.config.getoption('--env', default='test')
    if myenv == 'test':
        datapath = 'datas/test/data.yml'

    if myenv == 'dev':
        datapath = 'datas/dev/data.yml'

    if myenv == 'st':
        datapath = 'datas/st/data.yml'

    with open(datapath) as f:
        datas = yaml.safe_load(f)

    return myenv, datas


@pytest.fixture(scope='function', autouse=True)
def addconf():
    print('开始计算')
    yield
    print('\n计算结束')
