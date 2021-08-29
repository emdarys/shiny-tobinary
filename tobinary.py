# To convert a decimal number into binary number
import math

# To make the conversion
def toBinary(nmbrDec):
    negSign ="0"
    if nmbrDec == 0:
        return 0
    if nmbrDec < 0:
        negSign ="1"
        nmbrDec = abs(nmbrDec)
    nmbrBi = " "
    
    for i in range(int(math.log2(nmbrDec)+1)):
        nmbrDec2 = nmbrDec//2
        rem = str(nmbrDec%2)
        nmbrDec = nmbrDec2
        nmbrBi = rem + nmbrBi

    nmbrBi = negSign + nmbrBi
    return nmbrBi

# To print the numbers
def main():
    userInput = input("Enter the number to convert to binary (please give an integer number) or press q to exit: ")

    while userInput != "q":
        try:
            answer = toBinary(int(userInput))
            print("The binary form of", userInput, "is", answer)

        except:
            print("This was not a valid input!!") 

        userInput = input("Enter an integer or press q to exit: ") 

    print("Bye!")
    exit()

      
main()
