# -*- coding: utf-8 -*-
# @Author     : Bonnie
# @Time       : 2022/8/23 20:02
# @FileName   : pet_main.py
# @Description:

"""
这是宠物管理信息的主程序
"""
from pet_tools import *


def main():
    while True:
        print("宠物信息管理系统V1.0")
        show_menu()
        # 2、根据用户输入，调用不同的功能（函数）
        action = input("请选择希望执行的操作：")

        # action == 1 or action == 2 or action == 3
        # action == 0
        if action in ["1", "2", "3"]:
            if action == "1":
                # TODO 1、新增宠物信息
                new_pet()

                pass
            elif action == "2":
                # TODO 2、显示全部信息
                show_all()

                pass
            elif action == "3":
                # TODO 3、搜索宠物信息3
                search_pet()

                pass
        elif action == "0":
            print("欢迎再次使用【宠物管理系统】")
            break

        else:
            print("您输入的不正确，请重新选择")
        # 3、不断的执行上述操作


if __name__ == '__main__':
    main()
