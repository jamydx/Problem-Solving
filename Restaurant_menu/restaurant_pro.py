# PROGRAMA RESTAURANTE:
# By: Jonathan

# MY FUNCTIONS
def separador(message):
    print('=' * (len(message) * 2))


# DATA FROM THE PROBLEM
menu_options = {'1': ('Carne en su jugo', 89.60),
                '2': ('Higado encebollado', 60.25)}

dessert_options = {'1': ('Flan', 5),
                   '2': ('Gelatina', 3.50),
                   '3': ('No quiero postre', -10)}


# START THE PROGRAM:
mensaje = 'BIENVENIDO A MI RESTAURANTE'
print(mensaje)
print('Menu para hoy: ')


# Show the Main Menu
comprobar1 = True  # Por si el usuario elige mal el menu
while comprobar1:
    separador(mensaje)
    print('Menu para hoy: ')
    for key, (name, value) in menu_options.items():
        print('[{:>2}]  {:<20} | {:>5.2f} |'.format(key, name, value))
    separador(mensaje)

    # ELECTION 1
    choose1 = str(input('Elija un menu [1] o [2]: '))
    if choose1 not in menu_options:
        print('')
        print('¿No estan claras las opciones nob? Elige nuevamente...')
        print('')
    else:
        print('Eligió [{}] = {}'.format(choose1, menu_options.get(choose1)[0]))
        comprobar1 = False


# Show Desserts
comprobar2 = True  # Por si el usuario elige mal el postre
while comprobar2:
    separador(mensaje)
    print('Es momento de elegir el postre: ')
    for key, (name, value) in dessert_options.items():
        print('[{:>2}]  {:<20} | {:>6.2f} |'.format(key, name, value))
    separador(mensaje)

    # ELENTION 2
    choose2 = str(input('Elija una opción para el postre: '))
    if choose2 not in dessert_options:
        print(' ')
        print('¿En serio? Nuevamente tú... Escoge otra vez')
        print(' ')
    else:
        print('Eligió [{}] = {}'.format(choose2, dessert_options.get(choose2)[0]))
        comprobar2 = False


# Compute bill:
menu = menu_options.get(choose1)[1]
postre = dessert_options.get(choose2)[1]
total = menu + postre


# Show final result
separador(mensaje)
print('Total a pagar: {:.2f} pesos'.format(total))
separador(mensaje)
