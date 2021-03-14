import random
import pickle

alphabets = "abcdefghijklmnopqrstuvwxyz"

r1 = list(alphabets)
random.shuffle(r1)
r1 = "".join(r1)

r2 = list(alphabets)
random.shuffle(r2)
r2 = "".join(r2)

r3 = list(alphabets)
random.shuffle(r3)
r3 = "".join(r3)


f = open("rotor_state.enigma","wb")
pickle.dump((r1,r2,r3),f)
f.close() 
