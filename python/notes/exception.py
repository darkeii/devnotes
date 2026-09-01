# exception = An event that interrupts the flow of a program
#               (ZeroDivision, TypeError, ValueError)
#               1. try , 2. except , 3. finally

# try:
#       # try some code
# except Exception:
#       # Handle an Exception
# finally:
#       # Do some clean up


number = int(input("Enter a number: "))
try:
    print(1 / number)
except ZeroDivisionError:
    print("Undefined")
except ValueError:
    print("type a number")



