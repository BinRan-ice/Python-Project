# coding:utf-8
#所有的字符都是数字(十进制阿拉伯数字)
print('123'.isdigit())  #True
print('一二三'.isdigit())  #False
print('0b1001'.isdigit())   #False
print('-'*50)
#所有字符都是数字(阿拉伯数字，罗马数字...)
print('1234'.isnumeric())   #True
print('一二三四'.isnumeric())   #True
print('ⅢⅢ'.isnumeric()) #True
print('0b10001'.isnumeric())    #False
print('壹贰叁'.isnumeric())    #True
print('-'*50)
#所有都是字母(英文，中文)
print('hello你好'.isalpha())  #True
print('hello你好123'.isalpha())   #False
print('hello你好一二三'.isalpha())   #True
print('ⅢⅢ'.isalpha()) #False
print('-'*50)
#所有的都是字母+数字+中文
print('hello你好123'.isalnum())   #True
print('hello你好123.'.isalnum())   #False
print('hello你好一二三'.isalnum())   #True
print('hello你好壹贰叁'.isalnum())   #True
print('hello你好ⅢⅢ'.isalpha())   #True
print('-'*50)
#判断大小写
print('HelloWorld'.islower())   #False
print('helloworld'.islower())   #True
print('hello你好'.islower())  #True
print('Helloworld'.isupper())   #False
print('HELLOWORLD'.isupper())   #True
print('HELLO你好'.isupper())  #True
print('-'*50)
#是否是首字母大写
print('Hello'.istitle())    #True
print('HelloWorld'.istitle())   #False
print('Hellowold'.istitle())    #True
print('Hello world'.istitle())  #False
print('Hello World'.istitle())  #True
print('-'*50)
#是否都是空白字符
print('\t'.isspace())
print('\n'.isspace())
print('   '.isspace())


