# -*- coding: utf-8 -*-
"""
@author: itost
"""

datos=[0.43,0.28,0.33,0.27,0.12,0.31,0.42,0.01,0.32,0.45,0.98,0.79,0.99,0.55,0.67,0.74,0.16,0.2,0.12,0.58];
valores=[]
long=len(datos)

for i in range(1,long):
    if datos[i]<=datos[i-1]:
        valores.append(0)
    elif datos[i]>datos[i-1]:
        valores.append(1 )
print(valores)#muestra  las corridas
long2=(len(valores))
contador=0;
for i in range(0,long2-1):
    #print(contador)
    if i==long2-3:
        if valores[i+1] != valores[i+2]:
            contador+=1
    if valores[i] != valores[i+1]:
        contador+=1
        
print(contador)        
    
