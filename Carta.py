#!/usr/bin/env python
# coding: utf-8

# In[94]:


def validar_idade(idade):
    if idade < 18:
        print('\nDesculpe, você não tem idade para prosseguir,', nome)
        return False
    else:
        print('\nÓtimo! Podemos prosseguir,', nome)
        return True
    
def escolher_carta():
    print("Digite uma das opções abaixo:")
    print("1 - Carro\n2 - Moto\n3 - Carro e Moto")
        
    return int(input())
    
def calcular_preco(escolha):
    valor_carro = 1500
    valor_moto = 1000
    
    if escolha == 1:
        return valor_carro
    elif escolha == 2:
        return valor_moto
    else: 
        return valor_carro + valor_moto
def  desconto(valor):
     return valor - (valor * 0.10)
        
nome = input('Digite o seu nome:')
idade = int(input('Digite sua idade:'))
        
if validar_idade(idade):
    escolha = escolher_carta()
    
    print('\nPerfeito! Vou calcular o valor')
    valor = calcular_preco(escolha)        
    print('\n'+nome, 'o valor total é de', valor, 'reais')
    print('Mas vou ver com meu gerente se posso dar um desconto...')
    valor = desconto(valor)
            
    print('\nCom desconto eu consigo fazer por', valor, 'reais.')
            
    print('Te interessa?\n1 - Sim\n2 - Não')
    interesse = int(input())
    if interesse == 1:
        print('\nPerfeito! Começaremos amanhã!')
    else:
        print('\nTudo bem :(\nMe avise se mudar de ideia.')


# In[ ]:




