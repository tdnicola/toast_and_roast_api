import random
import os

def load_words(filename):
    path = os.path.join(os.path.dirname(__file__), filename)
    with open(path, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f if line.strip()]

adjectives = load_words('adjectives.txt')
nouns = load_words('nouns.txt')
openings = load_words('openings.txt')
templates = load_words('templates.txt')

def generate_insult():
    template = random.choice(templates)
    return template.format(
        opening=random.choice(openings),
        adjective=random.choice(adjectives),
        noun=random.choice(nouns)
    )
