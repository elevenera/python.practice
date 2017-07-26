# -*- coding: utf-8 -*-

#  参数变量argv，可以解包，获取用户输入

filename = raw_input(">")

txt = open(filename)  # 为txt变量赋值，用open（）函数实现

print "Here's your file %r:" % filename
print txt.read()   # txt变量后面加（.）执行命令，比如read（）函数就是直接读取文件
