from os import get_terminal_size,system
from json import loads

for _ in range(get_terminal_size().columns):
    print("=",end="")
print("Breadboard communication utility\n[+] Christian Fiore")
for _ in range(get_terminal_size().columns):
    print("=",end="")

def code(msg):
    with open("dictionary.txt", "r") as f:
        dictionary = f.read()
    dictionary = loads(dictionary)
    
    translated = ""
    for c in msg:
        translated=translated+dictionary[c]+"\n"
    return translated

def decode(received):
    with open("dictionary.txt", "r") as f:
        dictionary = f.read()
    dictionary = loads(dictionary)
    msg = [i for i in dictionary if dictionary[i] == received]
    msg = msg[0]
    return msg


while True:
    print("\n1) Code\n2) Decode\n99) Quit")
    choice = int(input("> "))
    system('cls')

    if choice == 1:
        print("0) Message\n1) Service\n99) Quit")
        codChoice = int(input("> "))
        if codChoice == 0:
            msg = input("Enter message: ")
            print(code(msg))
        elif codChoice == 1:
            print("0) Communication start\n1) Communication end")
            codChoice = int(input("> "))
            if codChoice == 0:
                print("111111")
            elif codChoice == 1:
                print("111011")

    elif choice == 2:
        msg = ""
        print("Enter the received codes: ")
        while(True):
            received = input()
            if received == "111011":
                break
            msg = msg + received + " "
        msg = msg.split()
        translated = ""
        for c in msg:
            translated+=decode(c)
        print("\n\n"+translated)

    elif choice == 99:
        break

    else:
        print("Invalid choice")

