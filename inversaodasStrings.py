def inverte_string(s):
  lista_caracteres = list(s)
  inicio, fim = 0, len(lista_caracteres) - 1
  while inicio < fim:
      lista_caracteres[inicio], lista_caracteres[fim] = lista_caracteres[fim], lista_caracteres[inicio]
      inicio += 1
      fim -= 1
  string_invertida = ''.join(lista_caracteres)
  return string_invertida

strings_pesquisadas = []

while True:
  entrada_string = input("Informe uma string ou digite 'sair' para encerrar: ")

  if entrada_string.lower() == 'sair':
      break

  resultado = inverte_string(entrada_string)
  strings_pesquisadas.append((entrada_string, resultado))

  print(f"String original: {entrada_string}")
  print(f"String invertida: {resultado}\n")

print("Lista de strings pesquisadas:")
for original, invertida in strings_pesquisadas:
  print(f"{original} -> {invertida}")
