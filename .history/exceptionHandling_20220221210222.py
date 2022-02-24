'''try:
except
else
finally'''

try:
    print("Execute this code ", 1/0)
except ZeroDivisionError:
    print("Handle exception")
except TypeError:
    print("Handle exception")
except Exception:
    print("Handle exception")
except:
    print("Handle exception")
else:
    print("Execute this code")
finally:
    print("Execute every time")
    