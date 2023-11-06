guess_me = 5

for number in range(10):
    print("Checking number:", number)
    if number < guess_me:
        print(number, 'is too low')
    elif number == guess_me:
        print('Found it!')
        break
    else:
        print(number, 'is too high')
        break
