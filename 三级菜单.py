data = {
'北京':{
        '海淀':{
            '五道口':{
                'soho':{},
                '网易':{},
                'google':{}
            },
            '中关村':{
                '爱奇艺':{},
                '汽车之家':{},
                'youku':{},
            },
            '上地':{
                '百度':{},
            },
        },
        '昌平':{
            '沙河':{
                '老男孩':{},
                '北航':{},
            },
            '天通苑':{},
            '回龙观':{},
        },
        '朝阳':{},
        '东城':{},
    },
'上海':{
        '闵行':{
            "人民广场":{
                '炸鸡店':{}
            }
        },
        '闸北':{
            '火车战':{
                '携程':{}
            }
        },
        '浦东':{},
    },
    '山东':{},
}

# while True:
#     for i in data:
#         print(i)
#     # 1
#     choice = input('选择进入》》')
#     if choice in data:
#         while True:
#             for i2 in data[choice]:
#                 print("\t",i2)
#             # 2
#             choice2 = input("选择进入》》")
#             if choice2 in data[choice]:
#                 while True:
#                     for i3 in data[choice][choice2]:
#                         print('\t\t',i3)
#                     # 3
#                     choice3 = input('选择输入》》')
#                     if choice3 in data[choice][choice2]:
#                         for i4 in data[choice][choice2][choice3]:
#                             print('\t\t\t',i4);
#                         # 4
#                         choice4 = input('最后一层按q返回')
#                         if choice4 == 'q':
#                             pass
#                     if choice3 == 'q':
#                         break
#             if choice2 == 'q':
#                 break
#     if choice3 == 'q':
#         break
exit_flag = False

while not exit_flag:
    for i in data:
        print(i)
    # 1
    choice = input('选择进入》》')
    if choice in data:
        while not exit_flag:
            for i2 in data[choice]:
                print("\t",i2)
            # 2
            choice2 = input("选择进入》》")
            if choice2 in data[choice]:
                while not exit_flag:
                    for i3 in data[choice][choice2]:
                        print('\t\t',i3)
                    # 3
                    choice3 = input('选择输入》》')
                    if choice3 in data[choice][choice2]:
                        for i4 in data[choice][choice2][choice3]:
                            print('\t\t\t',i4);
                        # 4
                        choice4 = input('最后一层按q返回')
                        if choice4 == 'q':
                            exit_flag = True
