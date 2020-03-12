## ask for 8 names. store in list
# pick random and print

import random
# names = []
# while len(names) < 8:
#   name = (input('Give me a name: '))
#   names.append(name)


# print(random.choice(names))

# guess game with colors
colors_list = ['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'brown', 'black']

color = random.choice(colors_list)
guess = (input('Guess what color I am thinking: '))
# print(color)

while guess != color:
  if(guess != color):
    guess = input('Guess again: ')
  
print('Correct! You guessed', guess)

