# """1."""
# class Rectangulo:  
#     def __init__(self, base, altura):  
#         self.base = base  
#         self.altura = altura  

#     def area(self):  
#         return self.base * self.altura  

 
# rectangulo = Rectangulo(5, 10)  
# print("El área del rectángulo es:", rectangulo.area()) 

# """2"""

# class Mate:  
#     def __init__(self, max_cebadas):  
#         self.max_cebadas = max_cebadas   
#         self.cebadas_restantes = max_cebadas    
#         self.estado = "lleno"   

#     def cebar(self):  
#         if self.estado == "lleno":  
#             raise Exception("¡Cuidado! ¡Te quemaste!")  
#         else:  
#             self.estado = "lleno"    
#             print("Mate cebado con agua.")  

#     def beber(self):  
#         if self.estado == "vacío":  
             
#             if self.cebadas_restantes > 0:  
#                 print("Advertencia: el mate está lavado.")  
#             else:  
#                 print("¡El mate está vacío!")  
#             return  

#         self.estado = "vacío"   
#         if self.cebadas_restantes > 0:  
#             self.cebadas_restantes -= 1   
#         if self.cebadas_restantes < 0:  
#             self.cebadas_restantes = 0   
#         print("Se ha bebido del mate.")  

#     def estado_mate(self):  
#         return {  
#             "cebadas_restantes": self.cebadas_restantes,  
#             "estado": self.estado  
#         }  


# """3"""
# class Botella:  
#     def __init__(self, corcho=None):  
#         self.corcho = corcho  

#     def destapada(self):  
#         return self.corcho is None    


# class Sacacorchos:  
#     def __init__(self):  
#         self.corcho_sacado = None   

#     def destapar(self, botella):  
#         if botella.destapada():  
#             raise Exception("¡La botella ya está destapada!")  
#         if self.corcho_sacado is not None:  
#             raise Exception("¡El sacacorchos ya tiene un corcho!")  
        
         
#         self.corcho_sacado = botella.corcho  
#         botella.corcho = None    
#         print(f"{self.corcho_sacado} ha sido sacado de la botella.")  

#     def limpiar(self):  
#         if self.corcho_sacado is None:  
#             raise Exception("¡No hay un corcho en el sacacorchos!")  
        
#         print(f"Limpiando el sacacorchos, el corcho {self.corcho_sacado} ha sido retirado.")  
#         self.corcho_sacado = None    


# """4"""
# class Restaurante:  
#     def __init__(self, restaurante_nombre, tipo_comida):  
#         self.restaurante_nombre = restaurante_nombre  
#         self.tipo_comida = tipo_comida   
    
#     def describir_restaurante(self):  
#         print(f"Restaurante: {self.restaurante_nombre}")  
#         print(f"Tipo de comida: {self.tipo_comida}")  
    
#     def abrir_restaurante(self):  
#         print(f"El restaurante {self.restaurante_nombre} está ahora abierto.")  


# class Heladeria(Restaurante):  
#     def __init__(self, restaurante_nombre, tipo_comida, sabores):  
#         super().__init__(restaurante_nombre, tipo_comida)  
#         self.sabores = sabores 
    
#     def mostrar_sabores(self):  
#         print(f"Sabores disponibles en {self.restaurante_nombre}:")  
#         for sabor in self.sabores:  
#             print(f"- {sabor}") 


# """5"""

# class Personaje:  
#     def __init__(self, vida, posicion, velocidad):  
#         self.vida = vida     
#         self.posicion = posicion    
#         self.velocidad = velocidad  

#     def recibir_ataque(self, cantidad):  
#         self.vida -= cantidad    
#         if self.vida <= 0:  
#             raise Exception("¡El personaje ha sido derrotado!")  
#         print(f"Vida restante: {self.vida}")  

#     def mover(self, direccion):      
#         self.posicion = (self.posicion[0] + direccion[0] * self.velocidad,  
#                          self.posicion[1] + direccion[1] * self.velocidad)  
#         print(f"Nueva posición: {self.posicion}")  


# class Soldado(Personaje):  
#     def __init__(self, vida, posicion, velocidad, ataque):  
#         super().__init__(vida, posicion, velocidad)   
#         self.ataque = ataque   

#     def atacar(self, enemigo):  
#         print(f"El soldado ataca con {self.ataque} de daño.")  
#         enemigo.recibir_ataque(self.ataque)  


# class Campesino(Personaje):  
#     def __init__(self, vida, posicion, velocidad, cosecha):  
#         super().__init__(vida, posicion, velocidad)  
#         self.cosecha = cosecha    

#     def cosechar(self):  
#         print(f"El campesino cosecha {self.cosecha} unidades.")  
#         return self.cosecha 
    

# """6"""    
# class Usuario:  
#     def __init__(self, nombre, apellido, email, edad, telefono):  
#         self.nombre = nombre           
#         self.apellido = apellido       
#         self.email = email             
#         self.edad = edad              
#         self.telefono = telefono        

#     def describir_usuario(self):    
#         print("Resumen del usuario:")  
#         print(f"Nombre: {self.nombre} {self.apellido}")  
#         print(f"Email: {self.email}")  
#         print(f"Edad: {self.edad}")  
#         print(f"Teléfono: {self.telefono}")  

#     def saludar_usuario(self):    
#         print(f"Hola, {self.nombre} {self.apellido}! Bienvenido a nuestro sistema.")  


# """7"""
# class Usuario:  
#     def __init__(self, nombre, apellido, email, edad, telefono):  
#         self.nombre = nombre          
#         self.apellido = apellido      
#         self.email = email              
#         self.edad = edad              
#         self.telefono = telefono        

#     def describir_usuario(self):    
#         print("Resumen del usuario:")  
#         print(f"Nombre: {self.nombre} {self.apellido}")  
#         print(f"Email: {self.email}")  
#         print(f"Edad: {self.edad}")  
#         print(f"Teléfono: {self.telefono}")  

#     def saludar_usuario(self):    
#         print(f"Hola, {self.nombre} {self.apellido}! Bienvenido a nuestro sistema.")  


# class Admin(Usuario):  
#     def __init__(self, nombre, apellido, email, edad, telefono):  
#         super().__init__(nombre, apellido, email, edad, telefono)  
#         self.privilegios = [  
#             "puede postear en el foro",  
#             "puede borrar un post",  
#             "puede banear usuarios",  
#             "puede acceder a informes",  
#             "puede gestionar cuentas de usuario"  
#         ]  

#     def mostrar_privilegios(self):    
#         print("Privilegios del administrador:")  
#         for privilegio in self.privilegios:  
#             print(f"- {privilegio}")     


# """8""" 

# class Usuario:  
#     def __init__(self, nombre, apellido, email, edad, telefono):  
#         self.nombre = nombre            
#         self.apellido = apellido        
#         self.email = email             
#         self.edad = edad                
#         self.telefono = telefono        

#     def describir_usuario(self):   
#         print("Resumen del usuario:")  
#         print(f"Nombre: {self.nombre} {self.apellido}")  
#         print(f"Email: {self.email}")  
#         print(f"Edad: {self.edad}")  
#         print(f"Teléfono: {self.telefono}")  

#     def saludar_usuario(self):    
#         print(f"Hola, {self.nombre} {self.apellido}! Bienvenido a nuestro sistema.")  


# class Privilegios:  
#     def __init__(self):  
#         self.privilegios = [  
#             "puede postear en el foro",  
#             "puede borrar un post",  
#             "puede banear usuarios",  
#             "puede acceder a informes",  
#             "puede gestionar cuentas de usuario"  
#         ]  

#     def mostrar_privilegios(self):  
#         """Muestra el conjunto de privilegios."""  
#         print("Privilegios del administrador:")  
#         for privilegio in self.privilegios:  
#             print(f"- {privilegio}")  


# class Admin(Usuario):  
#     def __init__(self, nombre, apellido, email, edad, telefono):  
#         super().__init__(nombre, apellido, email, edad, telefono) 
#         self.privilegios = Privilegios()  