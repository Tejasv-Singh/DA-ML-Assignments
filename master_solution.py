import random

def master_guess_game():
    print("\n--- WELCOME TO THE MASTER GUESSING GAME ---")
    
    while True:  # 1. THE GAME LOOP (Allows Replay)
        secret_number = random.randint(1, 10)
        attempts = 3
        print("\nI'm thinking of a number between 1 and 10.")
        
        while attempts > 0:  # 2. THE TURN LOOP
            user_input = input(f"Guess the number ({attempts} tries left): ")
            
            # 3. INPUT VALIDATION (Doesn't burn a life for typos!)
            if not user_input.isdigit():
                print("Please enter a valid integer!")
                continue # Skips to next loop iteration
            
            guess = int(user_input)
            
            # 4. RANGE CHECK
            if guess < 1 or guess > 10:
                print("Hey! Stay between 1 and 10.")
                continue

            # 5. WIN LOGIC
            if guess == secret_number:
                print(f"You won! The number was {secret_number}!")
                break # Exits the TURN loop
            else:
                attempts -= 1 # Only penalize valid, wrong guesses
                if attempts > 0:
                    # 6. HINTS (Smart UX)
                    if guess > secret_number:
                        print("Too high!")
                    else:
                        print("Too low!")
        
        # 7. GAME OVER (Using else on loop or checking attempts)
        if attempts == 0:
            print(f" Game Over! The secret number was {secret_number}.")
            
        # 8. PLAY AGAIN?
        again = input("\nPlay again? (y/n): ").lower()
        if again != 'y':
            print("Thanks for playing! ")
            break # Exits the GAME loop

if __name__ == "__main__":
    master_guess_game()
