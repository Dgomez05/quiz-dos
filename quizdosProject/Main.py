nombre = input("Introduzca su nombre: ")
diaslaborados = int(input("Introduzca el numero de dias laborados: "))
salario =  int(input("Introduzca el salario: "))

prima = int(salario * diaslaborados)/360
cesantias = int(salario * diaslaborados)/360
interesesC = int(cesantias*0.12)/diaslaborados
vacaciones = int(salario * diaslaborados)/720

liquidacion = cesantias + vacaciones + prima + interesesC
print(f"""Señor {nombre} para los {diaslaborados} días laborados y salario {salario}, su liquidación se compone así:" 
prima : {prima:.2f}, 
cesantías : {cesantias:.2f}, 
intereses : {interesesC:.2f},
vacaciones : {vacaciones:.2f},
liquidación : {liquidacion:.2f}""")

