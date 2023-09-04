# let's start with keyword { and }

''' score = int(input("score: "))

if score >= 90 and score <= 100:
    print("grade: A")

elif score >= 80 and score < 90: 
    print("grade: B")

elif score >=70 and score < 80: 
    print("grade: C")

elif score >=60 and score < 70: 
    print("grade: D")
    
else:
    print("grade: F") '''


# easier aternative of code above by asking less questions

''' score = int(input("score: "))

if score >= 90:
    print("grade: A")

elif score >= 80: 
    print("grade: B")

elif score >=70: 
    print("grade: C")

elif score >=60: 
    print("grade: D")
    
else:
    print("grade: F")  '''


score = int(input("score: ? "))

if score >= 90:
    print("grade: A")
elif score >= 80:
    print("grade: B")
elif score >= 70:
    print("grade: C") 
elif score >= 60:
    print("grade: D")
else:
    print("grade: F")         