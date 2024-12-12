# Dada uma string, crie uma função que retorne uma nova string 
# com a ordem reversa de caracteres

def reverse_String(string):
  # A função join junta todos os caracteres do array utilizando "" como junção
  # a função list cria um novo array a partir da reversão do array string.
  return "".join(list(reversed(string)))