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

def anagrams(string_1, string_2):
  if string_1 == "" or string_1 == "":
    return True
  
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