# -*- coding: utf-8 -*-
# @Time : 2020/12/24
# @Author : handsomezhou
import hashlib
import os
import shutil
import zipfile
from pathlib import Path


# https://docs.python.org/3/library/pathlib.html
# https://docs.python.org/3/library/shutil.html

#如果不存在,父目录一起创建

import requests

from constant import WindowsProgramConstant, Constant
from util import TimeUtil


def mkdir(dir):
    return Path(dir).mkdir(mode=0o777, parents=True, exist_ok=True)

def exists(path):
    return Path(path).exists()

def is_dir(path):
    return Path(path).is_dir()

def is_file(path):
    return Path(path).is_file()

def remove(path):
    os.remove(path)
    return

#删除整个目录
def rmtree(dir_path):
    rm_tree_success = True
    try:
        shutil.rmtree(dir_path)

    except Exception as e:
        print(TimeUtil.getLogTime(),Constant.COLON,"异常",e)
        rm_tree_success = False

    return rm_tree_success

#复制整个目录,目标目录可以不存在
def copytree(src, dst):
    copy_tree_success=True
    try:
        shutil.copytree(src,dst, dirs_exist_ok=True)
    except Exception as e:
        print(TimeUtil.getLogTime(),Constant.COLON,"异常",e)
        copy_tree_success = False
    return copy_tree_success

# https://blog.csdn.net/u013546508/article/details/101014284
def download_file(dst,url):
    whole_dst_path = None;
    try:
        response = requests.get(url, stream=True)
        whole_dst_path= dst+"\\"+url.split('/')[-1]
        print("whole_dst_path",whole_dst_path)
        with open(whole_dst_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
        f.close()
    except Exception as e:
        print(TimeUtil.getLogTime(),Constant.COLON,"异常",e)
    return whole_dst_path


#https://pypi.org/project/unrar/
def extract(dst_dir,zfile):
    extract_success = True
    try:
        print("dst_dir",dst_dir)
        print("zfile",zfile)
        if zfile.endswith(WindowsProgramConstant.FULL_STOP_AND_ZIP_SUFFIX) is True:
            f = zipfile.ZipFile(os.path.join(dst_dir, zfile),'r')
            print("f.namelist() ",f.namelist())
            full_stop_and_zip_suffix_len=len(WindowsProgramConstant.FULL_STOP_AND_ZIP_SUFFIX)
            for file in f.namelist():
                f.extract(file,os.path.join(dst_dir, zfile[:-full_stop_and_zip_suffix_len]))

            f.close()
        else:
            print(TimeUtil.getLogTime(),Constant.COLON,"未支持格式")
            extract_success = False
    except Exception as e:
        extract_success = False
        print(TimeUtil.getLogTime(),Constant.COLON,"异常",e)

        return extract_success

# [Python 获取文件的MD5值](https://blog.csdn.net/zheng_ruiguo/article/details/88717711)
def get_md5(file):
    m = hashlib.md5()
    with open(file,'rb') as f:
        for line in f:
            m.update(line)
    md5code = m.hexdigest()
    #print(md5code)
    return md5code

def is_same_md5(src,dst):
    same_md5 = False
    if src is None:
        return same_md5

    if dst is None:
        return same_md5

    if str(src).lower()== str(dst).lower():
        same_md5 = True

    return same_md5

if __name__ == "__main__":

    whole_dst_path=r'C:\Soft\xxxx.exe'
    src=get_md5(whole_dst_path)
    dst="00CE7128D22B89796D4B0B0A3213A0b8"
    print("src",src)
    print("dst",dst)

    print("same_md5",is_same_md5(src,dst))


