# salay = int(input('请输入你的工资'))
# goods = [['IPhone',5800],['MAC_pro',12000],['Alex_python',80],['bike',800]]
# buys = []
#
# while True:
#     print('\t\t购物车程序\t\t')
#     print('\t1)购买')
#     print('\t2)查看余额')
#     print('\t3)退出（q）')
#
#     choice = input('请输入选项(1|2|3):')
#
#     if choice == '1':
#         print(goods)
#         good=input('输入你想要的商品：')
#
#         cost = goods[goods.index(good)][1]
#     if choice == '2':
#         balance=salay-cost
#         print(balance)
#     if choice == '3':
#         break;

product_list = [
    ('Iphone',5800),
    ('Mac Pro',9800),
    ('Bike',800),
    ('Watch',10600),
    ('Coffee',31),
    ('python',120)
]
shoppint_list = []
salary = input('输入你的工资：')
if salary.isdigit():
    salary = int(salary)
    while True:
        # for item in product_list:
        #     print(product_list.index(item),item)
        for index,item in enumerate(product_list):
            print(index,item)
        user_choice = input("买什么？>>>:")

        if user_choice.isdigit():
            user_choice = int(user_choice)
            if -1 < user_choice < len(product_list):
                p_item = product_list[user_choice]
                if p_item[1] <= salary:
                    shoppint_list.append(p_item)
                    salary -= p_item[1]
                    print("Added %s into shopping cart ,your current balance is \033[31;1m%s\033[0m" %(p_item,salary))
                else:
                    print("\033[41;1m你的余额只剩[%s]啦\033[0m" % salary)
            else:
                print('商品不存在')
        elif user_choice == 'q':
            print('------shopping-------')
            for p in shoppint_list:
                print(p)
            print('你的余额',salary)
            exit()
        else:
            print('错误')

