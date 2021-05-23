import random
import time

print("""*****************
Random Number Estimate

Around 1-40
***************** """)

random_no = random.randint(1,40)
estimate_no=7
while (True):
    estimate =int(input("Let guess:"))
    if(0 < estimate <= 40):
        if (estimate< random_no):
            print("Checking...")
            time.sleep(1)
            print("Guess bigger than yours")
            estimate_no -= 1

        elif(estimate> random_no):
            print("Checking...")
            time.sleep(1)
            print("Guess less than yours")
            estimate_no -= 1
        else:
            print("Checking...")
            time.sleep(1)
            print("Congratulations",random_no)
            break
    else:
        print("Wrong Number")
        estimate_no -= 1
    if(estimate_no==0):
        print("You have no chance")
        print("No:",random_no)
        break
    


