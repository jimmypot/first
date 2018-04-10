# zhujun shoping

saving = int(input("亲，请输入你的工资 ："))
taobao = [["1 iphone","5999"],["2 Mac pro","13450"],["3 纸巾","5"],["4 bike","800"]]
print(taobao)
shopingcar = []
while True:
    N = int(input("亲，决定购买商品时。请输入编号："))
    if int(taobao[N-1][1])<saving:
        shopingcar.append(taobao[N-1])
        saving = saving - int(taobao[N-1][1])
        quiting = input("如果你想退出的话，请输入q,否则请输入b")
        if quiting == "q":
            break
        else:
            continue
    else:
        print("亲，您的余额不足啊，再看看别的商品吧")
        quiting = input("如果你想退出的话，请输入q")
        if quiting == "q":
            break
print(shopingcar)
