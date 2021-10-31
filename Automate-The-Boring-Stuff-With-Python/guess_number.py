s_num = '9'
count = 1
while count <= 3:
    g_num = input("Guees Number: ")
    count += 1
    if g_num == s_num:
        print("You win!")
        break
else:
    print("You faild")