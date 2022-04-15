# exercise for string ops

import random

words_list =["hello","apple","words","game","love"]
word = random.choice(words_list)
print(word)

match ='_'*len(word)
match = list(match)

print(match)
num =0

lives = len(word)
for char in word:
  if num < len(word):
      guess = input(f"Enter a letter {num} :").lower()
      for x in range(len(word)):
       if word[x] == guess:
         match[x]=guess
         num +=1

match = ''.join(match)
if match == word:
    print("You won!")
#    print(stages[num])
else:
    print ("You lost!")
#    print(stages[0])
