# Digital Clock using python programming language 

import time

# Display the current time
while True:
    current_time = time.strftime("%H:%M:%S")

    # Print the time
    print("Current Time:", current_time)

    # Wait for one second
    time.sleep(1)
