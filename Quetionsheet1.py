#good morning program according to the time

import time
'''timestamp = int(time.strftime('%H:%M:%S'))
print(timestamp)'''
timestamp=int(time.strftime('%H'))
print(timestamp)
'''timestamp=int(time.strftime('%M'))
print(timestamp)
timestamp=int(time.strftime('%S'))
print(timestamp)'''
if ( timestamp>0 and timestamp<12):
    print("Good Morning sir!!")
elif(timestamp >= 12 and timestamp <= 19):
    print("Good afternoon sir !!")
    if(timestamp >= 19 and timestamp <= 21):
        print("Good Evening Sir !!")
else:
    print("Good Night!!")
