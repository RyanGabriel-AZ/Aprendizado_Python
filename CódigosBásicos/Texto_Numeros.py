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

espaco= "               aqui                   "
hastag= "####toma##"
print(lista.upper()) #deixa tudo em caixa alta
print(lista.lower()) #deixa tudo em caixa  baixa
print(espaco.strip()) #remove espaço do inicio e do fim da string. 
print(hastag.strip("#")) # vai remover as # do inicio e fim do texto. ou seja, podemos ficar com o meio

#Aqui vamos agora manipular as strings, como se fossemos tratar dados
texto= "pesquisa"
subtexto= "qui"
print( texto.find(subtexto)) # ele vai procurar o subtexto do texto, e retornar a posição em que inicia
print( subtexto in texto) #verifica se o subtexto está em texto
print( texto.replace("quisa", "ca" )) #  replace( " parte antiga", "parte nova"), ele substitui o antigo pelo novo
# Podemos usar para limpar dados como datas também, etc

print( len(texto)) # retorna o tamnho do texto
print( texto.count(subtexto)) #mostra quantas vezes o termo apareceu na string
print( texto.startswith(subtexto))# ele verifica se o texto começa com o termo, pode colocar mais de um subtexto, retorna true ou false
print(texto.endswith(subtexto))# ele verifica se o texto termina com o termo, pode colocar mais de um subtexto, retorna true ou false
# eles são usados por exemplo para verificar se um arquivo termina com termo especifico, emails, hotmais, .csv, .pdf, etc

# agora essencial para verificar dados, separar, juntar, etc
texto= "Hoje eu vivo livre"
termos= texto.split() # podemos separar termos com o split, e isso gera um array com os termos. eu deixei em vazio, porque
#queria separar espaços, mas podemos colocar ou tros termos, como virgulas, letras, etc
print(termos) # vai printar a lista ['Hoje', 'eu', 'vivo', 'livre']
texto= ".".join(termos) # o Join faz o contrário do split, ele vai juntar os termos do array. mas entre os termos será colocado o que 
#foi colocado no " "
print(texto) # Hoje.eu.vivo.livre

texto = "6"
tamanho = 4
codigo= texto.zfill( tamanho) # 0006
print(codigo)
#basicamente o zfill ele preenche com 0 a esquerda  do texto , até completar o tamanho. pode até ter letras

#validando dados em strings. Vamos usar a função isTIPO(), isso vai retornar F ou V, se atender as condições, tem várias
#vou colocar algumas
numero= "123"
numero_texto= "123abc"
numero_espaco= "1 2"
texto= "abc"
print(numero.isdigit()) # ve se tem só digitos
print(numero_espaco.isdigit()) # falso
print(texto.isalpha()) # ve se so tem letra
print(numero_texto.isalpha()) # falso
print(numero_texto.isalnum()) # Ve se tem letras e numeros, sem espaços
print(numero_espaco.isalnum()) #falso, tem espaço

idade = 10
nome= "joão"
print(f" meu nome é {nome} e minha idade é {idade}")# isso é uma formatação de string. esse f lá no começo

#podemos transformar tipos
numero= 10
texto= str(numero) # vai transformar o numero/float em texto
flutuante = float(texto) # transformar o texto/numero em float, mas se o texto for em letras, dá erro 
numero= int(flutuante) # tranforma o texto/flutuante em numero, mas se o texto for em letras, dá erro , e também ele vai cortar casas decimais



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

