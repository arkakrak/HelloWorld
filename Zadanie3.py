def guess(val1):
    n = 0
    while n < 5:
        n += 1
        val2 = input('Guess the word: ')
        if val1 == val2:
            print('Good!')
            break
        else:
            print('Not good!')
            continue

guess('kot')