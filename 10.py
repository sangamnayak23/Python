# Countdown Timer using python programming language 

import time

print("⏳ Welcome to the Countdown Timer!")

# Get the countdown time from the user
seconds = int(input("Enter the number of seconds: "))

# Countdown loop
while seconds > 0:
    print("Time Left:", seconds, "seconds")
    time.sleep(1)  # Pause for 1 second
    seconds -= 1

# Display completion message
print("⏰ Time's up!")
print("Thank you for using the Countdown Timer!")
