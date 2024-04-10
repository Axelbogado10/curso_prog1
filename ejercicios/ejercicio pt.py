'''
Las posibles aplicaciones son las siguientes:
Inteligencia artificial (IA),
Realidad virtual/aumentada (RV/RA),
Internet de las cosas (IOT)

Para ello, la empresa realiza entre sus empleados una encuesta, con el propósito de conocer ciertas métricas.

A) Los datos a ingresar por cada empleado encuestado son:
nombre del empleado
edad (no menor a 18)
género (Masculino - Femenino - Otro)
tecnologia (IA, RV/RA, IOT)  

B) Cargar por terminal 10 encuestas.

C) Determinar:
Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad esté entre 25 y 50 años inclusive.
Porcentaje de empleados que no votaron por IA, siempre y cuando su género no sea Femenino o su edad se encuentre entre los 33 y 40.
Nombre y tecnología que votó, de los empleados de género masculino con mayor edad de ese género.
'''

i = 0
contador_Masculino_tec = 0
contador_no_ia = 0
bandera = True
contador = 0
Maximo_edad = 0


for i in range (10):
    nombre = input("ingrese su nombre")
    
    edad = input("ingrese su edad")
    edad = int(edad)
    while edad < 18:
        edad = input("reingrese su edad")
    
    genero = input("ingrese su genero")
    while genero != "Masculino" and genero != "Femenino" and genero != "Otro":
        genero = input ("reingrese su genero")
    
    tecnologia = input("tecnologia")
    while tecnologia != "IA" and tecnologia != "RV/RA" and tecnologia != "IOT":
        tecnologia = input ( "reingrese la tecnologia")
    
    contador += 1
    
    if genero == "Masculino":
        if tecnologia == "IA" or tecnologia == "IOT":
            if edad > 24 and edad < 51:
                contador_Masculino_tec +=1
                
    if genero != "Femenino":
        if edad < 33 and edad > 40:
            if tecnologia != "IA":
                contador_no_ia += 1
    
    if genero == "Masculino":
        edad > Maximo_edad or bandera == True
        edad = Maximo_edad
        tech_viejo = tecnologia
        nombre_viejo = nombre
    
Porcentaje_votos = (contador_no_ia * 100)/contador

print("",f"la cantidad de empleados masculinos que votaron por ia o iot es de {contador_Masculino_tec}\n el porcentaje de empleados que no votaron por ia es de {Porcentaje_votos} \n el nombre y tecnologia del Masculino mas viejo es {nombre_viejo} y voto {tech_viejo}")


