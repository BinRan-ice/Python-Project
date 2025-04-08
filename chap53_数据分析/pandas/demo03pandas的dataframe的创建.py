# coding:utf-8
import numpy as np
import pandas as pd

#DataFrame二维，Series容器
t=pd.DataFrame(np.arange(12).reshape((3,4)),index=list("abc"),columns=list("WXYZ"))
print(t)

#DataFrame传入字典作为数据
d1={"name":["小明","小红"],"age":[20,32],"tel":[1086,10010]}
t2=pd.DataFrame(d1)
print(t2)

#DataFrame传入字典作为数据,空字段用NAN填充
d2=[{'name':'小明','age':23,'tel':10086},{'name':'小红','tel':10010},{'age':33,'tel':10000}]
t3=pd.DataFrame(d2)
print(t3)