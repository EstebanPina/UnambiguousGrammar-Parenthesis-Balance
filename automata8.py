import random as rand
Lenguaje=["(",")"]
'''Funcion para generar una cadena aleatoria de longitud menor a 1000'''
def GenerarCadena():
    length_of_string = rand.randint(0,1000)
    Cadena=(''.join(rand.choice(Lenguaje) for _ in range(length_of_string)))       
    return Cadena
'''Funcion para validar que la cadena sea menor a 1000'''
def validaCadena(Cadena):
    if(len(Cadena)<1000):
        return True
    else:
        return False
'''Funcion para crear Archivo de historial de la evaluacion del automata'''
def CreaArchivo():
    archivo=open("GramaticaEvalucacion.txt","w")
    archivo.close()
'''Funcion para escribir en el archivo de historial de la evaluacion del automata'''
def escribirArchivo(cadena):
    archivo=open("GramaticaEvalucacion.txt","a")
    archivo.write(cadena)
    archivo.close()
'''Funcion de evaluacion de la cadena "Automata de gramatica no ambigua"'''
def Evalua(cadena):
    indice=0
    evaluacion=[]
    for i in cadena:
        #Caso 1: Es obligatorio abrir un parentesis al inicio de la cadena. Si este es el caso se evalua la cadena y empezamos con B->(RB
        if(i=="(" and len(evaluacion)==0):
            evaluacion.extend(["(","R","B"])
            escribirArchivo("Caracter Evaluado:(    Regla de produccion:B->(RB     evaluacion:"+"".join(evaluacion)+"\n")
        #Caso 2: Si se empieza cerrando una cadena es obvio que no se cumple la gramatica. devolvemos False
        elif(i==")" and len(evaluacion)==0):
            escribirArchivo("Primer Simbolo \")\" no es una cadena valida\n")
            return False
        #Caso 3: Si se cierra un parentesis en la cadena a evaluar y tenemos una R en nuestra lista de evaluacion, Aplicamos regla de produccion R->(RR
        elif(i=="(" and evaluacion[indice]=="R"):
            evaluacion[indice]="("
            evaluacion.insert(indice+1, 'R')
            evaluacion.insert(indice+2, 'R')
            escribirArchivo("Caracter Evaluado:(    Regla de produccion:R->(RR     evaluacion:"+"".join(evaluacion)+"\n")
        #Caso 4: Si se cierra un parentesis en la cadena a evaluar y tenemos un B en nuestra lista de evaluacion determinamos que se cerro un parentesis sin abrir uno previamente por lo que la cadena es invalida
        elif(i==")" and evaluacion[indice]=="B"):
            escribirArchivo("Se cerro un parentesis no abierto. no es una cadena valida\n")
            return False
        #Caso 5: Si se cierra un parentesis en la cadena a evaluar y tenemos una R en nuestra lista de evaluacion, Aplicamos regla de produccion R->)
        elif(i==")" and evaluacion[indice]=="R"):
            evaluacion[indice]=")"
            escribirArchivo("Caracter Evaluado:)    Regla de produccion:R->)     evaluacion:"+"".join(evaluacion)+"\n")
        #Caso 6: Si se abre un parentesis en la cadena a evaluar y tenemos una B en nuestra lista de evaluacion, Aplicamos regla de produccion B->(RB
        elif(i=="(" and evaluacion[indice]=="B"):
            evaluacion[indice]="("
            evaluacion.insert(indice+1, 'R')
            evaluacion.insert(indice+2, 'B')
            escribirArchivo("Caracter Evaluado:(    Regla de produccion:B->(RB     evaluacion:"+"".join(evaluacion)+"\n")
        indice+=1
        print(evaluacion)
    if(indice<len(evaluacion)):
        #Caso 7: Si llegamos al final de la cadena a evaluar y tenemos una B en el ultimo elemento de nuestra lista de evaluacion, Aplicamos regla de produccion B->epsilon y validamos la cadena
        if(evaluacion[indice]=="B"):
            evaluacion[indice]=""
            escribirArchivo("Caracter Evaluado:\"\"     Regla de Produccion:B->epsilon     evaluacion:"+"".join(evaluacion)+"\n")
            escribirArchivo("Cadena valida\n")
            return True
        #Caso 8: Si llegamos al final de la cadena a evaluar y tenemos una R en el ultimo elemento de nuestra lista de evaluacion determinamos que la cadena es invalida
        elif(evaluacion[indice]=="R"):
            escribirArchivo("Falta Cerrar uno o mas parentesis. no es una cadena valida\n")
            return False 
 
selec=0
while(selec!=3):
    print("Bienvenido al programa de gramatica no ambigua, seleccione una de las siguientes opciones para continuar:\n1-Insertar Cadena\n2-Cadena Aleatoria\n3-Salir")
    selec=input("Ingresa la opcion elegida:")
    if(selec=="1"):
        CreaArchivo()
        print("Ingrese la cadena a evaluar (Solo \"(\" o\")\"):")
        cad=input()
        if(validaCadena(cad)):#Funcion de evaluacion de la cadena 
            print (cad)
            if(Evalua(cad)):
                print("Cadena aceptada")
            else:
                print("Cadena rechazada")
        
    elif(selec=="2"):
        CreaArchivo()
        cad=GenerarCadena()
        print (cad)
        if(Evalua(cad)):#Funcion de evaluacion de la cadena
                print("Cadena aceptada")
        else:
            print("Cadena rechazada")
        
    elif(selec=="3"):
        exit()
    else:
        print("Error. Opcion no valida")
