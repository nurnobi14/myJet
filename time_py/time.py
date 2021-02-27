from datetime import *

now = datetime.now()
date = now.strftime("%d/%h/%Y")
print("date is :", date)
times = now.strftime("%I:%M %p")
print("Time is :",times)
