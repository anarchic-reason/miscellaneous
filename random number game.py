def random_number(n):
    import random
    num=random.randint(1,n)
    while True:
        print('Guess a number between 1 and %s' % n)
        guess=input()
        i=int(guess)
        if i==num:
            print('You guessed right')
            break
        elif i<num:
            print('Try higher')
        elif i>num:
            print('Try lower')
