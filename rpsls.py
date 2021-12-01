#coding:gbk
"""
第一个小项目：Rock-paper-scissors-lizard-Spock
作者：陈代磊
日期：2021/12/1
"""


import random



# 0 - 石头
# 1 - 史波克
# 2 - 纸
# 3 - 蜥蜴
# 4 - 剪刀

def name_to_number(name):
    """
    将游戏对象对应到不同的整数
    """
    while 1:
        if name=="石头":
            name=0
            return name
        if name=="史波克":
            name=1
            return name
        if name=="纸":
            name=2
            return name
        if name=="蜥蜴":
            name=3
            return name
        elif name=="剪刀":
            name=4
            return name
        else:
            print("Error: No Correct Name")

    # 使用if/elif/else语句将各游戏对象对应到不同的整数
    # 不要忘记返回结果


    #编写执行代码,代码完成后将pass删除


def number_to_name(number):
    """
    将整数 (0, 1, 2, 3, or 4)对应到游戏的不同对象
    """
    if number==0:
        number="石头"
        return number
    if number==1:
        number="史波克"
        return number
    if number==2:
        number="纸"
        return number
    if number==3:
        number="蜥蜴"
        return number
    if number==4:
        number="剪刀"
        return number

    # 使用if/elif/else语句将不同的整数对应到游戏的不同对象
    # 不要忘记返回结果

     #编写执行代码,代码完成后将pass删除


def rpsls(player_choice):
    """
    用户玩家任意给出一个选择，根据RPSLS游戏规则，在屏幕上输出对应的结果

    """
    player_choice_number=name_to_number(player_choice)# 调用name_to_number()函数将用户的游戏选择对象转换为相应的整数，存入变量player_choice_number
    comp_number=random.randrange(5)# 利用random.randrange()自动产生0-4之间的随机整数，作为计算机随机选择的游戏对象，存入变量comp_number
    comp_number=number_to_name(comp_number)# 调用number_to_name()函数将计算机产生的随机数转换为对应的游戏对象
    print("电脑的选择是："+str(comp_number))# 在屏幕上显示计算机选择的随机对象
    if player_choice_number==0 and comp_number=="石头":
        print("平局")
    elif player_choice_number==1 and comp_number=="史波克":
        print("平局")
    elif player_choice_number==2 and comp_number=="纸":
        print("平局")
    elif player_choice_number==3 and comp_number=="蜥蜴":
        print("平局")
    elif player_choice_number==4 and comp_number=="剪刀":
        print("平局")
    elif player_choice_number==4 and comp_number=="纸":
        print("你赢了")
    elif player_choice_number==2 and comp_number=="石头":
        print("你赢了")
    elif player_choice_number==0 and comp_number=="剪刀":
        print("你赢了")
    elif player_choice_number==0 and comp_number=="蜥蜴":
        print("你赢了")
    elif player_choice_number==3 and comp_number=="史波克":
        print("你赢了")
    elif player_choice_number==0 and comp_number=="剪刀":
        print("你赢了")
    elif player_choice_number==4 and comp_number=="蜥蜴":
        print("你赢了")
    elif player_choice_number==3 and comp_number=="纸":
        print("你赢了")
    elif player_choice_number==2 and comp_number=="史波克":
        print("你赢了")
    elif player_choice_number==1 and comp_number=="石头":
        print("你赢了")
    else:
        print("机器赢了")# 利用if/elif/else 语句，根据RPSLS规则对用户选择和计算机选择进行判断，并在屏幕上显示判断结果

    # 如果用户和计算机选择一样，则显示“您和计算机出的一样呢”，如果用户获胜，则显示“您赢了”，反之则显示“计算机赢了”

    #根据以上提示编写执行代码，代码完成后删除掉pass


# 对程序进行测试
print("欢迎使用RPSLS游戏")
print("请输入您的选择")
choice_name=input()
rpsls(choice_name)