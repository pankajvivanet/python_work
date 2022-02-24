'''try:
except
else
finally'''

try:
    x = -1
    if x != 1:
        raise Exception("there is exception")
except Exception:
    print("Handle exception")
finally:
    print("Execute every time")
    