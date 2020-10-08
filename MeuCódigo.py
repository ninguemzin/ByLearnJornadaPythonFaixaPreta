#!/usr/bin/env python
# coding: utf-8

# # Condicionais
# 
# Principal forma de atribuir uma lógica ao seu código.  
# 
# Basicamente é uma tomada de decisão caso a condição seja verdadeira.
# 
# Ex:
# 
# - Se o dia estiver quente:
#     - Vou tomar um sorvete
#     - Vou para a praia
# 
# - Do contrário (se não):
#     - Comer um chocolate
#     - Maratonar Netflix

# In[26]:


temperatura = 'quente'

print(temperatura)


# In[27]:


if temperatura == 'quente':
    print('Vou tomar um sorvete de Flocos')
    print('Vou para a praia (mentira, aqui não tem praia)')
else:
    print('Vou comer um chococlate')
    print('Vamos assistir Cobra Kai')


# In[28]:


horario = 'tarde'

if horario == 'manhã':
    print('O sol está quente')
elif horario == 'tarde':
    print('O por do sol está chegando')
else:
    print('A lua está linda')
    print('ESTÁ NA HORA DA JORNADA PYTHON FAIXA PRETA')


# In[29]:


idade = 17

if idade >= 18:
    print('Você já pode beber, mas com moderação')
else:
    print('Você não pode beber')


# In[30]:


temperatura = 37 

if temperatura <= 30:
    print('aceitável')
else:
    print('Socorro está muito quente')


# In[31]:


altura = 1.75 

if altura > 1.80:
    print('o Emerson é alto')
else:
    print('O Emerson é baixinho')


# In[32]:


quente = True
gosta_praia = False

if quente == True:
    print('Está quente')


# - Geladeira:
#    - Frutas:
#        - Maçã
#        - Pera
#        - Uva

# In[33]:


quente = False
gosta_praia = False
gosta_chocolate_quente = True

if quente == True:
    print('Está quente')
    if gosta_praia == True:
        print ('Vá para a praia')
    else:
        print('Não vá a praia')
else:
    print('Está frio')
    if gosta_chocolate_quente == True:
        print('Tome um chocolate quente')
    else:
        print('Não tome chocolate quente')


# In[63]:


dia = input (' Qual é o dia atual?  ')

if dia == 'sabado':
    print('É fim de semna :D')
elif dia == 'domingo':
    print('É fim de semana :D')
else:
    print('Não é fim de semana :(')


# In[64]:


# 1, 3, 6, 10 => Válido
# qualquer outro => Inválido 

numero = 11

if numero == 1:
    print('é valido')
elif numero == 3:
    print('é valida')
elif numero == 6:
    print('é valido')
elif numero == 10:
    print('é valido')
else:
    print('é inválido')


# # Operadores Lógicos 
# 
# #### Servem para fazer uma condição composta 
# 
# #### E => Ambas precisam ser verdade  
# #### OU => Pelo Menos UMA precisa ser verdade  
# 
# #### Ex:
# ####    - Se for manhã E estiver sol
# ####    - Se for sábado OU domingo
# ####    E => AND
# ####    OU => OR

# In[36]:


dia = input ('Qual é o dia atual? ')

if dia == 'sabado' or dia == 'domingo':
    print('É fim de semna :D')
else:
    print('Não é fim de semana :(')


# In[37]:


# 1, 3, 6, 10 => Válido
# qualquer outro => Inválido 

numero = 11

if numero == 1:
    print('é valido')
elif numero == 3:
    print('é valida')
elif numero == 6:
    print('é valido')
elif numero == 10:
    print('é valido')
else:
    print('é inválido')
    


# In[55]:


numero = 6
if numero == 1 or numero == 3 or numero == 6 or numero == 10:
    print('É valido')
else:
    print('É invalido')


# In[54]:


numero = int(input ('Numero '))
if numero == 1 or numero == 3 or numero == 6 or numero == 10:
    print('É valido')
else:
    print('É invalido')


# In[52]:


horario = 'manha'
sol = True

if horario == 'manha' and sol == True:
    print('Está uma manhã ensolarada')


# In[53]:


meu_nome = 'Emerson'

nome = input('Digite seu nome: ')

meu_sobrenome = 'Marques'
sobrenome = input('Digite seu sobrenome: ')

apelido = 'Ninguém'

if (nome == meu_nome and sobrenome == meu_sobrenome) or nome == apelido:
    print('Você é o Emerson Marques')
else:
    print('Você não é o Emerson Marques')


# In[82]:


numero_sorte = 10

numero = int(input('Escolha um numero: '))

if numero != 10:
    print('errou o numero')


# # Laços de Repetição 
# 
# #### É uma excelente forma de evitar repetição de código.
# 
# #### Ele vai *executar n vezes* uma operaçã.
# 
# #### *n* => quantidade de vezes definida.

# In[41]:


# De 1 até 10 vamos printar todos os numeros
print(1)
print(2)
print(3)
print(4)
print(5)
print(6)
print(7)
print(8)
print(9)
# Na programação o Minimo (1) é INCLUSIVO => Ele existe
# Já é maximo (10) é EXCLUSIVO => Ele não existe


# In[42]:


# Até 11 vamos printar todos os numeros
print(0)
print(1)
print(2)
print(3)
print(4)
print(5)
print(6)
print(7)
print(8)
print(9)
print(10)
# Na programação o Minimo (1) é INCLUSIVO => Ele existe
# Já é maximo (10) é EXCLUSIVO => Ele não existe


# In[43]:


for numero in range (1,10):
    print(numero)


# In[44]:


for numero in range (1,11):
    print(numero)


# #### *for* => Nossa palavra-chave para Repetição.  
# #### *Varíavel* => O dado que estamos trabalhando no momento atual.  
# #### *in* => Nossa palavra-chave para "onde vamos repetir?"
# #### intervalo/sequencia => O que vamos repetir 

# In[51]:


for numero in range(5):
    print(numero)
    
#    for         numero     in       range(5)
# para cada      numero     no      intervalo até 5


# In[48]:


for numero in range(1,11):
    print('O numero atual é:', numero)
    if numero == 5:
        print('É o numero 5')
    if numero == 2:
        print('É o numero 2')


# In[49]:


texto = 'Não trave o zap dos amiguinhos'

for vez in range(1000):
    print(vez, texto)


# In[65]:


nomes = ['Emerson', 'Camilly', 'Alexandre', 'Luciana']


# In[67]:


for nome in nomes:
    print('O nome atual é', nome)
    if nome== 'Emerson':
        print('Ou Ninguém')


# In[73]:


# len => Tamanho em ingles (abreviação)
    # 1 2 3 4 
nomes = ['Emerson', 'Camilly', 'Alexandre', 'Luciana']
len(nomes)


# In[76]:


# len => Tamanho em ingles (abreviação)
        # 1  2  3 
nomes = [6, 7, 4.6]
len(nomes)


# In[74]:


notas = [6, 7.5, 9, 10, 3, 5]

soma = 0
for nota in notas:
    soma = soma + nota 

print('A soma é', soma)

media = soma / len(notas)

print('A média é', media)


# In[83]:


lista1 = ['A', 'B', 'C']
lista2 = [1, 2, 3, 4, 5]

tam_lista1 = len(lista1)
tam_lista2 = len(lista2)
print(tam_lista1)
print(tam_lista2)


# # Função 
# #### Toda função é uma rotina.  
# #### Eu defino (def) uma rotinae a executo quantas vezes quiser.  
# #### É uma exelente forma de deixar nosso código dinâmicoe sem repetição. 

# In[85]:


# Definindo a função
def nome_funcao():
    # Código da função
    print('Código Da Função')
    
# Chamando a função
nome_funcao()


# In[88]:


def mostrar_nome():
    print('Emerson Marques')
    print('Ninguém')
    
mostrar_nome()
mostrar_nome()


# # Parâmetro/Argumento da função
# #### É uma maneira de enviar dados para a função 

# In[92]:


def mostrar_nome(nome_atual):
    print(nome_atual)
mostrar_nome('Emerson')
mostrar_nome('Camilly')
mostrar_nome('Alexandre')
mostrar_nome('Luciana')


# In[102]:


def calcular_media(nota1, nota2):
    soma = nota1 + nota2 
    media = soma / 2
    print(media)

primeira_nota = float(input('Sua primeira nota: '))    
segunda_nota = float(input('Sua segunda nota: '))                              
calcular_media(primeira_nota, segunda_nota)


# # Return
# #### Quando queremos retornar um valor da função, ou seja, a função devolce um valor cálculado, nós usamos o Return.

# In[108]:


def calcular_media(nota1, nota2):
    soma = nota1 + nota2
    media1 = soma / 2
    
calcular_media(10,8)

#DEU ERRO POIS NÃO USAMOS O RETURN
print(media1)


# In[105]:


def calcular_media(nota1, nota2):
    soma = nota1 + nota2
    media = soma / 2
    return media

media_calculada = calcular_media(10,8)

print(media_calculada)


# In[127]:


# IMC => PESO (KG) / ALTURA (M)² 

def numero_quadrado(numero):
    quadrado = numero * numero 
    return quadrado

def calcular_imc(peso, altura):
    altura_quadrada = numero_quadrado(altura)
    meu_imc = peso / altura_quadrada
    
    return meu_imc

def classificar_imc(meu_imc):
    if imc <18.5:
        print('Magreza')
    elif imc >= 18.5 and imc < 25:
        print('Normal')
    elif imc >= 25 and imc < 30:
        print('Sobrepeso')
    elif imc >= 30 and imc < 40:
        print('Obesidade')
    else:
        print('Obesidade Grave')

imc = calcular_imc(66, 1.75)

print('Seu IMC é:',imc)

print('Sua classificação é:')
classificar_imc(imc)

# Tabela IMC:
# <18.5 e 25 => Magreza
# Entre 18.5 e 25 => Normal
# Entre 25 e 30 => Sobrepeso
# Entre 30 e 40 => Obesidade
# Acima de 40 => Obesidade Grave


# In[ ]:




