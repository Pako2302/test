import os

def calculadora():
    nombre = input("Ingrese su nombre: ")
    print(f"Hola, {nombre}! Bienvenido a la calculadora.")
    
    while True:
        print("\nMenú de la Calculadora:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        if opcion == "5":
            print("Saliendo de la calculadora. Hasta luego!")
            break
        
        if opcion in ["1", "2", "3", "4"]:
            try:
                num1 = float(input("Ingrese el primer número: "))
                num2 = float(input("Ingrese el segundo número: "))
                
                if opcion == "1":
                    print(f"Resultado: {num1 + num2}")
                elif opcion == "2":
                    print(f"Resultado: {num1 - num2}")
                elif opcion == "3":
                    print(f"Resultado: {num1 * num2}")
                elif opcion == "4":
                    if num2 != 0:
                        print(f"Resultado: {num1 / num2}")
                    else:
                        print("Error: No se puede dividir por cero.")
            except ValueError:
                print("Error: Ingrese valores numéricos válidos.")
        else:
            print("Opción no válida. Intente de nuevo.")

def fibonacci():
    nombre = input("Ingrese su nombre: ")
    print(f"Hola, {nombre}! Bienvenido al programa de Fibonacci.")
    
    try:
        n = int(input("Ingrese un número entero positivo: "))
        if n < 0:
            print("Error: El número debe ser positivo.")
            return
        
        a, b = 0, 1
        resultado = []
        for _ in range(n):
            resultado.append(a)
            a, b = b, a + b
        
        print("Sucesión de Fibonacci:", resultado)
        
        with open("fibonacci.res", "w") as file:
            file.write(" ".join(map(str, resultado)))
            
        print("El resultado se ha guardado en fibonacci.res")
    except ValueError:
        print("Error: Ingrese un número entero válido.")

if __name__ == "__main__":
    while True:
        print("\nSeleccione el programa a ejecutar:")
        print("1. Calculadora")
        print("2. Fibonacci")
        print("3. Salir")
        opcion = input("Ingrese una opción: ")
        
        if opcion == "1":
            calculadora()
        elif opcion == "2":
            fibonacci()
        elif opcion == "3":
            print("Saliendo del programa. Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

