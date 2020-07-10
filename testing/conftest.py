#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest


@pytest.fixture(autouse=True)
def calconf():
    print('开始计算')
    yield
    print('\n计算结束')
