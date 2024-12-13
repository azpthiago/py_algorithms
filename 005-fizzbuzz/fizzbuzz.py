# -> Directions
# Escreva um programa que de console log nos numeros de 1 a n.
# Para múltiplos de 3 print "fizz" ao invés do número e para
# múltiplos de 5 print "buzz". Para números que sejam múltiplos
# de 3 e 5 print "fizzbuzz"

# -> Exemplos
# fizzbuzz(5)
# 1
# 2
# fizz
# 4
# buzz

def fizzbuzz(n):
  fizzbuss_arr = []
  for i in range(1, n+1):
    if i % 3 == 0 and i % 5 == 0:
      fizzbuss_arr.append("fizzbuzz")
    elif i % 3 == 0:
      fizzbuss_arr.append("fizz")
    elif i % 5 == 0:
      fizzbuss_arr.append("buzz")
    else:
      fizzbuss_arr.append(str(i))
  return fizzbuss_arr