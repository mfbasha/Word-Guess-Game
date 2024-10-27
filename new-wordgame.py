import random
words_list =["python", "java", "javascript", "ruby", "php", 
             "swift", "csharp", "cplus", "c", "go", "rust", "scala", 
             "kotlin", "dart", "typescript", "haskell", "erlang",
              "elixir", "clojure", "groovy", "kotlin", "scala", "dart", 
              "typescript", "haskell", "erlang", "elixir", "clojure", "groovy"
]
selected_word = random.choice(words_list)
print(selected_word)

masked_word = ["_"  for letter in selected_word]
print("".join(masked_word))
remaining_indexes = [i for i in range(len(selected_word))]
print(remaining_indexes)


def get_guess():
    counter = len(selected_word)
    while len(remaining_indexes) > 0:
        guess = input("Enter a letter or type 'Exit': ")
        if guess.lower() == "exit":
            break
        occurance = 0
        while True:
            if len(guess) == 1 and guess.isalpha():
                break
            else:
                guess = input("Please enter a single letter: ")
        
        if guess in selected_word:
           occurance = selected_word.count(guess)
           counter = counter - occurance
           if occurance > 1:
            indecies =[i for i, letter in enumerate(selected_word) if letter == guess]
            for index in indecies:
                masked_word[index] = guess
                remaining_indexes.remove(index)
                
           else:
                indx = selected_word.index(guess)
                masked_word[indx] = guess
                remaining_indexes.remove(indx)
        print("".join(masked_word))
        print(selected_word)
        if counter <= 0:
            print("Game over")
            break
    if "".join(masked_word) == selected_word:
        print("You won the game")
        print("".join(masked_word))
        print(selected_word)
    else:
        print("You lost the game")
        print("".join(masked_word))
        print(selected_word)
get_guess()
