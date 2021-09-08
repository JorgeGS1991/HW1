
""""This is my code for homewoork 1 """
#import datatime
from datetime import datetime

#get the lines stap fro today
today = datetime.now()

month_name = today.strftime("%B")


#Extract the day of the month as a number from today's date
day_number = today.day

if day_number == 1 or 21 or 31:
    suffix = "st"

elif day_number == 2 or 22:
    suffix = "nd"

elif day_number == 3 or 23:
    suffix = "rd"
else:
    suffix = "th"


print(suffix)
#extract the year as a number from today's date
year_number = today.year


if day_number% 2 == 0:
    day_type = "even"
else:
    day_type = "odd"

print("Hello. Todays Date is", month_name, str(day_number), suffix, "of", str(year_number),
      "The product of the month and day is", today.month * day_number, "which is an", day_type, "number.")


#Loop
#Define n-1
n = 1
#While  n< day_number
while n <= day_number:
    print(n)

# n= n-1
    n = n + 1
#End Loop

#Print days
print ("days")




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
