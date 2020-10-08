#!/usr/bin/env python
# coding: utf-8

# In[2]:


frutas = ['Maçã', 'Banana', 'Pera', 'Uva']
guloseimas = ['Bolacha', 'Batata', 'Fini', 'Chocolate']
comidas = ['Arroz', 'Feijão', 'Carne',]
bebidas = ['Refrigerante', 'Suco de Laranja', 'Água']

categorias = ['Frutas', 'Guloseimas', 'Comidas', 'Bebidas']
compras = ['frutas', 'guloseimas', 'comidas', 'bebidas']

for indice, categoria in enumerate(categorias):
    print('Você precisa comprar', len(compras[indice]), categoria+':')
    for compra in compras[indice]:
        print('-', compra)

