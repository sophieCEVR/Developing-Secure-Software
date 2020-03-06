# File containing functions used for hashing (hash, salt, pepper, etc)

import hashlib  # Python hashing library for hashing functions
import random  # Used to add randomness to generation
from string import ascii_letters, digits  # Used to generate salt


def generate_salt(characters=(ascii_letters + digits), length=32):
    try:
        rand_gen = random.SystemRandom()  # Try to use random.SystemRandom()
    except NotImplementedError:
        rand_gen = random.Random()  # Use random.Random() if random.SystemRandom() is not available
    my_salt = str()
    for i in range(0, length, 1):  # Generate random alphanumeric characters
        my_salt += rand_gen.choice(characters)
    return my_salt


def generate_hash(text, salt='', pepper=''):
    # Using sha512 algorithm
    h = hashlib.sha512()
    h.update(str(text).encode())
    h.update(str(pepper).encode())
    result = h.hexdigest()  # result = hash_algorithm( text + pepper )
    h = hashlib.sha512()
    h.update(str(result).encode())
    h.update(str(salt).encode())
    result = h.hexdigest()  # result = hash_algorithm( hash_algorithm( text + pepper ) + salt )
    return result
