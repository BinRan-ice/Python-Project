# coding:utf-8
import shutil

#把dir/a.txt移动到dir2文件夹内
shutil.move("dir1/a.txt","dir2")

#复制两个文件句柄
f1=open("dir2/a.txt",mode="rb")
f2=open("dir1/b.txt",mode="wb")
shutil.copyfileobj(f1,f2)

#执行两个文件路径，进行文件复制
#复制文件的内容
shutil.copyfile("dir1/b.txt","dir1/c.txt")  #参数是文件路径

#复制文件内容+文件的权限一起进行复制
shutil.copy("dir1/b.txt","dir1/d.txt")

#复制文件内容+权限+修改时间
shutil.copy2("demo06_hashlib.py","dir1/f.py")

#修改时间，权限的复制，不复制内容
shutil.copystat("demo06_hashlib.py","dir1/b.txt")

#只拷贝权限
shutil.copymode(".","dir1/b.txt")

#复制文件夹
shutil.copytree("dir1","dir3")

#删除文件夹
shutil.rmtree("dir2")