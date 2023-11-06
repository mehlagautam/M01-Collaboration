# Get user input for the 'secret' number
secret = int(input("Choose a number between 1 and 10 and enter it as the secret number: "))

# Get user input for the 'guess' number
guess = int(input("Guess a number between 1 and 10: "))

# Check if the guess is too low, too high, or just right
if guess < secret:
    print('Too low')
elif guess > secret:
    print('Too high')
else:
    print('Just right')
