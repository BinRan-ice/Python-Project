# coding:utf-8
import traceback
try:
    print('*'*50)
    print(10/0)
except:
    traceback.print_exc()