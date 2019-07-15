import simplejson as json
import difflib
from difflib import get_close_matches

def load_JSON_File(filePath):
        try:
            data = json.load(open(filePath))
        except FileNotFoundError as e:
            print(e)
            exit()
        return data


def find_Key_Value_Pair(data,key=""):
        if key=="" and type(str)==str:
            return print("blank Key value or not string type")

        value = data.get(key)
        if str(value)!="None":
             print_Defination(value)
             return
        else:
            close_matches=get_close_matches(key,data.keys())
            if len(close_matches)==0:
                print("Invalid word")
                return
            else:
                for word in close_matches:
                    while(True):
                        yn=input("Did you mean this word: %s ? please enters y for yes or n for no\n"%word).lower()
                        if yn=="y":
                            print_Defination(data.get(word))
                            return
                        if yn=="n":
                            break
                        else:
                            print("please type the letter y or n for the word %s"%word)
                            continue

def print_Defination(value):
     for line in value:
         print(str(line))


data=load_JSON_File("data.json")
print("To exit the system type: exit please")

exit=True
while(exit!=False):
    key=input("Please enter a word:\n ").lower()
    if key=="exit please":
        exit=False
        continue
    else:
        value=find_Key_Value_Pair(data,key)
