# coding:utf-8
import zipfile

#创建压缩包
f=zipfile.ZipFile("abc.zip",mode="w")
f.write("x1.txt")
f.write("x2.txt")
f.close()

#如何进行解压缩
f=zipfile.ZipFile("zip_dir/abc.zip",mode="r")
#直接全部解压缩
f.extractall("zip_dir/abc")
#一个一个的解压缩
print(f.namelist())
for name in f.namelist():
    f.extract(name,"zip_dir/hehe")