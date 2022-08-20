import time

n = int(input("Enter the time in minutes: "))
n = int(n * 60)

while n:
    minutes = n//60
    seconds = n % 60
    timer = '{:02d}:{:02d}'.format(minutes, seconds)
    print(timer, end="\r")
    time.sleep(1)
    n -= 1
print("Time's up")
