
import math

# Paso 1: Solicitar al usuario que ingrese el radio del ciruclo.

radio = float (input ("Por favor, ingrese el radio del ciruclo: "))

#Paso 2. Calcular el area del circulo utilizando la formula area = π * radio^2

area = math.pi * (radio**2)

# Paso 3: Monstrar al usuario el area calculada

print("El area del circulo con radio", radio, "es:", area )