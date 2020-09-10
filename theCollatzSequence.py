#the Collatz Sequence

#One pass of collatz
def collatz(number):
    if number % 2 == 0:
        value = (number//2)
        print(value)
        return value
    else:
        value = (3 * number + 1)
        print(value)
        return(value)

#collatz input, will only accept positive integer values
while True:
    try:    
        number = int(input("Enter a (integer)number for collatz: "))
    except ValueError:
        print("This is not a valid number")
        continue
    if number > 0:
        break

while number !=1:
    number= collatz(number)
    
