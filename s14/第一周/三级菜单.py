data = {
    '北京':{'昌平':{'沙河':['oldboyt','test'],'天通苑':['链家地产','我爱我家']},
                '朝阳':{'国贸':['cicc','太平洋保险'],'三里屯':['apple','朝阳shou'],'亚运村':['鸟巢','水立方']},
                '海淀':{'府学路':['人民大学','北京理工大学'],'紫金路':['北京大学','清华大学']}
                },
    '山东':{'青岛':{'a':[1,2,3],'b':[1,2,3]},
                '济南':{'c':[1,2,3],'d':[1,2,3]} }
}
exit_flag = False

while not exit_flag:
    for i1 in data:
        print(i1)    #打印城市

    choice1 = input("选择进入>>>")         #用输入城市名称
    if choice1 in data:
        #while True:
            for i2 in data[choice1]:
                print('\t\t',i2)           #打印用户选择的分级1菜单

            choice2 = input("选择进入>>>") # 用户输入城市区
            if choice2 in data[choice1]:
                    while not exit_flag:
                        for i3 in data[choice1][choice2]:
                           print('\t\t\t\t',i3)       #打印用户选择的或者街道

                        choice3 = input('选择进入>>>') #用户输入小街道名称
                        if choice3 in data[choice1][choice2]:
                            for i4 in data[choice1][choice2][choice3]:
                                print('\t\t\t\t\t\t',i4)               #打印用户选的公司
                            tuichu = input('最后一层,请按b退出，整个退出请按q>>>')
                            pass
                            if tuichu == "q":
                                exit_flag = True

                        elif choice3 == "b":
                            break                      #用户退出当前目录
                        elif choice3 == "q":
                            exit_flag = True
                        else:
                            print('输入错误')

            elif choice2 == 'b':
                 break                                 #用户退出当前目录
            elif choice2 == "q":
                 exit_flag = True
            else:
                print('输入错误')
