import time
from time import gmtime, strftime
s = strftime("%a, %d %b %Y %H:%M:%S", 
             gmtime(time.time()))
obj = time.strptime(s, "%a, %d %b %Y %H:%M:%S")
print(obj.tm_hour+5)
