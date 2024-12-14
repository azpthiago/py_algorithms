# -> Directions
# Dado um array e o tamanho de um chunk, divida o array em subarrays
# onde cada subarray é do tamanho de chunk. Caso sobre um elemento fora do range
# ele deve ser devolvido mesmo que esteja sozinho.
# -> Exemplos
# chunk([1, 2, 3, 4], 2) --> [ [ 1, 2 ], [ 3, 4 ] ]
# chunk([1, 2, 3, 4, 5], 2) --> [ [ 1, 2], [ 3, 4], [5] ]
# chunk([1, 2, 3, 4, 5, 6, 7, 8], 3) --> [ [ 1, 2, 3], [ 4, 5, 6], [ 7, 8 ] ]

def chunk(array, chunk_size):
  
  if array == []:
    return []
  
  chunk_arrays = []

  while len(array) > chunk_size:
    # Utiliza operador [:size] para dar split no array até a dada posição e adicionar os valores a um pedaço
    piece = array[:chunk_size]
    # Adiciona o pedaço removido ao array que será retornado
    chunk_arrays.append(piece)
    # Pega o restante do array após a dada posição e atribui novamente ao array original
    array = array[chunk_size:]
  
  # Após sair do loop adiciona o restante dos valores ao array original ao array que que sera retornado
  chunk_arrays.append(array)

  return chunk_arrays