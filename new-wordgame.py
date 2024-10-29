import random
words_list = tuple(sorted(set([
    "c", "go", "php", "dart", "java", "ruby", "rust", "scala", "swift",
    "cplus", "groovy", "kotlin", "python", "csharp", "elixir", "erlang",
    "haskell", "clojure", "typescript", "javascript"
])))

selected_word = random.choice(words_list)
print(selected_word)

masked_word = ["_"  for letter in selected_word]
print("".join(masked_word))
remaining_indexes = set(i for i in range(len(selected_word)))
print(remaining_indexes)


def get_guess() -> None:
    """
    Ask the user for a single letter to guess in the word.
    If the letter is in the word, reveal the letter in the masked word.
    If the letter is not in the word, decrement the counter.
    If the counter reaches 0, the game is over and the user lost.
    If the user guessed the word, the game is over and the user won.
    """
    counter = len(selected_word)
    while remaining_indexes:
        guess = input("Enter a letter or type 'Exit': ")
        if guess.lower() == "exit":
            break
        while not (len(guess) == 1 and guess.isalpha()):
            guess = input("Please enter a single letter: ")
        
        if guess in selected_word:
            occurance = selected_word.count(guess)
            counter -= occurance
            if occurance > 1:
                indecies = [i for i, letter in enumerate(selected_word) if letter == guess]
                for index in indecies:
                    masked_word[index] = guess
                    remaining_indexes.remove(index)
            else:
                indx = selected_word.index(guess)
                masked_word[indx] = guess
                remaining_indexes.remove(indx)
        print("".join(masked_word))
        # print(selected_word)
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
