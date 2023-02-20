import time

def timer():
    minutes = int(input("Enter the number of minutes: "))
    seconds = minutes * 60
    while seconds > 0:
        m, s = divmod(seconds, 60)
        print(f"Time remaining: {m:02d}:{s:02d}", end="\r")
        time.sleep(1)
        seconds -= 1
    print("Time's up!")

def stopwatch():
    start_time = time.time()
    input("Press Enter to stop the stopwatch")
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time:.2f} seconds")

# Main program
print("Choose an option:")
print("1. Timer")
print("2. Stopwatch")

while True:
    choice = input("Enter your choice (1 or 2): ")
    if choice == "1":
        timer()
        break
    elif choice == "2":
        stopwatch()
        break
    else:
        print("Invalid input. Please enter 1 or 2.")