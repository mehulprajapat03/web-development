for i in range (0,5):
    count=0
    for j in range (0,6):
        if i>=j:
            count=count+1
            print(count, end="")
        else:
            print(" ",end="")

    print()
