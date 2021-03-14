import pickle

alphabets = "abcdefghijklmnopqrstuvwxyz"

def load_data():
    global r1,r2,r3
    f = open("rotor_state.enigma","rb")
    r1 , r2 , r3 = pickle.load(f)
    print(r1)
def reflector(c):
    return alphabets[len(alphabets) - alphabets.find(c)-1]

def enigma_code(c):
   global r1 , r2 , r3
   c1  = r1[alphabets.find(c)]
   c2  = r2[alphabets.find(c1)]
   c3  = r3[alphabets.find(c2)]
   
   reflected_c = reflector(c3)
   
   c3 = alphabets[r3.find(reflected_c)]
   c2 = alphabets[r2.find(c3)]
   c1 = alphabets[r1.find(c2)]
   result = c1
   return result


def rotate_rotors():
    global r1 , r2 , r3
    r1 = r1[1:] + r1[0]
    if counter % 26:
        r2 = r2[1:] + r2[0]
    if counter % (26*26):
        r3 = r3[1:] + r3[0]
 


load_data()
while True:

    plain = input("enigma~")
    cipher = ""
    counter = 0

    for c in plain:
        
        if c == " ":
            cipher += " "
        
        elif c == "!":
            exit()

        elif c == "#":
            import rotor 
            open("rotor_state.enigma","rb")
            load_data()
            print(r1)
        else: 
            counter += 1    
            cipher += enigma_code(c)
            rotate_rotors()

    print(cipher)
