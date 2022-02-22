#!/usr/bin/env python3
# BTTUSJ 55
import subprocess
import urllib.request as urllib2
import re
import urllib
import os
import time
import base64
import requests

def get_sign(sign):
    result = ""
    if (sign == "+"):
        result = "+"
    elif (sign == "-"):
        result = "-"
    elif (sign == "/"):
        result = "/"
    elif (sign == "*"):
        result = "*"
    else:
        print("[ INFO ] Relance ta requête !")
    return result


def get_number():
    pass
    # WAITING FOR MOTIVATION


# Get infos from source code
# f = open("source.get", "r")
# file = f.read()
# f.close()

# Get source code from python request
headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "deflate, gzip, br",
    "Accept-Language": "en-US",
    "USER AGENT HEEERRRRE",
    "X-equested-With": "XMLHttpRequest",
    }
url = "NO SPOIL (even if my code doesn't work"
print(f"[+] Requesting URL: {url}")
response = requests.get(url, headers = headers, timeout = 10)
file = response.text


# Src code reading
fin_fichier = []
for i in range(217, len(file)):  # Throw the beginning of the packet
    fin_fichier.append(file[i])
is_positive = False
is_negative = False
# Check sign of Un+1 first member
if (fin_fichier[0] == "-"):
    compteur = 1
    is_negative = True
elif (fin_fichier[0] == "+"):
    compteur = 1
    is_positive = True
else:
    compteur = 0

foo = []  # For random storage
while (fin_fichier[compteur].isnumeric() == True):
    foo.append(fin_fichier[compteur])
    compteur += 1

# Capture the first number (definitly too long, but it works so...)
if (len(foo) == 1):
    first_member = int(foo[0])
elif (len(foo) == 2):
    first_member = ( int(foo[0]) * 10 ) + int(foo[1])
elif (len(foo) == 3):
    first_member = ( ( int(foo[0]) * 100 ) + ( int(foo[1]) * 10 ) + int(foo[2]) )
else:
    print("[ INFO ] Relance ta requête")

if (is_negative == True):
    print("le nombre est négatif ou positif mais avec un signe spécifié")
    # On doit passer en négatif
    first_member -= first_member * 2
else:
    print("Il n'y a pas de signe spécifié")  # Alles gut leute !

compteur += 1
first_sign = get_sign(fin_fichier[compteur])
compteur += 18
second_sign = get_sign(fin_fichier[compteur])
compteur += 6
third_sign = get_sign(fin_fichier[compteur])
compteur += 2

is_positive = False
is_negative = False
if (fin_fichier[compteur] == "-"):
    compteur += 1
    is_negative = True
elif (fin_fichier[compteur] == "+"):
    is_positive = True
    compteur += 1
else:
    pass
foo = []  # For random storage
compteur

while (fin_fichier[compteur].isnumeric() == True):
    foo.append(fin_fichier[compteur])
    compteur += 1
# Capture the first number (definitly too long...)
if (len(foo) == 1):
    last_member = int(foo[0])
elif (len(foo) == 2):
    last_member = ( int(foo[0]) * 10 ) + int(foo[1])
elif (len(foo) == 3):
    last_member = ( ( int(foo[0]) * 100 ) + ( int(foo[1]) * 10 ) + int(foo[2]) )
else:
    print("[ INFO ] Relance ta requête")

if (is_negative == True):
    print("le nombre est négatif ou positif mais avec un signe spécifié")
    # On doit passer en négatif
    last_member -= last_member * 2
else:
    print("Il n'y a pas de signe spécifié")  # Alles gut!

compteur += 25
foo = []
while (fin_fichier[compteur].isnumeric() == True):
    foo.append(fin_fichier[compteur])
    compteur += 1

if (len(foo) == 1):
    base_number = int(foo[0])
elif (len(foo) == 2):
    base_number = ( int(foo[0]) * 10 ) + int(foo[1])
elif (len(foo) == 3):
    base_number = ( ( int(foo[0]) * 100 ) + ( int(foo[1]) * 10 ) + int(foo[2]) )
else:
    print("[ INFO ] Relance ta requête")

if (is_negative == True):
    print("le nombre est négatif ou positif mais avec un signe spécifié")
    # On doit passer en négatif
    base_number -= base_number * 2
else:
    print("Il n'y a pas de signe spécifié")  # Alles gut!

compteur += 27
foo = []
while (fin_fichier[compteur].isnumeric() == True):
    foo.append(fin_fichier[compteur])
    compteur += 1

if (len(foo) == 6):
    road_to = ( ( int(foo[0]) * 100000 ) + ( int(foo[1]) * 10000 ) + ( int(foo[2]) * 1000 ) + ( int(foo[3]) * 100 ) + ( int(foo[4]) * 10 ) + int(foo[5]) )
else:
    print("[ INFO ] Relance ta requête")

if (is_negative == True):
    print("le nombre est négatif ou positif mais avec un signe spécifié")
    # On doit passer en négatif
    road_to -= road_to * 2
else:
    print("Il n'y a pas de signe spécifié")  # Alles gut!


# FINAL RÉSULT!
print(f"({first_member} {first_sign} {base_number}) {second_sign} ({road_to} {third_sign} {last_member})")

# Un+1 = [first_member first_sign base_number] second_sign [road_to third_sign last_member]
# U0 = base_number
# U(road_to)

# (dis)assemble

for i in range(road_to):
    base_number = (first_member + base_number) - (road_to * last_member)
print(base_number)

# VALIDATION

bashCommand = f"LOLILOL, challenge web site isn't here either"
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
output, error = process.communicate()
