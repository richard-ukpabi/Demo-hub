print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choose1=input('choose your path, either left or right?  ').lower()
if choose1 =='left':
    choose2=input('swim or wait '  ).lower()
    if choose2=='wait':
         choose3=input('which door red,blue or yellow ').lower()
         if choose3=='red':
             print('burned by fire,game over.')
         elif choose3=='blue':
             print('Eaten by the beast.game over')
         elif choose3=='yellow':
             print('You won, congratulation. collect you\'re flowers')
         else:
             print('GAME OVER')
    else:
         print('sorry mate you have been kicked out')


else:
    print('sorry my friend, your journey end here')
