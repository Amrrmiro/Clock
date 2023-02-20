import time
import winsound

def timer():
    minutes = int(input("Enter the number of minutes: "))
    seconds = minutes * 60
    while seconds > 0:
        m, s = divmod(seconds, 60)
        print(f"Time remaining: {m:02d}:{s:02d}", end="\r")
        time.sleep(1)
        seconds -= 1
    print("Time's up!")
    winsound.Beep(1000, 1000)  # beep sound for 1 second

def stopwatch():
    start_time = time.time()
    while True:
        elapsed_time = time.time() - start_time
        m, s = divmod(elapsed_time, 60)
        h, m = divmod(m, 60)
        print(f"Elapsed time: {h:02d}:{m:02d}:{s:02f}", end="\r")
        time.sleep(0.1)

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
        print("Press Enter to stop the stopwatch")
        stopwatch()
        break
    else:
        print("Invalid input. Please enter 1 or 2.")