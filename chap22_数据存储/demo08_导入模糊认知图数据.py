# coding:utf-8
import openpyxl
#创建工作簿对象
wb=openpyxl.Workbook()
#获取工作表sheet
sheet=wb.active
#一次写入一行数据
lst=['年份','社会物流总额','GDP','物流消费总额','固定资产投资','进口总额','出口总额']
year=[2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010]
total_social_logistics=[53.23,53.44,53.55,54.73,57.79,58.72,59.60,61.92,67.44,65.82,68.19]
GDP=[12.13,13.13,14.33,15.76,17.35,19.31,21.77,24.86,27.24,29.75,32.90]
total_logistics_consumption=[2.52,2.67,2.84,3.02,3.25,3.50,3.84,4.23,4.61,4.58,4.73]
investment_in_fixed_assets=[9.82,9.86,9.88,10.10,10.67,10.84,11.00,11.43,12.45,12.15,12.58]
total_imports=[1.80,1.95,2.36,3.31,4.50,5.29,6.34,7.97,9.36,7.86,10.32]
total_exports=[2.00,2.13,2.61,3.51,4.75,6.10,7.76,9.75,11.46,9.62,12.64]
for i in range(len(year)):
    if i==0:
        sheet.append(lst)
    data=[]
    data.append(year[i])
    data.append(total_social_logistics[i])
    data.append(GDP[i])
    data.append(total_logistics_consumption[i])
    data.append(investment_in_fixed_assets[i])
    data.append(total_imports[i])
    data.append(total_exports[i])
    sheet.append(data)
wb.save("文件/模糊认知图.xlsx")