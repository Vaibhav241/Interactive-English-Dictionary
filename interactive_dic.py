import json
import difflib
from difflib import get_close_matches as close

data=json.load(open("G:\\Python\\Codes\\app1\\data.json","r"))

def print_d(name):
    if name in data:
        l1=data[name]
        for x in l1:
            print(x)
    elif name.title() in data:
            l1=data[name.title()]
            for x in l1:
                print(x)
    elif name.upper() in data:
        l1=data[name.upper()]
        for x in l1:
            print(x)
    elif len(close(name,data.keys(),1,0.8))!=0:
        word=close(name,data.keys(),1)[0]
        v=input("Did you mean {} instead? Enter Y if yes or N if no: ".format(word)).lower().lstrip().rstrip()
        if(v=="y"):
            print_d(word)
        elif(v=='n'):
            print("The word doesn't exist. Please double check it.")
        else:
            print("We didn't understand your entry.")
    else:
        print("The word doesn't exist. Please double check it.")

a=input("Enter the word: ").lower().rstrip().lstrip()
print_d(a)
