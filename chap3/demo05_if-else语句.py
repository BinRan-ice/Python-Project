# coding:utf-8
number=eval(input('请输入您的六位中奖号码：'))
#if-else
if number==654321:
    print('恭喜您，中奖了')
else:
    print('很遗憾，没中奖')

print('以上代码还可以使用条件表达式实现')
#number==987654为True时，将'恭喜你，中奖了'赋值给变量result，否则将'很遗憾，未中奖'赋值给变量result
result = '恭喜你，中奖了' if number==987654 else '很遗憾，未中奖'
print(result)
print('恭喜你，中奖了' if number==987654 else '很遗憾，未中奖')