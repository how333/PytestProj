#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 测试文件
import pytest
import sys

sys.path.append('../')
from pythoncode.calc import Calculator


# 计算器测试类
class TestCalc:
    def setup(self):
        self.cal = Calculator()

    # 加法测试方法
    @pytest.mark.add
    @pytest.mark.parametrize('a, b, result', [
        (1, 2, 3),
        (1.1, 2.4, 3.5),
        (-2, -1, -3),
        (-2, 1, -1),
        (0, 3, 3)
    ], ids=['int',
            'float',
            'negative',
            'negative&int',
            'zero'])
    def test_add(self, a, b, result):
        assert result == self.cal.add(a, b)

    # 减法测试方法
    @pytest.mark.dec
    @pytest.mark.parametrize('a, b, result', [
        (4, 2, 2),
        (2.5, 1.2, 1.3),
        (-2, -1, -1),
        (-2, 1, -3),
        (3, 0, 3)
    ], ids=['int',
            'float',
            'negative',
            'negative&int',
            'zero'])
    def test_dec(self, a, b, result):
        assert result == self.cal.dec(a, b)

    # 乘法测试方法
    @pytest.mark.mcl
    @pytest.mark.parametrize('a, b, result', [
        (2, 3, 6),
        (2.2, 1.2, 2.64),
        (-2, -3, 6),
        (3, -2, -6),
        (0, 4, 0)
    ], ids=['int',
            'float',
            'negative',
            'negative&int',
            'zero'])
    def test_mcl(self, a, b, result):
        assert result == self.cal.mcl(a, b)

    # 除法测试方法
    @pytest.mark.div
    @pytest.mark.parametrize('a, b, result', [
        (6, 3, 2),
        (2.64, 2.2, 1.2),
        (-6, -2, 3),
        (-6, 2, -3),
        (0, 4, 0)
    ], ids=['int',
            'float',
            'negative',
            'negative&int',
            'zero'])
    def test_div(self, a, b, result):
        assert result == self.cal.div(a, b)
