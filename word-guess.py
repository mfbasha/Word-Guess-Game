import random
words_list =["python", "java", "javascript", "ruby", "php", 
             "swift", "csharp", "cplus", "c", "go", "rust", "scala", 
             "kotlin", "dart", "typescript", "haskell", "erlang",
              "elixir", "clojure", "groovy", "kotlin", "scala", "dart", 
              "typescript", "haskell", "erlang", "elixir", "clojure", "groovy"
]
selected_word = random.choice(words_list)
print(selected_word)
# masked_word = ["_" if letter != " " else " " for letter in selected_word]
masked_word = ["_"  for letter in selected_word]
# masked_word = "".join(masked_list)
print("".join(masked_word))

def get_guess():
    while True:
        guess = input("Enter a letter: ")
        if guess in selected_word:
            indx = selected_word.index(guess)
        right_guess =False
        for i in range(len(selected_word)):
            if len(guess) == 1 and guess.isalpha():
                print(f"You guessed {guess} with length {len(guess)} and alphaneumeric is {guess.isalpha()}")
                for index, letter in enumerate(selected_word):
                    if letter == guess:
                        masked_word[index] = guess
                        print("".join(masked_word))
                        print(selected_word)
                        guess= input(f"Enter a letter no. {i+1}: ")
                   
                    i+=1
                right_guess= "".join(masked_word) == selected_word
                if right_guess:
                    print("You won the game")
                    print("".join(masked_word))
                    print(selected_word)
                    break
                else:
                    print("Game overtry again !!!")
                    print("".join(masked_word))
                    print(selected_word)
                    break
            else:
                print("Please enter a valid one  letter.")
        
get_guess()