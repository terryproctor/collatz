#the Collatz Sequence
#The Collatz conjecture is a conjecture in mathematics that concerns a sequence defined as follows: start with any positive integer n. Then each term is obtained from the previous term as follows: if the previous term is even, the next term is one half of the previous term. If the previous term is odd, the next term is 3 times the previous term plus 1. The conjecture is that no matter what value of n, the sequence will always reach 1.


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
    
