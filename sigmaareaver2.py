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
    a = int(input(" → "))
    print(Fore.WHITE + "Ingrese el segundo intervalo (" + Fore.RED + "b" + Fore.WHITE + ")")
    b = int(input(" → "))
    if a < b:
        valid = 'yes'
    else:
        print(Fore.RED + "MATH ERROR: A MUST BE LESS THAN B " + Fore.WHITE)
        valid = 'no'
    print(Fore.WHITE + "Enter number of rectangles: ")
    n = int(input(" → "))


#Escriba la función y=f(x) bajo la curva
def function(x):
    '''escribe la función =f(x)y'''
    fdeX = 10 - 2*float(x)  
    return fdeX

#Largo del intervalo
intervalo = b - a

#Ancho de cada rectángulo
deltaX = float(b-a)/n

#Imprime el ancho de cada rectángulo
print("Número de Rectángulos: → ",  n)

#primer número muestra
xi_1 = a
xi_2 = a
xi_3 = a

#Inicialice la suma del Area a cero
SigmaArea_1=0
SigmaArea_2=0
SigmaArea_3=0

for item in range(n):
    # numero muestra
    xi_1 = xi_1 + deltaX
    areaActual = float(function(xi_1)) 
    SigmaArea_1 = SigmaArea_1 + areaActual
Area_1 = SigmaArea_1 * deltaX

for item in range(n):
    # numero muestra
    xi_2 = xi_2 - deltaX
    areaActual = float(function(xi_1))
    SigmaArea_2 = SigmaArea_2 + areaActual
Area_2 = SigmaArea_2 * deltaX

for item in range(n):
    # numero muestra
    xi_3 = xi_3 - deltaX
    areaActual = float(function(xi_1))
    SigmaArea_3 = SigmaArea_3 + areaActual 
Area_3 = SigmaArea_3 * deltaX

#Para obtener el área multiplique por la suma por el ancho delta x
def matriz(SigmaArea_1,SigmaArea_2,SigmaArea_3):
    
    print(Fore.BLUE + "|El área bajo la curva f(x) es: → ",Area_1, Fore.CYAN +  "|El área cuando Xi = Xi - deltaX es: → ", Area_2 , Fore.GREEN + "|El área cuando Xi = Xi -es: → ", Area_3, " " "|")

matriz(SigmaArea_1,SigmaArea_2,SigmaArea_3)




























# multiplicationOfFdeXandFdeXi = []

# iteration_1 = int(0)
# for items in listsOfX:
#     multiplicationOfFdeXandFdeXi.append(listsOfX[iteration_1] * listofFdeXi[iteration_1])
#     iteration = iteration + int(1)
# print(multiplicationOfFdeXandFdeXi)

# sigmaArea = sum(multiplicationOfFdeXandFdeXi)



# print("La suma de areas es", sigmaArea)





