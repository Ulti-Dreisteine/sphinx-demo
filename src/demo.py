# -*- coding: utf-8 -*-
"""
Created on 2020/8/4 10:41 上午

@File: sphinx_demo.py

@Department: AI Lab, Rockontrol, Chengdu

@Author: luolei

@Email: dreisteine262@163.com

@Describe: Sphinx demo
"""

import logging

logging.basicConfig(level = logging.INFO)

import sys, os

sys.path.append('../')


class SphinxDemo():
    """类的功能说明"""

    def add(self,a,b):
        """两个数字相加，并返回结果"""
        return a + b

    def google_style(arg1, arg2):
        """函数功能.

        函数功能说明.

        Args:
            arg1 (int): arg1的参数说明
            arg2 (str): arg2的参数说明

        Returns:
            bool: 返回值说明

        """
        return True

    def numpy_style(arg1, arg2):
        """函数功能.

        函数功能说明.

        Parameters
        ----------
        arg1 : int
            arg1的参数说明
        arg2 : str
            arg2的参数说明

        Returns
        -------
        bool
            返回值说明

        """
        return True
    

def my_function(a, b):
    """函数功能说明

     >>> my_function(3, 2)
     6
     >>> my_function('a', 3)
     'aaa'

    """
    return a * b



