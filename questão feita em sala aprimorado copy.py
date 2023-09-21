# Crie um algoritmo que simule o funcionamento de um caixa de supermercado. O caixa 
#fica aberto até o fim do expediente e pode processar a compra de vários clientes. 
#Cada cliente pode comprar vários itens (o operador fornece preço e quantidade de cada 
#item). Ao ler cada item deve ser exibida uma mensagem para o operador do caixa 
#perguntando se há mais itens a serem processados. Ao final, exiba quanto a compra custou 
#ao cliente. E então solicite do operador do caixa a informação se deseja fechar o caixa. 
#Quando o caixa for fechado, exiba quanto de dinheiro aquele caixa apurou no dia.
#comandos de entrada para o while do caixa
def repetir(repetição):
  if repetição!="S" and repetição !='N':
    repetição_de_caractere=True
  else:
    repetição_de_caractere=False
  return repetição_de_caractere
apurado=0
fechar_caixa=input("deseja fechar o caixa? S/N: ")
M_fechar=fechar_caixa.upper()
Repetição=repetir(M_fechar)
#sistema de repetição de caractere
while Repetição==True:
  fechar_caixa=input("ERROR, digite corretamente! Deseja fechar o caixa? S/N: ")
  M_fechar=fechar_caixa.upper()
  Repetição=repetir(M_fechar)
#While do caixa
while M_fechar !="S":
  print('''
  ===========================================
  ==============PRÓXIMO CLIENTE==============
  ===========================================
  ''')
  compra=0
  quant=float(input('Digite a quantidade do produto: '))
  preço=float(input('Digite o preço do produto: '))
  total=quant*preço
  compra=compra+total
  itens=input('Há mais produtos? S/N: ')
  i=itens.upper()
#sistema de repetição de caractere
  Repetição=repetir(i)
  while Repetição==True:
    itens=input('ERROR! DIGITE CORRETAMENTE. Há mais produtos? S/N: ')
    i=itens.upper()
    Repetição=repetir(i)
#while de mais de um produto!
  while i !="N":
    quant=float(input('Digite a quantidade do produto: '))
    preço=float(input('Digite o preço do produto: '))
    total=quant*preço
    compra=compra+total
    itens=input('Há mais produtos? S/N: ')
    i=itens.upper()
#sistema de repetição de caractere
    Repetição=repetir(i)
    while Repetição==True:
      itens=input('ERROR! DIGITE CORRETAMENTE. Há mais produtos? S/N: ')
      i=itens.upper()
      Repetição=repetir(i)
  apurado=apurado+compra
  print()
  print("Valor da compra: R$ %0.2f"%compra)
#codigo de troco
  dinheiro=float(input('Dinheiro do cliente: R$ '))
  if dinheiro>compra:
    troco=dinheiro-compra
    print('Haverá troco de R$ %0.2f'%troco)
    print()
  elif dinheiro<compra:
    troco=dinheiro-compra
    print('Está faltando R$ %0.2f'%(troco*-1))
    print()
  else:
    print('Não haverá troco!')
    print()
#resto do codigo do caixa
  fechar_caixa=input('Deseja fechar o caixa? S/N: ')
  M_fechar=fechar_caixa.upper()
  Repetição=repetir(M_fechar)
#sistema de repetição de caractere
  while Repetição==True:
    fechar_caixa=input("ERROR, digite corretamente! Deseja fechar o caixa? S/N: ")
    M_fechar=fechar_caixa.upper()
    Repetição=repetir(M_fechar)
print("Apurado do dia: %0.2f"%apurado)