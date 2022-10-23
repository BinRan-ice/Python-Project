# coding:utf-8
import os

filename = 'student.txt'


def menu():
    print('===========================学生信息管理系统=================================')
    print('------------------------------功能菜单--------------------------------------')
    print('\t\t\t\t\t\t1.录入学生信息')
    print('\t\t\t\t\t\t2.查找学生信息')
    print('\t\t\t\t\t\t3.删除学生信息')
    print('\t\t\t\t\t\t4.修改学生信息')
    print('\t\t\t\t\t\t5.排序')
    print('\t\t\t\t\t\t6.统计学生总人数')
    print('\t\t\t\t\t\t7.显示所有学生信息')
    print('\t\t\t\t\t\t0.退出系统')
    print('--------------------------------------------------------------------------')


def insert():
    student_list = []
    while True:
        id = input('请输入id(如1001):')
        if not id:
            break
        name = input('请输入name:')
        if not name:
            break
        try:
            english = int(input('请输入英语成绩：'))
            python = int(input('请输入Python成绩:'))
            java = int(input('请输入Java成绩:'))
        except:
            print('输入无效，不是整数，请重新输入')
            continue
        # 将录入的学生信息保存到字典中
        student = {'id': id, 'name': name, 'english': english, 'python': python, 'java': java}
        # 将学生信息添加到列表中
        student_list.append(student)
        answer = input('是否继续添加？y/n\n')  # \n是换行的意思
        if answer == 'y' or answer == 'Y':
            continue
        else:
            break

    # 调用save()函数，用于存储学生信息
    save(student_list)
    print('学生信息录入完毕！！！')


def save(lst):
    try:
        stu_txt = open(filename, 'a', encoding='utf-8')  # 以追加模式打开，如果没有的话，程序就会出错
    except:
        stu_txt = open(filename, 'w', encoding='utf-8')  # 如果出错，就以写入的方式打开
    for item in lst:  # 遍历列表lst
        stu_txt.write(str(item) + '\n')
    stu_txt.close()


def search():
    student_query = []
    while True:
        if os.path.exists(filename):
            mode = int(input('按ID查找请输入1，按姓名查找请输入2：'))
            if mode == 1:
                id = input('请输入学生ID:')
            elif mode == 2:
                name = input('请输入学生姓名:')
            else:
                print('您的输入有误，请重新输入')
                continue  # 也可以改用新方法 search()，可能会报错
            with open(filename, 'r', encoding='utf-8') as rfile:  # 读取filename内容
                student = rfile.readlines()  # 读取所有元素
                for item in student:  # 遍历列表
                    d = dict(eval(item))  # 字符串转成字典类型（也可以不写dict，因为eval之后就是字典，dict（）应该是为了创建一个字典）
                    if d != '':
                        if d['id'] == id:
                            student_query.append(d)
                    elif name != '':
                        if d['name'] == name:
                            student_query.append(d)
            show_student(student_query)  # 显示查询结果
            student_query.clear()  # 清空列表
            answer = input('是否继续查询？y/n\n')
            if answer == 'y':
                continue
            else:
                break
        else:
            print('暂未保存改学生信息')
            return


def show_student(lst):
    if len(lst) == 0:
        print('没有查到学生信息，无数据显示！！！')
        return
    # 如果查到，定义标题的显示
    format_title = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}\t'  # 冒号后面表示填充内容
    print(format_title.format('ID', '姓名', '英语成绩', 'python成绩', 'java成绩', '总成绩'))
    # 定义内容的显示格式
    format_data = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}\t'
    for item in lst:
        print(format_data.format(item.get('id'), item.get('name'), item.get('english'), item.get('python'),
                                 item.get('java'),
                                 int(item.get('english') + item.get('python') + item.get('java'))))


def delete():
    while True:
        student_id = input('请输入要删除的学生的id:')
        if student_id != '':  # 与 if not student_id: 功能相同
            if os.path.exists(filename):  # 判断文件是否存在
                with open(filename, 'r', encoding='utf-8') as file:
                    student_old = file.readlines()  # 读取学生信息放到列表当中
            else:
                student_old = []
            flag = False  # 标记是否删除
            if student_old:
                with open(filename, 'w', encoding='utf-8') as wfile:
                    d = {}
                    for item in student_old:  # 遍历列表
                        d = dict(eval(item))  # 将读出来的字符串转成字典类型，赋给d存储
                        if d['id'] != student_id:
                            wfile.write(str(d) + '\n')
                        else:
                            flag = True
                    if flag:
                        print(f'id为{student_id}的学生信息已经被删除')
                    else:
                        print(f'没有找到id为{student_id}的学生信息')
            else:
                print('无学生信息')
                break  # break 会退出 while True
            show()  # 删除之后要重新显示所有学生信息
            answer = input('是否继续删除呢？y/n\n')
            if answer == 'y':
                continue
            else:
                break


def modify():
    show()
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            student_old = rfile.readlines()
    else:
        return
    student_id = input('请输入要修搞得学生的ID：')
    with open(filename, 'w', encoding='utf-8') as wfile:
        for item in student_old:
            d = dict(eval(item))
            if d['id'] == student_id:
                print('找到学生信息了，可以修改他的相关信息了！')
                while True:
                    try:
                        d['name'] = input('请输入姓名')
                        d['english'] = input('请输入英语成绩')
                        d['python'] = input('请输入python成绩')
                        d['Java'] = input('请输入java成绩')
                    except:
                        print('您的输入有误，请重新输入')
                    else:
                        break
                wfile.write(str(d) + '\n')
                print('修改成功')
            else:
                wfile.write(str(d) + '\n')
        answer = input('是否继续修改其他学生信息呢呢？y/n\n')
        if answer == 'y':
            modify()


def sort():  # 排序
    show()  # 展示全部学生信息
    student_new = []
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            student_list = rfile.readlines()
        for item in student_list:
            d = dict(eval(item))
            student_new.append(d)
    else:
        return
    asc_or_desc = int(input('请选择（0.升序 1.降序):'))
    if asc_or_desc == 0:
        asc_or_desc_bool = False
    elif asc_or_desc == 1:
        asc_or_desc_bool = True
    else:
        print('您的输入有误，请重新输入')
        sort()
    mode = int(input('请选择排序方式(1.按英语成绩排序 2.按python你成绩排序 3.按java成绩排序 4.按总成绩排序)'))
    if mode == 1:
        student_new.sort(key=lambda x: int(x['english']), reverse=asc_or_desc_bool)  # 匿名函数lambda,x是一个参数，这个参数是一个字典
    elif mode == 2:
        student_new.sort(key=lambda x: int(x['python']), reverse=asc_or_desc_bool)
    elif mode == 3:
        student_new.sort(key=lambda x: int(x['java']), reverse=asc_or_desc_bool)
    elif mode == 4:
        student_new.sort(key=lambda x: int(x['english']) + int(x['python']) + int(x['java']), reverse=asc_or_desc_bool)
    else:
        print('您的输入有误，请重新输入')
        sort()
    show_student(student_new)


def total():  # 统计学生总人数
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:  ##读取filename内容
            students = rfile.readlines()  ##读取所有元素
            if students:
                print(f'一共有{len(students)}名学生')  # 计算学生总人数，实际上就是判断列表的长度
            else:
                print('还未录入学生信息')
    else:
        print('暂未保存数据。。。。')


def show():  # 查询所有学生信息
    student_lst = []
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:  ##读取filename内容
            students = rfile.readlines()  ##读取所有元素
            for item in students:
                student_lst.append(eval(item))
            if student_lst:  # 如果这个列表不为空的情况下
                show_student(student_lst)

    else:
        print('暂未保存过数据！！！！')


def main():
    while True:  # while true 就是无限循环，只要满足条件，直到break
        menu()
        choice = int(input('请选择：'))
        if choice in [0, 1, 2, 3, 4, 5, 6, 7]:
            if choice == 0:
                answer = input('您确定推出系统吗？y/n')
                if answer == 'y' or answer == 'Y':
                    print('谢谢您的使用！！！')
                    break  # 结束循环，退出系统
                else:
                    continue
            elif choice == 1:
                insert()  # 录入学生信息
            elif choice == 2:
                search()
            elif choice == 3:
                delete()
            elif choice == 4:
                modify()  # 修改学生信息
            elif choice == 5:
                sort()  # 排序
            elif choice == 6:
                total()  # 统计学生总人数
            elif choice == 7:
                show()  # 显示所有学生信息


if __name__ == '__main__':  # 以主程序的方式运行
    main()
