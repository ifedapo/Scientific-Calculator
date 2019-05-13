import math

while True:
    print("\nChoose the math operation. \n\n0 - Addition \n1 - Subtraction \n2 - Multiplication \n3 - Division "
          "\n4 - Modulo \n5 -Raising to Power \n6 - Square root ""\n7 - Logarithm \n8 - Sine  \n9 - Cosine  \n10"
          " - Tangent")

    oper = input("\n - Your Option from the menu:")

    # Addition
    if oper == "0":
        val1 = float(input("\nFirst Value: "))
        val2 = float(input("\nSecond Value: "))

        print("\n The result is: "+str((val1 + val2)) + "\n")
        # Going back to the main meu or exiting the code.
        back = input("\nGo back to the main menu? (y/n).")

        if back == 'y':
            continue
        else:
            break

    # Subtraction
    if oper == "1":
            val1 = float(input("\nFirst Value: "))
            val2 = float(input("\nSecond Value: "))

            print("\n The result is: " + str((val1 - val2)) + "\n")
            # Going back to the main meu or exiting the code.
            back = input("\nGo back to the main menu? (y/n).")

            if back == 'y':
                continue
            else:
                break

    # Multiplication
    if oper == "2":
        val1 = float(input("\nFirst Value: "))
        val2 = float(input("\nSecond Value: "))

        print("\n The result is: " + str((val1 * val2)) + "\n")
        # Going back to the main meu or exiting the code.
        back = input("\nGo back to the main menu? (y/n).")

        if back == 'y':
            continue
        else:
            break

    # Division
    if oper == "3":
            val1 = float(input("\nFirst Value: "))
            val2 = float(input("\nSecond Value: "))

            print("\n The result is: " + str((val1 / val2)) + "\n")
            # Going back to the main meu or exiting the code.
            back = input("\nGo back to the main menu? (y/n).")

            if back == 'y':
                continue
            else:
                break
    # Modulo
    if oper == "4":
        val1 = float(input("\nFirst Value: "))
        val2 = float(input("\nSecond Value: "))

        print("\n The result is: " + str((val1 % val2)) + "\n")
        # Going back to the main meu or exiting the code.
        back = input("\nGo back to the main menu? (y/n).")

        if back == 'y':
            continue
        else:
            break

    # Raising to Power
    if oper == "5":
            val1 = float(input("\nEnter the base: "))
            val2 = float(input("\nEnter the value: "))

            print("\n The result is: " + str(math.pow(val1, val2)) + "\n")
            # Going back to the main meu or exiting the code.
            back = input("\nGo back to the main menu? (y/n).")

            if back == 'y':
                continue
            else:
                break

    # Square Root
    if oper == "6":
        val1 = float(input("\nEnter the value for extracting the square root: "))

        print("\n The result is: " + str(math.sqrt(val1)) + "\n")
        # Going back to the main meu or exiting the code.
        back = input("\nGo back to the main menu? (y/n).")

        if back == 'y':
            continue
        else:
            break
    # Logarithm
    if oper == "7":
        val1 = float(input("\nEnter the value to calculating the logarithm to base 2 "))

        print("\n The result is: "+str(math.log(val1, 2)) + "\n")
        # Going back to the main meu or exiting the code.
        back = input("\nGo back to the main menu? (y/n).")

        if back == 'y':
            continue
        else:
            break
    # Sine
    if oper == "8":
            val1 = float(input("\nEnter the value(in degree) for calculating the sine "))

            print("\n The result is: " + str(math.sin(math.radians(val1))) + "\n")
            # Going back to the main meu or exiting the code.
            back = input("\nGo back to the main menu? (y/n).")

            if back == 'y':
                continue
            else:
                break
    # Cosine
    if oper == "9":
        val1 = float(input("\nEnter the value (in degree) for calculating the cosine "))

        print("\n The result is: " + str(math.cos(math.radians(val1))) + "\n")
        # Going back to the main meu or exiting the code.
        back = input("\nGo back to the main menu? (y/n).")

        if back == 'y':
            continue
        else:
            break
    # Tangent
    if oper == "10":
            val1 = float(input("\nEnter the value (in degree) for calculating the tangent"))

            print("\n The result is: " + str(math.tan(math.radians(val1))) + "\n")
            # Going back to the main meu or exiting the code.
            back = input("\nGo back to the main menu? (y/n).")

            if back == 'y':
                continue
            else:
                break

    # Handling Invalid Options
    else:
        print("\nInvalid Option!\n")
        continue
