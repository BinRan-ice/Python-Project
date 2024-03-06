# coding:utf-8
#使用python向Excel中写入数据
import openpyxl
#创建工作簿对象
wb=openpyxl.Workbook()
#获取工作表sheet
sheet=wb.active
#获取指定的单元格
cell=sheet['A1']
#向单元格中写数据
cell.value="中国魅力"
#一次写入一行数据
lst=['姓名','年龄','成绩']
sheet.append(lst)
#向Excel文件中一次写入多行数据
lst2=[
    ["张三",22,90],
    ['李四',18,100],
    ["王五",19,70]
]
for low in lst2:
    sheet.append(low)
#保存
wb.save("文件/我的Excel文件.xlsx")