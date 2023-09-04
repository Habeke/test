# this is input to ask people for their names 
'''name = input("what's your name?").strip().title()'''

# so it will print out any input was putten in it

"""print("hello," + name) 

print("hello")
print(name) 

print("hello," + name , sep="") """  

#spliting names creating some space between them

'''first, last = name.split(" ")'''

# removing whitespace from str
 #name = name.strip()

# makes very first letter capital
#name = name.capitalize()

  # name = name.title()
    #name = name.strip().title() 

#print(f"hello, {name}")  

'''print("hello, "+ first + last)   

age = input("what's your age?").strip()
print("so your age is " + age)'''

# creating your own function is by typing def 

''' def hello(to="world"):
    print("hello,", to)

hello()
name = input("what's your name?").strip().title() 
hello(name) '''
 

''' def hello():
    print("HI" , name) 

name = input("what's your name ?").strip().title()

hello()

age = input("what's your age ?")

print(f"so your age is {age}") '''


'''def options():
    input("what would you choose?")

print("what is your type in a relationshiop?")
options()'''

# def is for define 


def main():
    name = input("what's your name ?")
    hello(name) 
     

def hello(to="guys"):
    print("hello", to)   

main()