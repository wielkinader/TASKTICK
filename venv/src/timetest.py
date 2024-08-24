from datetime import *
currenttime = datetime.now()
newtime = currenttime + timedelta(hours = 24)
print(currenttime < newtime)

if currenttime < newtime:
    print('yes')
elif newtime < currenttime:
    print('noo')