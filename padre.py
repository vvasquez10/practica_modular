local_val = "unicornios mágicos"
def square(x):
    return x * x
class Usuario:
    def __init__(self, name):
        self.name = name
    def di_hola(self):
        return "hola"


# en el mismo archivo, agrega lo siguiente debajo de la clase Usuario
print(square(5))
user = Usuario("Anna")
print(user.name)
print(user.di_hola())

print(__name__)

if __name__ == "__main__":
    print("el archivo se está ejecutando directamente")
else:
    print("El archivo se está ejecutando porque es importado por otro archivo. El archivo se llama:", __name__)
  
"""
¿Cómo es esto útil? Podemos usar esta condicional para evitar que se ejecuten bloques de código
a menos que el archivo se esté ejecutando directamente.
"""