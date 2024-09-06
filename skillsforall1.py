hour= int(input("Enter the Hours:"))
mins= int(input("Enter the Minutes:"))
dura= int(input("Enter the Duration(in Minutes) of the Program:"))
mins+=dura#doing the total of the minutes
hour = hour + mins // 60 # find a number of hours hidden in minutes and update the hour
mins = mins % 60 # correct minutes to fall in the (0..59) range
hour = hour % 24 # correct hours to fall in the (0..23) range
print(hour, ":", mins, sep='')
