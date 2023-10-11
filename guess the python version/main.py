import random

version_1 = random.randint(1,4)
version_2 = random.randint(1,4)
version_3 = random.randint(1,4)
#print(version_1,version_2,version_3)

tries = 0

correct_1 = False
correct_2 = False
correct_3 = False
while True:
    #✅Checking if 3 parts of the version is correct then breaking from the loop
    if correct_1 and correct_2 and correct_3:
        break
    #✅Checking if 3 parts of the version is correct then breaking from the loop
    
    #✅Input prompt 
    print("Enter python version ",end="")
    if correct_1 == True:
        print(version_1,".",end = "")
    else:
        print("XX.",end = "")
    if correct_2 == True:
        print(version_2,".",end = "")
    else:
        print("XX.",end = "")
    if correct_3 == True:
        print(version_3,end = "")
    else:
        print("XX",end = "")
    print("( XX = [1,4] ):",end = "")
    #✅Input prompt
    
    #✅Taking input and converting it to 3 seperate numbers
    n = input()
    n = n.split('.')
    for i in range(3):
        n[i] = int(n[i])
    #print(n)
    #✅Taking input and converting it to 3 seperate numbers
    
    #✅updating correct variable and tries variable
    if n[0]==version_1:
        correct_1 = True
    if n[1]==version_2:
        correct_2 = True
    if n[2]==version_3:
        correct_3 = True
    tries+=1
    #✅updating correct variable and tries variable
#Print Rank
print("Rank:",end = "")
if tries == 1:
    print("General(Highest Rank)")
if tries>=2 and tries<=4:
    print("Lieutenant General(2nd Highest Rank)")
if tries>=5 and tries<=7:
    print("Major General(3rd Highest Rank)")
if tries>=8 and tries<=11:
    print("Brigadier General")
if tries>=12 and tries<=15:
    print("Colonel")
if tries>=16 and tries<=20:
    print("Lieutenant Colonel")
if tries>=21 and tries<=25:
    print("Major")
if tries>=26 and tries<=30:
    print("Captain")
if tries>=31 and tries <=35:
    print("Lieutenant")
if tries>=36 and tries<=40:
    print("Second Lieutenant")
if tries>=41 and tries<=45:
    print("Master Warrant Officer")
if tries>=46 and tries<=50:
    print("Senior Warrant Officer")
if tries>=51 and tries<=55:
    print("Warrant Officer")
if tries>=56 and tries<=60:
    print("Sergeant")
if tries>=61 and tries<=65:
    print("Corporal")
if tries>=66 and tries<=70:
    print("Lance Corporal")
if tries > 70:
    print("Soldier(Lowest Rank)")
#Print Rank
print("You Guessed the version in",tries,"try(tries)")