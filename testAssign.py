blocks = int(input("Enter number of blocks: "))
hegiht =0
counter=0
while counter < blocks:
    hegiht += 1
    counter += hegiht
    if(counter > blocks):
        hegiht -=1
        break

print("THe hegiht =", hegiht)