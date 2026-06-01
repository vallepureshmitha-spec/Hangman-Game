# Simple Text-Based Hangman Game

A lightweight, console-based implementation of the classic Hangman word-guessing game built entirely in Python. The game selects a secret word randomly, and the player attempts to guess it one letter at a time within a limited number of attempts.

## Key Features
* Random Word Selection: Automatically chooses a word from a predefined bank for each new game session.
* Input Validation: Safeguards the application by ensuring the player only enters valid single alphabetic characters.
* Dynamic Tracking: Keeps real-time track of guessed letters, correct positions, and remaining incorrect turn allowances.

## Core Concepts Used
* Random Selection (random.choice)
* Set Data Structures (for optimized unique guess tracking)
* Conditional Flow Mechanics (if-elif-else blocks)
* String and List Manipulation (joining and formatting hidden characters)
* Input/Output Data Handling

## Game Rules
* You must guess the hidden word letter by letter.
* You are allowed a maximum of 6 incorrect guesses before the game ends.
* Repeatedly guessing the same letter will not penalize your turn count.

## How to Run
1. Ensure you have Python installed on your machine.
2. Download or clone this repository.
3. Open your terminal, navigate to the folder, and run:
   ```bash
   python hangman.py
