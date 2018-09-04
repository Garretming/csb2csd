#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: clark
"""
 
import os, re, plistlib
import sys
 
def parseArgument():
    argus = []
    for i in range(0,len(sys.argv)):
        #  print(sys.argv[i])
         argus.append(sys.argv[i])
    return argus

def traverse(f,l,n):
    fs = os.listdir(f)
    for f1 in fs:
        tmp_path = os.path.join(f,f1)
        if not os.path.isdir(tmp_path):
            # print('文件: %s'%tmp_path)
             # 文件名
            name = os.path.basename(tmp_path)
            # filename = re.match(r'(.*)\.csb$', name).group(1)
            # filename = re.search(r'(.*)\.csb$', tmp_path).group(1)
            # print('文件: %s'%name)
           
            if l==0:
                os.system('lua lily.lua '+ n +'/' + name)
            else:
                
                os.system('lua lily.lua '+'' + Lname +'/'+ n +'/' + name)
        else:
            # print('文件夹：%s'%tmp_path)
            fname = os.path.basename(tmp_path)
            # print('文件夹：%s'%fname)
            # print("l:%s"%l)
            if l==0:
                b = './out/'+ Lname +'/'+fname
                if  not os.path.exists(b):
                    # print("=======")
                    os.makedirs(b)

            traverse(tmp_path,l+1,fname)


             

 

def test(path):
    for fpathe,dirs,fs in os.walk(path):
        for f in fs:
            print(os.path.join(fpathe,f))


#             返回的是一个三元tupple(dirpath, dirnames, filenames),
# 其中第一个为起始路径，第二个为起始路径下的文件夹,第三个是起始路径下的文件。
# dirpath是一个string，代表目录的路径，
# dirnames是一个list，包含了dirpath下所有子目录的名字，
# filenames是一个list，包含了非目录文件的名字，这些名字不包含路径信息。如果需要得到全路径,需要使用 os.path.join(dirpath, name)。
Lname = ""
if __name__ == '__main__': 
    argus = parseArgument()
    # print(argus)
    path = os.getcwd() + "/" + argus[1]

   

    Lname = os.path.basename(path)
    
    a = './out/'+ Lname 
    if  not os.path.exists(a):
            os.makedirs(a)
    
    # print('文件夹 : %s'%name)
    traverse(path,0,Lname)
    # test(path)



