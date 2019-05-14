import math
from colorama import init, Fore, Back, Style
init(convert=True)
#recibir numero de rectangulos
#recibir intervalos
#calcular f(Xi) y Area

valid = 'no'

#En estas instrucciones el programa le pide los inputs al usuario
while valid == 'no':
    print(Fore.WHITE + "Ingrese el primer intervalo (" + Fore.RED + "a" + Fore.WHITE + ")")
    a = float(input(" → "))
    print(Fore.WHITE + "Ingrese el segundo intervalo (" + Fore.RED + "b" + Fore.WHITE + ")")
    b = float(input(" → "))
    if a < b:
        valid = 'yes'
    else:
        print(Fore.RED + "MATH ERROR: A MUST BE LESS THAN B " + Fore.WHITE)
        valid = 'no'
    #print(Fore.WHITE + "Enter number of rectangles: ")
    # n = int(input(" → "))
    inputOfn = input("Ingrese los diferentes valores de 'n' en una lista separada por espacios: → ")
    Listofn = inputOfn.split()
    

#Escriba la función y=f(x) bajo la curva
def function(x):
    '''escribe la función =f(x)y'''
    fdeX = float(x)**3+4
 
    return fdeX


##Imprime el ancho de cada rectángulo
#print("Número de Rectángulos: → ",  n)

iteration = 0

print("| " + "Rectángulos" + Fore.CYAN + " | Izquierda  " +  Fore.GREEN + "| Centro    " + Fore.BLUE + "| Derecha    |" + Fore.WHITE  )

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

    for item in range(n):
        # numero muestra
        xi_1 = xi_1 + deltaX
        areaActual = float(function(xi_1)) 
        SigmaArea_1 = SigmaArea_1 + areaActual
    Area_1 = SigmaArea_1 * deltaX

    for item in range(n):
        # numero muestra
        xi_2 = xi_2 + deltaX
        SigmaArea_2 = SigmaArea_2 + float(function(xi_2))
    Area_2 = SigmaArea_2 * deltaX

    for item in range(n):
        # numero muestra
        xi_3 = xi_3 + deltaX
        areaActual = float(function(xi_3))
        SigmaArea_3 = SigmaArea_3 + areaActual 
    Area_3 = SigmaArea_3 * deltaX

    iteration = iteration + 1

    
    print("| ",format(n,"6d") ,"    | ",format(Area_2, "2.6f"), "|" ,format(Area_3, "2.6f"), "|" ,format(Area_1,"2.6f"), " |")

