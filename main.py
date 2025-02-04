# Variáveis -> React = Estados(useState), JavaScript = var, let e const
#Variáveis no python = nome_da_variavel 

# Comentário

"""
    outro tipo de comentário
"""

nome = "Gabrielle" 
print(nome) 

idade = 22
print(nome)

"""
    nomeclatura de variáveis
    
    camelCase -> Uma forma de nomear as nossas variáveis
    
    snakeCase -> Uma forma de nomear variável usando underline _
"""
primeiroNome = "Gabrielle"

segundo_nome = "Oliveira"

print(primeiroNome + segundo_nome)
print(primeiroNome, segundo_nome)

# Variavel com letra maiúscula -> Constante
#pode ser mudada mas sendo toda maiuscula é pra identificar que é constante

TIPO_CARRO = "UNO"

TIPO_CARRO = "CHEVROLET"

#tipos de dados em python

#Inteiros (int) -> São todos os números positivos e negativos que não possuem vírgulas

temperatura = -273

idade_da_terra = 45000000000000000000000000000000000000

#Ponto Fluante ou decimais (float) -> São todos os números positivos e negativos que contém virgulas

pi = 3.14159

preco = 49.90

print(preco)

#Strings ou textos (str)
dados_textuais = "Arcane"

#Booleanos (bool) -> São os dados do tipo Verdadeiro ou falso

maior_de_dezoito = True
print(maior_de_dezoito)

aula_amanha = False

#Nulos (none) -> São dados do tipo Nulo, declaram que o valor daquela variável e do tipo Nulo

vazio = None

print(vazio)

#Type() -> Função padrão do python que exibe para a gente o tipo da variável colocada entre parenteses

print(type(aula_amanha))

# f strings (formatted strings) -> misturar 

tema_aula = "Python, passarela, Rato, Arcane"

print(f"O tema da aula hoje é {tema_aula}")