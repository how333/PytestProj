#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 测试文件
import pytest
import sys

import yaml

sys.path.append('../')
from pythoncode.calc import Calculator

with open("datas/calc.yml") as f:
    datas = yaml.safe_load(f)
    # 取出加法测试数据
    add_data = datas['add']
    add_ids = add_data.keys()
    add_datas = add_data.values()
    # 取出减法测试数据
    dec_data = datas['dec']
    dec_ids = dec_data.keys()
    dec_datas = dec_data.values()
    # 取出除法测试数据
    div_data = datas['div']
    div_ids = div_data.keys()
    div_datas = div_data.values()
    # 取出乘法测试数据
    mcl_data = datas['mcl']
    mcl_ids = mcl_data.keys()
    mcl_datas = mcl_data.values()


# 计算器测试类
class TestCalc:

    def setup(self):
        self.cal = Calculator()

    # 加法测试方法
    @pytest.mark.add
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize('a, b, result', add_datas, ids=add_ids)
    def check_add(self, a, b, result):
        assert result == self.cal.add(a, b)

    # 减法测试方法
    @pytest.mark.dec
    @pytest.mark.run(order=2)
    @pytest.mark.dependency(depends=['check_add'])
    @pytest.mark.parametrize('a, b, result', dec_datas, ids=dec_ids)
    def check_dec(self, a, b, result):
        assert result == self.cal.dec(a, b)

    # 乘法测试方法
    @pytest.mark.mcl
    @pytest.mark.run(order=3)
    @pytest.mark.parametrize('a, b, result', mcl_datas, ids=mcl_ids)
    def check_mcl(self, a, b, result):
        assert result == self.cal.mcl(a, b)

    # 除法测试方法
    @pytest.mark.div
    @pytest.mark.run(order=4)
    @pytest.mark.dependency(depends=['check_mcl'])
    @pytest.mark.parametrize('a, b, result', div_datas, ids=div_ids)
    def check_div(self, a, b, result):
        assert result == self.cal.div(a, b)
