# mystery_word

This program is a simple game of hangman called Mystery Word!

Lets the user choose a level of difficulty at the beginning of the program. Easy mode only has words of 4-6 characters; normal mode only has words of 6-8 characters; hard mode only has words of 8+ characters.
At the start of the game, let the user know how many letters the computer's word contains.
Ask the user to supply one guess (i.e. letter) per round. This letter can be upper or lower case and it does not matter. If a user enters more than one letter, tell them the input is invalid and let them try again.

Lets the user know if their guess appears in the computer's word.
Display the partially guessed word, as well as letters that have not been guessed.

A user is allowed 8 guesses. Remind the user of how many guesses they have left after each round.

A user loses a guess only when they guess incorrectly. If they guess a letter that is in the computer's word, they do not lose a guess.

If the user guesses the same letter twice, do not take away a guess. Instead, print a message letting them know they've already guessed that letter and ask them to try again.

The game will end when the user constructs the full word or runs out of guesses. If the player runs out of guesses, reveal the word to the user when the game ends.

When a game ends, ask the user if they want to play again. The game begins again if they reply positively.

##Requirements

  - Write functions to select a subset of the complete word list.
  - Write a function to select a word at random from the word list.
  - Write a function to display a word with blanks/letters filled in the appropriate spots.
  - Write a function to check if a word has been completely guessed.
  - Write other helper functions as necessary to help with the flow of the game.

##Objectives

- Be able to create an interactive program.
- Be able to choose a random value.
- Be able to keep track of state.
- Be able to read from a file.
