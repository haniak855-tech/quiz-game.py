print("welcome to my computer quiz")

playing=input("Do you want to play? ")

if playing != "yes":
    quit()

print("okay! Let's play :) ")

answer= input("what does CPU stand for? ")
if answer =="central processing unit":
    print('Correct!')
else:
    print("incorrect!")

answer= input("what does GPU stand for? ")
if answer =="graphics processing unit":
    print('Correct!')
else:
    print("incorrect!")

answer= input("what does RAM stand for? ")
if answer =="random access memory":
    print('Correct!')
else:
    print("incorrect!")