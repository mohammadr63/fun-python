print('welcom')
def timer ():
    name = input('please enter  your name ? >')
    print(' Hi , {}'.format(name))




    import sys
    import time


    Counter = 0
    s = 0
    m = 0 
    n = int(input('{} how secondes do you want  the timer to be?: '.format(name)))
    print('')


    while Counter <= n:
        sys.stdout.write("\x1b[1A\x1b[2k")
        print(m, 'minutes' , s, 'secounds')
        time.sleep(1)
        s += 1
        Counter += 1
        if s == 60 :
            m+=1
            s = 0

    print('\nTime is over ! Timer completed')

       
    again()
def again():

    timer_again = input('''
    Do you want to timer again?
    Please type Y for YES or N for NO.
    ''')
    if timer_again.upper() == 'Y':
      timer ()
    elif timer_again.upper() == 'N':
        print('See you later.')
    else:
        again()
timer()
