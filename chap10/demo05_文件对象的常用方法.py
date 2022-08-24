# coding:utf-8
#file=open('a.txt','r')
#print(file.read(2))
#print(file.readline())
#print(file.readlines())

#file=open('a.txt','a')
#file.write('hello')
#lst=['java','python','c++']
#file.write(lst)


#file=open('a.txt','r')
#file.seek(2)
#print(file.read())
#print(file.tell())

file=open('a.txt','a')
file.write('hello')
file.flush()
file.write('world')
file.close()