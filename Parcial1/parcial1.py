class Contacto:
    def __init__(self, nombre, apellido, organizacion, telefono, direccion):
     self.nombre = nombre
     self.apellido = apellido
     self.organizacion = organizacion
     self.telefono = telefono
     self.direccion = direccion

    def obtener_datos(self):
     return [self.nombre, self.apellido, self.organizacion, self.telefono, self.direccion]


class Directorio:
    def __init__(self):

     self.contactos = [["Nombre","Apellido","Organización","Teléfono","Dirección"]]

    def agregar_contacto(self, contacto):
     self.contactos.append(contacto.obtener_datos())

    def mostrar_contactos(self):
        print("Contact Directory:\n")
        for fila in self.contactos:
            print("\t".join(map(str, fila)))

directorio = Directorio()

contacto1 = Contacto("David","Fernandez","Biosalc","320065780","Calle 44AN#4N-105")
contacto2 = Contacto("Maria","Gonzalez","Postobon","3188507789","Calle 55 # 1e-45")
contacto3 = Contacto("Pedro","Jimenez","Helppeople","300556790","Carrera 59Bis-34")

directorio.agregar_contacto(contacto1)
directorio.agregar_contacto(contacto2)
directorio.agregar_contacto(contacto3)

directorio.mostrar_contactos()
