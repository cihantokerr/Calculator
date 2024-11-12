from contextlib import nullcontext

numberinput=""
sum_value=0
substarciton_value=0


def addition():
    global sum_value
    global numberinput

    # Number input
    while True:

        try:
            numberinput = input("Please enter an input:")

            # If user has typed 'quit';System is going to stop to take number inputs and empty the array for another operation.
            # If not;System is going to convert input value to an Float value;Append it into an array and display the sum.

            if numberinput == "quit":
                # Stop taking inputs
                break

            else:
                # Convert the value into a Float and add it to the sum
                numberinput=float(numberinput)
                sum_value+=numberinput

                print("Sum:"+str(sum_value))



        except:
            print("The value that you have inputted can not be converted to an Integer. ")






def substraction():
    result=nullcontext

    #Number Input
    while True:
        try:
            numberinput = input("Please enter an input:")

            if numberinput == "quit":
                # Stop taking inputs
                break

            else:
                #If result is null;System is going to put the input value to result variable
                if(result==nullcontext):
                    result=float(numberinput)

                else:
                    #Substract everything from result
                    result=result-float(numberinput)
                    print(result)





        except:
            print("The value that you have inputted can not be converted to an Integer. ")




def division():
    result=nullcontext

    while True:
        # Number Input
        try:
            numberinput = input("Please enter an input:")

            if numberinput == "quit":
                # Stop taking inputs
                break

            else:
                # If result is null;System is going to put the input value to result variable
                if (result == nullcontext):
                    result = float(numberinput)

                else:
                    result=result/float(numberinput)
                    print("Division:"+str(result))



        except:
            print("The value that you have inputted can not be converted to an Integer. ")





def multiplication():
    result=nullcontext

    while True:
        try:
            numberinput = input("Please enter an input:")

            if numberinput == "quit":
                # Stop taking inputs
                break

            else:
                # If result is null;System is going to put the input value to result variable
                if (result == nullcontext):
                    result = float(numberinput)

                else:
                    result=result*float(numberinput)
                    print("Multiplication:"+str(result))


        except:
            print("The value that you have inputted can not be converted to an Integer. ")




#Taking operation input
while True:
    try:
        print("[1] Addition")
        print("[2] Substraction")
        print("[3] Multiplication")
        print("[4] Division")
        operation_input = input("Welcome To The Calculator.Please enter an operation:")

        if operation_input=="1":
            addition()

        elif operation_input=="2":
            substraction()

        elif operation_input=="3":
            multiplication()

        elif operation_input=="4":
            division()


    except:
        print("Invalid Input.Please try again.")
