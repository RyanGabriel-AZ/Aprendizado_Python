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


#ok agora vamos usar o numeros
# NUmeros podem ser atribuidos a variaveis, podem ser pontos flutuantes, ter expressões, etc

# temos operadores: + soma, - subtração, 
# * multiplicação, ** potencia, / divisão, // divisão inteira, % resto
# Podemos colocar eles em listas também
x = 3.1415926535
print(round(x, 2)) # aqui por exemplo uma aritmetrica de ponto flutuante, 
#A função round é muito importante, pois ela vai arredondar casas  pós virgula.
# Ele recebe X, e nesse caso, só vai mostrar 2 casas pós a virgula
#Podemos também converter um numero em string
y = str(x) #formatei para string
print(y)

dois = 2
Um = 1
resultado = dois + Um #expressão com variaveis
print(resultado)

#Ok vamos agora para listas
teste = "012345678"
print( teste[0]) # o colchetes retorna a posição
print(teste[4: 7])
print(teste[4: ])
print(teste[: 4])
#vamos entender assim para ficar
#melhor, teste[ A partir daqui será incluido: A partir daqui será excluido]
#Isso de forma leiga, claro. Pois sabemos que isso é a cauda: cabeça da lista.

