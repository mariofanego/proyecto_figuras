from lib import cuadrado,cincurferencia

print("Proyecto Figuras")

lado = 4
print(f"El area de un cuadrado de lado {lado} es: {cuadrado.get_area(lado)}")


radio = 5
area = cincurferencia.get_area(radio)

print("El área de la circunferencia es:", area)

