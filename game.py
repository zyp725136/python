import random
choices = ['石头','剪刀','布']
win_list = [['石头','剪刀'],['剪刀','布'],['布','石头']]
prompt = """(0) 石头
(1)剪刀
(2)布
请选择(0/1/2):"""
pwin = 0
cwin = 0

while pwin < 2 and cwin < 2:
    computer = random.choice(choices)
    ind = int(input(prompt))
    player = choices[ind]

    print("Your choice: %s,computer choice: %s" % (player,computer))
    if player == computer:
        print('\033[33;1m平局\033[0m')
    elif [player , computer] in win_list:
        pwin += 1
        print('\033[31;1m你赢了!!!\033[0m')
    else:
        cwin += 1
        print('\033[31;1m你输了!!!\033[0m')