# exception = An event that interrupts the flow of a program
#               (ZeroDivision, TypeError, ValueError)
#               1. try , 2. except , 3. finally

# try:
#       # try some code
# except Exception:
#       # Handle an Exception
# finally:
#       # Do some clean up


#
# try:
#     number = int(input("Enter a number: "))
#     print(1 / number)
# except ZeroDivisionError:
#     print("Undefined")
# except ValueError:
#     print("type a number")


try:
     number = int(input("Enter a number: "))
     print(1 / number)
except Exception:                               # usually a bad practice... because we are giving user a very broad range of errors to check.
     print("Something went wrong !")
finally:
    print("Do some cleanup")                    # always executes this block of code... whether there is an exception or not.

# https://docs.python.org/3/library/exceptions.html
