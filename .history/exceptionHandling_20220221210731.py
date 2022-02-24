'''try:
except
else
finally'''

try:
    print("Execute this code ", 1/0)
except ZeroDivisionError:
    print("Handle exception 1")
except TypeError:
    print("Handle exception 2")
except Exception:
    print("Handle exception3")
except:
    print("Handle exception4")
else:
    print("Execute this code")
finally:
    print("Execute every time")
    
    
BaseException
SystemExit / Exception / KeyboardInterrupt
ValueError / LookupError / ArithmeticError
ImportError / KeyError / ZeroDivisionError