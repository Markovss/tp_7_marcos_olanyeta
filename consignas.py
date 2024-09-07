#1 clase rectangulo

class Rectangulo:
    
    def __init__(self,base,altura):
        self.base= base
        self.altura= altura

    def area(self):
        return self.base * self.altura

rectangulo = Rectangulo(10,26)
print("El área del rectángulo es:",rectangulo.area())
#2 clase mate

class Mate:
    def __init__(self, n):
        self.n= n
        self.cebadas_restantes= n
        self.lleno= False
    
    def cebar(self):
        if self.lleno:
            raise Exception("¡Cuidado! ¡Te quemaste!")
        else:
            self.lleno= True

    def beber(self):
        if not self.lleno:
            raise Exception("¡El mate está vacío!")
        else:
            self.lleno= False
            if self.cebadas_restantes > 0:
                self.cebadas_restantes -= 1
            else:
                print("Advertencia: el mate está lavado.")

mate = Mate(5)

try:
    mate.cebar()
    mate.beber()
    mate.beber()
except Exception as e:
    print(e)

for _ in range(5):
    try:
        mate.cebar()
        mate.beber()
    except Exception as e:
        print(e)

#3 Botella y Sacacorchos

class Corcho:
    def __init__(self, bodega):
        self.bodega= bodega

class Botella:
    def __init__(self, corcho):
        self.corcho= corcho

class Sacacorchos:
    def __init__(self):
        self.corcho= None

    def destapar(self, botella):
        if botella.corcho is None:
            print("La botella ya está destapada.")
        elif self.corcho is not None:
            print("El sacacorchos ya contiene un corcho.")
        else:
            self.corcho= botella.corcho
            botella.corcho= None
            print("Botella destapada. Corcho sacado.")

    def limpiar(self):
        if self.corcho is None:
            print("No hay corcho en el sacacorchos.")
        else:
            print(f"Corcho de la bodega {self.corcho.bodega} removido del sacacorchos.")
            self.corcho = None

corcho = Corcho('"lo de Corleone"')
botella = Botella(corcho)
sacacorchos = Sacacorchos()
sacacorchos.destapar(botella)
sacacorchos.limpiar()
sacacorchos.destapar(botella)
sacacorchos.limpiar()

#4 heladeria

class Restaurante:
    def __init__(self, restaurante_nombre, tipo_comida):
        self.restaurante_nombre = restaurante_nombre
        self.tipo_comida = tipo_comida

    def describir_restaurante(self):
        print(f"Restaurante: {self.restaurante_nombre}")
        print(f"Tipo de comida: {self.tipo_comida}")

    def abrir_restaurante(self):
        print(f"El restaurante {self.restaurante_nombre} ahora está abierto.")

class Heladeria(Restaurante):
    def __init__(self, restaurante_nombre, tipo_comida, sabores):
        super().__init__(restaurante_nombre, tipo_comida)
        self.sabores = sabores

    def mostrar_sabores(self):
        print(f"Sabores disponibles en {self.restaurante_nombre}:")
        for sabor in self.sabores:
            print(f"- {sabor}")

heladeria = Heladeria('Heladería "Grido"',"Helados",["Vainilla", "Chocolate", "Frutilla", "Maracuyá"])
heladeria.describir_restaurante()
heladeria.abrir_restaurante()
heladeria.mostrar_sabores()

#5 personajes

class Personaje:
    def __init__(self, vida, posicion, velocidad):
        self.vida= vida
        self.posicion = posicion
        self.velocidad = velocidad
    def recibir_ataque(self, cantidad):
        self.vida -= cantidad
        if self.vida <= 0:
            print("El personaje murió.")

    def mover(self, direccion):
        if direccion == "izquierda":
            self.posicion[0] -= self.velocidad
        elif direccion == "derecha":
            self.posicion[0] += self.velocidad
        elif direccion == "arriba":
            self.posicion[1] += self.velocidad
        elif direccion == "abajo":
            self.posicion[1] -= self.velocidad
        print(f"El personaje se ha movido a la posición {self.posicion}")

class Soldado(Personaje):
    def __init__(self, vida, posicion, velocidad, ataque):
        super().__init__(vida, posicion, velocidad)
        self.ataque = ataque

    def atacar(self, otro_personaje):
        print(f"El soldado ataca y causa {self.ataque} puntos de daño.")
        otro_personaje.recibir_ataque(self.ataque)

class Campesino(Personaje):
    def __init__(self, vida, posicion, velocidad, cosecha):
        super().__init__(vida, posicion, velocidad)
        self.cosecha = cosecha

    def cosechar(self):
        print(f"El campesino ha cosechado {self.cosecha} unidades.")
        return self.cosecha

soldado = Soldado(100, [0, 0], 2, 10)
campesino = Campesino(50, [5, 5], 1, 20)
soldado.atacar(campesino)
campesino.mover("izquierda")
campesino.cosechar()

#6 usuario

class Usuario:
    def __init__(self, nombre, apellido, correo, ciudad):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.ciudad = ciudad

    def describir_usuario(self):
        print(f"Perfil del usuario:")
        print(f"Nombre: {self.nombre} {self.apellido}")
        print(f"Correo: {self.correo}")
        print(f"Ciudad: {self.ciudad}")

    def saludar_usuario(self):
        print(f"Hola, {self.nombre} {self.apellido} ¡Bienvenido!")

usuario1 = Usuario("John", "Mamani Quispe", "mamaniwilliam@hotmail.com", "San Salvador de Jujuy")
usuario2 = Usuario("Mona", "Gimenez", "lamonagimenez@gmail.com", "Córdoba")
usuario3 = Usuario("Lionel", "Messi", "lionel_messi_10@bgmail.com", "Rosario")
usuario1.describir_usuario()
usuario1.saludar_usuario()
usuario2.describir_usuario()
usuario2.saludar_usuario()
usuario3.describir_usuario()
usuario3.saludar_usuario()

#7 admin

class Admin(Usuario):
    def __init__(self, nombre, apellido, correo, ciudad, privilegios):
        super().__init__(nombre, apellido, correo, ciudad)
        self.privilegios = privilegios

    def mostrar_privilegios(self):
        print(f"Privilegios del administrador {self.nombre} {self.apellido}:")
        for privilegio in self.privilegios:
            print(f"- {privilegio}")

admin = Admin("Marc", "zuquermon", "creadordelfeisbuk@meta.com", "Chelsea",["puede postear en el foro", "puede borrar un post", "puede banear usuarios"])
admin.describir_usuario()
admin.saludar_usuario()
admin.mostrar_privilegios()

#8

class Privilegios:
    def __init__(self, privilegios):
        self.privilegios = privilegios

    def mostrar_privilegios(self):
        print(f"Privilegios:")
        for privilegio in self.privilegios:
            print(f"- {privilegio}")

class Admin(Usuario):
    def __init__(self, nombre, apellido, correo, ciudad, privilegios):
        super().__init__(nombre, apellido, correo, ciudad)
        self.privilegios = Privilegios(privilegios)

admin = Admin("Niki", "Nicol", "lanickynicol@yahoo.com", "Tamaulipas",["puede postear en el foro", "puede borrar un post", "puede banear usuarios"])
admin.describir_usuario()
admin.saludar_usuario()
admin.privilegios.mostrar_privilegios()