# -> Directions
# Cria uma função que verifique se duas strings são anagramas uma da outra
# Uma string é anagrama da outra se as duas utilizarem os mesmos caracteres
# na mesma quantidade. 
# Considere apenas caracteres, não espaços ou pontuação;
# Considere letras maiúsculas o mesmo que minúsculas;
# -> Exemplos
# anagrams('rail safety', 'fairy tales') --> True
# anagrams('RAIL, SAFETY', 'fairy tales') --> True
# anagrams('Hi, There', 'Bye There') --> True

import re

# Este código pode ser solucionado de diversas outras maneiras
# A remoção de pontuação pode ser feita utilizando um filter + str.isalnum
# Ex: clear_string_1 = ''.join(filter(str.isalnum, string_1.lower()))
# E a contagem dos caracteres pode ser feita utilizando um Counter
# Ex: Counter(clear_string_1) == Counter(clear_string_2)

# Solução com Counter

# from collections import Counter
#def anagrams(string_1, string_2):
#    Remove espaços, pontuações e transforma em minúsculas
#    clear_string_1 = ''.join(filter(str.isalnum, string_1.lower()))
#    clear_string_2 = ''.join(filter(str.isalnum, string_2.lower()))   
#    Conta os caracteres de cada string e compara
#    return Counter(clear_string_1) == Counter(clear_string_2)

def anagrams(string_1, string_2):
  # Utiliza regex para tirar pontuação, .lower() para deixar minuscula e remove espaços da string
  clear_string_1 = re.sub(r'[^\w\s]','',string_1.lower()).replace(' ', '')
  clear_string_2 = re.sub(r'[^\w\s]','',string_2.lower()).replace(' ', '')

  # Cria maps para verificar a quantidade de caracteres em cada string
  string_1_map ={}
  string_2_map ={}

  # Executa o for para mapear as strings
  # Utilizando a mesma implementação do max_char
  for char in clear_string_1:
    if char in string_1_map:
      string_1_map[char] += 1
    else:
      string_1_map[char] = 1

  for char in clear_string_2:
    if char in string_2_map:
      string_2_map[char] += 1
    else:
      string_2_map[char] = 1

  # Valida os maps e retorna True ou False
  if string_1_map == string_2_map: 
    return True 
  else: 
    return False