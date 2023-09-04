# intoduction of { % }
# when you devide something does it give any remainers
''' 
x = int(input("what's x?"))
if x % 2 == 0:
    print("even")

else:
    print("odd") '''

#bool is something that gives tru or false 
#bool is similar to float and int 

''' 
def main():
    x = int(input("what's x?"))
    if is_even(x):
        print("even")
    else:
        print("odd")

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False  
         
main() ''' 

# rewriting it again from m memory 

''' def main():
    x = int(input("what's x?"))
    if is_even(x):
      print("even")
    else: 
       print("odd")

def is_even(n):
   return True if n % 2 == 0 else False 

main() '''

# { match }
    
def main():
    x = int(input("what's x?"))
    if is_even(x):
        print("even")
    else:
        print("odd")

def is_even(n):
    return True if n % 2 == 0 else False 
    
main()

