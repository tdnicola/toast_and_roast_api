from insults import generate_insult
from compliments import generate_compliment
import random

if __name__ == "__main__":
    choice = random.choice(["insult", "compliment"])
    
    if choice == "insult":
        print(generate_insult())
    else:
        print(generate_compliment())
