# Countdown Timer using python programming language 

import time

seconds = int(input("Enter countdown time in seconds: "))

# Start countdown
while seconds > 0:
    print("Time left:", seconds, "seconds")
    time.sleep(1)
    seconds -= 1

print("Time's up! ⏰")
