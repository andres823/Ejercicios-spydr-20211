print("ingrese 3 numeros enteros diferentes")
# ingrese a realizar dependiendo de lo que necesite
e = int(input("elija 1 si lo quiere de mayor a menor y 2 si lo quiere de menor a mayor"))
# ingrese los numeros que solicita el problema
a = int(input("ingrese el numero a"))
b = int(input("ingrese el numero b"))
c = int(input("ingrese el numero c"))

if (e == 1):  # Si la variable es igual a 1
    if (a > b): #la variable a debe ser mayor que b para poder seguir la condicion y se ejecute
        if (a > c): # la variable a es debe ser mayor que c para poder seguir la condicion y se ejecute
            if(b > c): # la variable b debe ser mayor que c para seguir la condicion y se ejecute
                
               print(a, b, c)  #ejecutar las variables (a,b,c)
            else: #de lo contrario ejecute la variable (a,c,b)
               print(a, c, b)               
    if (c > a):  #si la variable c es mayor que a es verdadero
        if (c > b): # si la variable c es mayor que b es verdadero
            if(b > a):  #si la variable b es mayor que a es verdadero

               print(c, b, a) # de lo contrario ejecute la variable (c,b,a)
            else:
               print(c, a, b) #de lo contrario ejecutar la variable (c,a,b) 
               
    if (b > a): #si la variable b es mayor que a es verdadero
        if (b > c): #si la variable b es mayor que c es verdadero
            if(a > c): #si la variable a es mayor que c es verdadero
                #ejecute (b,a,c) de lo contrarion ejecute (b,c,a)
               print(b, a, c)
            else:
               print(b, c, a)

# si la seleccion es igual a 2
if (e == 2):
    if (a < b): #si la variable a es menor que b
        if (a < c): #si la variable a es menor que c
            if(b < c): # si la variale b es menor que c
                #ejecute (a,b,c) de lo contrario ejecute (a,c,b)
               print(a, b, c)
            else:
               print(a, c, b)
               
               
    if (c < a): #si la variable c es menor que a
        if (c < b): #si la varible c es menor que b
            if(b < a): #si la variable b es menor que a
                #ejecute (c,b,a) de lo contrario ejecute (c,a,b)
               print(c, b, a)
            else:
               print(c, a, b)
    if (b < a): #si la variable b es menor que a 
        if (b < c): #si la variable b es menor que c
            if(a < c): #si la variable b es menor que c
                
            #ejecute (b,a,c) de lo contrario ejecute (b,c,a)
               print(b, a, c)
            else:
               print(b, c, a)
if (a == b): #si la variable a es igual que b
    print("b y a son iguales") #ejecute que los numeros b y a son iguales
   
    if (a == c):  #si la variable a es igual a c ejecute a y c son iguales
        print("a y c son iguales")  
        if(b == c):  #si la variable b es igual a c ejecute b y c son iguales
           print(" b y c con iguales")
           if(a == b == c):  #si la variable b y c son igual ejecute  (a,b,c) son iguales
              print("todos son iguales")
  