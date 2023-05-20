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




def imprimir_contenido_archivo(title):
    try:
        with open(title, 'r') as archivo:
            contenido = archivo.read()
            print(contenido)
    except FileNotFoundError:
        print(f"El archivo {title} no existe.")
    except IOError:
        print(f"No se puede abrir el archivo {title}.")








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

def main():
    
    

    generate = False
    while generate == False:
        
        size = whatSize()


        printTriForce(size, (size*2)-1)
        
        print("Do you want to generate another Triforce?")
        print("1 - Yes")
        print("2 - No")
        option = str(input(" "))
        print(" ")
        if option == "2" or option == "n" or option == "N" or option == "No":
            generate = True
            print("")
        elif option == "1" or option == "y" or option == "Y" or option == "Yes":  
            print("")
        else:
            print("Please! write a correct option.")

if __name__ == "__main__":
    # Llamada a la función para imprimir el contenido del archivo "portada.txt"
    imprimir_contenido_archivo("title.txt")
    main()