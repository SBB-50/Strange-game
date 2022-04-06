#imports
import time
import arcade

#constant vars
schght = 600
scwdth = 800
title = "game lmao"
rad = 150
narr = "Narrator"
#code i guess


print(f"{narr}: hello, what is your name?")
ans = input("")
print(f"{narr}: {ans}. that is one of the names ever!")
print(f"{narr}: anyways,")
time.sleep(0.5)
print(f"{narr}: do you know what you are here for?")
ans = input("y/n ")
if ans == "y":
    print(f"{narr}: oh?")
    time.sleep(1)
    print(f"{narr}: can you tell me then?")
    time.sleep(0.5)
    print(f"{narr}: no you cant now restart and let the story go on dipshit")
if ans == "n":
    print(f"{narr}: no?")
    time.sleep(1)
    print(f"{narr}: ok then,")
    time.sleep(0.5)
    print(f"{narr}: you are here to complete the game.")
    time.sleep(1)
    print(f"{narr}: but you can't do that without a body.")
    time.sleep(2)
    print(f"{narr}: so that is your goal for now.")
    time.sleep(1)
    print(f"{narr}: to find a usable body, that is.")
    uselessvar = input("(press enter to continue)")

#
