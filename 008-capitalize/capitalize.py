# -> Directions
# Escreva uma função que aceite uma string, a função deve
# capitalizar a primeira letra de cada palavra na string e 
# retornar a string capitalizada
# -> Exemplos
# capitalize('a short sentence') --> 'A Short Sentence' 
# capitalize('a lazy fox') --> 'A Lazy Fox' 
# capitalize('look, its is working') --> 'Look, It Is Working'

def capitalize(string):
  # Define uma array de palavras para utilizarmos no FOR
  words = []

  if string == '': 
    return '' 
  else:
    for word in string.split(" "):
      # Capitaliza a posição 0 da palavra e concatena com todo o resto a partir da posição 1
      capitalize_word = word[0].upper() + word[1::]
      # Adiciona a palavra no array de palavras
      words.append(capitalize_word)

  # Retorna a sentença completa
  return " ".join(words)

# Solução alternativas:
# string.title() --> Função do python O(n) que devolve a string capitalizada, além de lidar com erros de múltiplos espaços vazios, mas apresenta problemas pois afeta letras após '