
import random
characters = ["a brave knight", "a curious scientist", "an adventurous pirate", "a clever detective","a mischievous elf"]
settings = ["in a haunted castle", "on a distant planet", "in a deep jungle", "inside ahidden cave", "on a mysterious island"]
events = ["found a hidden treasure", "discovered a magical portal", "solved a centuries-old mystery", "escaped a dangerous trap", "met an unknown creature"]

def generate_story():
    character = random.choice(characters)
    setting = random.choice(settings)
    event = random.choice(events)
    return f"one day, {character} was, {setting} when they {event}"
    return story

if __name__ == "__main__":
    print(generate_story())
