# -*- coding: utf-8 -*-
# @Author     : Bonnie
# @Time       : 2022/8/26 16:48
# @FileName   : pet_tools.py
# @Description:

'''
1、新增宠物信息
2、显示全部信息
3、搜索宠物信息

0、退出系统
'''
pet_info = []  # 用来保存宠物信息

# pet_info = [{'nickname': '萝莉', 'age': '3', 'sex': '雌性', 'weight': '15'}]
pet_info = [{'nickname': '萝莉', 'age': '3', 'sex': '雌性', 'weight': '15'},
            {'nickname': '正太', 'age': '3', 'sex': '雌性', 'weight': '15'}]
header = ["昵称", "年龄", "性别", "体重"]


def show_menu():
    """
    #显示系统菜单
    :return:
    """
    print("宠物信息管理系统V1.0".center(25, '*'))
    print()
    print("1、新增宠物信息")
    print("2、显示全部信息")
    print("3、搜索宠物信息")
    print()
    print("0、退出系统")
    print("*" * 30)


def new_pet():
    print("新增宠物信息".center(24, "="))
    nickname = input("请输入昵称:")
    age = input("请输入年龄：")
    sex = input("请输入性别（雄性/雌性）：")
    weight = input("请输入体重（kg）：")

    pet = {"nickname": nickname,
           "age": age,
           "sex": sex,
           "weight": weight}
    pet_info.append(pet)
    # print(pet)
    print(f"【添加{nickname}成功】")


def show_all():
    """
    #显示全部信息
    :return:
    """
    print("显示全部信息".center(24, "="))

    # 判断信息列表是否为空
    if len(pet_info) == 0:
        print("【当前没有任何宠物信息记录，请使用新增功能添加宠物信息！】")
        return
    # 打印表头
    # print("昵称\t\t年龄\t\t性别\t\t体重")
    for title in header:
        print(title, end="\t\t")
    print()
    print("-" * 30)

    # 逐一打印列表的每个宠物信息
    for pet in pet_info:
        for value in pet.values():
            print(f"{value}", end="\t\t")
        print()


def deal_pet(find_pet):
    """
    处理查找到的信息
    :param find_pet: 查找我的宠物信息
    :return:
    """
    action = input("请选择要执行的操作：【1】 修改 【2】 删除 【0】 返回上级菜单")
    if action == "1":
        # 执行修改的操作
        find_pet["nickname"] = input_pet_info(find_pet["nickname"], "昵称：[回车不修改]")
        find_pet["age"] = input_pet_info(find_pet["age"], "年龄：[回车不修改]")
        find_pet["sex"] = input_pet_info(find_pet["sex"], "性别（雄性/雌性）：[回车不修改]")
        find_pet["weight"] = input_pet_info(find_pet["weight"], "体重（kg)：[回车不修改]")
        print("【删除宠物信息成功】")
    elif action == "2":
        # 执行删除操作
        pet_info.remove(find_pet)
        print("【删除宠物信息成功】")
        pass


def search_pet():
    """
    查询宠物信息
    :return:
    """
    print("搜索宠物信息".center(24, "="))

    # 1、引导用户输入要搜索的昵称
    find_name = input("请输入要搜索的昵称：")

    # 2、在宠物信息列表中查找对应昵称的宠物信息
    for pet in pet_info:
        if pet["nickname"] == find_name:
            # 打印表头
            for title in header:
                print(title, end="\t\t")
            print()
            print("-" * 30)
            # 打印宠物的详细信息
            for value in pet.values():
                print(f"{value}", end="\t\t")
            print()
            # 提示用户对于找到的信息，进行操作
            deal_pet(pet)
            break
    else:
        print(f"抱歉，没有找到{find_name}")


def input_pet_info(pet_value, tip):
    """
    输入宠物信息的功能拓展
    :param pet_value: 字典中原有的值
    :param tip: 输入的提示文字
    :return: 如果用户输入内容，就返回内容，否则返回字典中原有的值
    """
    # 1、提示用户输入信息
    result = input(tip)
    # 2、用户输入内容不为空，返回输入的值
    if len(result) > 0:
        return result
    # 3、如果用户输入为空，返回宠物信息原有的值
    else:
        return pet_value


if __name__ == '__main__':
    # show_menu()
    # new_pet()
    # show_all()
    search_pet()
