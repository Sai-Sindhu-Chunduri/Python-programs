def bunnyEars(bunnies):
    if(bunnies==0):
        return 0
    else:
        return 2+bunnyEars(bunnies-1)

