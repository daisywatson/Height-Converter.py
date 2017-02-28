# This program takes in user input height in centimeters
# It outputs the height in feet and inches rounded to the nearest inch
# 2/2/17         Daisy Watson

#Loops so that user can input more than one height
while True:

    while True:
        try:
            #The input should be an integer greater than zero
            centiHeight = int(raw_input("Enter the height in centimeters: "))
            if (centiHeight > 0):
                break
            else:
                print "That is not a valid number. Please try again."
        except (TypeError, ValueError):
            print "That is not a valid number. Please try again."
        

    #conversion:
    inchHeight = float(centiHeight) * 0.3937007874
    footHeight = inchHeight / 12
    remainderInch = inchHeight % 12
    #change values into integers and round inches
    footHeight = int(footHeight)
    remainderInch = int(round(remainderInch, 0))
    inchHeight = int(round(inchHeight, 0))
    if remainderInch == 12:
        remainderInch = 0
        footHeight += 1

    #Display results     
    if inchHeight == 1:
        print "%s cm. in inches is %s inch." % (centiHeight, inchHeight)
    elif inchHeight < 12 and inchHeight > 1:
        print "%s cm. in inches is %s inches" % (centiHeight, inchHeight)       
    elif remainderInch == 1:
        print "%s cm. in feet is %s feet %s inch." % (centiHeight, footHeight, remainderInch)
    elif footHeight == 1:
        if remainderInch == 1:
            print "%s cm. in feet is %s foot %s inch." % (centiHeight, footHeight, remainderInch)
        elif remainderInch == 0:
            print "%s cm. in feet is %s foot." % (centiHeight, footHeight)
        else:
            print "%s cm. in feet is %s feet %s inches." % (centiHeight, footHeight, remainderInch)
    elif remainderInch > 1:
        print "%s cm. in feet is %s feet %s inches." % (centiHeight, footHeight, remainderInch)
    elif footHeight == 1:
        print "%s cm. in feet is %s foot." % (centiHeight, footHeight)
    else:
        print "%s cm. in feet is %s feet." % (centiHeight, footHeight)

    #Prompt user for more heights
    while True:
        userConfirm = raw_input("Would you like to enter another number? (yes/no): ")
        userConfirm = userConfirm.lower()
        if userConfirm != "yes" and userConfirm != "no":
            print "Please enter 'yes' or 'no'"
        else:
            break
    
    if userConfirm == "no":
        break
