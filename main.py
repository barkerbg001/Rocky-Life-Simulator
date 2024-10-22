import random
import time
import threading
from plyer import notification

class PetRock:
    def __init__(self, name):
        self.name = name
        self.age = 0
        self.mood = "confused"
        self.coolness = 10
        self.insanity_level = 1
        self.accessories = self.random_accessory()
        self.actions = [
            "plotting world domination", 
            "having an existential crisis", 
            "wondering if it's actually a potato", 
            "hosting a rock concert (pun intended)", 
            "sitting majestically on a throne of dirt", 
            "staring into the void", 
            "inventing rock-based puns", 
            "rolling around for no reason", 
            "learning quantum mechanics"
        ]
        self.special_events = [
            "has discovered a new planet made of rocks", 
            "has been knighted by the Queen of Pebbles", 
            "was mistaken for a celebrity rock", 
            "won the ‘Best Rock Haircut’ award", 
            "started a rock revolution", 
            "got hired as a rock therapist"
        ]
        self.toaster = notification

    def random_accessory(self):
        accessories = ["tiny top hat", "cool sunglasses", "rockin' scarf", "a mini cape", "pet pebble", "wizard hat"]
        return random.choice(accessories)

    def display_status(self):
        print(f"Rock Name: {self.name}")
        print(f"Age: {self.age} rock years")
        print(f"Current Mood: {self.mood}")
        print(f"Coolness: {self.coolness}/100")
        print(f"Insanity Level: {self.insanity_level}/10")
        print(f"Accessory: {self.accessories}")
        print()

    def perform_action(self):
        action = random.choice(self.actions)
        print(f"{self.name} is currently {action}.")

    def update_mood(self):
        moods = [
            "ecstatic for no reason", 
            "confused about reality", 
            "too cool for this world", 
            "suspiciously calm", 
            "feeling like a superstar", 
            "ready to rock and roll", 
            "thinking it’s a philosopher"
        ]
        self.mood = random.choice(moods)

    def age_rock(self):
        self.age += 1
        self.coolness += random.randint(0, 5)  # Rocks get cooler with age, obviously
        self.insanity_level += random.randint(0, 2)  # Rocks slowly go insane over time

    def special_event(self):
        if random.random() > 0.8:  # 20% chance of a special event
            event = random.choice(self.special_events)
            print(f"SPECIAL EVENT: {self.name} {event}!")
            # Send a notification about the special event
            self.toaster.notify(
                title=f"Special Event for {self.name}!",
                message=f"{self.name} {event}!",
                timeout=5
            )
            print()

    def rock_birthday(self):
        if self.age % 5 == 0 and self.age > 0:
            print(f"\n🎉 BIRTHDAY ALERT: {self.name} is now {self.age} rock years old! Time to celebrate with a rock party! 🎉\n")
            new_accessory = self.random_accessory()
            print(f"{self.name} now has a new accessory: {new_accessory}!")
            self.accessories = new_accessory
            # Send a notification for the birthday
            self.toaster.notify(
                title=f"{self.name}'s Birthday!",
                message=f"{self.name} is now {self.age} rock years old! 🎉",
                timeout=5
            )

    def automatic_rock_paper_scissors(self):
        """Play rock-paper-scissors with a random opponent."""
        options = ['rock', 'paper', 'scissors']
        rock_choice = random.choice(options)
        opponent_choice = random.choice(options)

        # Display the choices and automatically determine the outcome
        print(f"{self.name} found another rock to battle!")
        print(f"{self.name} chose {rock_choice}, and the opponent chose {opponent_choice}.")

        if rock_choice == opponent_choice:
            print(f"Both chose {rock_choice}. It's a tie!")
        elif (rock_choice == "rock" and opponent_choice == "scissors") or \
             (rock_choice == "scissors" and opponent_choice == "paper") or \
             (rock_choice == "paper" and opponent_choice == "rock"):
            print(f"{self.name} wins!")
        else:
            print(f"{self.name} loses!")
        print()

    def challenge_to_rock_paper_scissors(self):
        """Challenge the user to Rock-Paper-Scissors, with a timeout for automatic play."""
        if random.random() > 0.9:  # 10% chance to challenge
            print(f"\n💥 {self.name} challenges you to a Rock-Paper-Scissors duel! 💥\n")
            self.toaster.notify(
                title=f"{self.name} Challenges You!",
                message=f"{self.name} wants to play Rock-Paper-Scissors!",
                timeout=5
            )

            options = ['rock', 'paper', 'scissors']

            # Shared variable to store user choice
            user_choice = [None]

            # Function to get user input
            def get_user_choice():
                try:
                    choice = input("Choose rock, paper, or scissors: ").strip().lower()
                    if choice in options:
                        user_choice[0] = choice
                    else:
                        user_choice[0] = None
                except:
                    user_choice[0] = None

            # Start input thread
            input_thread = threading.Thread(target=get_user_choice)
            input_thread.daemon = True
            input_thread.start()

            # Wait for user input with timeout
            input_thread.join(timeout=5)

            if user_choice[0] is None:
                print(f"{self.name} waited too long... challenging another rock instead!")
                self.automatic_rock_paper_scissors()
            else:
                rock_choice = random.choice(options)
                print(f"You chose {user_choice[0]}, and {self.name} chose {rock_choice}.")
                if user_choice[0] == rock_choice:
                    print(f"Both chose {rock_choice}. It's a tie!")
                elif (user_choice[0] == "rock" and rock_choice == "scissors") or \
                     (user_choice[0] == "scissors" and rock_choice == "paper") or \
                     (user_choice[0] == "paper" and rock_choice == "rock"):
                    print("You win!")
                else:
                    print(f"{self.name} wins!")
            print()

    def live_life(self):
        """Simulate the rock's life in a loop."""
        while True:
            self.display_status()
            self.perform_action()
            self.update_mood()
            self.age_rock()
            self.special_event()
            self.rock_birthday()
            self.challenge_to_rock_paper_scissors()
            time.sleep(5)  # Give it a bit of time between actions

def user_interaction(rock):
    """Allow the user to interact with the rock in a separate thread."""
    while True:
        user_input = input("\nPress 's' to see status or 'q' to quit: ").lower()
        if user_input == 's':
            rock.display_status()
        elif user_input == 'q':
            print(f"\n{rock.name} will now retreat to its majestic rock throne. Goodbye!")
            # Exit the program gracefully
            # Since live_life is running on a daemon thread, exiting main thread will terminate it
            import os
            os._exit(0)
        else:
            print("Invalid input. Please try again.")

def main():
    name = input("What would you like to name your rock overlord? ")
    rock = PetRock(name)
    
    print(f"\nAll hail {name} the all-powerful rock!\n")

    # Create two threads: one for the rock's life and one for user interaction
    life_thread = threading.Thread(target=rock.live_life)
    life_thread.daemon = True  # Daemonize thread to exit when main thread exits
    interaction_thread = threading.Thread(target=user_interaction, args=(rock,))
    
    # Start both threads
    life_thread.start()
    interaction_thread.start()

    # Wait for the interaction thread to finish (when the user quits)
    interaction_thread.join()

if __name__ == "__main__":
    main()
