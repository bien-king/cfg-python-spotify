import requests
import random
from pprint import pprint

def generate_rand_int(min,max):
    random_int = random.randint(min,max)
    return random_int

def get_characters():
    url = "http://hp-api.herokuapp.com/api/characters"
    response = requests.get(url)
    characters = response.json()
    return characters

def get_random_character():
    my_int = generate_rand_int(min=0, max=24)
    characters = get_characters()
    random_character = characters[my_int]
    pprint("User ID: %d" % my_int)
    pprint(random_character)

get_random_character()

