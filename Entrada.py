import Classes
import csv
import GenMod as rand

def entrada():
    c=12345
    m=32768
    a=1103515245
    Error=0
    Cantidad=0
    sizeC=''
    nameC=''
    maxWeightC=''
    nboxes=[]
    boxtypes=[]
    nombres = []
    #size=(200, 700, 300), name='Main Container', maxWeight=rand.randint(10, 20) * 100000000
    Entrada=int(input("Ingrese el tipo de entrada que desea realizar:\n1.-Consola\n2.-Archivo CSV\n3.-Aleatorio\n"))

    if Entrada==1:
    #CONTENEDOR
        Cadena=''
        while True:
            try:
                sizeC=input("Ingrese el tamaño del contenedor de la siguiente forma: X, Y, Z\n")
                sizeC = sizeC.split(',')
                if len(sizeC) != 3: raise IOError
                for i in range(len(sizeC)):
                    if float(sizeC[i]) <= 0:
                        raise ValueError
                    else:
                        sizeC[i] = float(sizeC[i])
                break
            except:
                print('Ha ocurrido un problema, se va a reiniciar el proceso')

        while True:
            try:
                nameC=input("Ingrese el nombre del contenedor\n")
                if nameC == ('' or ' ') or len(nameC) == 0: raise ValueError
                if nameC not in nombres: nombres.append(nameC)
                elif nameC in nombres: raise ValueError
                break

            except:
                print('Ha ocurrido un problema, se va a reiniciar el proceso')

        while True:
            try:
                maxWeightC=float(input("Ingrese el peso maximo del contenedor\n"))
                if maxWeightC<1:
                    raise TypeError
                break
            except:
                print('Ha ocurrido un problema, se va a reiniciar el proceso')

        while True:
            try:
                Cantidad=int(input('Ingrese la cantidad de tipos de caja\n'))
                if Cantidad < 1:
                    raise ValueError
                break
            except:
                print('Ha ocurrido un problema, se va a reiniciar el proceso')

    #FIN CONTENEDOR
    # TIPO DE CAJA

        for i in range(Cantidad):
            while True:
                try:
                    nombre = input('Ingrese el nombre de la caja no.' + str(i + 1) + '\n')
                    if nombre == ('' or ' ') or nombre == None: raise ValueError
                    if nombre not in nombres: nombres.append(nameC)
                    elif nombre in nombres: raise ValueError
                    break
                except:
                    print('Ha ocurrido un problema, se va a reiniciar el proceso')

            while True:
                try:
                    beneficio = float(input('Ingrese el Beneficio de la caja no.' + str(i + 1) + '\n'))
                    if beneficio <= 0: raise ValueError
                    break
                except:
                    print('Ha ocurrido un problema, se va a reiniciar el proceso')

            while True:
                try:
                    peso = float(input('Ingrese el Peso de la caja no.' + str(i + 1) + '\n'))
                    if peso <= 0: raise ValueError
                    break
                except:
                    print('Ha ocurrido un problema, se va a reiniciar el proceso')

            while True:
                try:
                    dimensiones = input('Ingrese las dimensiones de la caja no.' + str(i + 1) + 'con formato: X, Y, Z \n')
                    dimensiones = dimensiones.split(',')
                    dimensiones =[float(dimensiones[0]), float(dimensiones[1]), float(dimensiones[2])]
                    for element in dimensiones:
                        if element <= 0: raise ValueError
                    break
                except:
                    print('Ha ocurrido un problema, se va a reiniciar el proceso')

            while True:
                try:
                    ncajas = int(input('Ingrese la cantidad de cajas deltipo de caja no.' + str(i + 1) + '\n'))
                    if ncajas <= 0: raise ValueError
                    break
                except:
                    print('Ha ocurrido un problema, se va a reiniciar el proceso')

            boxtypes.append(Classes.BoxType(type=nombre, benefit=beneficio, weight=peso, size=dimensiones))
            nboxes.append(ncajas)

        bin = Classes.Bin(size=(float(sizeC[0]), float(sizeC[1]), float(sizeC[2])), name=nameC,
                          maxWeight=maxWeightC)
        return ([bin, boxtypes, nboxes])
    #FIN TIPO DE CAJA

    elif Entrada==2:
        try:
            CSV=[]
            #CONTENEDOR
            with open ('3D Bin Packing.csv','r') as Archivo:
                Lineas=csv.reader(Archivo,delimiter=';')
                for row in Lineas:
                    CSV.append(row)

            sizeC=CSV[0][0]
            sizeC=sizeC.split(',')
            if len(sizeC) != 3: raise IOError
            for element in sizeC:
                if float(element) <= 0: raise ValueError
            nameC=CSV[0][1]
            if nameC == ('' or ' ') or len(nameC) == 0: raise IOError
            if nameC not in nombres: nombres.append(nameC)
            elif nameC in nombres: raise ValueError
            maxWeightC=float(CSV[0][2])
            if maxWeightC <= 0: raise ValueError
            #FIN CONTENEDOR
            CSV.pop(0)
            #TIPO DE CAJA
            for Tipo in CSV:
                if len(Tipo) < 5: raise ValueError
                if int(Tipo[4])<1: raise ValueError
                Tipo[3]=Tipo[3].split(',')
                if Tipo[0] == ('' or ' ') or len(Tipo[0]) == 0: raise IOError
                if Tipo[0] not in nombres: nombres.append(Tipo[0])
                elif Tipo[0] in nombres: raise ValueError
                if float(Tipo[1]) <= 0 or float(Tipo[2]) <= 0: raise ValueError
                if (float(Tipo[3][0]) or float(Tipo[3][1]) or float(Tipo[3][2])) <= 0: raise ValueError
                boxtypes.append(Classes.BoxType(type=Tipo[0],benefit=float(Tipo[1]),weight=float(Tipo[2]),
                                                size=(float(Tipo[3][0]),float(Tipo[3][1]),float(Tipo[3][2]))))
                nboxes.append(int(Tipo[4]))

            bin = Classes.Bin(size=(float(sizeC[0]), float(sizeC[1]), float(sizeC[2])), name=nameC,
                              maxWeight=maxWeightC)
            return ([bin, boxtypes, nboxes])
            #FIN TIPO DE CAJA
        except:
            print('Ocurrio un error durante la carga del archivo \'3D Bin Packing\'. \
                  \nRevise que la información sea correcta y cuente con el formato necesario.')

    elif Entrada==3:

        # bin = Classes.Bin(size=(rand.randint(100,300), rand.randint(100, 300), rand.randint(100, 300)))
        sizeC = [rand.randint(100,300), rand.randint(100, 300), rand.randint(100, 300)]
        nameC = 'Main Container'
        maxWeightC = rand.randint(1000, 10000)

        for i in range(rand.randint(1, 10)):
            depth = rand.randint(20, 100)
            width = rand.randint(20, 100)
            height = rand.randint(20, 100)
            boxtypes.append(Classes.BoxType(i + 1, rand.randint(20, 50), rand.randint(20, 30),
                                            (width, depth, height)))
            nboxes.append(rand.randint(20, 50))
           # print(boxtypes[i])
        bin = Classes.Bin(size=(float(sizeC[0]), float(sizeC[1]), float(sizeC[2])), name=nameC,
                          maxWeight=maxWeightC)
        return ([bin, boxtypes, nboxes])
    # print(sizeC)
    #print(nameC)
    # if Entrada != 3:
    #     sizeC=sizeC.split(",")