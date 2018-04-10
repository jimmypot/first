# zhujun
product_list = [
    ("iphone",5800),
    ("mac pro",10200),
    ("watch",4500),
    ("alex book",120),
]
shoping_list=[]
salary =input("亲，请输入你的工资 : ")
if salary.isdigit():
    salary = int(salary)
    while True:
        for index,i in enumerate(product_list):
            # print(product_list.index(i),i)
            print(index,i)
        user_choice = input("确认购买，请输入商品的编号 : ")
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice <len(product_list)and user_choice>=0 :
                p_item = product_list[user_choice]
                if salary >= p_item[1]:
                    shoping_list.append(p_item)
                    salary -= p_item[1]
                    print("您已购买%s啦"%p_item[0])
                else:
                    print("您的余额不足哦，购买失败！")
            else:
                print("您输入的商品号码有误，请重新输入")
        elif user_choice == "q":
            print("------shoping list------")
            for index,i in enumerate(shoping_list):
                print(index,i)
            print("您的余额为 : ",salary)
            exit()
        else:
            print("亲，请正确输入商品号码！")













