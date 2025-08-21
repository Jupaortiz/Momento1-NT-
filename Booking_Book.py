friends = {}      # Diccionario para almacenar usuarios
books = {}        # Diccionario para almacenar libros
booking = {}      # Diccionario para almacenar préstamos
lend_book = True  # Variable de control para el ciclo principal
action = ''       # Variable para guardar la función a ejecutar

# Registro de usuario
def createFriend():
    data = []  # Lista para guardar datos del usuario
    id_friend = int(input("Id Amigo: "))
    name = input("Nombre amigo: ")
    data.append(name)
    phone = input("Telefono: ")
    data.append(phone)
    friends.update({id_friend: data})

# Registro de libros
def create_books():
    data = []  # Lista para guardar datos del libro
    id_book = int(input("Id libro: "))
    title = input("Nombre Libro: ")
    data.append(title)
    author = input("Autor: ")
    data.append(author)
    data.append("Libre")  # Estado del libro
    books.update({id_book: data})

# Préstamo de libros
def booking_books():
    loan_data = []  # Lista para guardar datos del préstamo
    id_loan = int(input("id prestamo: "))
    id_friend = int(input("Buscar amigo por id: "))
    friend = search_friend_by_id(id_friend)
    if not friend:
        print("Usuario no encontrado")
        return
    user_name = friend[0]
    loan_data.append(user_name)
    id_book = int(input("Buscar libro por id: "))
    book = search_book_by_id(id_book)
    if not book:
        print("Libro no encontrado")
        return
    if book[2] == "Libre":
        book[2] = "En prestamo"
    else:
        print("El libro ya fue prestado")
        return
    book_title = book[0]
    loan_data.append(book_title)
    loan_date = input("Fecha préstamo (dia/mes/año): ")
    loan_data.append(loan_date)
    return_date = input("Fecha devolución (dia/mes/año): ")
    loan_data.append(return_date)
    booking.update({id_loan: loan_data})

# Mostrar todos los usuarios registrados
def show_friend():
    for id, data in friends.items():
        print(f"ID: {id}, Nombre: {data[0]}, Teléfono: {data[1]}")

# Mostrar todos los libros registrados
def show_books():
    for id, data in books.items():
        print(f"ID: {id}, Título: {data[0]}, Autor: {data[1]}, Estado: {data[2]}")

# Mostrar todos los préstamos realizados
def show_booking():
    for id, data in booking.items():
        print(f"ID Préstamo: {id}, Usuario: {data[0]}, Libro: {data[1]}, Fecha préstamo: {data[2]}, Fecha devolución: {data[3]}")

# Buscar usuario por ID
def search_friend_by_id(id_friend):
    return friends.get(id_friend)

# Buscar libro por ID
def search_book_by_id(id_book):
    return books.get(id_book)

def salir():
    pass  # Función vacía para salir

# Menú de opciones
menu_options = '''
1. Prestar un libro.
2. Mostrar libros registrados.
3. Mostrar usuarios registrados.
4. Registrar un libro.
5. Registrar un usuario.
6. Mostrar préstamos.
7. Salir
'''

# Diccionario que relaciona opciones del menú con funciones
operations = {
    '1': booking_books,
    '2': show_books,
    '3': show_friend,
    '4': create_books,
    '5': createFriend,
    '6': show_booking,
    '7': salir,
}

# Mensajes de respuesta para casos especiales
response = {
    "1": "No hay libros o usuarios registrados",
    "2": "No hay libros registrados",
    "3": "No hay usuarios registrados"
}

print("Bienvenido a la biblioteca pública piloto")

# Ciclo principal del programa
while lend_book:
    print(menu_options)
    entrada = input("Elige una opción: ")

    # Validaciones para mostrar mensajes si no hay datos registrados
    no_books_or_users = (entrada == '1' and (len(books) == 0 or len(friends) == 0))
    no_books = (entrada == '2' and len(books) == 0)
    no_users = (entrada == '3' and len(friends) == 0)

    if no_books_or_users or no_books or no_users:
        print(response.get(entrada))
        print("---------------------------------------")
    else:
        action = operations.get(entrada)
        if action:
            action()
        else:
            print("Opción inválida")
        print("---------------------------------------")

    # Salir del programa
    if entrada == '7':
        print("¡Haz salido exitosamente!")
        lend_book = False