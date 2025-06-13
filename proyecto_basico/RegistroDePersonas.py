mibase = []
#CRUD Create - Read - Update - Delete
def agregarPersona(persona):
    mibase.append(persona)
    print("Agregando Personas")
def listarPersona(rut):
    for persona in mibase:
        if(persona.get("rut")==rut):
            return persona
    return ({"message":"Persona no encontrada."})
def listarPersonas():
    for persona in mibase:
        print(persona)
    print("Listando Personas")
def eliminarPersona(rut):
    for persona in mibase:
        if(persona.get("rut")==rut):
            mibase.remove(persona)
            return({"message":"Persona Eliminada"})
    return ({"message":"Persona no Encontrada"})
def modificarPersona(rut,persona):
    print("Modificando Persona")
    for buscar in mibase:
        if(buscar.get("rut")==rut):
            buscar = persona
            return({"message":"Persona modificada"})
    return ({"message":"Persona no encontrada."})
def menu():
    while(True):
        print("1. Para agregar")
        print("2. Para Listar Personas")
        print("3. Para Buscar una Persona")
        print("4. Para Eliminar")
        print("5. Para Modificar")
        opcion = input("Ingrese opción")
        if(opcion=="1"):
            persona = {}
            persona['rut'] = input("Ingrese Rut de la persona:\n")
            persona['nombre'] = input("Ingrese Nombre:\n")
            persona['apellido'] = input("Ingrese Apellido:\n")
            print(persona)
            agregarPersona(persona)
        elif(opcion=="2"):
            nombre = input("Ingrese nombre a buscar")
            apellido = input("Ingrese apellido a buscar")
            listarPersonas()
        elif(opcion=="3"):
            rut = input("Ingrese rut a buscar")
            persona = listarPersona(rut)
            print("El nombre de la persona es: ", persona)
        elif(opcion=="4"):
            rut = input("Ingrese rut a Eliminar")
            eliminarPersona(rut)
        elif(opcion=="5"):
            rut=input("Ingrese rut a Modificar")
            persona = listarPersona(rut)
            if(persona.get("message") is None):
                persona["nombre"]=input("Ingrese el Nuevo Nombre")
                persona["apellido"]=input("Ingrese el Nuevo Apellido")
            modificarPersona(rut,persona)
def main():
    menu()

main()