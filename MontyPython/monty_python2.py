#!/usr/bin/python3

round=0
while True:
    round = round + 1
    print('finish the movie title, "Monty Python\'s "The Life of ____"')
    answer = input("Your guess---> ")
    if answer== 'Brian':
        print('correct!')
        break
    elif round== 3:
        print('Sorry, the answer was Brian')
        break
    else:
        print('Sorry, Try Again!')
