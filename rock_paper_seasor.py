import random
import sys

class RockPaperScissors:
    def __init__(self):
        # Game choices aur unke proper string names map kiye hain
        self.choices = {"1": "rock", "2": "paper", "3": "scissor"}
        # Score counters jo professional portfolio scripts mein zaroori hote hain
        self.player_score = 0
        self.computer_score = 0
        self.ties = 0

    def display_header(self):
        """Game ka professional welcome header display karne ke liye."""
        print("\n" + "=" * 50)
        print("    🎰 WELCOME TO ROCK, PAPER, SCISSORS GAME 🎰    ")
        print("=" * 50)
        print(f"📊 CURRENT SCORE | You: {self.player_score} | Computer: {self.computer_score} | Ties: {self.ties}")
        print("-" * 50)

    def get_user_choice(self):
        """User ke input ko validate aur clean karne ke liye."""
        print("1. 🪨 Rock")
        print("2. 📄 Paper")
        print("3. ✂️ Scissor")
        print("4. ❌ Exit Game")
        print("-" * 50)
        
        user_input = input("Enter Your Choice (1-4): ").strip()
        return user_input

    def process_game_logic(self, you, computer):
        """Core algorithmic logic handles game outcome."""
        if you == "4":
            print(f"\n👋 Final Score -> You: {self.player_score} | Computer: {self.computer_score}")
            print("Game Over. Thanks for playing!")
            sys.exit()
            
        if you not in self.choices:
            print("\n❌ Invalid choice! Please select a valid number between 1 and 4.")
            return

        you_name = self.choices[you].capitalize()
        computer_name = self.choices[computer].capitalize()

        print(f"\n👉 You chose: {you_name}")
        print(f"🤖 Computer chose: {computer_name}")
        print("." * 30)

        # Winning conditions for the user
        if (you == "1" and computer == "3") or \
           (you == "3" and computer == "2") or \
           (you == "2" and computer == "1"):
            print("🥇 Outcome: You Win! 🥳")
            self.player_score += 1
            
        elif you == computer:
            print("🤝 Outcome: It's a Tie! 😂")
            self.ties += 1
            
        else:
            print("🤖 Outcome: Computer Wins! 🥺")
            self.computer_score += 1

    def start(self):
        """Main loop execution entry point."""
        while True:
            self.display_header()
            user_choice = self.get_user_choice()
            computer_choice = random.choice(["1", "2", "3"])
            self.process_game_logic(user_choice, computer_choice)

# Game ko run karne ke liye main entry point block
if __name__ == "__main__":
    game = RockPaperScissors()
    game.start()
    