#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest

add_data = [
    (1, 2, 3),
    (1.1, 2.4, 3.5),
    (-2, -1, -3),
    (-2, 1, -1),
    (0, 3, 3)
]


@pytest.fixture(scope='function', params=add_data)
def addconf(request):
    data = request.param
    print('开始计算')
    yield data
    print('\n计算结束')
