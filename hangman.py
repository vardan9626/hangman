import random as rnd
from wordlist import words
from art import stages, logo


def get_word(curr_word: str, correct_word: str, guess: chr) -> str:
    new_word = [curr_word[i] if guess != correct_word[i]
                else guess for i in range(len(curr_word))]
    new_word = "".join(new_word)
    return new_word


if __name__ == "__main__":
    print(logo)
    correct_word = rnd.choice(words)
    guessed_word = "_" * len(correct_word)
    print(f"Pssts the word is {correct_word}")
    num_lives = 6
    while num_lives > 0:
        lives = num_lives * '*'
        print(f"Lives Left: {lives}")
        print(f"current word: {guessed_word}")
        letter = input("Enter a guess: ").lower()
        guessed_word_new = get_word(guessed_word, correct_word, letter)
        if guessed_word_new == guessed_word:
            print(stages[num_lives])
            num_lives = num_lives - 1
        guessed_word = guessed_word_new
        if '_' not in guessed_word:
            break
    if num_lives == 0:
        print("OOPPPPSSSS!!! You died")
        print(stages[0])
        exit(0)
    print(f"Congo!! You got the word: '{guessed_word}'")
