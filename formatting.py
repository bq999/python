#Formatting

from datetime import datetime

def main():
 # Times and dates can be formatted using a set of predefined string
  # control codes 
  now = datetime.now() # get the current date and time



  #### Date Formatting ####
  
  # %y/%Y - Year, %a/%A - weekday, %b/%B - month, %d - day of month
  print(" ")
  print("Date Formatting")
  print (now.strftime("%Y")) # full year with century
  print (now.strftime("%a, %d %B, %y")) # abbreviated day, num, full month, abbreviated year



  # %c - locale's date and time, %x - locale's date, %X - locale's time
  print(" ")
  print("Local Time")
  print (now.strftime("%c"))
  print (now.strftime("%x"))
  print (now.strftime("%X"))


#### Time Formatting ####
  
  # %I/%H - 12/24 Hour, %M - minute, %S - second, %p - locale's AM/PM
  print(" ")
  print("Time Formatting")
  print (now.strftime("%I:%M:%S %p")) # 12-Hour:Minute:Second:AM
  print (now.strftime("%H:%M")) # 24-Hour:Minute


  
if __name__ == "__main__":
  main();
