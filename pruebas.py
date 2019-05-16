from sympy import var
from sympy import sympify

# x = var('x')  # the possible variable names must be known beforehand...
# user_input = input('Enter mathematical function here: → ')
# expr = sympify(user_input)
# res = expr.subs(x,3.14)
# print(res)  # -1.322...


# # 'x * sin(x**2)'

# # n=[2,3,4,5,6]
# # result = []
# # counter = 0
# # for items in n:
# #     x = n[counter]
# #     x = var('x')
# #     conversionAMatematicas = sympify(inputDelUsuario)
# #     operaciones = conversionAMatematicas.subs(x,n[counter])
# #     result.append(operaciones)
# #     counter = counter + 1

# # print(result)
# xi = 2
# def funcion(inputDelUsuario,xi):
#     x = var('x')
#     conversionAMatematicas = sympify(inputDelUsuario)
#     operaciones = conversionAMatematicas.subs(x,xi)
#     return operaciones

# b= []
# for items in range(8):
#     a = funcion(inputDelUsuario,xi)
#     xi = xi + 1
#     b.append(a)
# print(b)

validFunction = 'no'
while validFunction == 'no':
    inputDelUsuario = input('Ingresar su función matemática: → ')
    validFunction = input('¿Has ingresado tu function correctamente? ("si","no"): → ')
    

def funcion(inputDelUsuario,xi):
    x = var('x')
    conversionAMatematicas = sympify(inputDelUsuario)
    operaciones = conversionAMatematicas.subs(x,xi)
    return operaciones

def iteracionesDeXi(n,Xi, deltaX, SimgmaArea):
    for item in range(n):
        Xi = Xi + deltaX
        SimgmaArea = SimgmaArea + float(funcion(inputDelUsuario, Xi))
    Area = SimgmaArea * deltaX
    return Area
