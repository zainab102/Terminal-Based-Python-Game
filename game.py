import random
import os
import json

# Function to save scores to a file
def save_score(game_name, score):
    scores_file = 'scores.json'
    if os.path.exists(scores_file):
        with open(scores_file, 'r') as f:
            scores = json.load(f)
    else:
        scores = {}
    
    if game_name not in scores:
        scores[game_name] = []
    scores[game_name].append(score)
    
    with open(scores_file, 'w') as f:
        json.dump(scores, f, indent=4)
    print(f"Score saved for {game_name}!")

# Function to load and display high scores
def display_high_scores():
    scores_file = 'scores.json'
    if os.path.exists(scores_file):
        with open(scores_file, 'r') as f:
            scores = json.load(f)
        print("\nHigh Scores:")
        for game, score_list in scores.items():
            if score_list:
                high_score = max(score_list)
                print(f"{game}: {high_score}")
    else:
        print("No scores saved yet.")

# Rock-Paper-Scissors Game
def rock_paper_scissors():
    choices = ['rock', 'paper', 'scissors']
    user_score = 0
    computer_score = 0
    rounds = 3
    
    print("Welcome to Rock-Paper-Scissors!")
    print("Best of 3 rounds.")
    
    for round_num in range(1, rounds + 1):
        print(f"\nRound {round_num}:")
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        while user_choice not in choices:
            user_choice = input("Invalid choice. Choose rock, paper, or scissors: ").lower()
        
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")
        
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissors' and computer_choice == 'paper'):
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1
    
    print(f"\nFinal Score: You {user_score} - Computer {computer_score}")
    if user_score > computer_score:
        print("🎉 You win the game!")
        score = user_score
    elif user_score < computer_score:
        print("😢 Computer wins the game!")
        score = 0
    else:
        print("It's a tie game!")
        score = user_score
    
    save_option = input("Save your score? (y/n): ").lower()
    if save_option == 'y':
        save_score("Rock-Paper-Scissors", score)

# Word Guessing (Hangman Lite)
def word_guessing():
    words = ['python', 'hangman', 'computer', 'programming', 'algorithm', 'elephant', 'butterfly', 'mountain', 'ocean', 'galaxy', 'sunflower', 'telescope', 'keyboard', 'adventure', 'mystery', 'puzzle', 'journey', 'discovery', 'challenge', 'victory']
    word = random.choice(words)
    guessed_letters = set()
    attempts = 6
    score = 0
    
    print("Welcome to Word Guessing (Hangman Lite)!")
    print(f"The word has {len(word)} letters.")
    
    while attempts > 0:
        display = ''.join([letter if letter in guessed_letters else '_' for letter in word])
        print(f"\nWord: {display}")
        print(f"Attempts left: {attempts}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")
        
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        
        guessed_letters.add(guess)
        if guess in word:
            print("Good guess!")
            score += 10
        else:
            print("Wrong guess!")
            attempts -= 1
        
        if all(letter in guessed_letters for letter in word):
            print(f"\nCongratulations! You guessed the word: {word}")
            print(f"Your score: {score}")
            break
    else:
        print(f"\nGame over! The word was: {word}")
        score = 0
    
    save_option = input("Save your score? (y/n): ").lower()
    if save_option == 'y':
        save_score("Word Guessing", score)

# Simple Adventure Story
def adventure_story():
    score = 0
    stories = [
        {
            "intro": "You are a brave adventurer on a quest to find the lost city.",
            "level1": "Level 1: You encounter a fork in the road.",
            "level1_options": ["left", "right"],
            "level1_outcomes": ["You find a hidden map! +20 points", "You get lost in the forest! -10 points"],
            "level1_scores": [20, -10],
            "level2": "Level 2: A mysterious creature appears.",
            "level2_options": ["fight", "run"],
            "level2_outcomes": ["You befriend the creature! +30 points", "You find a shortcut. +10 points"],
            "level2_scores": [30, 10]
        },
        {
            "intro": "You are an explorer searching for ancient ruins.",
            "level1": "Level 1: You see a cave entrance.",
            "level1_options": ["enter", "climb"],
            "level1_outcomes": ["You discover artifacts! +25 points", "You reach a viewpoint! +15 points"],
            "level1_scores": [25, 15],
            "level2": "Level 2: A storm approaches.",
            "level2_options": ["shelter", "continue"],
            "level2_outcomes": ["You wait out the storm safely! +20 points", "You push through and find ruins! +35 points"],
            "level2_scores": [20, 35]
        }
    ]
    story = random.choice(stories)
    
    print("Welcome to the Simple Adventure Story!")
    print(story["intro"])
    
    # Level 1
    print(f"\n{story['level1']}")
    choice = input(f"Do you {story['level1_options'][0]} or {story['level1_options'][1]}? ").lower()
    while choice not in story['level1_options']:
        choice = input(f"Invalid choice. {story['level1_options'][0]} or {story['level1_options'][1]}? ").lower()
    
    index = story['level1_options'].index(choice)
    print(story['level1_outcomes'][index])
    score += story['level1_scores'][index]
    
    # Level 2
    print(f"\n{story['level2']}")
    choice = input(f"Do you {story['level2_options'][0]} or {story['level2_options'][1]}? ").lower()
    while choice not in story['level2_options']:
        choice = input(f"Invalid choice. {story['level2_options'][0]} or {story['level2_options'][1]}? ").lower()
    
    index = story['level2_options'].index(choice)
    print(story['level2_outcomes'][index])
    score += story['level2_scores'][index]
    
    print(f"\nAdventure complete! Your final score: {score}")
    if score > 30:
        print("🏆 Excellent adventurer!")
    elif score > 10:
        print("👍 Good job!")
    else:
        print("😞 Better luck next time!")
    
    save_option = input("Save your score? (y/n): ").lower()
    if save_option == 'y':
        save_score("Adventure Story", score)

# Main Menu
def main():
    while True:
        print("\n" + "="*40)
        print("Terminal-Based Python Games")
        print("="*40)
        print("1. Rock-Paper-Scissors")
        print("2. Word Guessing (Hangman Lite)")
        print("3. Simple Adventure Story")
        print("4. View High Scores")
        print("5. Exit")
        print("="*40)
        
        choice = input("Choose a game (1-5): ")
        if choice == '1':
            rock_paper_scissors()
        elif choice == '2':
            word_guessing()
        elif choice == '3':
            adventure_story()
        elif choice == '4':
            display_high_scores()
        elif choice == '5':
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Please select 1-5.")

if __name__ == "__main__":
    main()
