import math

# -> Directions
# Dado um inteiro, retorne um inteiro na ordem reversa
# dos números que formam o inteiro original

# -> Exemplos 
# reverseInt(15) == 51


def reverse_int(integer):
  # -> Solução inicial
  # Converte o número para string `str()`
  # Da um replace no sinal de negativo para uma string vazia `.replace("-", "")`
  # Converte a string em uma lista `list()` e a reverte `reversed()`
  # Depois junta todos os index da lista em uma nova string `"".join()` e o converte em inteiro `int()`
  # No final copiamos o sinal do inteiro original para o novo inteiro utilizando a lib `math` com `math.copysign()`
  
  # reversed_number = int("".join(list(reversed(str(integer).replace("-", "")))))
  # return math.copysign(reversed_number, integer)
  
  # ---------------------------------------------------------------------------------------------------------------------

  # -> Solução mais limpa;
  
  # Verifica se o número original é negativo, atribuindo 1 ou -1 a variável sign
  # para realizar multiplicação com o inteiro inverso;
  # Converte o inteiro para o seu valor absoluto removendo o sinal;
  # o [::-1] inverte uma string sem a necessidade de converter em uma list;

  sign = -1 if integer < 0 else 1
  integer = abs(integer)
  reversed_number = int(str(integer)[::-1]) 
  return sign * reversed_number