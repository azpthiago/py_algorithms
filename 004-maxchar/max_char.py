# -> Directions
# Dada uma string, retorne o caractere mais utilizado na string
# -> Exemplos
# max_char("abcccccccd") == "c"
# max_char("apple 1231111") == "1"

def max_char(string):
  # Valida se a string não está vazia
  if not string:
    return ""
  
  # Cria um dicionário para iterarmos a string e guardarmos a quantidade
  string_map = {}

  # Iteramos sobre a string original
  for char in string:
    # Utilizamos um if para buscarmos se aquela chave (caractere) existe no dicionario
    if char in string_map:
      # Caso exista adicionamos + 1 ao valor daquela chave
      string_map[char] += 1
    else:
      # Caso não exista criamos a chave e adicionamos 1
      string_map[char] = 1

  # Retorna o maior valor utilizando o max com 2 argumentos
  # O primeiro sendo a lista/dicionarios que queremos achar o maior valor
  # O segundo sendo buscamos a chave e retornamos ela ja que é a chave que importa por ser o caractere que buscamos
  return max(string_map, key=string_map.get)