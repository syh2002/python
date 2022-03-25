age_of_syh = 33
count = 0

while count < 3:

    guess_age = int(input("年龄是？"))
    if guess_age == age_of_syh:
        print("是的")
        break;
    elif guess_age > age_of_syh:
        print("你才真么老")
    else:
        print("谢谢你，但是不对")
    count += 1

    if count == 3:
        continue_confirm = input("你还玩吗..(Enter/n)？")
        if continue_confirm == 'n':
            print('在见')
        else:
            count=0

else:
    print('看看脑子')