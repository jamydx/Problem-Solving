# Juego para practicar Ingles
# By Jonathan Machuca

# Modules
import pandas as pd
import random

# Cargar los datos
data = pd.read_csv('english_and_spanish_words.csv')
# data.head(10) Mostrar los datos en pantalla.


# Extraer los datos
indice = len(data['N'])
english_word = data['English']
spanish_word = data['Spanish']


# Presentación del juego
print("=====================================================")
print("| Welcome to: Practice your English Vocabulary      |")
#print("| Topic: Elements of Artifical Intelligence         |")
print("=====================================================")
print('INSTRUCCTIONS:')
print('Do yoy know the translation of the word? Choose any answers:')
print(' [yes] or [y] means you know the translation')
print(" [no]  or [n] means you don't know the translation")
print(' [fin] or [f] terminate the game')
print("=====================================================")


# Variables para el juego
aciertos    = 0
fails       = 0

# Numero de palabras a practicar
n_of_words_to_guess = int(20)


# Cuerpo del juego
game_inicio = int(0)
while game_inicio < n_of_words_to_guess:
    ran_word = random.choice(range(1, indice))
    print("-----------------------------------------------------")
    print('Do you know the meaning of |--->', english_word[ran_word].upper(), '<---| in Spanish')
    answer = str(input("Your answer: "))
    print("-----------------------------------------------------")

    if answer == 'y' or answer == 'yes':
        aciertos += 1
        print('Great job! It means: ', spanish_word[ran_word].title())
    
    elif answer == 'n' or answer == 'no':
        fails += 1
        #print("*****************************************************")
        print('Time to learn:', english_word[ran_word], ' = ', spanish_word[ran_word])
        print("*****************************************************")
        print("try with the next word...")
    
    elif answer == 'f' or answer == 'fin':
        game_inicio = indice + 1
    
    else:
        print("Skipping the word. It count as a failure")
        fails += 1
        
    
    # To advance in the game
    game_inicio += 1
    


# Resultado del juego
print("=====================================================")
print("| El resultado de la partida es:")
print('| Intentos: ' + str(aciertos + fails))
print('| Aciertos: ' + str(aciertos))
print("=======================")
print('| EFECTIVIDAD: {:.2f}/10'.format(aciertos/(aciertos + fails)*10))
print("=======================")



# Cerrar el programa con C
print("Press C key to end the program.")
value = str(input())
comprobador = 1
while comprobador > 0:
    if value == 'c' or value == 'C':
        comprobador = 0
    else:
        print("That letter is not C! Try again ...")
        value = str(input())

