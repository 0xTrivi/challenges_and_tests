def printSpaces(number: int):
    for j in range(number):
        print("",end=' ')

def printAsterisks(number: int):
    for k in range(number):
        print("\033[33m*\033[0m", end=" ")


def dibujarPrimerTriagunlo(number: int, rowMax: int):
    for i in range(number):

        printSpaces(rowMax-i)
            
        

        printAsterisks(i+1)

        printSpaces(rowMax-i)
        print(" ")



def dibujarTriangulosDebajo(number: int,rowMax: int):
    for i in range(number):

        printSpaces((number-i)-1)
        printAsterisks(i+1)
        printSpaces((rowMax-(2*i)-1))
        printAsterisks(i+1)
        printSpaces((number-i)-1)
        print(" ")






def print_file(file_name: str):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"The file {file_name} does not exist.")
    except IOError:
        print(f"Unable to open the file {file_name}.")






def printTriForce(number: int, rowMax: int):
    dibujarPrimerTriagunlo(number, rowMax)
    dibujarTriangulosDebajo(number, rowMax)
    print(" ")



def whatSize():
    print("How big do you want your triforce?:")

    size = False
    while size == False:
        
        number = int(input(" "))
        print(" ")
        if number > 0:
            size = True
            print("")
        else:
            print("Please! write a positive integer number:")
    print("")
    return number


def printEnd():
    print_file("end.txt")
    print("")
    print("Take care of Hyrule!")
    print("")


def main():
    
    
    print_file("title.txt")
    generate = False
    while generate == False:
        
        size = whatSize()


        printTriForce(size, (size*2)-1)

        correctOption = False
        while correctOption == False:
            print("Do you want to generate another Triforce?")
            print("1 - Yes")
            print("2 - No")
            option = str(input(" "))
            print(" ")
            
            
            if option == "2" or option == "n" or option == "N" or option == "No":
                generate = True
                correctOption = True
                print("")
            elif option == "1" or option == "y" or option == "Y" or option == "Yes":  
                print("")
                correctOption = True
            else:
                print("Please! write a correct option.")

    printEnd()

if __name__ == "__main__":
   
    main()