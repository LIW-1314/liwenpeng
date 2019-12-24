#coding:gbk
"""
程序：第一个小项目：Rock-paper-scissors-lizard-Spock
作者：李文鹏
"""

import random


# 0 - 石头
# 1 - 史波克
# 2 - 纸
# 3 - 蜥蜴
# 4 - 剪刀

# 以下为完成游戏所需要用到的自定义函数

def name_to_number(name):
    """
    将游戏对象对应到整数
    """
    if name=="石头":
       snum=0
    elif name=="史波克":
        snum=1
    elif name=="纸":
        snum=2
    elif name=="蜥蜴":
        snum=3
    elif name=="剪刀":
        snum=4
    return snum
    
def number_to_name(number):
    """
    将整数对应到游戏对象
    """
    if number==0:
       dnum="石头"
    elif number==1:
        dnum="史波克"
    elif number==2:
        dnum="纸"
    elif number==3:
        dnum="蜥蜴"
    elif number==4:
        dnum="剪刀"
    return dnum
    
def rpsls(player_choice):
    """
    用户玩家任意给出一个选择，根据RPSLS游戏规则，在屏幕上输出对应的结果
    """
    a=random.randint(0,4)
    b=name_to_number(player_choice)
    print("--------")
    print("您的选择为：%s"%player_choice)
    print("计算机的选择是：%s"%number_to_name(a))
    if a==0:
       if b==1 or b==2:
          print("您赢了")
       elif b==3 or b==4:
          print("计算机赢了")
       else:
           print("您和计算机出的一样呢")
    if a==1:
       if b==3 or b==2:
          print("您赢了")
       elif b==0 or b==4:
          print("计算机赢了")
       else:
          print("您和计算机出的一样呢")
    if a==2:
       if b==3 or b==4:
          print("您赢了")
       elif b==0 or b==1:
          print("计算机赢了")
       else:
          print("您和计算机出的一样呢")
    if a==3:
       if b==1 or b==2:
          print("计算机赢了")
       elif b==0 or b==4:
          print("您赢了")
       else:
          print("您和计算机出的一样呢")
    if a==4:
       if b==0 or b==1:
          print("您赢了")
       elif b==2 or b==3:
          print("计算机赢了")
       else:
          print("您和计算机出的一样呢")
       # 输出"-------- "进行分割
    # 显示用户输入提示，用户通过键盘将自己的游戏选择对象输入，存入变量player_choice

    # 调用name_to_number()函数将用户的游戏选择对象转换为相应的整数，存入变量player_choice_number

    # 利用random.randrange()自动产生0-4之间的随机整数，作为计算机随机选择的游戏对象，存入变量comp_number

    # 调用number_to_name()函数将计算机产生的随机数转换为对应的游戏对象

    # 在屏幕上显示计算机选择的随机对象

    # 利用if/elif/else 语句，根据RPSLS规则对用户选择和计算机选择进行判断，并在屏幕上显示判断结果

    # 如果用户和计算机选择一样，则显示“您和计算机出的一样呢”，如果用户获胜，则显示“您赢了”，反之则显示“计算机赢了”

    #根据以上提示编写执行代码，代码完成后删除掉pass


# 对程序进行测试
print("欢迎使用RPSLS游戏")
print("----------------")
print("请输入您的选择:")
choice_name=input()
rpsls(choice_name)
