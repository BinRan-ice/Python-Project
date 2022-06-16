# coding:utf-8
answer=input('请问，您喝酒了么？y/n')
if answer=='y':  #代表喝酒了
    proof=eval(input('请输入酒精含量:'))
    if proof<20:
        print('构不成酒驾,你可以走了')
    elif proof<80:
        print('已构成酒驾标准，请不要开车')
    else:
        print('已达到醉驾标准')
else:   #没有喝酒的情况
    print('你走吧，没你啥事儿')