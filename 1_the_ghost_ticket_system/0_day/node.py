import time
import random
import os
import sys

FILENAME = 'tickets.txt'
NODE_NAME = sys.argv[1]
if not os.path.exists(FILENAME):
    with open(FILENAME, 'w') as f: f.write("100")

def sell_tickets():
    total_ticket_sold = 0
    for i in range(30):
        # Read file

        with open(FILENAME, 'r') as f:
            count = int(f.read().strip())

        if count > 0:
            # network delays
            time.sleep(random.uniform(0.5, 0.9))

            # write new value to file
            new_count = count - 1
            with open(FILENAME, 'w') as f: f.write(str(new_count))
            total_ticket_sold += 1
            print(f"[{NODE_NAME}] Sold 1! (File says: {new_count})")
        else:
            print(f"{NODE_NAME} sold out")
            break

        print(f"Total ticket sold by {NODE_NAME} is: {total_ticket_sold}")


sell_tickets()
