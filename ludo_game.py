import random

# Dictionary of company logos and their names
logos = {
    "apple": "Apple Inc.",
    "google": "Google Inc.",
    "facebook": "Facebook, Inc.",
    "amazon": "Amazon.com, Inc.",
    "microsoft": "Microsoft Corporation",
}

def play_logo_game():
    print("Welcome to the Guess the Logo game!")
    print("Can you guess the company based on its logo?")
    
    # Choose a random logo from the dictionary
    logo_name, company_name = random.choice(list(logos.items()))
    
    # Display the logo (you can replace this with actual logos)
    print(f"Guess the company: {logo_name.capitalize()}")
    
    # Ask the player to guess the company name
    guess = input("Your guess: ").strip().lower()
    
    # Check if the guess is correct
    if guess == logo_name:
        print(f"Congratulations! You guessed it. It's {company_name}.")
    else:
        print(f"Sorry, that's incorrect. It's {company_name}.")

if __name__ == "__main__":
    play_logo_game()
