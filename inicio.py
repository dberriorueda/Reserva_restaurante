#Nombre de la clase
class Reserva:
    #Llamar metodo constructor
    print(f"...Bienvenido al restaurante el buen sabor...")

    def __init__(self,nombre,telefono,num_comensales,mesa):
        self.nombre = nombre
        self.telefono = telefono
        self.num_comensales = num_comensales
        self.mesa = mesa
    
    def asignar_mesa(self):
        print("")

while True:
    nombre = input("Nombre del titular de la reserva:")

    while True:
        telefono = (input("Numero de telefono del contacto:"))
        if telefono.isdigit():
            telefono = int(telefono)
            break
        else:
            print("No valido. Digite su numero de telefono.")
    
    while True:
        num_comensales = (input("Numero de personas en la reserva:"))
        if num_comensales.isdigit():
            num_comensales = int(num_comensales)
            break
        else:
            print("No valido. Cuantas personas van a estar en la reserva.")
    
    while True:
        mesa = input("Numero de mesa asignada.")

        restaurante = Reserva(nombre,telefono,num_comensales,mesa)

        print("Opciones:")
        print("1- Mesa")
        print("2- Salir")

        opcion = input("Seleccione una opcion (1/2): ")

        if opcion == '1':
            restaurante.asignar_mesa()
            print(f"""
            El nombre del titular de la reserva es : {nombre}
            Numero de telefono es : {telefono}
            Numero de personas en la reservas son : {num_comensales}
            La mesa asignada es: Mesa {mesa}
           """)
            break
        elif opcion =='2':
            print("Salir")
            break
        else:
            print("Opcion no valida. Intente de nuevo.")