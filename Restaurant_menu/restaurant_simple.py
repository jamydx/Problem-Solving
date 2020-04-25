# PROGRAMA RESTAURANTE:
# By: Jonathan

# MY FUNCTIONS
def separador(message):
    print('=' * (len(message) * 2))


# DATA FROM THE PROBLEM
menu_options = {'1': ('Carne en su jugo', 89.60),
                '2': ('Higado encebollado', 60.25)}

dessert_options = {'1': ('Flan', 5.00),
                   '2': ('Gelatina', 3.50),
                   '3': ('No quiero postre', -10)}


# START THE PROGRAM:
mensaje = 'BIENVENIDO A MI RESTAURANTE'
print(mensaje.upper())


# Show first Menu: Main
separador(mensaje)
print('Menu para hoy: ')
for key, (name, value) in menu_options.items():
    print('[{:>2}]  {:<20} | {:>5.2f} |'.format(key, name, value))
separador(mensaje)

# ELECTION 1
choose1 = str(input('Elija un menu [1] o [2]: '))
print('Eligió [{}] = {}'.format(choose1, menu_options.get(choose1)[0]))


# Show Second Menu: Desserts
separador(mensaje)
print('Es momento de elegir el postre: ')
for key, (name, value) in dessert_options.items():
    print('[{:>2}]  {:<20} | {:>6.2f} |'.format(key, name, value))
separador(mensaje)

# ELECTION 2
choose2 = str(input('Elija una opción para el postre: '))
print('Eligió [{}] = {}'.format(choose2, dessert_options.get(choose2)[0]))


# Compute the bill:
menu = menu_options.get(choose1)[1]
postre = dessert_options.get(choose2)[1]
total = menu + postre


# Show final result
separador(mensaje)
print('Total a pagar: {:.2f} pesos'.format(total))
separador(mensaje)
