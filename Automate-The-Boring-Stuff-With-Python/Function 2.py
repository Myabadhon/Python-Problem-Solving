import random
def getanswer(answernumber):

    if answernumber == 1 :
        print('it is the number one')
    elif answernumber == 2 :
        print('it is the nummber two')
    elif answernumber == 4 :
        print('it is the number two')
    elif answernumber == 5 :
        print('it is the nummber two')
    elif answernumber == 6 :
        print('it is the number two')
    elif answernumber == 7 :
        print('it is the nummber two')
    elif answernumber == 8 :
        print('it is the number two')
    elif answernumber == 9 :
        print('it is the nummber two')
    else :
        print('It is so much duitable')

r = random.randint(1 , 9)
fortune = getanswer(r)
print(fortune)