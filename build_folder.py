#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-10-09 14:45:57
# @Author  : 崔立波 (baiyuexingchen@gmail.com)
# @Link    : https://github.com/Franklyn1987
# @Version : $Id$

import os
import time
print("用于批量生成文件夹，build_folder(需要生成文件夹的名称文档.txt,生成的目录所在文件夹，True则同时生成txt注释文档)")
def build_folder(readtxt_path,folder_path,typee):
	path = folder_path 
	with open(readtxt_path, 'r', encoding='utf-8') as f:
	    l = []
	    for i in f.readlines():
	        if i != None:
	            l.append(i.replace("\n", ""))
	 
	# 创建l中所有名字的文件夹
	tyt=time.strftime('%Y-%m-%d', time.localtime(time.time()))
	for i in l:
		if i=="":
			break
		os.mkdir(path + '\\'+i)
		if typee==True:
			filename = i + ".txt"
			fp = open(path + '\\'+filename,'w')
			fp.write(str(tyt))
			fp.close()
			# print(i)
	 
	#创建l中所有名字的文件
	
	# for i in l:
	#     f = open(i + ".txt", 'a')
	#     f.write("")
	#     f.close()
# build_folder(r"D:\note.txt",r'D:\test',False)