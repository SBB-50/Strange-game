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
    print(f"{narr}: no you cant now let the story go on dipshit")
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
print(" \x1B[3m you look around  \x1B[3m")
print(" \x1B[3m jk you cant you literally don't have eyes\x1B[3m")
print(" \x1B[3m you feel energy coming from different spots around you \x1B[3m")
print(" \x1B[3m the biggest source is to your left, the second largest is in front of you, and the smallest is behind you \x1B[3m")
direct = input("where would you like to investigate? (right/left/forward/back)")
#italic template print(" \x1B[3m \x1B[3m")
