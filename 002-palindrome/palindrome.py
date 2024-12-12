# -> Direction
# Dada uma string, retorne true se ela for um palíndromo
# o falso se não for. Um palíndromo é uma string que forma
# a mesma palavra se ela for invertida, inclua espaços e acentos
# para determinar se uma string é um palíndromo.

# -> Exemplos
# palindromo("abba") == true
# palindromo("abcdefg") == false

def palindrome(string):
  # Remove espaços vazios e deixa a string em lower case
  # assim normalizando a entrada e realizando comparações corretas
  clear_string = string.replace(" ", "").lower()
  reversed_String = "".join(list(reversed(clear_string)))
  return clear_string == reversed_String

print(palindrome("nurses run"))