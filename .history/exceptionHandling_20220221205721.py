'''try:
except
else
finally'''

try:
    print("Execute this code ", 1/0)
except Exception:
    print("Handle exception")
else:
    print("Execute this code")
finally:
    print("Execute every time")
    