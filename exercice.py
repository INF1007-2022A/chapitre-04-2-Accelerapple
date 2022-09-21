#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def get_first_part_of_name(name):
	premier_nom = name.split("-")
	premier_nom = premier_nom[0].lower().capitalize()
	return premier_nom

def get_random_sentence(animals, adjectives, fruits):
	animal = random.choice(animals)
	adjectif = random.choice(adjectives)
	fruit = random.choice(fruits)
	return f"Aujourd’hui, j’ai vu un {animal} s’emparer d’un panier {adjectif} plein de {fruit}."

def encrypt(text, shift):
	resultat = ""
	text_maj = text.upper()
	for letter in text_maj:
		if letter.isalpha():
			letter_chiffre = ord(letter)
			letter_chiffre += shift
			if letter_chiffre > 90:
				letter_chiffre -= 26
			elif letter_chiffre < 65:
				letter_chiffre += 26
			letter = chr(letter_chiffre)
		resultat += letter
	return resultat

def decrypt(encrypted_text, shift):
	not_chiffre = -shift
	return encrypt(encrypted_text, not_chiffre)


if __name__ == "__main__":
	parrot = "jEaN-MARC"
	print(f"Pour {parrot}, on a '{get_first_part_of_name(parrot)}'.")

	animals = ("chevreuil", "chien", "pigeon")
	adjectives = ("rouge", "officiel", "lourd")
	fruits = ("pommes", "kiwis", "mangue")
	print(get_random_sentence(animals, adjectives, fruits))
	
	print(encrypt("ABC", 1))
	print(encrypt("abc 123 XYZ", 3))
	print(decrypt("DEF 123 ABC", 3))
