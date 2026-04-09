#Vamos começar com um comentário, ele é super útil para explicar o
# que o código faz, ou para deixar uma mensagem para quem for ler o código depois de um tempo. 

texto = "Olá, mundo!"  #isso é um texto por causa das aspas duplas
print( "podemos imprimir coisas aqui")
print( texto)# inclusive outras variáveis

texto = "onda" # aqui o texto está recebendo uma nova palavra  
print(texto)
#Podemos também concatena palavras usando +, e variáveis
print ('conca' + 'tenação')
#Agora vamos fazer uma brincadeira 
print('ba'+ 2*'na') #o resultado é banana, isso eu não sabia que o python fazia, é bem legal

#Toda palavra também é um array, a gente vai se aprofundar em outro módulo
lista= 'antena'
print( lista[0]) # ele vai printar 'a', que é a posição 0 da lista

# Temos alguns operadores que podemos usar em print
valor= 2*3
print(f" matematica :", valor ) #Esse f, permite usar texto e variáveis
print(" meu nome \n quebrou página \t dei tab \\ isso é uma barra \' isso é uma aspa simples, \" isso é uma aspa dupla") 
print(" Aqui temos abc agora temos abc\b, eu acabei de dar um backspace")
print("ABCrepetiu\rDEF")# ele volta pro inicio da frase e substitui ABC por DEF

