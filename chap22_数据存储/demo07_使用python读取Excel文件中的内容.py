# coding:utf-8
#从Excel文件中读取数据
import  openpyxl
#加载Excel文件（创建一个python中的工作簿对象）
wb=openpyxl.load_workbook("文件/我的Excel文件.xlsx")
#获取工作表对象
#sheet=wb.active
sheet=wb["Sheet"]
#获取指定的单元格
cell=sheet['A1']
value=cell.value
print(value)
#获取一系列的格子
columns=sheet['A']
#print(columns)
for col in columns:     #获取A列中的每一个单元格
    print(col.value)    #获取A列中每一个单元格中的值
print("-------------------------------------------")
row=sheet[3]
for cell in row:    #获取第三行的每一个单元格
    print(cell.value)   #获取第三行的每一个单元格的值
print("===========================================")
cols=sheet["A:C"]
for col in cols:    #获取每一列
    for cell in col:    #获取每一列中的单元格
        print(cell.value)