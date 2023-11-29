class Persona:#instancia es un objeto en memoria
    #funcion dentro de una clases se llama metodo
    
    def __init__(self, id: int, nombre: str, apellido: str, edad: int, email: str, deportes: list) -> None:
        #self direccion de memoria entonces id, nombre, apellido, edad se guardan en la direccion de memoria de self
        #hay 3 tipos de atributos publico, privado y protegido
        self.id = id
        self.__nombre = nombre.capitalize()
        self.apellido = apellido#publico
        self.__edad = edad #privado
        self._email = email#protegido
        self.deportes = deportes

    def __contains__(self, item):
        return item in self.deportes

    #se programa lo que se va a mostrar si se printea a persona_1
    def __str__(self) -> str:
        return f"{self.__nombre} {self.apellido} {self.__edad} {self._email}" 
    
    def __getitem__(self, key: str):

        match key:
            case "id":
                value = self.id 
            case "nombre":
                value = self.nombre 
            case "apellido":
                value = self.apellido 
            case "edad":
                value = self.edad 
            case "email":
                value = self._email 
            case 0:
                value = self.id 
            case 1:
                value = self.nombre 
            case 2:
                value = self.apellido 
            case 3:
                value = self.edad 
            case 4:
                value = self._email 
        
        return value

    def __setitem__(self, index, value):
        match index:
            case "id":
                value = self.id = value
            case "nombre":
                value = self.nombre = value
            case "apellido":
                value = self.apellido = value
            case "edad":
                value = self.edad = value
            case "email":
                value = self._email = value
            case 0:
                value = self.id = value
            case 1:
                value = self.nombre = value
            case 2:
                value = self.apellido = value
            case 3:
                value = self.edad = value
            case 4:
                value = self._email = value

    def __iter__(self):
        for value in [self.id, self.nombre, self.apellido, self.edad, self._email]:
            yield value#es como un return pero que termina cuando termina de iterar
    
    def __gt__(self, objeto):
        return self.edad > objeto.edad
    

    

    @property
    def edad(self):  #esto es el getter
        return self.__edad
    
    @edad.setter
    def edad(self, value: int):  #esto es el setter
        if value > 0 and value < 100:
            self.__edad = value

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, value: str):
        self.__nombre = value.capitalize()
    
    def get_nombre_completo(self):
        return f"{self.__nombre} {self.apellido}"

    def presentarse(self):
        print(f"Hola mi nombre es {self.__nombre} {self.apellido} y mi edad es {self.__edad}")



class Empleado(Persona):
    def __init__(self, id: int, nombre: str, apellido: str, edad: int, email: str, deportes: list, sueldo: int) -> None:
        super().__init__(id, nombre, apellido, edad, email, deportes)
        self.sueldo = sueldo
    
    def presentarse(self):
        print(f"Hola soy un empleado mi apellido es {self.apellido} y mi sueldo es ${self.sueldo}")

    def saludar(self):
        print("Hola pobres")

persona_1 = Persona(10, "Jose", "Lopez", 30, "pepe@gmail.com",["futbol", "natacion","golf"])
persona_2 = Persona(14, "Mariana", "Suarez", 24, "marian@gmail.com",["voley", "tenis", "golf", "polo", "handball"])

empleado_1 = Empleado(15, "Mariano", "Alvarez", 24, "marian@gmail.com",["voley", "tenis", "golf", "polo", "handball"],456000)

# persona_1.presentarse()
# persona_2.presentarse()
# print(persona_1.get_nombre_completo())
# persona_1.nombre = ("mario")
# persona_1.presentarse()
# persona_1.nombre
#print(persona_1)

#print(persona_1["nombre"])

# for value in persona_1:
#     print(value)


# persona_1[1] = "sebastian"
# print(persona_1["nombre"])


# print("golf" in persona_1)#devuelve true si esta o false si no esta

empleado_1.presentarse()
persona_2.presentarse()

print(persona_1 > persona_2)