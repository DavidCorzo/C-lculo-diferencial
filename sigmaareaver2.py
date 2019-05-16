#IMPORTAR LIBRERÍAS
#Para importar las funciones básicas como sum() etcétera
import math
#Para importar colores de impresión
from colorama import init, Fore, Back, Style
init(convert=True)
#Para hacer el input de la función matemática por el usuario
from sympy import var
from sympy import sympify


    
#definicion de funciones
def iteracionesDeXi(n,Xi, deltaX, SimgmaArea,inputDelUsuario):
    '''Esta funcion permite no repetir código que anteriormente estaba repetido como 3 diferentes operaciones for, esta función economiza líneas de código.'''
    for item in range(n):
        Xi = Xi + deltaX
        SimgmaArea = SimgmaArea + float(funcion(inputDelUsuario, Xi))
    Area = SimgmaArea * deltaX
    return Area

#Definición de funciones matemáticas
def funcion(inputDelUsuario,xi):
    '''Esta función permite convertir el input del usuario en una funcion como tal capaz de ser interpretada por python como código matemático funcional.'''
    x = var('x')
    conversionAMatematicas = sympify(inputDelUsuario)
    operaciones = conversionAMatematicas.subs(x,xi)
    return operaciones



def main():
    #INPUT MATEMÁTICO POR EL USUARIO
    validFunction = 'no'
    while validFunction == 'no':
        inputDelUsuario = input('Ingresar su función matemática: → ')
        validFunction = input('¿Has ingresado tu función correctamente? ("si","no"): → ')
        if validFunction == 'no':
            print("Input de nuevo.")
            print("_________________________________________________________________________________________________________________________________________________________________")

    #En estas instrucciones el programa le pide los inputs al usuario, dichos inputs son únicamente a,b,n
    validABN = 'no'
    while validABN == 'no':
        #El primer intervalo es 'a'
        print(Fore.WHITE + "Ingrese el primer intervalo (" + Fore.RED + "a" + Fore.WHITE + ")")
        a = float(input(" → "))
        #El segundo intervalo es 'b'
        print(Fore.WHITE + "Ingrese el segundo intervalo (" + Fore.RED + "b" + Fore.WHITE + ")")
        b = float(input(" → "))
        #'a' debe ser menor que 'b'
        if a < b:
            validABN = 'yes'
        else:
            print(Fore.RED + "ERROR MATEMÁTICO: EL PRIMER INTERVALO DEBE DE SER MAYOR QUE EL SEGUNDO" + Fore.WHITE)
            validABN = 'no'
    validN = 'no'
    while validN == 'no':
        inputOfn = input("Ingrese los diferentes valores de 'n' en una lista separada por espacios: → ")
        validN = input('¿Ha ingresado "n" correctamente? ("si","no"): → ')
        if validN == 'no':
            print("Input de nuevo.")
            print("_________________________________________________________________________________________________________________________________________________________________")
    
    Listofn = inputOfn.split()

    #Imprime el header
    print("| " + "Rectángulos" + Fore.CYAN + " | Izquierda  " +  Fore.GREEN + "| Centro    " + Fore.BLUE + "| Derecha    |" + Fore.WHITE  )

    #defino la variable iteracion esta es la variable contador
    iteration = 0
    for item in Listofn:
        #Ancho de cada rectángulo
        n = int(Listofn[iteration])
        deltaX = float(b-a)/n


        #Inicialice la suma del Area a cero
        SigmaArea_1=0
        SigmaArea_2=0
        SigmaArea_3=0


        #primer número muestra
        xi_1 = a
        xi_2 = a - deltaX
        xi_3 = a - 0.5 * deltaX

        #funcion de iteraciones de cada fórmula de Xi
        Area_1 = iteracionesDeXi(n,xi_1,deltaX,SigmaArea_1,inputDelUsuario)
        Area_2 = iteracionesDeXi(n,xi_2,deltaX,SigmaArea_2,inputDelUsuario)
        Area_3 = iteracionesDeXi(n,xi_3,deltaX,SigmaArea_3,inputDelUsuario)

        #itero para cambiar el valor de n
        iteration = iteration + 1

        
        print("| ",format(n,"6d") ,"    | ",format(Area_2, "2.6f"), "|" ,format(Area_3, "2.6f"), "|" ,format(Area_1,"2.6f"), " |")


if __name__ == "__main__":
    main()