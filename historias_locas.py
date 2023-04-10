# Concatenar cadenas de caracteres
# Supongamos que queremos crear una cadena que diga:
# Estoy aprendiendo el lenguaje de  _____________.

# # Vamos a crear una variable
# language = "Python"

# # Mostrar un mensaje se usa print
# # Con las comillas indicamos que es una cadena de caracteres
# print("Estoy aprendiendo el lenguaje de " + language) 
# # Esas llaves nos indican que y va reemplazar un valor en especifico, y como se puede especificar el valor, con el metodo format()
# # format es un metodo de cadena de caracteres que nos va permitir reemplazar el valor de la variable en los corchetes
# print("Estoy aprendiendo el lenguaje de {}".format(language))
# # Aca se usa lo que se llama f string
# print(f"Estoy aprendiendo el lenguaje de {language}")#f-string


# Mad Libs (Historias Locas)
# Primero necesitamos un parrafo donde podamos sustituir o reemplazar las palabras que vamos a pedir del usuario que ingrese
# Entonces vamos a guardar el parrafo en una variable
# usamos una f-string
# Adentro de los corchetes se pondra un adjetivo 

# DEFINIR VARIABLES
# Se obtendran del usuario
# input() nos permite pedirle al usuario un valor y obtener ese valor
adj=input("Adjetivo: ")
verbo1=input("Verbo: ")
verbo2=input("Verbo: ")
sustantivo_plural=input("Sustantivo (Plural): ")


# PLANTILLA
madlib = f"¡Programar es tan {adj}! Siempre me emociona porque me encanta {verbo1} problemas. ¡Aprende a {verbo2} viendo tutoriales y alcanza tus {sustantivo_plural}!"

# Mostrar la cadena
print(madlib)

    