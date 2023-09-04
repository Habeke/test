# match 

''' 
name = input("what's your name?")

if name == "haba" or name == "jako":
    print("shymkent")
elif name == "kana":
    print("almaty")
elif name == "nur":
    print("shu")
else: 
    print("who???") '''

''' name = input("what's your name ?")

match name: 
    case "haba" | "jako" | "aiba":
        print("shymkent")
    case "kana":
        print("almaty")
    case _: 
        print("who??") ''' 

name = input("what's your name ?")

match name: 
    case "haba" | "koko" | "lola": 
        print("from Shym")
    case "kana" | "nurbek":
        print("ALmaty")
    case _: 
        print("Unknown city")