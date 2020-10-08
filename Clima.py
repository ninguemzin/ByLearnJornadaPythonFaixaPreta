#!/usr/bin/env python
# coding: utf-8

# In[1]:


horario = 'manhã'
clima = 'ensolarado'
temperatura = 'quente'

if horario == 'manhã' or horario == 'tarde':
    if clima == 'ensolarado' and temperatura == 'quente':
        print("Uma piscina cairia bem")
        
    if(clima == 'ensolarado' and clima == 'qnublado') and (temperatura == 'amena' or temperatura == 'frio'):
        print("Seria legal praticar algum esporte")
        
    if clima == 'chuvoso':
        print("Aproveite para treinar seu Python")
else:
    if clima == 'chuvoso':
        print("que tal um filme, série ou jogatina?")
    else:
        print("Um jantar fora parece interessante...")
        
    


# In[ ]:




