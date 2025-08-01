from datetime import datetime
import os

class Amigo:
    def __init__(self, id_amigo, nombre, telefono, email):
        self.id = id_amigo
        self.nombre = nombre
        self.telefono = telefono
        self.email = email
    
    def __str__(self):
        return f"ID: {self.id} | Nombre: {self.nombre} | Tel: {self.telefono} | Email: {self.email}"

class Libro:
    def __init__(self, id_libro, titulo, autor, genero):
        self.id = id_libro
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.disponible = True
    
    def prestar(self):
        self.disponible = False
    
    def devolver(self):
        self.disponible = True
    
    def __str__(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f"ID: {self.id} | Título: {self.titulo} | Autor: {self.autor} | Estado: {estado}"

class Prestamo:
    def __init__(self, id_prestamo, id_amigo, id_libro):
        self.id = id_prestamo
        self.id_amigo = id_amigo
        self.id_libro = id_libro
        self.fecha_prestamo = datetime.now().strftime("%d/%m/%Y")
        self.activo = True
    
    def devolver_libro(self):
        self.activo = False
    
    def __str__(self):
        estado = "Activo" if self.activo else "Devuelto"
        return f"ID: {self.id} | Amigo: {self.id_amigo} | Libro: {self.id_libro} | Fecha: {self.fecha_prestamo} | Estado: {estado}"

class Biblioteca:
    def __init__(self):
        self.amigos = []
        self.libros = []
        self.prestamos = []
        self.id_amigo = 1
        self.id_libro = 1
        self.id_prestamo = 1
    
    def mostrar_menu(self):
        print("\n=== BIBLIOTECA ===")
        print("1. Registrar amigo")
        print("2. Registrar libro")
        print("3. Ver amigos")
        print("4. Ver libros")
        print("5. Crear préstamo")
        print("6. Devolver libro")
        print("7. Ver préstamos")
        print("8. Salir")
        return input("Opción: ")
    
    def registrar_amigo(self):
        print("\n=== REGISTRAR AMIGO ===")
        nombre = input("Nombre: ")
        telefono = input("Teléfono: ")
        email = input("Email: ")
        
        amigo = Amigo(self.id_amigo, nombre, telefono, email)
        self.amigos.append(amigo)
        self.id_amigo += 1
        print(f"Amigo registrado con ID: {amigo.id}")
    
    def registrar_libro(self):
        print("\n=== REGISTRAR LIBRO ===")
        titulo = input("Título: ")
        autor = input("Autor: ")
        genero = input("Género: ")
        
        libro = Libro(self.id_libro, titulo, autor, genero)
        self.libros.append(libro)
        self.id_libro += 1
        print(f"Libro registrado con ID: {libro.id}")
    
    def ver_amigos(self):
        print("\n=== LISTA DE AMIGOS ===")
        if not self.amigos:
            print("No hay amigos registrados")
        else:
            for amigo in self.amigos:
                print(amigo)
    
    def ver_libros(self):
        print("\n=== LISTA DE LIBROS ===")
        if not self.libros:
            print("No hay libros registrados")
        else:
            for libro in self.libros:
                print(libro)
    
    def crear_prestamo(self):
        print("\n=== CREAR PRÉSTAMO ===")
        
        if not self.amigos:
            print("No hay amigos registrados")
            return
        
        libros_disponibles = [l for l in self.libros if l.disponible]
        if not libros_disponibles:
            print("No hay libros disponibles")
            return
        
        print("Amigos:")
        for amigo in self.amigos:
            print(f"{amigo.id}. {amigo.nombre}")
        
        id_amigo = int(input("ID del amigo: "))
        amigo = next((a for a in self.amigos if a.id == id_amigo), None)
        if not amigo:
            print("Amigo no encontrado")
            return
        
        print("Libros disponibles:")
        for libro in libros_disponibles:
            print(f"{libro.id}. {libro.titulo}")
        
        id_libro = int(input("ID del libro: "))
        libro = next((l for l in libros_disponibles if l.id == id_libro), None)
        if not libro:
            print("Libro no encontrado")
            return
        
        prestamo = Prestamo(self.id_prestamo, id_amigo, id_libro)
        self.prestamos.append(prestamo)
        self.id_prestamo += 1
        libro.prestar()
        
        print(f"Préstamo creado con ID: {prestamo.id}")
    
    def devolver_libro(self):
        print("\n=== DEVOLVER LIBRO ===")
        
        prestamos_activos = [p for p in self.prestamos if p.activo]
        if not prestamos_activos:
            print("No hay préstamos activos")
            return
        
        print("Préstamos activos:")
        for prestamo in prestamos_activos:
            amigo = next((a for a in self.amigos if a.id == prestamo.id_amigo), None)
            libro = next((l for l in self.libros if l.id == prestamo.id_libro), None)
            print(f"{prestamo.id}. {libro.titulo} - {amigo.nombre}")
        
        id_prestamo = int(input("ID del préstamo: "))
        prestamo = next((p for p in prestamos_activos if p.id == id_prestamo), None)
        if not prestamo:
            print("Préstamo no encontrado")
            return
        
        prestamo.devolver_libro()
        libro = next((l for l in self.libros if l.id == prestamo.id_libro), None)
        libro.devolver()
        
        print("Libro devuelto exitosamente")
    
    def ver_prestamos(self):
        print("\n=== LISTA DE PRÉSTAMOS ===")
        if not self.prestamos:
            print("No hay préstamos registrados")
        else:
            for prestamo in self.prestamos:
                print(prestamo)
    
    def ejecutar(self):
        while True:
            opcion = self.mostrar_menu()
            
            if opcion == '1':
                self.registrar_amigo()
            elif opcion == '2':
                self.registrar_libro()
            elif opcion == '3':
                self.ver_amigos()
            elif opcion == '4':
                self.ver_libros()
            elif opcion == '5':
                self.crear_prestamo()
            elif opcion == '6':
                self.devolver_libro()
            elif opcion == '7':
                self.ver_prestamos()
            elif opcion == '8':
                print("¡Adiós!")
                break
            else:
                print("Opción inválida")
            
            input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    biblioteca = Biblioteca()
    biblioteca.ejecutar()