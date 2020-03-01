#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-01-09 10:26:27
# @Author  : 崔立波 (baiyuexingchen@gmail.com)
# @Link    : https://github.com/Franklyn1987
# @Version : $Id$

import os
import tushare as ts
import pandas as pd
import requests
import numpy as np
import matplotlib.pyplot as plt
import time
import sys
import requests
import bs4
import csv
import datetime
from envelopes import Envelope
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

#########################################
from setuptools import setup
setup(
    name='build_folder',
    version='1.0',
    description='生成文件夹库',
    author='崔立波',
    author_email='cuilibo@gmail.com',
    url='https://github.com/Franklyn1987',
    py_modules=['build_folder'],
)
