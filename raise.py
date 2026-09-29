#Ask the user to enter a number.if the number is less than or equal to 0,
# raise a ValueError with the message "Number must be Positive"

try:
    num=int(input('Enter number'))
    if(num<=0):
        raise ValueError('Number should be Positive')
    else:
        print(num)

except ValueError as e:
    print(e)





#Ask the user to enter a password.if its length is less than 8 characters ,raise
#a customexception InvalidPasswordError with the message ("Password should be 8
# characters")


class InvalidPasswordError(Exception):
    pass


try:
    password=input("Enter password")

    if len(password)<8:
        raise InvalidPasswordError("Password should be 8 characters")
    else:
        print("Valid Password")

except InvalidPasswordError as e:
    print(e)


#Ask the user to enter an amount and if the amount<balance ,raise customException
#InsuffientBalanceError with the message("Not Enough Balance.Transaction Failed")

class InsufficientBalanceError(Exception):
    pass


balance=5000

try:
    amount=int(input("Enter amount"))

    if amount>balance:
        raise InsufficientBalanceError("Not Enough Balance.Transaction Failed")
    else:
        print("Transaction Successful")

except InsufficientBalanceError as e:
    print(e)