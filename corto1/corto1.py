#funcion que genera la secuencia collatz de un número n
def collatzf(n):
    num = n #se asigna la entrada de a otra variable
    listacollatz = [num]
    while (num != 1): #mientras el número no se reduzca hasta 1 continuar operando
        if num%2 == 0 : #si el número es par
            #print("es par")
            num /= 2  #se divide entre 2
            listacollatz.append(num) #se agrega a la lista
            
        else: #si el número es impar
            #print("es impar")
            num *= 3 #se multiplica por 3
            num += 1 #se le suma 1
            listacollatz.append(num) #se agrega a la lista
    return  listacollatz   

#a = int(input())
archivo = open("collatz.txt", 'w')
fc = 10
for i in range (2, fc+1):
    print(str(collatzf(i)))