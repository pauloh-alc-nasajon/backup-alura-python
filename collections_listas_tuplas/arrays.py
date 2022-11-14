# Array evitaremos usar (usado quando queremos eficiencia), muito mais comum trabalhar com o numpy:
import array as arr
import numpy as np

print(arr.array('d', [1, 3.5])) # arr.array(tipo, elementos)

numeros = np.array([1, 3.5])
print(numeros)
numeros = numeros + 3
print(numeros)

