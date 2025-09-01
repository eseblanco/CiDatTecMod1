from sympy import symbols, solve

# Definir las variables simbólicas
x, y = symbols('x y')

# Definir las dos ecuaciones del sistema
ecuacion1 = 3*x**2 - 6*x - 3*y
ecuacion2 = 3*y**2 - 6*y - 3*x

# Resolver el sistema de ecuaciones
soluciones = solve((ecuacion1, ecuacion2), (x, y))

# Imprimir las soluciones
print("Las soluciones (x, y) que hacen que las funciones sean 0 son:")
for sol in soluciones:
    # Usar .evalf() para obtener valores decimales, si los hay
    x_val = sol[0].evalf()
    y_val = sol[1].evalf()
    
    # Imprimir los valores
    print(f"x = {x_val}, y = {y_val}")
print(len(soluciones))