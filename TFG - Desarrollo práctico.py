#!/usr/bin/env python
# coding: utf-8

# # Título del TFG

# ## 1. Importación de librerías

# En este primer apartado se importan todas las librerías necesarias para el desarrollo del estudio.

# In[1]:


import os
from PIL import Image
import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import math
from copy import copy
from networkx.algorithms import community 
import itertools
from operator import itemgetter
from networkx import edge_betweenness_centrality as betweenness
from random import random
from scipy.stats import kendalltau
from pylab import *


# ## 2. Ingesta de datos

# Para poder desarrollar el estudio es necesario cargar los datos en el entorno de trabajo. La finalidad de esta sección es eso mismo, recoger toda la ingesta de datos para su posterior uso. Estos datos recogen la información relativa a la cotización de las 35 empresas del IBEX 35 desde el 22/04/2022 hasta el 21/10/2022.
# 
# Puesto que son 35 las empresas que cotizan en el Ibex 35, habrá 35 cargas, correspondientes cada una de ellas a cada empresa. Para ello, se lee un archivo.csv donde está toda la información de la cotización relativa a estas durante los últimos 6 meses.

# In[2]:


os.chdir(r'C:\Users\danir\OneDrive\Escritorio\TFG\Data')


# In[3]:


df_acciona = pd.read_csv("Acciona.csv",sep=";",header=0,encoding="unicode_escape")
df_acciona


# In[4]:


df_accionaEnergia = pd.read_csv("AccionaEnergia.csv",sep=";",header=0,encoding="unicode_escape")
df_accionaEnergia


# In[5]:


df_acerinox = pd.read_csv("Acerinox.csv",sep=";",header=0,encoding="unicode_escape")
df_acerinox


# In[6]:


df_acs = pd.read_csv("Acs.csv",sep=";",header=0,encoding="unicode_escape")
df_acs


# In[7]:


df_aena = pd.read_csv("Aena.csv",sep=";",header=0,encoding="unicode_escape")
df_aena


# In[8]:


df_amadeus = pd.read_csv("Amadeus.csv",sep=";",header=0,encoding="unicode_escape")
df_amadeus


# In[9]:


df_arcelormittal = pd.read_csv("Arcelormittal.csv",sep=";",header=0,encoding="unicode_escape")
df_arcelormittal


# In[10]:


df_santander = pd.read_csv("Santander.csv",sep=";",header=0,encoding="unicode_escape")
df_santander


# In[11]:


df_sabadell = pd.read_csv("Sabadell.csv",sep=";",header=0,encoding="unicode_escape")
df_sabadell


# In[12]:


df_bankinter = pd.read_csv("Bankinter.csv",sep=";",header=0,encoding="unicode_escape")
df_bankinter


# In[13]:


df_bbva = pd.read_csv("BBVA.csv",sep=";",header=0,encoding="unicode_escape")
df_bbva


# In[14]:


df_caixabank = pd.read_csv("Caixabank.csv",sep=";",header=0,encoding="unicode_escape")
df_caixabank


# In[15]:


df_cellnex = pd.read_csv("Cellnex.csv",sep=";",header=0,encoding="unicode_escape")
df_cellnex


# In[16]:


df_enagas = pd.read_csv("Enagas.csv",sep=";",header=0,encoding="unicode_escape")
df_enagas


# In[17]:


df_endesa = pd.read_csv("Endesa.csv",sep=";",header=0,encoding="unicode_escape")
df_endesa


# In[18]:


df_ferrovial = pd.read_csv("Ferrovial.csv",sep=";",header=0,encoding="unicode_escape")
df_ferrovial


# In[19]:


df_fluidra = pd.read_csv("Fluidra.csv",sep=";",header=0,encoding="unicode_escape")
df_fluidra


# In[20]:


df_grifols = pd.read_csv("Grifols.csv",sep=";",header=0,encoding="unicode_escape")
df_grifols


# In[21]:


df_IAG = pd.read_csv("IAG.csv",sep=";",header=0,encoding="unicode_escape")
df_IAG


# In[22]:


df_iberdrola = pd.read_csv("Iberdrola.csv",sep=";",header=0,encoding="unicode_escape")
df_iberdrola


# In[23]:


df_inditex = pd.read_csv("Inditex.csv",sep=";",header=0,encoding="unicode_escape")
df_inditex


# In[24]:


df_indra = pd.read_csv("Indra.csv",sep=";",header=0,encoding="unicode_escape")
df_indra


# In[25]:


df_colonial = pd.read_csv("Colonial.csv",sep=";",header=0,encoding="unicode_escape")
df_colonial


# In[26]:


df_mapfre = pd.read_csv("Mapfre.csv",sep=";",header=0,encoding="unicode_escape")
df_mapfre


# In[27]:


df_melia = pd.read_csv("Melia.csv",sep=";",header=0,encoding="unicode_escape")
df_melia


# In[28]:


df_merlin = pd.read_csv("Merlin.csv",sep=";",header=0,encoding="unicode_escape")
df_merlin


# In[29]:


df_naturgy = pd.read_csv("Naturgy.csv",sep=";",header=0,encoding="unicode_escape")
df_naturgy


# In[30]:


df_pharmaMar = pd.read_csv("PharmaMar.csv",sep=";",header=0,encoding="unicode_escape")
df_pharmaMar


# In[31]:


df_redElectrica = pd.read_csv("RedElectrica.csv",sep=";",header=0,encoding="unicode_escape")
df_redElectrica


# In[32]:


df_repsol = pd.read_csv("Repsol.csv",sep=";",header=0,encoding="unicode_escape")
df_repsol


# In[33]:


df_rovi = pd.read_csv("Rovi.csv",sep=";",header=0,encoding="unicode_escape")
df_rovi


# In[34]:


df_sacyr = pd.read_csv("Sacyr.csv",sep=";",header=0,encoding="unicode_escape")
df_sacyr


# In[35]:


df_siemens = pd.read_csv("Siemens.csv",sep=";",header=0,encoding="unicode_escape")
df_siemens


# In[36]:


df_solaria = pd.read_csv("Solaria.csv",sep=";",header=0,encoding="unicode_escape")
df_solaria


# In[37]:


df_telefonica = pd.read_csv("Telefonica.csv",sep=";",header=0,encoding="unicode_escape")
df_telefonica


# ## 3. Desarrollo del estudio: Perpectivas para estudiar la cotización de las acciones

# Una investigación en torno a los productos de inversión como las acciones es un campo amplio que puede enfocarse desde diferentes perspectivas y centrándose en variedad de características. Es por ello que se pretende establecer bien los criterios que rigen cada una de las tres variantes que se van a exponer en este estudio.
# 
# Aunque en vista general hay tres vertientes, dentro de ellas hay subvariantes cuyas ideas son comunes a todas estas vertientes debido a los resultados obtenidos en todas ellas. Estas perspectivas se explicarán en detalle para el primer caso de estudio, pero será extrapolable al resto.
# 
# Para establecer diferentes medidas asociadas a las acciones se recurre a trabajar con el <u>***precio de cierre diario***</u> de cada una de ellas en las diferentes sesiones. A continuación, se van a explicar los tres enfoques de forma breve y posteriormente se pasará a detallar y trabajar con cada uno de ellos:
# 
#    * Bajo una inversión inicial de 1000 € en cada una de las empresas, se trabaja con la evolución diaria del total de la            inversión al cierre de la sesión.
#    * Bajo una inversión inicial de 1000 € en cada una de las empresas, se trabaja con la diferencia diaria del total de la          evolución de la inversión al cierre de la sesión respecto de la sesión anterior.
#    * Estudio mediante el cálculo de la variación porcentual en el precio de cierre de la sesión de cada acción respecto de la        sesión anterior.
#    
# Las dos últimas perspectivas responden al concepto volatilidad.

# Previamente al trabajo con los diferentes enfoques, se crean variables que serán de utilidad para el desarrollo de los mismos.
# 
# En primer lugar, se almacena en una variable una lista con los nombres de todas las empresas que participan en el estudio. Esto va a resultar de utilidad para la creación de las matrices de adyacencia, los grafos y otros elementos posteriores del análisis.

# In[38]:


stocks = ['Acciona','Acciona Energía','Acerinox','Acs','Aena','Amadeus','Arcelormittal','Banco Santander',
          'Banco Sabadell','Bankinter','BBVA','Caixabank','Cellnex','Enagás','Endesa','Ferrovial','Fluidra',
          'Grifols','IAG','Iberdrola','Inditex','Indra','Inmobiliaria Colonial','Mapfre','Meliá Hotels',
          'Merlin Properties','Naturgy','Pharma Mar','Red Eléctrica','Repsol','Rovi','Sacyr','Siemens Gamesa',
          'Solaria','Telefónica']


# Además, se generan más variables que posteriormente se utilizarán, por ejemplo, en la definición de los dataFrame que serán las matrices de adyacencia de los grafos, y que serán empleadas en todas las perspectivas que se desarrollen.

# In[39]:


n_sesions = len(df_acciona)
rankings = range(0,n_sesions-1)
n_stocks = len(stocks)
classification = range(0,n_stocks)


# La primera perspectiva se detallará, pero las siguientes, puesto que llevarán una estructura prácticamente idéntica en las comprobaciones y en el desarrollo de las mismas, simplemente se comentarán aspectos relevantes de esos enfoques. Comentarios generales sobre el desarrollo se extrapolan del primer caso.

# In[40]:


#Cambio de directorio para que todas las imágenes se guarden juntas
os.chdir(r'C:\Users\danir\OneDrive\Escritorio\TFG\Imagenes')


# ### 3.1. Perspectiva 1: Bajo una inversión inicial de 1000 €, estudio de la evolución diaria del total de la inversión al cierre de la sesión

# Previamente al desarrollo de esta perspectiva hay que clarificar la idea en la cual se basa. El concepto es el siguiente:
# 
#    * Se hace una inversión inicial al cierre de la primera sesión de 1000 € en cada una de las empresas. Esto lleva a tener          tras esa primera sesión un número de acciones equivalentes de cada empresa. Este número de acciones inicial es constante        en el tiempo, en el sentido de que en ningún momento se modifica el número de acciones que se posee de cada empresa.
#    * Este número fijo de acciones de cada una de las empresas permite poder calcular a lo largo del resto de las sesiones de        las que se tiene registro el valor que tiene esa inversión inicial al cierre de cada una de las sesiones.
#    * Con estos valores para cada empresa y para cada sesión se construyen los rankings, se calculan los números de cruces y se      obtiene así la matriz de adyacencia para la posterior representación del grafo de competitividad.

# Explicado el enfoque, en primer lugar es necesario calcular el número de acciones que se tiene de cada empresa mediante una inversión inicial de 1000 € sobre el precio de cierre de esa primera sesión. Así, para cada empresa se calcula el número de acciones equivalentes a los 1000 €.

# In[41]:


n_stocks_acciona = 1000/df_acciona.iloc[0,1]
n_stocks_accionaEnergia = 1000/df_accionaEnergia.iloc[0,1]
n_stocks_acerinox = 1000/df_acerinox.iloc[0,1]
n_stocks_acs = 1000/df_acs.iloc[0,1]
n_stocks_aena = 1000/df_aena.iloc[0,1]
n_stocks_amadeus = 1000/df_amadeus.iloc[0,1]
n_stocks_arcelormittal = 1000/df_arcelormittal.iloc[0,1]
n_stocks_bankinter = 1000/df_bankinter.iloc[0,1]
n_stocks_bbva = 1000/df_bbva.iloc[0,1]
n_stocks_caixabank = 1000/df_caixabank.iloc[0,1]
n_stocks_cellnex = 1000/df_cellnex.iloc[0,1]
n_stocks_colonial = 1000/df_colonial.iloc[0,1]
n_stocks_enagas = 1000/df_enagas.iloc[0,1]
n_stocks_endesa = 1000/df_endesa.iloc[0,1]
n_stocks_ferrovial = 1000/df_ferrovial.iloc[0,1]
n_stocks_fluidra = 1000/df_fluidra.iloc[0,1]
n_stocks_grifols = 1000/df_grifols.iloc[0,1]
n_stocks_IAG = 1000/df_IAG.iloc[0,1]
n_stocks_iberdrola = 1000/df_iberdrola.iloc[0,1]
n_stocks_inditex = 1000/df_inditex.iloc[0,1]
n_stocks_indra = 1000/df_indra.iloc[0,1]
n_stocks_mapfre = 1000/df_mapfre.iloc[0,1]
n_stocks_melia = 1000/df_melia.iloc[0,1]
n_stocks_merlin = 1000/df_merlin.iloc[0,1]
n_stocks_naturgy = 1000/df_naturgy.iloc[0,1]
n_stocks_pharmaMar = 1000/df_pharmaMar.iloc[0,1]
n_stocks_redElectrica = 1000/df_redElectrica.iloc[0,1]
n_stocks_repsol = 1000/df_repsol.iloc[0,1]
n_stocks_rovi = 1000/df_rovi.iloc[0,1]
n_stocks_sabadell = 1000/df_sabadell.iloc[0,1]
n_stocks_sacyr = 1000/df_sacyr.iloc[0,1]
n_stocks_santander = 1000/df_santander.iloc[0,1]
n_stocks_siemens = 1000/df_siemens.iloc[0,1]
n_stocks_solaria = 1000/df_solaria.iloc[0,1]
n_stocks_telefonica = 1000/df_telefonica.iloc[0,1]


# Para visualizar el número de acciones y que se ha hecho correctamente el cálculo, se construye una tabla con el nombre de la empresa, el número de acciones obtenidas y el valor de esas acciones en el cierre de sesión de la primera sesión, el cual debe ser 1000 € para comprobar que el cálculo ha sido correcto.

# In[42]:


data_table_n_stocks = [['Acciona', n_stocks_acciona, n_stocks_acciona*df_acciona.iloc[0,1]],
                       ['Acciona Energía', n_stocks_accionaEnergia, n_stocks_accionaEnergia*df_accionaEnergia.iloc[0,1]],
                       ['Acerinox', n_stocks_acerinox, n_stocks_acerinox*df_acerinox.iloc[0,1]],
                       ['Acs', n_stocks_acs, n_stocks_acs*df_acs.iloc[0,1]],
                       ['Aena', n_stocks_aena, n_stocks_aena*df_aena.iloc[0,1]],
                       ['Amadeus', n_stocks_amadeus, n_stocks_amadeus*df_amadeus.iloc[0,1]],
                       ['Arcelormittal', n_stocks_arcelormittal, n_stocks_arcelormittal*df_arcelormittal.iloc[0,1]],
                       ['Banco Santander', n_stocks_santander, n_stocks_santander*df_santander.iloc[0,1]],
                       ['Banco Sabadell', n_stocks_sabadell, n_stocks_sabadell*df_sabadell.iloc[0,1]],
                       ['Bankinter', n_stocks_bankinter, n_stocks_bankinter*df_bankinter.iloc[0,1]],
                       ['BBVA', n_stocks_bbva, n_stocks_bbva*df_bbva.iloc[0,1]],
                       ['Caixabank', n_stocks_caixabank, n_stocks_caixabank*df_caixabank.iloc[0,1]],
                       ['Cellnex', n_stocks_cellnex, n_stocks_cellnex*df_cellnex.iloc[0,1]],
                       ['Enagás', n_stocks_enagas, n_stocks_enagas*df_enagas.iloc[0,1]],
                       ['Endesa', n_stocks_endesa, n_stocks_endesa*df_endesa.iloc[0,1]],
                       ['Ferrovial', n_stocks_ferrovial, n_stocks_ferrovial*df_ferrovial.iloc[0,1]],
                       ['Fluidra', n_stocks_fluidra, n_stocks_fluidra*df_fluidra.iloc[0,1]],
                       ['Grifols', n_stocks_grifols, n_stocks_grifols*df_grifols.iloc[0,1]],
                       ['IAG', n_stocks_IAG, n_stocks_IAG*df_IAG.iloc[0,1]],
                       ['Iberdrola', n_stocks_iberdrola, n_stocks_iberdrola*df_iberdrola.iloc[0,1]],
                       ['Inditex', n_stocks_inditex, n_stocks_inditex*df_inditex.iloc[0,1]],
                       ['Indra', n_stocks_indra, n_stocks_indra*df_indra.iloc[0,1]],
                       ['Inmobiliaria Colonial', n_stocks_colonial, n_stocks_colonial*df_colonial.iloc[0,1]],
                       ['Mapfre', n_stocks_mapfre, n_stocks_mapfre*df_mapfre.iloc[0,1]],
                       ['Meliá Hotels', n_stocks_melia, n_stocks_melia*df_melia.iloc[0,1]],
                       ['Merlin Properties', n_stocks_merlin, n_stocks_merlin*df_merlin.iloc[0,1]],
                       ['Naturgy', n_stocks_naturgy, n_stocks_naturgy*df_naturgy.iloc[0,1]],
                       ['Pharma Mar', n_stocks_pharmaMar, n_stocks_pharmaMar*df_pharmaMar.iloc[0,1]],
                       ['Red Eléctrica', n_stocks_redElectrica, n_stocks_redElectrica*df_redElectrica.iloc[0,1]],
                       ['Repsol', n_stocks_repsol, n_stocks_repsol*df_repsol.iloc[0,1]],
                       ['Rovi', n_stocks_rovi, n_stocks_rovi*df_rovi.iloc[0,1]],
                       ['Sacyr', n_stocks_sacyr, n_stocks_sacyr*df_sacyr.iloc[0,1]],
                       ['Siemens Gamesa', n_stocks_siemens, n_stocks_siemens*df_siemens.iloc[0,1]],
                       ['Solaria', n_stocks_solaria, n_stocks_solaria*df_solaria.iloc[0,1]],
                       ['Telefónica', n_stocks_telefonica, n_stocks_telefonica*df_telefonica.iloc[0,1]]]
df_table_n_stocks = pd.DataFrame(data_table_n_stocks,columns=['Nombre', 'Nº de acciones iniciales', 'Valor'])
df_table_n_stocks


# Una vez se tiene este número total de acciones de cada una de las empresas, se pueden construir los rankings multiplicando el número de acciones de dicha empresa por su precio de cierre en cada sesión. Ello origina la necesidad de ordenar esos valores para la construcción del ranking. Para ello se genera la siguiente función, ***ordenarRanking***, la cual es una implementación del algoritmo de ordenación: <u>**Selection sort**</u>. Esta función ordena los valores de forma decreciente, es decir, de mayor a menor.
#     
# Puesto que el planteamiento para el almacenamiento de los rankings son dos columnas donde la primera es el nombre de la empresa y la segunda es el valor a ordenar, el algoritmo realmente ordena la segunda columna y es consecuente cambiando también la posición de los nombres de la primera. 

# In[43]:


#Algoritmo para ordenar los rankings
def ordenarRanking(data):
    n = len(data)
    for i in range(n-1):
        minimo = i
        temp_val = data.iloc[i,1]
        temp_name = data.iloc[i,0]
        for j in range(i,n):
            if data.iloc[j,1] > temp_val:
                minimo = j
                temp_val = data.iloc[j,1]
                temp_name = data.iloc[j,0]
        data.iloc[minimo,1] = data.iloc[i,1]
        data.iloc[minimo,0] = data.iloc[i,0]
        data.iloc[i,1] = temp_val
        data.iloc[i,0] = temp_name
    return None


# Seguidamente, se hace la prueba del algoritmo *ordenarRanking*.
# En primer lugar, se muestra una tabla con la estructura que van a tener los rankings:
# 
#    * Primera columna: nombre de la empresa
#    * Segunda columna: valor empleado para la ordenación.

# In[44]:


#Prueba del algoritmo ordenarRanking
data_test_organize_ranking = [['A',-10.6],
                              ['B',4.6],
                              ['C',1.6],
                              ['D',0],
                              ['E',3.6],
                              ['F',5.67],
                              ['G',5.665],
                              ['H',-5.6],
                              ['I',3.6],
                              ['J',6],
                              ['K',-4.9764]]
df_test_organize_ranking = pd.DataFrame(data_test_organize_ranking,columns=['Nombre','Valor'])
df_test_organize_ranking


# Y se ejecuta la función *ordenarRanking* para la ordenación del ranking.

# In[45]:


ordenarRanking(df_test_organize_ranking)
df_test_organize_ranking


# Como se puede observar, los valores son ordenados y sus nombres asociados también, consecuentemente.

# Con el algoritmo para ordenar los rankings y la idea que sigue este enfoque, se calcula el primero, el segundo y el último de los rankings que se van a necesitar posteriormente, los cuales ocuparán las posiciones 0, 1 y 129, respectivamente, en la matriz de rankings que después se creará. Estos serán útiles para comprobar si una vez se escale el modelo, está bien automatizado.
# 
# La estrcutura es la comentada anteriormente, un dataFrame con dos columnas: nombre de la empresa y valor de la inversión en esa sesión. Hay que observar que el número de ranking va asociado a una sesión, es decir, por ejemplo, el ranking 1 utiliza para el cálculo de los valores la información de la sesión 2.
# 
# Se ejecuta la creación de un dataFrame para el primer ranking multiplicando el precio de cierre de cada acción en la sesión número 2 registrada por el número de acciones en las que se inviertieron 1000 € en la primera sesión. Además, dicho ranking se ordena.

# In[46]:


data_ranking_0_inv = [['Acciona',df_table_n_stocks.iloc[0,1]*df_acciona.iloc[1,1]],
                      ['Acciona Energía',df_table_n_stocks.iloc[1,1]*df_accionaEnergia.iloc[1,1]], 
                      ['Acerinox',df_table_n_stocks.iloc[2,1]*df_acerinox.iloc[1,1]], 
                      ['Acs',df_table_n_stocks.iloc[3,1]*df_acs.iloc[1,1]], 
                      ['Aena',df_table_n_stocks.iloc[4,1]*df_aena.iloc[1,1]], 
                      ['Amadeus',df_table_n_stocks.iloc[5,1]*df_amadeus.iloc[1,1]], 
                      ['Arcelormittal',df_table_n_stocks.iloc[6,1]*df_arcelormittal.iloc[1,1]], 
                      ['Banco Santander',df_table_n_stocks.iloc[7,1]*df_santander.iloc[1,1]], 
                      ['Banco Sabadell',df_table_n_stocks.iloc[8,1]*df_sabadell.iloc[1,1]], 
                      ['Bankinter',df_table_n_stocks.iloc[9,1]*df_bankinter.iloc[1,1]], 
                      ['BBVA',df_table_n_stocks.iloc[10,1]*df_bbva.iloc[1,1]], 
                      ['Caixabank',df_table_n_stocks.iloc[11,1]*df_caixabank.iloc[1,1]], 
                      ['Cellnex',df_table_n_stocks.iloc[12,1]*df_cellnex.iloc[1,1]], 
                      ['Enagás',df_table_n_stocks.iloc[13,1]*df_enagas.iloc[1,1]], 
                      ['Endesa',df_table_n_stocks.iloc[14,1]*df_endesa.iloc[1,1]], 
                      ['Ferrovial',df_table_n_stocks.iloc[15,1]*df_ferrovial.iloc[1,1]], 
                      ['Fluidra',df_table_n_stocks.iloc[16,1]*df_fluidra.iloc[1,1]], 
                      ['Grifols',df_table_n_stocks.iloc[17,1]*df_grifols.iloc[1,1]], 
                      ['IAG',df_table_n_stocks.iloc[18,1]*df_IAG.iloc[1,1]], 
                      ['Iberdrola',df_table_n_stocks.iloc[19,1]*df_iberdrola.iloc[1,1]], 
                      ['Inditex',df_table_n_stocks.iloc[20,1]*df_inditex.iloc[1,1]], 
                      ['Indra',df_table_n_stocks.iloc[21,1]*df_indra.iloc[1,1]], 
                      ['Inmobiliaria Colonial',df_table_n_stocks.iloc[22,1]*df_colonial.iloc[1,1]], 
                      ['Mapfre',df_table_n_stocks.iloc[23,1]*df_mapfre.iloc[1,1]], 
                      ['Meliá Hotels',df_table_n_stocks.iloc[24,1]*df_melia.iloc[1,1]], 
                      ['Merlin Properties',df_table_n_stocks.iloc[25,1]*df_merlin.iloc[1,1]], 
                      ['Naturgy',df_table_n_stocks.iloc[26,1]*df_naturgy.iloc[1,1]], 
                      ['Pharma Mar',df_table_n_stocks.iloc[27,1]*df_pharmaMar.iloc[1,1]], 
                      ['Red Eléctrica',df_table_n_stocks.iloc[28,1]*df_redElectrica.iloc[1,1]], 
                      ['Repsol',df_table_n_stocks.iloc[29,1]*df_repsol.iloc[1,1]], 
                      ['Rovi',df_table_n_stocks.iloc[30,1]*df_rovi.iloc[1,1]], 
                      ['Sacyr',df_table_n_stocks.iloc[31,1]*df_sacyr.iloc[1,1]], 
                      ['Siemens Gamesa',df_table_n_stocks.iloc[32,1]*df_siemens.iloc[1,1]], 
                      ['Solaria',df_table_n_stocks.iloc[33,1]*df_solaria.iloc[1,1]], 
                      ['Telefónica',df_table_n_stocks.iloc[34,1]*df_telefonica.iloc[1,1]]]
df_ranking_0_inv = pd.DataFrame(data_ranking_0_inv,columns=['Nombre','Valor'])
ordenarRanking(df_ranking_0_inv)
df_ranking_0_inv


# A modo comentario, como ejemplos, al cierre de la segunda sesión, la inversión inicial de 1000 € en Arcelormittal ha pasado a tener un valor de 913.705584 €, en contraposición del valor para Grifols que asciende a los 1047.443007 €.
# 
# De forma análoga se calculan y se ordenan el segundo y el último ranking.

# In[47]:


#Segundo ranking
data_ranking_1_inv = [['Acciona',df_table_n_stocks.iloc[0,1]*df_acciona.iloc[2,1]],
                      ['Acciona Energía',df_table_n_stocks.iloc[1,1]*df_accionaEnergia.iloc[2,1]], 
                      ['Acerinox',df_table_n_stocks.iloc[2,1]*df_acerinox.iloc[2,1]], 
                      ['Acs',df_table_n_stocks.iloc[3,1]*df_acs.iloc[2,1]], 
                      ['Aena',df_table_n_stocks.iloc[4,1]*df_aena.iloc[2,1]], 
                      ['Amadeus',df_table_n_stocks.iloc[5,1]*df_amadeus.iloc[2,1]], 
                      ['Arcelormittal',df_table_n_stocks.iloc[6,1]*df_arcelormittal.iloc[2,1]], 
                      ['Banco Santander',df_table_n_stocks.iloc[7,1]*df_santander.iloc[2,1]], 
                      ['Banco Sabadell',df_table_n_stocks.iloc[8,1]*df_sabadell.iloc[2,1]], 
                      ['Bankinter',df_table_n_stocks.iloc[9,1]*df_bankinter.iloc[2,1]], 
                      ['BBVA',df_table_n_stocks.iloc[10,1]*df_bbva.iloc[2,1]], 
                      ['Caixabank',df_table_n_stocks.iloc[11,1]*df_caixabank.iloc[2,1]], 
                      ['Cellnex',df_table_n_stocks.iloc[12,1]*df_cellnex.iloc[2,1]], 
                      ['Enagás',df_table_n_stocks.iloc[13,1]*df_enagas.iloc[2,1]], 
                      ['Endesa',df_table_n_stocks.iloc[14,1]*df_endesa.iloc[2,1]], 
                      ['Ferrovial',df_table_n_stocks.iloc[15,1]*df_ferrovial.iloc[2,1]], 
                      ['Fluidra',df_table_n_stocks.iloc[16,1]*df_fluidra.iloc[2,1]], 
                      ['Grifols',df_table_n_stocks.iloc[17,1]*df_grifols.iloc[2,1]], 
                      ['IAG',df_table_n_stocks.iloc[18,1]*df_IAG.iloc[2,1]], 
                      ['Iberdrola',df_table_n_stocks.iloc[19,1]*df_iberdrola.iloc[2,1]], 
                      ['Inditex',df_table_n_stocks.iloc[20,1]*df_inditex.iloc[2,1]], 
                      ['Indra',df_table_n_stocks.iloc[21,1]*df_indra.iloc[2,1]], 
                      ['Inmobiliaria Colonial',df_table_n_stocks.iloc[22,1]*df_colonial.iloc[2,1]], 
                      ['Mapfre',df_table_n_stocks.iloc[23,1]*df_mapfre.iloc[2,1]], 
                      ['Meliá Hotels',df_table_n_stocks.iloc[24,1]*df_melia.iloc[2,1]], 
                      ['Merlin Properties',df_table_n_stocks.iloc[25,1]*df_merlin.iloc[2,1]], 
                      ['Naturgy',df_table_n_stocks.iloc[26,1]*df_naturgy.iloc[2,1]], 
                      ['Pharma Mar',df_table_n_stocks.iloc[27,1]*df_pharmaMar.iloc[2,1]], 
                      ['Red Eléctrica',df_table_n_stocks.iloc[28,1]*df_redElectrica.iloc[2,1]], 
                      ['Repsol',df_table_n_stocks.iloc[29,1]*df_repsol.iloc[2,1]], 
                      ['Rovi',df_table_n_stocks.iloc[30,1]*df_rovi.iloc[2,1]], 
                      ['Sacyr',df_table_n_stocks.iloc[31,1]*df_sacyr.iloc[2,1]], 
                      ['Siemens Gamesa',df_table_n_stocks.iloc[32,1]*df_siemens.iloc[2,1]], 
                      ['Solaria',df_table_n_stocks.iloc[33,1]*df_solaria.iloc[2,1]], 
                      ['Telefónica',df_table_n_stocks.iloc[34,1]*df_telefonica.iloc[2,1]]]
df_ranking_1_inv = pd.DataFrame(data_ranking_1_inv,columns=['Nombre','Valor'])
ordenarRanking(df_ranking_1_inv)
df_ranking_1_inv


# In[48]:


#Último ranking
data_ranking_129_inv = [['Acciona',df_table_n_stocks.iloc[0,1]*df_acciona.iloc[130,1]],
                        ['Acciona Energía',df_table_n_stocks.iloc[1,1]*df_accionaEnergia.iloc[130,1]], 
                        ['Acerinox',df_table_n_stocks.iloc[2,1]*df_acerinox.iloc[130,1]], 
                        ['Acs',df_table_n_stocks.iloc[3,1]*df_acs.iloc[130,1]], 
                        ['Aena',df_table_n_stocks.iloc[4,1]*df_aena.iloc[130,1]], 
                        ['Amadeus',df_table_n_stocks.iloc[5,1]*df_amadeus.iloc[130,1]], 
                        ['Arcelormittal',df_table_n_stocks.iloc[6,1]*df_arcelormittal.iloc[130,1]], 
                        ['Banco Santander',df_table_n_stocks.iloc[7,1]*df_santander.iloc[130,1]], 
                        ['Banco Sabadell',df_table_n_stocks.iloc[8,1]*df_sabadell.iloc[130,1]], 
                        ['Bankinter',df_table_n_stocks.iloc[9,1]*df_bankinter.iloc[130,1]], 
                        ['BBVA',df_table_n_stocks.iloc[10,1]*df_bbva.iloc[130,1]], 
                        ['Caixabank',df_table_n_stocks.iloc[11,1]*df_caixabank.iloc[130,1]], 
                        ['Cellnex',df_table_n_stocks.iloc[12,1]*df_cellnex.iloc[130,1]], 
                        ['Enagás',df_table_n_stocks.iloc[13,1]*df_enagas.iloc[130,1]], 
                        ['Endesa',df_table_n_stocks.iloc[14,1]*df_endesa.iloc[130,1]], 
                        ['Ferrovial',df_table_n_stocks.iloc[15,1]*df_ferrovial.iloc[130,1]], 
                        ['Fluidra',df_table_n_stocks.iloc[16,1]*df_fluidra.iloc[130,1]], 
                        ['Grifols',df_table_n_stocks.iloc[17,1]*df_grifols.iloc[130,1]], 
                        ['IAG',df_table_n_stocks.iloc[18,1]*df_IAG.iloc[130,1]], 
                        ['Iberdrola',df_table_n_stocks.iloc[19,1]*df_iberdrola.iloc[130,1]], 
                        ['Inditex',df_table_n_stocks.iloc[20,1]*df_inditex.iloc[130,1]], 
                        ['Indra',df_table_n_stocks.iloc[21,1]*df_indra.iloc[130,1]], 
                        ['Inmobiliaria Colonial',df_table_n_stocks.iloc[22,1]*df_colonial.iloc[130,1]], 
                        ['Mapfre',df_table_n_stocks.iloc[23,1]*df_mapfre.iloc[130,1]], 
                        ['Meliá Hotels',df_table_n_stocks.iloc[24,1]*df_melia.iloc[130,1]], 
                        ['Merlin Properties',df_table_n_stocks.iloc[25,1]*df_merlin.iloc[130,1]], 
                        ['Naturgy',df_table_n_stocks.iloc[26,1]*df_naturgy.iloc[130,1]], 
                        ['Pharma Mar',df_table_n_stocks.iloc[27,1]*df_pharmaMar.iloc[130,1]], 
                        ['Red Eléctrica',df_table_n_stocks.iloc[28,1]*df_redElectrica.iloc[130,1]], 
                        ['Repsol',df_table_n_stocks.iloc[29,1]*df_repsol.iloc[130,1]], 
                        ['Rovi',df_table_n_stocks.iloc[30,1]*df_rovi.iloc[130,1]], 
                        ['Sacyr',df_table_n_stocks.iloc[31,1]*df_sacyr.iloc[130,1]], 
                        ['Siemens Gamesa',df_table_n_stocks.iloc[32,1]*df_siemens.iloc[130,1]], 
                        ['Solaria',df_table_n_stocks.iloc[33,1]*df_solaria.iloc[130,1]], 
                        ['Telefónica',df_table_n_stocks.iloc[34,1]*df_telefonica.iloc[130,1]]]
df_ranking_129_inv = pd.DataFrame(data_ranking_129_inv,columns=['Nombre','Valor'])
ordenarRanking(df_ranking_129_inv)
df_ranking_129_inv


# Bajo estas ideas, es momento de escalar el modelo. Es decir, lo que se ha construido para rankings concretos hay que hacerlo utilizando la información de todas las sesiones de las que se tiene información. 
# 
# Puesto que el valor de la inversión solamente es el instrumento para poder establecer el orden, lo importante es quedarse con el nombre de las empresas ordenadas por ese valor. Dicho esto, para almacenar toda la información de los rankings se construye un dataFrame con tantas columnas como rankings se vayan a construir (número de sesiones totales menos una, la primera, la cual se utiliza para calcular el número de acciones equivalentes), es decir, 130 columnas, y tantas filas como empresas haya, en este caso 35.
# 
# Con ello, se busca recorrer todas las sesiones de las que se tiene información mediante un bucle *for* y, mediante una variable auxiliar, ir creando rankings con la misma estructura que los ejemplos anteriores, ordenándolos y almacenando en ese dataFrame inicial el nombre de las empresas ordenadas <u>decrecientemente</u> según el valor equivalente en esa sesión concreta. Así, la columna *j* hará referencia al ranking *j+1* que ha empleado el precio de cierre de sesión de la sesión *j+2* almacenada en los dataFrame de las empresas en la fila *j+1*.

# In[49]:


########################################### Escalabilidad del modelo ###########################################
#Creación de un Data Frame con tantas filas como empresas y tantas columnas como rankings 
df_rankings_inv = pd.DataFrame(columns=rankings,index=classification)

#Bucle
for i in range(1,n_sesions):
    data_aux_inv = [['Acciona',df_table_n_stocks.iloc[0,1]*df_acciona.iloc[i,1]],
                    ['Acciona Energía',df_table_n_stocks.iloc[1,1]*df_accionaEnergia.iloc[i,1]], 
                    ['Acerinox',df_table_n_stocks.iloc[2,1]*df_acerinox.iloc[i,1]], 
                    ['Acs',df_table_n_stocks.iloc[3,1]*df_acs.iloc[i,1]], 
                    ['Aena',df_table_n_stocks.iloc[4,1]*df_aena.iloc[i,1]], 
                    ['Amadeus',df_table_n_stocks.iloc[5,1]*df_amadeus.iloc[i,1]], 
                    ['Arcelormittal',df_table_n_stocks.iloc[6,1]*df_arcelormittal.iloc[i,1]], 
                    ['Banco Santander',df_table_n_stocks.iloc[7,1]*df_santander.iloc[i,1]], 
                    ['Banco Sabadell',df_table_n_stocks.iloc[8,1]*df_sabadell.iloc[i,1]], 
                    ['Bankinter',df_table_n_stocks.iloc[9,1]*df_bankinter.iloc[i,1]], 
                    ['BBVA',df_table_n_stocks.iloc[10,1]*df_bbva.iloc[i,1]],
                    ['Caixabank',df_table_n_stocks.iloc[11,1]*df_caixabank.iloc[i,1]], 
                    ['Cellnex',df_table_n_stocks.iloc[12,1]*df_cellnex.iloc[i,1]], 
                    ['Enagás',df_table_n_stocks.iloc[13,1]*df_enagas.iloc[i,1]], 
                    ['Endesa',df_table_n_stocks.iloc[14,1]*df_endesa.iloc[i,1]], 
                    ['Ferrovial',df_table_n_stocks.iloc[15,1]*df_ferrovial.iloc[i,1]], 
                    ['Fluidra',df_table_n_stocks.iloc[16,1]*df_fluidra.iloc[i,1]], 
                    ['Grifols',df_table_n_stocks.iloc[17,1]*df_grifols.iloc[i,1]], 
                    ['IAG',df_table_n_stocks.iloc[18,1]*df_IAG.iloc[i,1]], 
                    ['Iberdrola',df_table_n_stocks.iloc[19,1]*df_iberdrola.iloc[i,1]], 
                    ['Inditex',df_table_n_stocks.iloc[20,1]*df_inditex.iloc[i,1]], 
                    ['Indra',df_table_n_stocks.iloc[21,1]*df_indra.iloc[i,1]], 
                    ['Inmobiliaria Colonial',df_table_n_stocks.iloc[22,1]*df_colonial.iloc[i,1]], 
                    ['Mapfre',df_table_n_stocks.iloc[23,1]*df_mapfre.iloc[i,1]], 
                    ['Meliá Hotels',df_table_n_stocks.iloc[24,1]*df_melia.iloc[i,1]], 
                    ['Merlin Properties',df_table_n_stocks.iloc[25,1]*df_merlin.iloc[i,1]], 
                    ['Naturgy',df_table_n_stocks.iloc[26,1]*df_naturgy.iloc[i,1]], 
                    ['Pharma Mar',df_table_n_stocks.iloc[27,1]*df_pharmaMar.iloc[i,1]], 
                    ['Red Eléctrica',df_table_n_stocks.iloc[28,1]*df_redElectrica.iloc[i,1]], 
                    ['Repsol',df_table_n_stocks.iloc[29,1]*df_repsol.iloc[i,1]], 
                    ['Rovi',df_table_n_stocks.iloc[30,1]*df_rovi.iloc[i,1]], 
                    ['Sacyr',df_table_n_stocks.iloc[31,1]*df_sacyr.iloc[i,1]], 
                    ['Siemens Gamesa',df_table_n_stocks.iloc[32,1]*df_siemens.iloc[i,1]], 
                    ['Solaria',df_table_n_stocks.iloc[33,1]*df_solaria.iloc[i,1]], 
                    ['Telefónica',df_table_n_stocks.iloc[34,1]*df_telefonica.iloc[i,1]]]
    df_aux_inv = pd.DataFrame(data_aux_inv,columns=['Nombre','Valor'])
    ordenarRanking(df_aux_inv)
    df_rankings_inv.iloc[:,i-1]=df_aux_inv.iloc[:,0]
df_rankings_inv


# Puesto que se habían creado y ordenado tres rankings concretos para su posterior comprobación, se evalúa si realmente se obtiene lo mismo.
# 
# Para ello, se construyen tres variables flag que recorran los 6 rankings comparando por pares correspondientes.

# In[50]:


flag0_inv=True
flag1_inv=True
flag129_inv=True

for i in range(n_stocks):
    flag0_inv = (df_rankings_inv.iloc[i,0]==df_ranking_0_inv.iloc[i,0])

for j in range(n_stocks):
    flag1_inv = (df_rankings_inv.iloc[j,1]==df_ranking_1_inv.iloc[j,0])

for k in range(n_stocks):
    flag129_inv = (df_rankings_inv.iloc[k,129]==df_ranking_129_inv.iloc[k,0])

(flag0_inv,flag1_inv,flag129_inv)


# Como se podía ver visualmente, la ordenación en los tres rankings es la misma, por lo que se puede dar por bueno el modelo planteado.
# 
# El dataFrame anterior es la recogida de todos los rankings generados a lo largo de todas las sesiones. Con ello, hay que evaluar si para cada par de acciones y para cada par de rankings contiguos las acciones intercambian su posición relativa. Es decir, si la que antes estaba por encima de la otra ahora está por debajo o viceversa. 
# 
# Tras evaluar esto mismo para cada par de acciones y cada par de rankings contiguos, se obtiene el número de veces que las acciones han intercambiado su posición, o dicho análogamente, que se cruzan y por tanto compiten. Este número de intercambios será el peso de la arista que una ambas acciones (nodos) en el grafo de competitividad.
# 
# Para estudiar los posibles cruces, se crea la siguiente función, llamada ***seCruza***. Esta función toma como argumentos dos columnas de datos (en este estudio, dos rankings) y dos nombres de acciones. Su funcionamento es el descrito anteriormente, conocer si dada esas dos acciones, estas intercambian sus posiciones relativas en los dos rankings. 
# 
# Con ella, una vez se tenga implementada, se podrá recorrer mediante un bucle el dataFrame de rankings con la lista de empresas almacenadas en la variable *stocks* para ir tomando pares de rankings y pares de acciones e ir estudiando los posibles cruces.

# In[51]:


#Algoritmo para saber si dado un par de acciones estas se cruzan en dos rankings dados
def seCruza(data1,data2,stock1,stock2):
    n = len(data1) 
    find1_1 = False
    find1_2 = False
    i = 0
    
    while (i<n and (find1_1==False or find1_2==False)):
        if data1[i] == stock1:
            find1_1 = True
            pos1_1 = i
        if data1[i] == stock2:
            find1_2 = True
            pos1_2 = i
        i=i+1
    
    find2_1 = False
    find2_2 = False
    j = 0
    
    while (j<n and (find2_1==False or find2_2==False)):
        if data2[j] == stock1:
            find2_1 = True
            pos2_1 = j
        if data2[j] == stock2:
            find2_2 = True
            pos2_2 = j
        j=j+1
    
    up1= stock1 if (pos1_1>pos1_2) else stock2
    up2= stock1 if (pos2_1>pos2_2) else stock2
        
    flag = not(up1==up2)
        
    return flag


# Con el algoritmo implementado, es momento de probarlo.

# In[52]:


# Prueba algoritmo seCruza
a = seCruza(df_ranking_0_inv.iloc[:,0],df_ranking_1_inv.iloc[:,0],'Pharma Mar','Sacyr')
b = seCruza(df_ranking_0_inv.iloc[:,0],df_ranking_1_inv.iloc[:,0],'Acs','Telefónica')
c = seCruza(df_ranking_0_inv.iloc[:,0],df_ranking_1_inv.iloc[:,0],'Telefónica','Acs')
d = seCruza(df_ranking_0_inv.iloc[:,0],df_ranking_1_inv.iloc[:,0],'Sacyr','Pharma Mar')

(a,b,c,d)


# Volviendo a los dos rankings primeros creados, se tiene claramente que Pharma Mar y Sacyr sí intercambian su posición relativa, pues inicialmente Pharma Mar estaba por encima de Sacyr y en el siguiente ranking es Sacyr quien está por encima de Pharma Mar. Además, por otro lado, en ambos rankings, Acs se encuentra por encima de Telefónica, por lo que no  han intercambiado su posición relativa.
# 
# Adicionalmente a la simple comprobación de si se cruzan o no, se prueba el algoritmo en ambas direcciones, tanto si una está primera como si está la última, observando que para los casos anteriores la evaluación se hace de la manera deseada.
# 
# Con el dataFrame de rankings creado, es momento de recorrerlo por pares de rankings contiguos y con la lista de empresas almacenada en la variable *stocks* ir tomando pares de acciones para comprobar si se cruzan o no. Con ello, se construye una matriz que será la matriz de adyacencia del grafo de competitividad. Esta tiene por filas y columnas las acciones del estudio, en donde un cruce fila-columna indica el número de veces que la acción de la fila se ha cruzado con la acción de la columna a lo largo de los 130 rankings. Como observación, la diagonal es de ceros debido a que una acción no intercambia posición consigo misma y la matriz es simétrica debido a que es igual que su traspuesta. Esto último se debe a que la empresa *i* compite con la empresa *j* tantas veces como la empresa *j* lo hace con la empresa *i*.
# 
# Bajo esta idea, se ejecuta el siguiente bloque.

# In[53]:


#Definición de la matriz de adyacencia del grafo, donde sus filas y sus columnas son las acciones
adj_matrix_inv = pd.DataFrame(columns=stocks,index=stocks)

#Dicha matriz se rellena de 0's para asegurarse de que posteriormente se puede rellenar de la forma que se desea en el estudio
for i in range(n_stocks):
    for j in range(n_stocks):
        adj_matrix_inv.iloc[i,j]=0

#Iteraciones para completarla con el dataFrame de rankings: Se toma una acción y cada una de sus sucesivas a lo largo
#de todos los rankings, tomados de dos en dos de forma contigua
for k in range(n_sesions-2):
    for i in range(n_stocks):
        for j in range(i+1,n_stocks):
            if (seCruza(df_rankings_inv.iloc[:,k],df_rankings_inv.iloc[:,k+1],stocks[i],stocks[j])):
                adj_matrix_inv.iloc[i,j] = adj_matrix_inv.iloc[i,j]+1
                adj_matrix_inv.iloc[j,i] = adj_matrix_inv.iloc[j,i]+1
adj_matrix_inv


# Con esta matriz de adyacencia, se puede representar el grafo de competitividad de esta perspectiva. Primeramente, hay que crear el objeto *grafo* en el entorno de trabajo.

# In[54]:


#Creación del grafo
G_inv = nx.Graph()
G_inv.add_nodes_from(stocks)

for i in range(n_stocks):
    for j in range(i+1,n_stocks):
        if(adj_matrix_inv.iloc[i,j]>0):
            G_inv.add_edge(stocks[i],stocks[j],weight=adj_matrix_inv.iloc[i,j])


# A continuación, aunque se ha probado con representaciones simples y diferentes posibilidades de este software para la representación de grafos (shell, ciruclar, kamada_kawai,etc.) en las sucesivas representaciones de grafos solamente se incluirá aquella que mejor disposición tenga de los nodos y de las aristas, de forma que se pueda ver, de manera más o menos clara, la representación del grafo.
# 
# Para llevar a cabo esta representación, se utilizan diferentes funciones de la librería *networkx* que permite esa mejor disposición de los objetos del grafo. Para aligerarla y puesto que tampoco aporta nada, en lugar de agregar los pesos de las aristas se va a representar las aristas con un grosor proporcional a su peso.

# In[55]:


#Primero se genera el tipo de diseño del grafo para que los nodos estén bien diferenciados en la representación
pos_inv = nx.circular_layout(G_inv)

#Para representar las aristas se va a representar el grosor de la misma en proporcion a su peso
edgew_inv = [0.15*G_inv.get_edge_data(u, v)['weight'] for u, v in G_inv.edges()]
#Con la siguiente expresión se consigue establecer el ancho (x) y el alto (y) del espacio donde se va a representar el grafo
x_inv, y_inv = plt.subplots(figsize=(12, 12))
#Título del grafo
y_inv.set_title("Competitivity graph: Perspective 1", dict(fontweight="bold",fontsize=22,color="black"),loc="center")

#Representación de los objetos del grafo
    #Aristas
nx.draw_networkx_edges(G_inv, pos_inv, width=edgew_inv, edge_color="navy", style='-')
    #Nodos
nx.draw_networkx_nodes(G_inv, pos_inv, node_size=700, node_shape='o', node_color="gold", linewidths=1,edgecolors="black")
    #Etiquetas sobre nodos
nx.draw_networkx_labels(G_inv, pos_inv, font_size=11, bbox=dict(ec="black",boxstyle="round",facecolor="white",pad=0.3,alpha=0.6), font_weight='normal', font_family='Verdana', horizontalalignment='center', verticalalignment='center',clip_on=False)

#Modificaciones sobre el espacio de representación para optimizar la representación
x_inv.tight_layout()
plt.axis("off") #Para no representar los ejes
y_inv.margins(0.05,0.05)
plt.savefig("CG1.png") #Para guardar la imagen para exportarla al documento de texto
plt.show() #Para mostrar el grafo


# El resultado obtenido es un grafo donde se observa que todas compiten con todas y que no hay nada que permita distinguir alguna de ellas por encima del resto. Por ello, se plantean tres alternativas:
# 
#  * Tomar solo aquellas aristas cuyo peso sea mayor que el de la media del total de pesos mayores que 0 de las aristas del          grafo.
#  * Tomar aquellas aristas con un peso mayor que la medida 1 del total de pesos mayores que 0 de las aristas del grafo.
#  * Tomar aquellas aristas con un peso mayor que la medida 2 del total de pesos mayores que 0 de las aristas del grafo.
# 
# Las medida 1 y medida 2 serán explicadas posteriormente en cada subvariante. Por el momento, es suficiente con saber que son un valor.

# #### 3.1.1. Perspectiva 1.1: Bajo una inversión inicial de 1000 €, estudio de la evolución diaria del total de la inversión al cierre de la sesión para aquellas empresas que se crucen más que la media del total de pesos de las aristas del grafo

# Bajo esta idea, se hace un evolutivo de la primera perspectiva. Para ello, simplemente:
#    * Se hace una copia de la matriz original.
#    * Se calcula la <u>media</u> de todos los pesos mayores que 0 que están escritos en dicha matriz, con cuidado de no duplicar      pesos, en el sentido de que el valor [i,j] hace referencia a la misma arista que el valor [j,i].
#    * Se actualiza sobre la matriz copia el valor de las aristas, a través de dos opciones:
#        1. Si una arista tiene un peso inferior a la media, este se actualiza a 0.
#        2. Si una arista tiene un peso mayor o igual a la media, se actualiza con la diferencia entre ambos valores.
#    * Con esta nueva matriz de adyacencia se representa el grafo adjunto.
# 

# In[56]:


#Copia de la matriz original
adj_matrix_inv_avg = pd.DataFrame.copy(adj_matrix_inv)

#Cálculo de la media de pesos. Para ello, solo se recorre la mitad de la matriz, debido a que la información está duplicada
aux_inv_avg=[]
for i in range(0,n_stocks):
    for j in range(i+1,n_stocks):
        if(adj_matrix_inv_avg.iloc[i,j]>0):
            aux_inv_avg.append(adj_matrix_inv_avg.iloc[i,j])
mean_aux_inv_avg = np.mean(aux_inv_avg)
        
#A continuación, se actualiza la matriz adj_matrix_inv_avg
for i in range(0,n_stocks):
    for j in range(i+1,n_stocks):
        if(adj_matrix_inv_avg.iloc[i,j] < mean_aux_inv_avg):
            adj_matrix_inv_avg.iloc[i,j] = 0
            adj_matrix_inv_avg.iloc[j,i] = 0 
        else:
            adj_matrix_inv_avg.iloc[i,j] = adj_matrix_inv_avg.iloc[i,j] - mean_aux_inv_avg
            adj_matrix_inv_avg.iloc[j,i] = adj_matrix_inv_avg.iloc[j,i] - mean_aux_inv_avg
adj_matrix_inv_avg


# De manera análoga al desarrollo anterior de esta sección, se representa el grafo asociado a esta matriz de adyacencia.

# In[58]:


#Creación del grafo
G_inv_avg = nx.Graph()
G_inv_avg.add_nodes_from(stocks)

for i in range(n_stocks):
    for j in range(i+1,n_stocks):
        if(adj_matrix_inv_avg.iloc[i,j]>0):
            G_inv_avg.add_edge(stocks[i],stocks[j],weight=adj_matrix_inv_avg.iloc[i,j])


# In[59]:


#Tipo de diseño del grafo
pos_inv_avg = nx.circular_layout(G_inv_avg)

#Grosor de las aristas
edgew_inv_avg = [0.2*G_inv_avg.get_edge_data(u, v)['weight'] for u, v in G_inv_avg.edges()]
#Espacio de representación
x_inv_avg, y_inv_avg = plt.subplots(figsize=(12, 12))
#Título del grafo
y_inv_avg.set_title("Competitivity graph: Perspective 1.1", dict(fontweight="bold",fontsize=22,color="black"),loc="center")

#Representación de los objetos del grafo
    #Aristas
nx.draw_networkx_edges(G_inv_avg, pos_inv_avg, width=edgew_inv_avg, edge_color="navy", style='-')
    #Nodos
nx.draw_networkx_nodes(G_inv_avg, pos_inv_avg, node_size=700, node_shape='o', node_color="gold", linewidths=1,edgecolors="black")
    #Etiquetas sobre nodos
nx.draw_networkx_labels(G_inv_avg, pos_inv_avg, font_size=11, bbox=dict(ec="black",boxstyle="round",facecolor="white",pad=0.3,alpha=0.6), font_weight='normal', font_family='Verdana', horizontalalignment='center', verticalalignment='center',clip_on=False)

#Modificaciones sobre el espacio de representación
x_inv_avg.tight_layout()
plt.axis("off")
y_inv_avg.margins(0.05,0.05)
plt.savefig("CG1-1.png")
plt.show()


# Pese a que se ve algo más claro que en el caso anterior, es necesario subir el límite para considerar los pesos de las aristas de forma que queden las aristas más signficativas. Por ello, se pasa a la siguiente subvariante.

# #### 3.1.2. Perspectiva 1.2: Bajo una inversión inicial de 1000 €, estudio de la evolución diaria del total de la inversión al cierre de la sesión para aquellas empresas que se crucen más que la medida 1 del total de pesos de las aristas del grafo

# Para este evolutivo, la idea es exactamente la misma que la del apartado 3.1.1, pero en lugar de considerar aristas cuyo valor sea mayor que la media, se consideran aristas que superen la <u>medida 1</u>. Esta medida 1 es el valor que ocupa la posición intermedia entre la media anteriormente calculada y el máximo peso existente entre todas las aristas del grafo.

# In[60]:


#Copia de la matriz original
adj_matrix_inv_ms1 = pd.DataFrame.copy(adj_matrix_inv)

#Cálculo del valor medida 1
measure_1_inv = mean_aux_inv_avg + 0.5*(max(aux_inv_avg)-mean_aux_inv_avg) 

#A continuación, se actualiza la matriz adj_matrix_inv_ms1
for i in range(0,n_stocks):
    for j in range(i+1,n_stocks):
        if(adj_matrix_inv_ms1.iloc[i,j] < measure_1_inv):
            adj_matrix_inv_ms1.iloc[i,j] = 0
            adj_matrix_inv_ms1.iloc[j,i] = 0 
        else:
            adj_matrix_inv_ms1.iloc[i,j] = adj_matrix_inv_ms1.iloc[i,j] - measure_1_inv
            adj_matrix_inv_ms1.iloc[j,i] = adj_matrix_inv_ms1.iloc[j,i] - measure_1_inv
adj_matrix_inv_ms1


# Y de nuevo, de forma totalmente análoga se crea y se representa el grafo adjunto a esta matriz de adyacencia.

# In[61]:


#Creación del grafo
G_inv_ms1 = nx.Graph()
G_inv_ms1.add_nodes_from(stocks)

for i in range(n_stocks):
    for j in range(i+1,n_stocks):
        if(adj_matrix_inv_ms1.iloc[i,j]>0):
            G_inv_ms1.add_edge(stocks[i],stocks[j],weight=adj_matrix_inv_ms1.iloc[i,j])


# In[62]:


#Tipo de diseño del grafo
pos_inv_ms1 = nx.circular_layout(G_inv_ms1)

#Grosor de las aristas
edgew_inv_ms1 = [0.9*G_inv_ms1.get_edge_data(u, v)['weight'] for u, v in G_inv_ms1.edges()]
#Espacio de representación
x_inv_ms1, y_inv_ms1 = plt.subplots(figsize=(12, 12))
#Título del grafo
y_inv_ms1.set_title("Competitivity graph: Perspective 1.2", dict(fontweight="bold",fontsize=22,color="black"),loc="center")

#Representación de los objetos del grafo
    #Aristas
nx.draw_networkx_edges(G_inv_ms1, pos_inv_ms1, width=edgew_inv_ms1, edge_color="navy", style='-')
    #Nodos
nx.draw_networkx_nodes(G_inv_ms1, pos_inv_ms1, node_size=700, node_shape='o', node_color="gold", linewidths=1,edgecolors="black")
    #Etiquetas sobre nodos
nx.draw_networkx_labels(G_inv_ms1, pos_inv_ms1, font_size=11, bbox=dict(ec="black",boxstyle="round",facecolor="white",pad=0.3,alpha=0.6), font_weight='normal', font_family='Verdana', horizontalalignment='center', verticalalignment='center',clip_on=False)

#Modificaciones sobre el espacio de representación
x_inv_ms1.tight_layout()
plt.axis("off") 
y_inv_ms1.margins(0.05,0.05)
plt.savefig("CG1-2.png")
plt.show() 


# Como se puede observar en este momento, el número de aristas que han quedado tras subir el límite es muy bajo y se puede concluir que estás son las más relevantes en el grafo, es decir, aquellas cuyos nodos adyacentes son los que más compiten.
# 
# Por último, se aumenta este límite una última vez en la siguiente subsección aunque con este nivel ya sería suficiente.

# #### 3.1.3. Perspectiva 1.3: Bajo una inversión inicial de 1000 €, estudio de la evolución diaria del total de la inversión al cierre de la sesión para aquellas empresas que se crucen más que la medida 2 del total de pesos de las aristas del grafo

# Para esta subvariante se trabaja de forma totalmente análoga a las anteriores, pero colocando el límite para tener en cuenta las aristas en aquellas cuyo peso sea mayor que la <u>medida 2</u> del total de pesos de las aristas del grafo. Esta medida 2 es un valor un poco mayor a la medida 1, en el sentido de que está en una posición más alta que el punto intermedio entre la media y el valor del máximo peso de las aristas del grafo. Concretamente, si el factor para la medida 1 es 0.5, para esta medida 2 se situa en 0.6.

# In[63]:


#Copia de la matriz original
adj_matrix_inv_ms2 = pd.DataFrame.copy(adj_matrix_inv)

#Cálculo del valor medida 2
measure_2_inv = mean_aux_inv_avg + 0.6*(max(aux_inv_avg)-mean_aux_inv_avg) 

#A continuación, se actualiza la matriz adj_matrix_inv_ms2
for i in range(0,n_stocks):
    for j in range(i+1,n_stocks):
        if(adj_matrix_inv_ms2.iloc[i,j] < measure_2_inv):
            adj_matrix_inv_ms2.iloc[i,j] = 0
            adj_matrix_inv_ms2.iloc[j,i] = 0 
        else:
            adj_matrix_inv_ms2.iloc[i,j] = adj_matrix_inv_ms2.iloc[i,j] - measure_2_inv
            adj_matrix_inv_ms2.iloc[j,i] = adj_matrix_inv_ms2.iloc[j,i] - measure_2_inv
adj_matrix_inv_ms2


# Dicha matriz de adyacencia acompañada de la representación del grafo asociado.

# In[64]:


#Creación del grafo
G_inv_ms2 = nx.Graph()
G_inv_ms2.add_nodes_from(stocks)

for i in range(n_stocks):
    for j in range(i+1,n_stocks):
        if(adj_matrix_inv_ms2.iloc[i,j]>0):
            G_inv_ms2.add_edge(stocks[i],stocks[j],weight=adj_matrix_inv_ms2.iloc[i,j])


# In[65]:


#Tipo de diseño del grafo
pos_inv_ms2 = nx.circular_layout(G_inv_ms2)

#Grosor de las aristas
edgew_inv_ms2 = [G_inv_ms2.get_edge_data(u, v)['weight'] for u, v in G_inv_ms2.edges()]
#Espacio de representación
x_inv_ms2, y_inv_ms2 = plt.subplots(figsize=(12, 12))
#Título del grafo
y_inv_ms2.set_title("Competitivity graph: Perspective 1.3", dict(fontweight="bold",fontsize=22,color="black"),loc="center")

#Representación de los objetos del grafo
    #Aristas
nx.draw_networkx_edges(G_inv_ms2, pos_inv_ms2, width=edgew_inv_ms2, edge_color="navy", style='-')
    #Nodos
nx.draw_networkx_nodes(G_inv_ms2, pos_inv_ms2, node_size=700, node_shape='o', node_color="gold", linewidths=1,edgecolors="black")
    #Etiquetas sobre nodos
nx.draw_networkx_labels(G_inv_ms2, pos_inv_ms2, font_size=11, bbox=dict(ec="black",boxstyle="round",facecolor="white",pad=0.3,alpha=0.6), font_weight='normal', font_family='Verdana', horizontalalignment='center', verticalalignment='center',clip_on=False)

#Modificaciones sobre el espacio de representación
x_inv_ms2.tight_layout()
plt.axis("off") 
y_inv_ms2.margins(0.05,0.05)
plt.savefig("CG1-3.png")
plt.show() 


# Como se había comentado anteriormente, subir el límite para esta perspectiva no iba a aportar mucho valor porque se iba a perder demasiada información. Para este caso, por ejemplo, solo han quedado aquellas aristas que en la perspectiva 1.2 presentaban un grosor considerable, equivalentemente, un peso considerable, eliminando aquellas cuyas aristas eran muy débiles.
# 
# Sin embargo, habrá que ver qué ocurre para esta subvariante en el resto de perspectivas.

# ### 3.2. Perspectiva 2: Bajo una inversión inicial de 1000 €, estudio de la diferencia diaria del total de la inversión al cierre de la sesión

# Para el desarrollo de esta variante hay que recurrir a la idea desarrollada en el apartado anterior. La situación inicial es la misma, dada la primera sesión se hace una inversión inicial al cierre de esta sesión de 1000 € en cada una de las empresas. Esto conlleva un número de acciones equivalente para cada una de ellas. Como anteriormente, hay que puntuar que el número de acciones es fijo en el tiempo y que a lo largo del estudio este no varía. Una vez explicado esto, lo siguiente que acompaña a este enfoque es:
# 
#    * A lo largo de las sucesivas sesiones, dado el número de acciones de cada empresa, estas tienen un valor que va variando a      lo largo de todas las sesiones, siempre fijándose en el precio de cierre de cada sesión.
#    * En este enfoque en lugar de utilizar este valor directamente hay que trabajar con la diferencia entre el valor de la            inversión en cada empresa en la sesión que se observa respecto del valor que tenían las mismas en la sesión anterior.
#    * Con estos valores para cada empresa y para cada sesión se construyen los rankings, se calculan los números de cruces y se      obtiene así la matriz de adyacencia para la posterior representación del grafo.
# 
# Una vez visto el enfoque de la idea, hay que desarrollarla. Para ello, se utiliza el número de acciones de cada empresa calculado en el apartado anterior sobre el precio de cierre de la primera sesión, equivalentes a 1000 €. Hay que recordar que dicha información se encuentra en la variable *df_table_n_stocks*.
# 
# Aunque a continuación se creará una tabla para clarificar el concepto que sigue esta perspectiva, la base de todo es calcular la diferencia entre dos valores. Puesto que estos valores estarán en dos columnas, de 35 filas cada una, se crea la función ***insertarColumnaDiferencia*** para automatizar esta misma idea.

# In[66]:


def insertarColumnaDiferencia(data):
    n_rows = len(data)
    diferencia = []
    for i in range(0,n_rows):
        aux = data.iloc[i,3]-data.iloc[i,2]
        diferencia.append(aux)

    data.insert(4,"Diferencia valor",diferencia,True) #Permite duplicados
    return None


# La estructuración de los datos, sobre todo para facilitar su comprensión, es, por columnas: 
#    1. Nombre de la empresa.
#    2. Número de acciones que se tiene de esa empresa. 
#    3. Valor de esas acciones en la sesión anterior. 
#    4. Valor de esas acciones en la sesión actual.
#    
# Es por ello que la función ***insertarColumnaDiferencia*** toma las columnas con índices 2 y 3 para calcular la diferencia entre valores.
# Fijado esto, se pasa a calcular el primer ranking, con la primera y la segunda sesión, y así también probar la función definida anteriormente.

# In[67]:


data_pre_ranking_0_inv_ac = [['Acciona', n_stocks_acciona, n_stocks_acciona*df_acciona.iloc[0,1], n_stocks_acciona*df_acciona.iloc[1,1]],
                             ['Acciona Energía', n_stocks_accionaEnergia, n_stocks_accionaEnergia*df_accionaEnergia.iloc[0,1], n_stocks_accionaEnergia*df_accionaEnergia.iloc[1,1]],
                             ['Acerinox', n_stocks_acerinox, n_stocks_acerinox*df_acerinox.iloc[0,1], n_stocks_acerinox*df_acerinox.iloc[1,1]],
                             ['Acs', n_stocks_acs, n_stocks_acs*df_acs.iloc[0,1], n_stocks_acs*df_acs.iloc[1,1]],
                             ['Aena', n_stocks_aena, n_stocks_aena*df_aena.iloc[0,1], n_stocks_aena*df_aena.iloc[1,1]],
                             ['Amadeus', n_stocks_amadeus, n_stocks_amadeus*df_amadeus.iloc[0,1], n_stocks_amadeus*df_amadeus.iloc[1,1]],
                             ['Arcelormittal', n_stocks_arcelormittal, n_stocks_arcelormittal*df_arcelormittal.iloc[0,1], n_stocks_arcelormittal*df_arcelormittal.iloc[1,1]],
                             ['Banco Santander', n_stocks_santander, n_stocks_santander*df_santander.iloc[0,1], n_stocks_santander*df_santander.iloc[1,1]],
                             ['Banco Sabadell', n_stocks_sabadell, n_stocks_sabadell*df_sabadell.iloc[0,1], n_stocks_sabadell*df_sabadell.iloc[1,1]],
                             ['Bankinter', n_stocks_bankinter, n_stocks_bankinter*df_bankinter.iloc[0,1], n_stocks_bankinter*df_bankinter.iloc[1,1]],
                             ['BBVA', n_stocks_bbva, n_stocks_bbva*df_bbva.iloc[0,1], n_stocks_bbva*df_bbva.iloc[1,1]],
                             ['Caixabank', n_stocks_caixabank, n_stocks_caixabank*df_caixabank.iloc[0,1], n_stocks_caixabank*df_caixabank.iloc[1,1]],
                             ['Cellnex', n_stocks_cellnex, n_stocks_cellnex*df_cellnex.iloc[0,1], n_stocks_cellnex*df_cellnex.iloc[1,1]],
                             ['Enagás', n_stocks_enagas, n_stocks_enagas*df_enagas.iloc[0,1], n_stocks_enagas*df_enagas.iloc[1,1]],
                             ['Endesa', n_stocks_endesa, n_stocks_endesa*df_endesa.iloc[0,1], n_stocks_endesa*df_endesa.iloc[1,1]],
                             ['Ferrovial', n_stocks_ferrovial, n_stocks_ferrovial*df_ferrovial.iloc[0,1], n_stocks_ferrovial*df_ferrovial.iloc[1,1]],
                             ['Fluidra', n_stocks_fluidra, n_stocks_fluidra*df_fluidra.iloc[0,1], n_stocks_fluidra*df_fluidra.iloc[1,1]],
                             ['Grifols', n_stocks_grifols, n_stocks_grifols*df_grifols.iloc[0,1], n_stocks_grifols*df_grifols.iloc[1,1]],
                             ['IAG', n_stocks_IAG, n_stocks_IAG*df_IAG.iloc[0,1], n_stocks_IAG*df_IAG.iloc[1,1]],
                             ['Iberdrola', n_stocks_iberdrola, n_stocks_iberdrola*df_iberdrola.iloc[0,1], n_stocks_iberdrola*df_iberdrola.iloc[1,1]],
                             ['Inditex', n_stocks_inditex, n_stocks_inditex*df_inditex.iloc[0,1], n_stocks_inditex*df_inditex.iloc[1,1]],
                             ['Indra', n_stocks_indra, n_stocks_indra*df_indra.iloc[0,1], n_stocks_indra*df_indra.iloc[1,1]],
                             ['Inmobiliaria Colonial', n_stocks_colonial, n_stocks_colonial*df_colonial.iloc[0,1], n_stocks_colonial*df_colonial.iloc[1,1]],
                             ['Mapfre', n_stocks_mapfre, n_stocks_mapfre*df_mapfre.iloc[0,1], n_stocks_mapfre*df_mapfre.iloc[1,1]],
                             ['Meliá Hotels', n_stocks_melia, n_stocks_melia*df_melia.iloc[0,1], n_stocks_melia*df_melia.iloc[1,1]],
                             ['Merlin Properties', n_stocks_merlin, n_stocks_merlin*df_merlin.iloc[0,1], n_stocks_merlin*df_merlin.iloc[1,1]],
                             ['Naturgy', n_stocks_naturgy, n_stocks_naturgy*df_naturgy.iloc[0,1], n_stocks_naturgy*df_naturgy.iloc[1,1]],
                             ['Pharma Mar', n_stocks_pharmaMar, n_stocks_pharmaMar*df_pharmaMar.iloc[0,1], n_stocks_pharmaMar*df_pharmaMar.iloc[1,1]],
                             ['Red Eléctrica', n_stocks_redElectrica, n_stocks_redElectrica*df_redElectrica.iloc[0,1], n_stocks_redElectrica*df_redElectrica.iloc[1,1]],
                             ['Repsol', n_stocks_repsol, n_stocks_repsol*df_repsol.iloc[0,1], n_stocks_repsol*df_repsol.iloc[1,1]],
                             ['Rovi', n_stocks_rovi, n_stocks_rovi*df_rovi.iloc[0,1], n_stocks_rovi*df_rovi.iloc[1,1]],
                             ['Sacyr', n_stocks_sacyr, n_stocks_sacyr*df_sacyr.iloc[0,1], n_stocks_sacyr*df_sacyr.iloc[1,1]],
                             ['Siemens Gamesa', n_stocks_siemens, n_stocks_siemens*df_siemens.iloc[0,1], n_stocks_siemens*df_siemens.iloc[1,1]],
                             ['Solaria', n_stocks_solaria, n_stocks_solaria*df_solaria.iloc[0,1], n_stocks_solaria*df_solaria.iloc[1,1]],
                             ['Telefónica', n_stocks_telefonica, n_stocks_telefonica*df_telefonica.iloc[0,1], n_stocks_telefonica*df_telefonica.iloc[1,1]]]
df_pre_ranking_0_inv_ac = pd.DataFrame(data_pre_ranking_0_inv_ac,columns=['Nombre', 'Número de acciones', 'Valor sesión anterior','Valor sesión actual'])
insertarColumnaDiferencia(df_pre_ranking_0_inv_ac)
df_pre_ranking_0_inv_ac


# Visto esto, que ayuda a clarificar las ideas, lo que realmente interesa al estudio es captar las columnas con índices 0 y 4 para construir los rankings y ordenarlos. En este caso para construir el primer ranking.

# In[68]:


#Creación del primer ranking y su ordenación
df_ranking_0_inv_ac = df_pre_ranking_0_inv_ac.iloc[:,[0,4]]
ordenarRanking(df_ranking_0_inv_ac)
df_ranking_0_inv_ac


# Así pues, se puede observar que la inversión inicial de 1000 € en Arcelormittal ha sufrido una variación de -86.294416 €, consecuente con lo obtenido en el primer ranking de la primera perspectiva; mientras que, por otro lado, la inversión en Grifols ha aumentado 47.443007 €, de nuevo también en concordancia con la visión anterior.
# 
# Como en la perspectiva primera, se calculan el segundo y el último ranking que, una vez se escale el modelo, permitirán comprobar si este está bien creado.

# In[69]:


#Segundo ranking
data_pre_ranking_1_inv_ac = [['Acciona', n_stocks_acciona, n_stocks_acciona*df_acciona.iloc[1,1], n_stocks_acciona*df_acciona.iloc[2,1]],
                             ['Acciona Energía', n_stocks_accionaEnergia, n_stocks_accionaEnergia*df_accionaEnergia.iloc[1,1], n_stocks_accionaEnergia*df_accionaEnergia.iloc[2,1]],
                             ['Acerinox', n_stocks_acerinox, n_stocks_acerinox*df_acerinox.iloc[1,1], n_stocks_acerinox*df_acerinox.iloc[2,1]],
                             ['Acs', n_stocks_acs, n_stocks_acs*df_acs.iloc[1,1], n_stocks_acs*df_acs.iloc[2,1]],
                             ['Aena', n_stocks_aena, n_stocks_aena*df_aena.iloc[1,1], n_stocks_aena*df_aena.iloc[2,1]],
                             ['Amadeus', n_stocks_amadeus, n_stocks_amadeus*df_amadeus.iloc[1,1], n_stocks_amadeus*df_amadeus.iloc[2,1]],
                             ['Arcelormittal', n_stocks_arcelormittal, n_stocks_arcelormittal*df_arcelormittal.iloc[1,1], n_stocks_arcelormittal*df_arcelormittal.iloc[2,1]],
                             ['Banco Santander', n_stocks_santander, n_stocks_santander*df_santander.iloc[1,1], n_stocks_santander*df_santander.iloc[2,1]],
                             ['Banco Sabadell', n_stocks_sabadell, n_stocks_sabadell*df_sabadell.iloc[1,1], n_stocks_sabadell*df_sabadell.iloc[2,1]],
                             ['Bankinter', n_stocks_bankinter, n_stocks_bankinter*df_bankinter.iloc[1,1], n_stocks_bankinter*df_bankinter.iloc[2,1]],
                             ['BBVA', n_stocks_bbva, n_stocks_bbva*df_bbva.iloc[1,1], n_stocks_bbva*df_bbva.iloc[2,1]],
                             ['Caixabank', n_stocks_caixabank, n_stocks_caixabank*df_caixabank.iloc[1,1], n_stocks_caixabank*df_caixabank.iloc[2,1]],
                             ['Cellnex', n_stocks_cellnex, n_stocks_cellnex*df_cellnex.iloc[1,1], n_stocks_cellnex*df_cellnex.iloc[2,1]],
                             ['Enagás', n_stocks_enagas, n_stocks_enagas*df_enagas.iloc[1,1], n_stocks_enagas*df_enagas.iloc[2,1]],
                             ['Endesa', n_stocks_endesa, n_stocks_endesa*df_endesa.iloc[1,1], n_stocks_endesa*df_endesa.iloc[2,1]],
                             ['Ferrovial', n_stocks_ferrovial, n_stocks_ferrovial*df_ferrovial.iloc[1,1], n_stocks_ferrovial*df_ferrovial.iloc[2,1]],
                             ['Fluidra', n_stocks_fluidra, n_stocks_fluidra*df_fluidra.iloc[1,1], n_stocks_fluidra*df_fluidra.iloc[2,1]],
                             ['Grifols', n_stocks_grifols, n_stocks_grifols*df_grifols.iloc[1,1], n_stocks_grifols*df_grifols.iloc[2,1]],
                             ['IAG', n_stocks_IAG, n_stocks_IAG*df_IAG.iloc[1,1], n_stocks_IAG*df_IAG.iloc[2,1]],
                             ['Iberdrola', n_stocks_iberdrola, n_stocks_iberdrola*df_iberdrola.iloc[1,1], n_stocks_iberdrola*df_iberdrola.iloc[2,1]],
                             ['Inditex', n_stocks_inditex, n_stocks_inditex*df_inditex.iloc[1,1], n_stocks_inditex*df_inditex.iloc[2,1]],
                             ['Indra', n_stocks_indra, n_stocks_indra*df_indra.iloc[1,1], n_stocks_indra*df_indra.iloc[2,1]],
                             ['Inmobiliaria Colonial', n_stocks_colonial, n_stocks_colonial*df_colonial.iloc[1,1], n_stocks_colonial*df_colonial.iloc[2,1]],
                             ['Mapfre', n_stocks_mapfre, n_stocks_mapfre*df_mapfre.iloc[1,1], n_stocks_mapfre*df_mapfre.iloc[2,1]],
                             ['Meliá Hotels', n_stocks_melia, n_stocks_melia*df_melia.iloc[1,1], n_stocks_melia*df_melia.iloc[2,1]],
                             ['Merlin Properties', n_stocks_merlin, n_stocks_merlin*df_merlin.iloc[1,1], n_stocks_merlin*df_merlin.iloc[2,1]],
                             ['Naturgy', n_stocks_naturgy, n_stocks_naturgy*df_naturgy.iloc[1,1], n_stocks_naturgy*df_naturgy.iloc[2,1]],
                             ['Pharma Mar', n_stocks_pharmaMar, n_stocks_pharmaMar*df_pharmaMar.iloc[1,1], n_stocks_pharmaMar*df_pharmaMar.iloc[2,1]],
                             ['Red Eléctrica', n_stocks_redElectrica, n_stocks_redElectrica*df_redElectrica.iloc[1,1], n_stocks_redElectrica*df_redElectrica.iloc[2,1]],
                             ['Repsol', n_stocks_repsol, n_stocks_repsol*df_repsol.iloc[1,1], n_stocks_repsol*df_repsol.iloc[2,1]],
                             ['Rovi', n_stocks_rovi, n_stocks_rovi*df_rovi.iloc[1,1], n_stocks_rovi*df_rovi.iloc[2,1]],
                             ['Sacyr', n_stocks_sacyr, n_stocks_sacyr*df_sacyr.iloc[1,1], n_stocks_sacyr*df_sacyr.iloc[2,1]],
                             ['Siemens Gamesa', n_stocks_siemens, n_stocks_siemens*df_siemens.iloc[1,1], n_stocks_siemens*df_siemens.iloc[2,1]],
                             ['Solaria', n_stocks_solaria, n_stocks_solaria*df_solaria.iloc[1,1], n_stocks_solaria*df_solaria.iloc[2,1]],
                             ['Telefónica', n_stocks_telefonica, n_stocks_telefonica*df_telefonica.iloc[1,1], n_stocks_telefonica*df_telefonica.iloc[2,1]]]
df_pre_ranking_1_inv_ac = pd.DataFrame(data_pre_ranking_1_inv_ac,columns=['Nombre', 'Número de acciones', 'Valor sesión anterior','Valor sesión actual'])
insertarColumnaDiferencia(df_pre_ranking_1_inv_ac)
df_ranking_1_inv_ac = df_pre_ranking_1_inv_ac.iloc[:,[0,4]]
ordenarRanking(df_ranking_1_inv_ac)
df_ranking_1_inv_ac


# In[70]:


# Último ranking
data_pre_ranking_129_inv_ac = [['Acciona', n_stocks_acciona, n_stocks_acciona*df_acciona.iloc[129,1], n_stocks_acciona*df_acciona.iloc[130,1]],
                               ['Acciona Energía', n_stocks_accionaEnergia, n_stocks_accionaEnergia*df_accionaEnergia.iloc[129,1], n_stocks_accionaEnergia*df_accionaEnergia.iloc[130,1]],
                               ['Acerinox', n_stocks_acerinox, n_stocks_acerinox*df_acerinox.iloc[129,1], n_stocks_acerinox*df_acerinox.iloc[130,1]],
                               ['Acs', n_stocks_acs, n_stocks_acs*df_acs.iloc[129,1], n_stocks_acs*df_acs.iloc[130,1]],
                               ['Aena', n_stocks_aena, n_stocks_aena*df_aena.iloc[129,1], n_stocks_aena*df_aena.iloc[130,1]],
                               ['Amadeus', n_stocks_amadeus, n_stocks_amadeus*df_amadeus.iloc[129,1], n_stocks_amadeus*df_amadeus.iloc[130,1]],
                               ['Arcelormittal', n_stocks_arcelormittal, n_stocks_arcelormittal*df_arcelormittal.iloc[129,1], n_stocks_arcelormittal*df_arcelormittal.iloc[130,1]],
                               ['Banco Santander', n_stocks_santander, n_stocks_santander*df_santander.iloc[129,1], n_stocks_santander*df_santander.iloc[130,1]],
                               ['Banco Sabadell', n_stocks_sabadell, n_stocks_sabadell*df_sabadell.iloc[129,1], n_stocks_sabadell*df_sabadell.iloc[130,1]],
                               ['Bankinter', n_stocks_bankinter, n_stocks_bankinter*df_bankinter.iloc[129,1], n_stocks_bankinter*df_bankinter.iloc[130,1]],
                               ['BBVA', n_stocks_bbva, n_stocks_bbva*df_bbva.iloc[129,1], n_stocks_bbva*df_bbva.iloc[130,1]],
                               ['Caixabank', n_stocks_caixabank, n_stocks_caixabank*df_caixabank.iloc[129,1], n_stocks_caixabank*df_caixabank.iloc[130,1]],
                               ['Cellnex', n_stocks_cellnex, n_stocks_cellnex*df_cellnex.iloc[129,1], n_stocks_cellnex*df_cellnex.iloc[130,1]],
                               ['Enagás', n_stocks_enagas, n_stocks_enagas*df_enagas.iloc[129,1], n_stocks_enagas*df_enagas.iloc[130,1]],
                               ['Endesa', n_stocks_endesa, n_stocks_endesa*df_endesa.iloc[129,1], n_stocks_endesa*df_endesa.iloc[130,1]],
                               ['Ferrovial', n_stocks_ferrovial, n_stocks_ferrovial*df_ferrovial.iloc[129,1], n_stocks_ferrovial*df_ferrovial.iloc[130,1]],
                               ['Fluidra', n_stocks_fluidra, n_stocks_fluidra*df_fluidra.iloc[129,1], n_stocks_fluidra*df_fluidra.iloc[130,1]],
                               ['Grifols', n_stocks_grifols, n_stocks_grifols*df_grifols.iloc[129,1], n_stocks_grifols*df_grifols.iloc[130,1]],
                               ['IAG', n_stocks_IAG, n_stocks_IAG*df_IAG.iloc[129,1], n_stocks_IAG*df_IAG.iloc[130,1]],
                               ['Iberdrola', n_stocks_iberdrola, n_stocks_iberdrola*df_iberdrola.iloc[129,1], n_stocks_iberdrola*df_iberdrola.iloc[130,1]],
                               ['Inditex', n_stocks_inditex, n_stocks_inditex*df_inditex.iloc[129,1], n_stocks_inditex*df_inditex.iloc[130,1]],
                               ['Indra', n_stocks_indra, n_stocks_indra*df_indra.iloc[129,1], n_stocks_indra*df_indra.iloc[130,1]],
                               ['Inmobiliaria Colonial', n_stocks_colonial, n_stocks_colonial*df_colonial.iloc[129,1], n_stocks_colonial*df_colonial.iloc[130,1]],
                               ['Mapfre', n_stocks_mapfre, n_stocks_mapfre*df_mapfre.iloc[129,1], n_stocks_mapfre*df_mapfre.iloc[130,1]],
                               ['Meliá Hotels', n_stocks_melia, n_stocks_melia*df_melia.iloc[129,1], n_stocks_melia*df_melia.iloc[130,1]],
                               ['Merlin Properties', n_stocks_merlin, n_stocks_merlin*df_merlin.iloc[129,1], n_stocks_merlin*df_merlin.iloc[130,1]],
                               ['Naturgy', n_stocks_naturgy, n_stocks_naturgy*df_naturgy.iloc[129,1], n_stocks_naturgy*df_naturgy.iloc[130,1]],
                               ['Pharma Mar', n_stocks_pharmaMar, n_stocks_pharmaMar*df_pharmaMar.iloc[129,1], n_stocks_pharmaMar*df_pharmaMar.iloc[130,1]],
                               ['Red Eléctrica', n_stocks_redElectrica, n_stocks_redElectrica*df_redElectrica.iloc[129,1], n_stocks_redElectrica*df_redElectrica.iloc[130,1]],
                               ['Repsol', n_stocks_repsol, n_stocks_repsol*df_repsol.iloc[129,1], n_stocks_repsol*df_repsol.iloc[130,1]],
                               ['Rovi', n_stocks_rovi, n_stocks_rovi*df_rovi.iloc[129,1], n_stocks_rovi*df_rovi.iloc[130,1]],
                               ['Sacyr', n_stocks_sacyr, n_stocks_sacyr*df_sacyr.iloc[129,1], n_stocks_sacyr*df_sacyr.iloc[130,1]],
                               ['Siemens Gamesa', n_stocks_siemens, n_stocks_siemens*df_siemens.iloc[129,1], n_stocks_siemens*df_siemens.iloc[130,1]],
                               ['Solaria', n_stocks_solaria, n_stocks_solaria*df_solaria.iloc[129,1], n_stocks_solaria*df_solaria.iloc[130,1]],
                               ['Telefónica', n_stocks_telefonica, n_stocks_telefonica*df_telefonica.iloc[129,1], n_stocks_telefonica*df_telefonica.iloc[130,1]]]
df_pre_ranking_129_inv_ac = pd.DataFrame(data_pre_ranking_129_inv_ac,columns=['Nombre', 'Número de acciones', 'Valor sesión anterior','Valor sesión actual'])
insertarColumnaDiferencia(df_pre_ranking_129_inv_ac)
df_ranking_129_inv_ac = df_pre_ranking_129_inv_ac.iloc[:,[0,4]]
ordenarRanking(df_ranking_129_inv_ac)
df_ranking_129_inv_ac


# Una vez desarrollados algunos rankings, es momento de escalar el modelo. Para ello, la información de los rankings se registra igual que en la primera perspectiva, es decir, una matriz donde cada columna es una lista de nombres de las empresas asociados a un ranking ya ordenado. De nuevo, las dimensiones de la matriz son 35 filas, una por cada empresa, y 130 rankings.

# In[71]:


########################################### Escalabilidad del modelo ###########################################
#Creación de un Data Frame con tantas filas como empresas y tantas columnas como rankings 
df_rankings_inv_ac = pd.DataFrame(columns=rankings,index=classification)

#Bucle
for i in range(1,n_sesions):
    data_aux_inv_ac = [['Acciona', n_stocks_acciona, n_stocks_acciona*df_acciona.iloc[i-1,1], n_stocks_acciona*df_acciona.iloc[i,1]],
                       ['Acciona Energía', n_stocks_accionaEnergia, n_stocks_accionaEnergia*df_accionaEnergia.iloc[i-1,1], n_stocks_accionaEnergia*df_accionaEnergia.iloc[i,1]],
                       ['Acerinox', n_stocks_acerinox, n_stocks_acerinox*df_acerinox.iloc[i-1,1], n_stocks_acerinox*df_acerinox.iloc[i,1]],
                       ['Acs', n_stocks_acs, n_stocks_acs*df_acs.iloc[i-1,1], n_stocks_acs*df_acs.iloc[i,1]],
                       ['Aena', n_stocks_aena, n_stocks_aena*df_aena.iloc[i-1,1], n_stocks_aena*df_aena.iloc[i,1]],
                       ['Amadeus', n_stocks_amadeus, n_stocks_amadeus*df_amadeus.iloc[i-1,1], n_stocks_amadeus*df_amadeus.iloc[i,1]],
                       ['Arcelormittal', n_stocks_arcelormittal, n_stocks_arcelormittal*df_arcelormittal.iloc[i-1,1], n_stocks_arcelormittal*df_arcelormittal.iloc[i,1]],
                       ['Banco Santander', n_stocks_santander, n_stocks_santander*df_santander.iloc[i-1,1], n_stocks_santander*df_santander.iloc[i,1]],
                       ['Banco Sabadell', n_stocks_sabadell, n_stocks_sabadell*df_sabadell.iloc[i-1,1], n_stocks_sabadell*df_sabadell.iloc[i,1]],
                       ['Bankinter', n_stocks_bankinter, n_stocks_bankinter*df_bankinter.iloc[i-1,1], n_stocks_bankinter*df_bankinter.iloc[i,1]],
                       ['BBVA', n_stocks_bbva, n_stocks_bbva*df_bbva.iloc[i-1,1], n_stocks_bbva*df_bbva.iloc[i,1]],
                       ['Caixabank', n_stocks_caixabank, n_stocks_caixabank*df_caixabank.iloc[i-1,1], n_stocks_caixabank*df_caixabank.iloc[i,1]],
                       ['Cellnex', n_stocks_cellnex, n_stocks_cellnex*df_cellnex.iloc[i-1,1], n_stocks_cellnex*df_cellnex.iloc[i,1]],
                       ['Enagás', n_stocks_enagas, n_stocks_enagas*df_enagas.iloc[i-1,1], n_stocks_enagas*df_enagas.iloc[i,1]],
                       ['Endesa', n_stocks_endesa, n_stocks_endesa*df_endesa.iloc[i-1,1], n_stocks_endesa*df_endesa.iloc[i,1]],
                       ['Ferrovial', n_stocks_ferrovial, n_stocks_ferrovial*df_ferrovial.iloc[i-1,1], n_stocks_ferrovial*df_ferrovial.iloc[i,1]],
                       ['Fluidra', n_stocks_fluidra, n_stocks_fluidra*df_fluidra.iloc[i-1,1], n_stocks_fluidra*df_fluidra.iloc[i,1]],
                       ['Grifols', n_stocks_grifols, n_stocks_grifols*df_grifols.iloc[i-1,1], n_stocks_grifols*df_grifols.iloc[i,1]],
                       ['IAG', n_stocks_IAG, n_stocks_IAG*df_IAG.iloc[i-1,1], n_stocks_IAG*df_IAG.iloc[i,1]],
                       ['Iberdrola', n_stocks_iberdrola, n_stocks_iberdrola*df_iberdrola.iloc[i-1,1], n_stocks_iberdrola*df_iberdrola.iloc[i,1]],
                       ['Inditex', n_stocks_inditex, n_stocks_inditex*df_inditex.iloc[i-1,1], n_stocks_inditex*df_inditex.iloc[i,1]],
                       ['Indra', n_stocks_indra, n_stocks_indra*df_indra.iloc[i-1,1], n_stocks_indra*df_indra.iloc[i,1]],
                       ['Inmobiliaria Colonial', n_stocks_colonial, n_stocks_colonial*df_colonial.iloc[i-1,1], n_stocks_colonial*df_colonial.iloc[i,1]],
                       ['Mapfre', n_stocks_mapfre, n_stocks_mapfre*df_mapfre.iloc[i-1,1], n_stocks_mapfre*df_mapfre.iloc[i,1]],
                       ['Meliá Hotels', n_stocks_melia, n_stocks_melia*df_melia.iloc[i-1,1], n_stocks_melia*df_melia.iloc[i,1]],
                       ['Merlin Properties', n_stocks_merlin, n_stocks_merlin*df_merlin.iloc[i-1,1], n_stocks_merlin*df_merlin.iloc[i,1]],
                       ['Naturgy', n_stocks_naturgy, n_stocks_naturgy*df_naturgy.iloc[i-1,1], n_stocks_naturgy*df_naturgy.iloc[i,1]],
                       ['Pharma Mar', n_stocks_pharmaMar, n_stocks_pharmaMar*df_pharmaMar.iloc[i-1,1], n_stocks_pharmaMar*df_pharmaMar.iloc[i,1]],
                       ['Red Eléctrica', n_stocks_redElectrica, n_stocks_redElectrica*df_redElectrica.iloc[i-1,1], n_stocks_redElectrica*df_redElectrica.iloc[i,1]],
                       ['Repsol', n_stocks_repsol, n_stocks_repsol*df_repsol.iloc[i-1,1], n_stocks_repsol*df_repsol.iloc[i,1]],
                       ['Rovi', n_stocks_rovi, n_stocks_rovi*df_rovi.iloc[i-1,1], n_stocks_rovi*df_rovi.iloc[i,1]],
                       ['Sacyr', n_stocks_sacyr, n_stocks_sacyr*df_sacyr.iloc[i-1,1], n_stocks_sacyr*df_sacyr.iloc[i,1]],
                       ['Siemens Gamesa', n_stocks_siemens, n_stocks_siemens*df_siemens.iloc[i-1,1], n_stocks_siemens*df_siemens.iloc[i,1]],
                       ['Solaria', n_stocks_solaria, n_stocks_solaria*df_solaria.iloc[i-1,1], n_stocks_solaria*df_solaria.iloc[i,1]],
                       ['Telefónica', n_stocks_telefonica, n_stocks_telefonica*df_telefonica.iloc[i-1,1], n_stocks_telefonica*df_telefonica.iloc[i,1]]]
    df_pre_aux_inv_ac = pd.DataFrame(data_aux_inv_ac,columns=['Nombre', 'Número de acciones', 'Valor sesión anterior','Valor sesión actual'])
    insertarColumnaDiferencia(df_pre_aux_inv_ac)
    df_aux_inv_ac=df_pre_aux_inv_ac.iloc[:,[0,4]]
    ordenarRanking(df_aux_inv_ac)
    df_rankings_inv_ac.iloc[:,i-1]=df_aux_inv_ac.iloc[:,0]
df_rankings_inv_ac


# Con este dataFrame de información creado y los tres rankings desarrollados como ejemplos, se hace la misma prueba que para la primera sección, con el fin de asegurarse que está bien escalado el modelo.

# In[72]:


flag0_inv_ac=True
flag1_inv_ac=True
flag129_inv_ac=True

for i in range(n_stocks):
    flag0_inv_ac = (df_rankings_inv.iloc[i,0]==df_ranking_0_inv.iloc[i,0])

for j in range(n_stocks):
    flag1_inv_ac = (df_rankings_inv.iloc[j,1]==df_ranking_1_inv.iloc[j,0])

for k in range(n_stocks):
    flag129_inv_ac = (df_rankings_inv.iloc[k,129]==df_ranking_129_inv.iloc[k,0])

(flag0_inv_ac,flag1_inv_ac,flag129_inv_ac)


# De nuevo, la construcción es correcta y los rankings se han construido de manera eficaz.
# 
# Con los rankings calculados, es momento de construir la matriz de adyacencia del grafo de competitividad para su posterior representación. Como se hizo anteriormente, hay que recurrir a la función *seCruza* para estudiar por pares de acciones si estas intercambian sus posiciones relativas a lo largo de los pares de rankings consecutivos. La generación de pesos de las aristas es la misma que antes.

# In[73]:


#Definición de la matriz de adyacencia del grafo, donde sus filas y sus columnas son las acciones
adj_matrix_inv_ac = pd.DataFrame(columns=stocks,index=stocks)

#Dicha matriz se rellena de 0's para asegurarse de que posteriormente se puede rellenar de la forma que se desea en el estudio
for i in range(n_stocks):
    for j in range(n_stocks):
        adj_matrix_inv_ac.iloc[i,j]=0

#Iteraciones para completarla con el dataFrame de rankings: Se toma una acción y cada una de sus sucesivas a lo largo
#de todos los rankings, tomados de dos en dos de forma contigua
for k in range(n_sesions-2):
    for i in range(n_stocks):
        for j in range(i+1,n_stocks):
            if (seCruza(df_rankings_inv_ac.iloc[:,k],df_rankings_inv_ac.iloc[:,k+1],stocks[i],stocks[j])):
                adj_matrix_inv_ac.iloc[i,j] = adj_matrix_inv_ac.iloc[i,j]+1
                adj_matrix_inv_ac.iloc[j,i] = adj_matrix_inv_ac.iloc[j,i]+1
adj_matrix_inv_ac


# Con esta matriz de adyacencia del grafo de competitividad, es momento de su representación, de forma totalmente análoga a las representaciones que se han hecho de estos objetos anteriormente, manteniendo en este estudio la disposición de los nodos que mayor interpretación del grafo permiten.

# In[74]:


#Creación del grafo
G_inv_ac = nx.Graph()
G_inv_ac.add_nodes_from(stocks)

for i in range(n_stocks):
    for j in range(i+1,n_stocks):
        if(adj_matrix_inv_ac.iloc[i,j]>0):
            G_inv_ac.add_edge(stocks[i],stocks[j],weight=adj_matrix_inv_ac.iloc[i,j])


# In[75]:


#Primero se genera el tipo de diseño del grafo para que los nodos estén bien diferenciados en la representación
pos_inv_ac = nx.circular_layout(G_inv_ac)

#Para representar las aristas se va a representar el grosor de la misma en proporcion a su peso
edgew_inv_ac = [0.005*G_inv_ac.get_edge_data(u, v)['weight'] for u, v in G_inv_ac.edges()]
#Con la siguiente expresión se consigue establecer el ancho (x) y el alto (y) del espacio donde se va a representar el grafo
x_inv_ac, y_inv_ac = plt.subplots(figsize=(12, 12))
#Título del grafo
y_inv_ac.set_title("Competitivity graph: Perspective 2", dict(fontweight="bold",fontsize=22,color="black"),loc="center")

#Representación de los objetos del grafo
    #Aristas
nx.draw_networkx_edges(G_inv_ac, pos_inv_ac, width=edgew_inv_ac, edge_color="navy", style='-')
    #Nodos
nx.draw_networkx_nodes(G_inv_ac, pos_inv_ac, node_size=700, node_shape='o', node_color="gold", linewidths=1,edgecolors="black")
    #Etiquetas sobre nodos
nx.draw_networkx_labels(G_inv_ac, pos_inv_ac, font_size=11, bbox=dict(ec="black",boxstyle="round",facecolor="white",pad=0.3,alpha=0.6), font_weight='normal', font_family='Verdana', horizontalalignment='center', verticalalignment='center',clip_on=False)

#Modificaciones sobre el espacio de representación para optimizar el resultado
x_inv_ac.tight_layout()
plt.axis("off")
y_inv_ac.margins(0.05,0.05)
plt.savefig("CG2.png")
plt.show()


# A diferencia de la primera perspectiva donde las empresas competían de forma elevada, en este caso compiten aún más. Esto es debido a que los valores empleados para estos rankings están más cohesionados, en el sentido de que sobre el valor de las acciones cuando una empresa subía o bajaba mucho, para alcanzar otra que se hubiese movido en su sentido tenía que escalar bastante. Mientras que en esta casuística, para competir con otra empresa basta con ganar o perder más que la otra en una misma sesión.
# 
# Repetidamente, aparece la necesidad de intentar filtrar las aristas y quedarse con aquellas que sean más representativas en el grafo de competitividad. Para ello, se opera de manera análoga a la primera visión estableciendo los mismo criterios para considerar una arista o no. Hay que recordar que aparecían tres vías.

# #### 3.2.1. Perspectiva 2.1: Bajo una inversión inicial de 1000 €, estudio de la diferencia diaria del total de la inversión al cierre de la sesión para aquellas empresas que se crucen más que la media del total de pesos de las aristas del grafo

# En esta subsección se hace un evolutivo de la segunda perspectiva al mismo modo que se hizo el evolutivo para la primera. Se hace el mismo proceso para obtener la matriz de adyacencia del grafo y se representa el mismo.

# In[76]:


#Copia de la matriz original
adj_matrix_inv_ac_avg = pd.DataFrame.copy(adj_matrix_inv_ac)

#Cálculo de la media de pesos. Para ello, solo se recorre la mitad de la matriz, debido a que la información está duplicada
aux_inv_ac_avg=[]
for i in range(0,n_stocks):
    for j in range(i+1,n_stocks):
        if(adj_matrix_inv_ac_avg.iloc[i,j]>0):
            aux_inv_ac_avg.append(adj_matrix_inv_ac_avg.iloc[i,j])
mean_aux_inv_ac_avg = np.mean(aux_inv_ac_avg)
        
#A continuación, se actualiza la matriz adj_matrix_inv_avg
for i in range(0,n_stocks):
    for j in range(i+1,n_stocks):
        if(adj_matrix_inv_ac_avg.iloc[i,j] < mean_aux_inv_ac_avg):
            adj_matrix_inv_ac_avg.iloc[i,j] = 0
            adj_matrix_inv_ac_avg.iloc[j,i] = 0 
        else:
            adj_matrix_inv_ac_avg.iloc[i,j] = adj_matrix_inv_ac_avg.iloc[i,j] - mean_aux_inv_ac_avg
            adj_matrix_inv_ac_avg.iloc[j,i] = adj_matrix_inv_ac_avg.iloc[j,i] - mean_aux_inv_ac_avg
adj_matrix_inv_ac_avg


# Y con esta matriz de adyacencia se representa el grafo de competitividad para este caso.

# In[77]:


#Creación del grafo
G_inv_ac_avg = nx.Graph()
G_inv_ac_avg.add_nodes_from(stocks)

for i in range(n_stocks):
    for j in range(i+1,n_stocks):
        if(adj_matrix_inv_ac_avg.iloc[i,j]>0):
            G_inv_ac_avg.add_edge(stocks[i],stocks[j],weight=adj_matrix_inv_ac_avg.iloc[i,j])


# In[78]:


#Tipo de diseño del grafo
pos_inv_ac_avg = nx.circular_layout(G_inv_ac_avg)

#Grosor de las aristas
edgew_inv_ac_avg = [0.2*G_inv_ac_avg.get_edge_data(u, v)['weight'] for u, v in G_inv_ac_avg.edges()]
#Espacio  de representación
x_inv_ac_avg, y_inv_ac_avg = plt.subplots(figsize=(12, 12))
#Título del grafo
y_inv_ac_avg.set_title("Competitivity graph: Perspective 2.1", dict(fontweight="bold",fontsize=22,color="black"),loc="center")

#Representación de los objetos del grafo
    #Aristas
nx.draw_networkx_edges(G_inv_ac_avg, pos_inv_ac_avg, width=edgew_inv_ac_avg, edge_color="navy", style='-')
    #Nodos
nx.draw_networkx_nodes(G_inv_ac_avg, pos_inv_ac_avg, node_size=700, node_shape='o', node_color="gold", linewidths=1,edgecolors="black")
    #Etiquetas sobre nodos
nx.draw_networkx_labels(G_inv_ac_avg, pos_inv_ac_avg, font_size=11, bbox=dict(ec="black",boxstyle="round",facecolor="white",pad=0.3,alpha=0.6), font_weight='normal', font_family='Verdana', horizontalalignment='center', verticalalignment='center',clip_on=False)

#Modificaciones sobre el espacio de representación
x_inv_ac_avg.tight_layout()
plt.axis("off")
y_inv_ac_avg.margins(0.05,0.05)
plt.savefig("CG2-1.png")
plt.show()


# Nuevamente, debido a la alta competencia entre las empresas se reduce mucho la extracción de información del grafo. Se pasa al siguiente evolutivo.

# #### 3.2.2. Perspectiva 2.2: Bajo una inversión inicial de 1000 €, estudio de la diferencia diaria del total de la inversión al cierre de la sesión para aquellas empresas que se crucen más que la medida 1 del total de pesos de las aristas del grafo

# Para este caso, el esquema es el mismo que en la anterior subsección pero trabajando con la medida 1 que se construye de forma análoga al apartado 3.1.2.

# In[79]:


#Copia de la matriz original
adj_matrix_inv_ac_ms1 = pd.DataFrame.copy(adj_matrix_inv_ac)

#Cálculo del valor medida 1
measure_1_inv_ac = mean_aux_inv_ac_avg + 0.5*(max(aux_inv_ac_avg)-mean_aux_inv_ac_avg) 

#A continuación, se actualiza la matriz adj_matrix_inv_ms1
for i in range(0,n_stocks):
    for j in range(i+1,n_stocks):
        if(adj_matrix_inv_ac_ms1.iloc[i,j] < measure_1_inv_ac):
            adj_matrix_inv_ac_ms1.iloc[i,j] = 0
            adj_matrix_inv_ac_ms1.iloc[j,i] = 0 
        else:
            adj_matrix_inv_ac_ms1.iloc[i,j] = adj_matrix_inv_ac_ms1.iloc[i,j] - measure_1_inv_ac
            adj_matrix_inv_ac_ms1.iloc[j,i] = adj_matrix_inv_ac_ms1.iloc[j,i] - measure_1_inv_ac
adj_matrix_inv_ac_ms1


# Por último, para cerrar la subsección, dada la anterior matriz de adyacencia del grafo de competitividad, se procede a su representación.

# In[80]:


#Creación del grafo
G_inv_ac_ms1 = nx.Graph()
G_inv_ac_ms1.add_nodes_from(stocks)

for i in range(n_stocks):
    for j in range(i+1,n_stocks):
        if(adj_matrix_inv_ac_ms1.iloc[i,j]>0):
            G_inv_ac_ms1.add_edge(stocks[i],stocks[j],weight=adj_matrix_inv_ac_ms1.iloc[i,j])


# In[81]:


#Tipo de diseño del grafo
pos_inv_ac_ms1 = nx.circular_layout(G_inv_ac_ms1)

#Grosor de las aristas
edgew_inv_ac_ms1 = [0.8*G_inv_ac_ms1.get_edge_data(u, v)['weight'] for u, v in G_inv_ac_ms1.edges()]
#Espacio de representación
x_inv_ac_ms1, y_inv_ac_ms1 = plt.subplots(figsize=(12, 12))
#Título del grafo
y_inv_ac_ms1.set_title("Competitivity graph: Perspective 2.2", dict(fontweight="bold",fontsize=22,color="black"),loc="center")

#Representación de los objetos del grafo
    #Aristas
nx.draw_networkx_edges(G_inv_ac_ms1, pos_inv_ac_ms1, width=edgew_inv_ac_ms1, edge_color="navy", style='-')
    #Nodos
nx.draw_networkx_nodes(G_inv_ac_ms1, pos_inv_ac_ms1, node_size=700, node_shape='o', node_color="gold", linewidths=1,edgecolors="black")
    #Etiquetas sobre nodos
nx.draw_networkx_labels(G_inv_ac_ms1, pos_inv_ac_ms1, font_size=11, bbox=dict(ec="black",boxstyle="round",facecolor="white",pad=0.3,alpha=0.6), font_weight='normal', font_family='Verdana', horizontalalignment='center', verticalalignment='center',clip_on=False)

#Modificaciones sobre el espacio de representación
x_inv_ac_ms1.tight_layout()
plt.axis("off")
y_inv_ac_ms1.margins(0.05,0.05)
plt.savefig("CG2-2.png")
plt.show()


# #### 3.2.3. Perspectiva 2.3: Bajo una inversión inicial de 1000 €, estudio de la diferencia diaria del total de la inversión al cierre de la sesión para aquellas empresas que se crucen más que la medida 2 del total de pesos de las aristas del grafo
# 

# Se procede a ejecutar los bloques de códigos análogos a las anteriores subvariantes pero tomando como límite para considerar las aristas el valor medida 2, cuya construcción es análoga al apartado 3.1.3.
# 
# Seguidamente de la matriz de adyacencia del grafo construido, se realizará su representación asociada.

# In[82]:


#Copia de la matriz original
adj_matrix_inv_ac_ms2 = pd.DataFrame.copy(adj_matrix_inv_ac)

#Cálculo del valor medida 2
measure_2_inv_ac = mean_aux_inv_ac_avg + 0.6*(max(aux_inv_ac_avg)-mean_aux_inv_ac_avg) 

#A continuación, se actualiza la matriz adj_matrix_inv_ac_ms2
for i in range(0,n_stocks):
    for j in range(i+1,n_stocks):
        if(adj_matrix_inv_ac_ms2.iloc[i,j] < measure_2_inv_ac):
            adj_matrix_inv_ac_ms2.iloc[i,j] = 0
            adj_matrix_inv_ac_ms2.iloc[j,i] = 0 
        else:
            adj_matrix_inv_ac_ms2.iloc[i,j] = adj_matrix_inv_ac_ms2.iloc[i,j] - measure_2_inv_ac
            adj_matrix_inv_ac_ms2.iloc[j,i] = adj_matrix_inv_ac_ms2.iloc[j,i] - measure_2_inv_ac
adj_matrix_inv_ac_ms2


# In[83]:


#Creación del grafo
G_inv_ac_ms2 = nx.Graph()
G_inv_ac_ms2.add_nodes_from(stocks)

for i in range(n_stocks):
    for j in range(i+1,n_stocks):
        if(adj_matrix_inv_ac_ms2.iloc[i,j]>0):
            G_inv_ac_ms2.add_edge(stocks[i],stocks[j],weight=adj_matrix_inv_ac_ms2.iloc[i,j])


# In[84]:


#Tipo de diseño del grafo
pos_inv_ac_ms2 = nx.circular_layout(G_inv_ac_ms2)

#Grosor de las aristas
edgew_inv_ac_ms2 = [2*G_inv_ac_ms2.get_edge_data(u, v)['weight'] for u, v in G_inv_ac_ms2.edges()]
#Espacio de representación
x_inv_ac_ms2, y_inv_ac_ms2 = plt.subplots(figsize=(12, 12))
#Título del grafo
y_inv_ac_ms2.set_title("Competitivity graph: Perspective 2.3", dict(fontweight="bold",fontsize=22,color="black"),loc="center")

#Representación de los objetos del grafo
    #Aristas
nx.draw_networkx_edges(G_inv_ac_ms2, pos_inv_ac_ms2, width=edgew_inv_ac_ms2, edge_color="navy", style='-')
    #Nodos
nx.draw_networkx_nodes(G_inv_ac_ms2, pos_inv_ac_ms2, node_size=700, node_shape='o', node_color="gold", linewidths=1,edgecolors="black")
    #Etiquetas sobre nodos
nx.draw_networkx_labels(G_inv_ac_ms2, pos_inv_ac_ms2, font_size=11, bbox=dict(ec="black",boxstyle="round",facecolor="white",pad=0.3,alpha=0.6), font_weight='normal', font_family='Verdana', horizontalalignment='center', verticalalignment='center',clip_on=False)

#Modificaciones sobre el espacio de representación
x_inv_ac_ms2.tight_layout()
plt.axis("off") 
y_inv_ac_ms2.margins(0.05,0.05)
plt.savefig("CG2-3.png")
plt.show() 


# Con la obtención de este grafo, se han conservado aquellas aristas con mayor peso en el grafo. Aunque  la anterior subvariante sí permitía un estudio del problema, este ha aligerado el volumen de aristas y, a diferencia de la perspectiva 1 donde apenas se mejoraba la situación con esta subvariante, aquí sí que se ha obtenido un grafo de competitividad con mejor situación que el de la subvariante 2.2.

# ### 3.3. Perspectiva 3: Estudio mediante el cálculo de la variación porcentual en el precio de cierre de la sesión de cada acción respecto de la sesión anterior

# Vistas las dos perspectivas anteriores es momento de explicar la tercera. Esta no está tan relacionada como lo estaban las dos primeras entre ellas, si no que todos los cálculos necesarios se van a implementar en esta sección.
# 
# Para su desarrollo hay que clarificar cuál es el fin de la misma. En este apartado se busca enfocar el estudio a través de la diferencia porcentual que hay en el precio de cierre de cada acción a lo largo de las sesiones registradas, siempre tomando dicha diferencia a partir de dos sesiones contiguas. Con ello, cada empresa tendrá asociado un valor porcentual que permitirá crear rankings con sus posteriores ordenaciones. De forma análoga a lo ya visto en este estudio, dichos rankings llevarán asociados una matriz de adyacencia que permitirá la representación del grafo de competitividad asociado.
# 
# Previamente a la visualización de la generación de un ranking para esta sección, hay que definir la función ***insertarColumnaVariacion*** cuya finalidad es insertar una columna en cada uno de los dataDrame de información de cada empresa con la variación porcentual de una sesión respecto de la sesión anterior.

# In[85]:


def insertarColumnaVariacion(data):
    n_sesions = len(data)
    variacion = [0]
    for i in range(1,n_sesions):
        aux = ((data.iloc[i,1]-data.iloc[i-1,1])*100/data.iloc[i-1,1])
        variacion.append(round(aux,4))

    data.insert(9,"% Variacion cierre sesion",variacion,True)
    return None


# Creada esta función, se emplea sobre todas los dataFrame de las empresas que se tienen en el estudio.

# In[86]:


insertarColumnaVariacion(df_acciona)
insertarColumnaVariacion(df_accionaEnergia)
insertarColumnaVariacion(df_acerinox)
insertarColumnaVariacion(df_acs)
insertarColumnaVariacion(df_aena)
insertarColumnaVariacion(df_amadeus)
insertarColumnaVariacion(df_arcelormittal)
insertarColumnaVariacion(df_bankinter)
insertarColumnaVariacion(df_bbva)
insertarColumnaVariacion(df_caixabank)
insertarColumnaVariacion(df_cellnex)
insertarColumnaVariacion(df_colonial)
insertarColumnaVariacion(df_enagas)
insertarColumnaVariacion(df_endesa)
insertarColumnaVariacion(df_ferrovial)
insertarColumnaVariacion(df_fluidra)
insertarColumnaVariacion(df_grifols)
insertarColumnaVariacion(df_IAG)
insertarColumnaVariacion(df_iberdrola)
insertarColumnaVariacion(df_inditex)
insertarColumnaVariacion(df_indra)
insertarColumnaVariacion(df_mapfre)
insertarColumnaVariacion(df_melia)
insertarColumnaVariacion(df_merlin)
insertarColumnaVariacion(df_naturgy)
insertarColumnaVariacion(df_pharmaMar)
insertarColumnaVariacion(df_redElectrica)
insertarColumnaVariacion(df_repsol)
insertarColumnaVariacion(df_rovi)
insertarColumnaVariacion(df_sabadell)
insertarColumnaVariacion(df_sacyr)
insertarColumnaVariacion(df_santander)
insertarColumnaVariacion(df_siemens)
insertarColumnaVariacion(df_solaria)
insertarColumnaVariacion(df_telefonica)


# Visualmente, se tiene lo siguiente, por ejemplo para la información de Acciona.

# In[87]:


df_acciona


# Como se comentaba, se ha añadido una última columna donde se recoge el crecimiento o decrecimiento porcentual entre las diferentes sesiones consecutivas.
# 
# En estos momentos, se construye la siguiente tabla, correspondiente a la creación del primer ranking que ayuda a clarificar la idea de este apartado.

# In[88]:


data_table_example_per = [['Acciona',df_acciona.iloc[0,1],df_acciona.iloc[1,1],df_acciona['% Variacion cierre sesion'][1]], 
                          ['Acciona Energía',df_accionaEnergia.iloc[0,1],df_accionaEnergia.iloc[1,1],df_accionaEnergia['% Variacion cierre sesion'][1]],
                          ['Acerinox',df_acerinox.iloc[0,1],df_acerinox.iloc[1,1],df_acerinox['% Variacion cierre sesion'][1]],
                          ['Acs',df_acs.iloc[0,1],df_acs.iloc[1,1],df_acs['% Variacion cierre sesion'][1]],
                          ['Aena',df_aena.iloc[0,1],df_aena.iloc[1,1],df_aena['% Variacion cierre sesion'][1]],
                          ['Amadeus',df_amadeus.iloc[0,1],df_amadeus.iloc[1,1],df_amadeus['% Variacion cierre sesion'][1]],
                          ['Arcelormittal',df_arcelormittal.iloc[0,1],df_arcelormittal.iloc[1,1],df_arcelormittal['% Variacion cierre sesion'][1]],
                          ['Banco Santander',df_santander.iloc[0,1],df_santander.iloc[1,1],df_santander['% Variacion cierre sesion'][1]],
                          ['Banco Sabadell',df_sabadell.iloc[0,1],df_sabadell.iloc[1,1],df_sabadell['% Variacion cierre sesion'][1]],
                          ['Bankinter',df_bankinter.iloc[0,1],df_bankinter.iloc[1,1],df_bankinter['% Variacion cierre sesion'][1]],
                          ['BBVA',df_bbva.iloc[0,1],df_bbva.iloc[1,1],df_bbva['% Variacion cierre sesion'][1]],
                          ['Caixabank',df_caixabank.iloc[0,1],df_caixabank.iloc[1,1],df_caixabank['% Variacion cierre sesion'][1]],
                          ['Cellnex',df_cellnex.iloc[0,1],df_cellnex.iloc[1,1],df_cellnex['% Variacion cierre sesion'][1]],
                          ['Enagás',df_enagas.iloc[0,1],df_enagas.iloc[1,1],df_enagas['% Variacion cierre sesion'][1]],
                          ['Endesa',df_endesa.iloc[0,1],df_endesa.iloc[1,1],df_endesa['% Variacion cierre sesion'][1]],
                          ['Ferrovial',df_ferrovial.iloc[0,1],df_ferrovial.iloc[1,1],df_ferrovial['% Variacion cierre sesion'][1]],
                          ['Fluidra',df_fluidra.iloc[0,1],df_fluidra.iloc[1,1],df_fluidra['% Variacion cierre sesion'][1]],
                          ['Grifols',df_grifols.iloc[0,1],df_grifols.iloc[1,1],df_grifols['% Variacion cierre sesion'][1]],
                          ['IAG',df_IAG.iloc[0,1],df_IAG.iloc[1,1],df_IAG['% Variacion cierre sesion'][1]],
                          ['Iberdrola',df_iberdrola.iloc[0,1],df_iberdrola.iloc[1,1],df_iberdrola['% Variacion cierre sesion'][1]],
                          ['Inditex',df_inditex.iloc[0,1],df_inditex.iloc[1,1],df_inditex['% Variacion cierre sesion'][1]],
                          ['Indra',df_indra.iloc[0,1],df_indra.iloc[1,1],df_indra['% Variacion cierre sesion'][1]],
                          ['Inmobiliaria Colonial',df_colonial.iloc[0,1],df_colonial.iloc[1,1],df_colonial['% Variacion cierre sesion'][1]],
                          ['Mapfre',df_mapfre.iloc[0,1],df_mapfre.iloc[1,1],df_mapfre['% Variacion cierre sesion'][1]],
                          ['Meliá Hotels',df_melia.iloc[0,1],df_melia.iloc[1,1],df_melia['% Variacion cierre sesion'][1]],
                          ['Merlin Properties',df_merlin.iloc[0,1],df_merlin.iloc[1,1],df_merlin['% Variacion cierre sesion'][1]],
                          ['Naturgy',df_naturgy.iloc[0,1],df_naturgy.iloc[1,1],df_naturgy['% Variacion cierre sesion'][1]],
                          ['Pharma Mar',df_pharmaMar.iloc[0,1],df_pharmaMar.iloc[1,1],df_pharmaMar['% Variacion cierre sesion'][1]],
                          ['Red Eléctrica',df_redElectrica.iloc[0,1],df_redElectrica.iloc[1,1],df_redElectrica['% Variacion cierre sesion'][1]],
                          ['Repsol',df_repsol.iloc[0,1],df_repsol.iloc[1,1],df_repsol['% Variacion cierre sesion'][1]],
                          ['Rovi',df_rovi.iloc[0,1],df_rovi.iloc[1,1],df_rovi['% Variacion cierre sesion'][1]],
                          ['Sacyr',df_sacyr.iloc[0,1],df_sacyr.iloc[1,1],df_sacyr['% Variacion cierre sesion'][1]],
                          ['Siemens Gamesa',df_siemens.iloc[0,1],df_siemens.iloc[1,1],df_siemens['% Variacion cierre sesion'][1]],
                          ['Solaria',df_solaria.iloc[0,1],df_solaria.iloc[1,1],df_solaria['% Variacion cierre sesion'][1]],
                          ['Telefónica',df_telefonica.iloc[0,1],df_telefonica.iloc[1,1],df_telefonica['% Variacion cierre sesion'][1]]]
df_table_example_per = pd.DataFrame(data_table_example_per,columns=['Nombre','Sesión anterior','Sesión actual','% Variacion cierre sesión'])
df_table_example_per


# La idea que se plantea es la reflejada en la tabla anterior. En ella, tomando como ejemplo Indra, se observa que en la primera sesión registrada, la columna *Sesión anterior*, su precio de cierre fue 9.25 €, mientras que en la sesión segunda, la siguiente, en la columna *Sesión actual*, su precio de cierre fue 9.2 €. Con estos precios, se tiene que la diferencia porcentual fue de -0.5404%, con signo negativo en consecuencia a su bajada de precio. Esto mismo se podría extrapolar para todas las acciones y para todas las sesiones y con ellos construir los rankings para esta perspectiva.
# 
# Para el primer ranking, habría que tomar la primera columna y la última, manteniendo la estructura de rankings con la que se viene trabajando a lo largo del estudio: primera columna, nombre de la empresa, y segunda, valor para la creación del ranking. Con ello, se pasa a la construcción y ordenación del primer ranking.

# In[89]:


df_ranking_0_per = df_table_example_per.iloc[:,[0,3]]
ordenarRanking(df_ranking_0_per)
df_ranking_0_per


# La idea para el ranking es la que se viene trabajando, ordenando de mayor a menor por el porcentaje de variación en el precio de cierre de sesión.
# 
# Como se hizo en las perspectivas anteriores, se crean los segundo y último ranking para cuando se escale el modelo comprobar que es correcto.

# In[90]:


#Segundo ranking
data_ranking_1_per = [['Acciona',df_acciona['% Variacion cierre sesion'][2]], 
                      ['Acciona Energía',df_accionaEnergia['% Variacion cierre sesion'][2]],
                      ['Acerinox',df_acerinox['% Variacion cierre sesion'][2]],
                      ['Acs',df_acs['% Variacion cierre sesion'][2]],
                      ['Aena',df_aena['% Variacion cierre sesion'][2]],
                      ['Amadeus',df_amadeus['% Variacion cierre sesion'][2]],
                      ['Arcelormittal',df_arcelormittal['% Variacion cierre sesion'][2]],
                      ['Banco Santander',df_santander['% Variacion cierre sesion'][2]],
                      ['Banco Sabadell',df_sabadell['% Variacion cierre sesion'][2]],
                      ['Bankinter',df_bankinter['% Variacion cierre sesion'][2]],
                      ['BBVA',df_bbva['% Variacion cierre sesion'][2]],
                      ['Caixabank',df_caixabank['% Variacion cierre sesion'][2]],
                      ['Cellnex',df_cellnex['% Variacion cierre sesion'][2]],
                      ['Enagás',df_enagas['% Variacion cierre sesion'][2]],
                      ['Endesa',df_endesa['% Variacion cierre sesion'][2]],
                      ['Ferrovial',df_ferrovial['% Variacion cierre sesion'][2]],
                      ['Fluidra',df_fluidra['% Variacion cierre sesion'][2]],
                      ['Grifols',df_grifols['% Variacion cierre sesion'][2]],
                      ['IAG',df_IAG['% Variacion cierre sesion'][2]],
                      ['Iberdrola',df_iberdrola['% Variacion cierre sesion'][2]],
                      ['Inditex',df_inditex['% Variacion cierre sesion'][2]],
                      ['Indra',df_indra['% Variacion cierre sesion'][2]],
                      ['Inmobiliaria Colonial',df_colonial['% Variacion cierre sesion'][2]],
                      ['Mapfre',df_mapfre['% Variacion cierre sesion'][2]],
                      ['Meliá Hotels',df_melia['% Variacion cierre sesion'][2]],
                      ['Merlin Properties',df_merlin['% Variacion cierre sesion'][2]],
                      ['Naturgy',df_naturgy['% Variacion cierre sesion'][2]],
                      ['Pharma Mar',df_pharmaMar['% Variacion cierre sesion'][2]],
                      ['Red Eléctrica',df_redElectrica['% Variacion cierre sesion'][2]],
                      ['Repsol',df_repsol['% Variacion cierre sesion'][2]],
                      ['Rovi',df_rovi['% Variacion cierre sesion'][2]],
                      ['Sacyr',df_sacyr['% Variacion cierre sesion'][2]],
                      ['Siemens Gamesa',df_siemens['% Variacion cierre sesion'][2]],
                      ['Solaria',df_solaria['% Variacion cierre sesion'][2]],
                      ['Telefónica',df_telefonica['% Variacion cierre sesion'][2]]]
df_ranking_1_per = pd.DataFrame(data_ranking_1_per,columns=['Nombre','% Variacion cierre sesion'])
ordenarRanking(df_ranking_1_per)
df_ranking_1_per


# In[91]:


#Último ranking
data_ranking_129_per = [['Acciona',df_acciona['% Variacion cierre sesion'][130]], 
                        ['Acciona Energía',df_accionaEnergia['% Variacion cierre sesion'][130]],
                        ['Acerinox',df_acerinox['% Variacion cierre sesion'][130]],
                        ['Acs',df_acs['% Variacion cierre sesion'][130]],
                        ['Aena',df_aena['% Variacion cierre sesion'][130]],
                        ['Amadeus',df_amadeus['% Variacion cierre sesion'][130]],
                        ['Arcelormittal',df_arcelormittal['% Variacion cierre sesion'][130]],
                        ['Banco Santander',df_santander['% Variacion cierre sesion'][130]],
                        ['Banco Sabadell',df_sabadell['% Variacion cierre sesion'][130]],
                        ['Bankinter',df_bankinter['% Variacion cierre sesion'][130]],
                        ['BBVA',df_bbva['% Variacion cierre sesion'][130]],
                        ['Caixabank',df_caixabank['% Variacion cierre sesion'][130]],
                        ['Cellnex',df_cellnex['% Variacion cierre sesion'][130]],
                        ['Enagás',df_enagas['% Variacion cierre sesion'][130]],
                        ['Endesa',df_endesa['% Variacion cierre sesion'][130]],
                        ['Ferrovial',df_ferrovial['% Variacion cierre sesion'][130]],
                        ['Fluidra',df_fluidra['% Variacion cierre sesion'][130]],
                        ['Grifols',df_grifols['% Variacion cierre sesion'][130]],
                        ['IAG',df_IAG['% Variacion cierre sesion'][130]],
                        ['Iberdrola',df_iberdrola['% Variacion cierre sesion'][130]],
                        ['Inditex',df_inditex['% Variacion cierre sesion'][130]],
                        ['Indra',df_indra['% Variacion cierre sesion'][130]],
                        ['Inmobiliaria Colonial',df_colonial['% Variacion cierre sesion'][130]],
                        ['Mapfre',df_mapfre['% Variacion cierre sesion'][130]],
                        ['Meliá Hotels',df_melia['% Variacion cierre sesion'][130]],
                        ['Merlin Properties',df_merlin['% Variacion cierre sesion'][130]],
                        ['Naturgy',df_naturgy['% Variacion cierre sesion'][130]],
                        ['Pharma Mar',df_pharmaMar['% Variacion cierre sesion'][130]],
                        ['Red Eléctrica',df_redElectrica['% Variacion cierre sesion'][130]],
                        ['Repsol',df_repsol['% Variacion cierre sesion'][130]],
                        ['Rovi',df_rovi['% Variacion cierre sesion'][130]],
                        ['Sacyr',df_sacyr['% Variacion cierre sesion'][130]],
                        ['Siemens Gamesa',df_siemens['% Variacion cierre sesion'][130]],
                        ['Solaria',df_solaria['% Variacion cierre sesion'][130]],
                        ['Telefónica',df_telefonica['% Variacion cierre sesion'][130]]]
df_ranking_129_per = pd.DataFrame(data_ranking_129_per,columns=['Nombre','% Variacion cierre sesion'])
ordenarRanking(df_ranking_129_per)
df_ranking_129_per


# Vistos estos ejemplo, se pasa a escalar el modelo para obtener en un dataFrame todos los rankings relativos a todas las sesiones registradas.

# In[92]:


########################################### Escalabilidad del modelo ###########################################
#Creación de un Data Frame con tantas filas como empresas y tantas columnas como rankings 
df_rankings_per = pd.DataFrame(columns=rankings,index=classification)

#Bucle
for i in range(1,n_sesions):
    data_aux_per =  [['Acciona',df_acciona['% Variacion cierre sesion'][i]], 
                   ['Acciona Energía',df_accionaEnergia['% Variacion cierre sesion'][i]],
                   ['Acerinox',df_acerinox['% Variacion cierre sesion'][i]],
                   ['Acs',df_acs['% Variacion cierre sesion'][i]],
                   ['Aena',df_aena['% Variacion cierre sesion'][i]],
                   ['Amadeus',df_amadeus['% Variacion cierre sesion'][i]],
                   ['Arcelormittal',df_arcelormittal['% Variacion cierre sesion'][i]],
                   ['Banco Santander',df_santander['% Variacion cierre sesion'][i]],
                   ['Banco Sabadell',df_sabadell['% Variacion cierre sesion'][i]],
                   ['Bankinter',df_bankinter['% Variacion cierre sesion'][i]],
                   ['BBVA',df_bbva['% Variacion cierre sesion'][i]],
                   ['Caixabank',df_caixabank['% Variacion cierre sesion'][i]],
                   ['Cellnex',df_cellnex['% Variacion cierre sesion'][i]],
                   ['Enagás',df_enagas['% Variacion cierre sesion'][i]],
                   ['Endesa',df_endesa['% Variacion cierre sesion'][i]],
                   ['Ferrovial',df_ferrovial['% Variacion cierre sesion'][i]],
                   ['Fluidra',df_fluidra['% Variacion cierre sesion'][i]],
                   ['Grifols',df_grifols['% Variacion cierre sesion'][i]],
                   ['IAG',df_IAG['% Variacion cierre sesion'][i]],
                   ['Iberdrola',df_iberdrola['% Variacion cierre sesion'][i]],
                   ['Inditex',df_inditex['% Variacion cierre sesion'][i]],
                   ['Indra',df_indra['% Variacion cierre sesion'][i]],
                   ['Inmobiliaria Colonial',df_colonial['% Variacion cierre sesion'][i]],
                   ['Mapfre',df_mapfre['% Variacion cierre sesion'][i]],
                   ['Meliá Hotels',df_melia['% Variacion cierre sesion'][i]],
                   ['Merlin Properties',df_merlin['% Variacion cierre sesion'][i]],
                   ['Naturgy',df_naturgy['% Variacion cierre sesion'][i]],
                   ['Pharma Mar',df_pharmaMar['% Variacion cierre sesion'][i]],
                   ['Red Eléctrica',df_redElectrica['% Variacion cierre sesion'][i]],
                   ['Repsol',df_repsol['% Variacion cierre sesion'][i]],
                   ['Rovi',df_rovi['% Variacion cierre sesion'][i]],
                   ['Sacyr',df_sacyr['% Variacion cierre sesion'][i]],
                   ['Siemens Gamesa',df_siemens['% Variacion cierre sesion'][i]],
                   ['Solaria',df_solaria['% Variacion cierre sesion'][i]],
                   ['Telefónica',df_telefonica['% Variacion cierre sesion'][i]]]
    df_aux_per = pd.DataFrame(data_aux_per,columns=['Nombre','% Variacion cierre sesion'])
    ordenarRanking(df_aux_per)
    df_rankings_per.iloc[:,i-1]=df_aux_per.iloc[:,0]
df_rankings_per


# Aprovechando los ejemplos de rankings creados anteriormente, se ejecuta el siguiente bloque para comprobar que el modelo se ha escalado de forma correcta.

# In[93]:


flag0_per=True
flag1_per=True
flag129_per=True

for i in range(n_stocks):
    flag0_per = (df_rankings_per.iloc[i,0]==df_ranking_0_per.iloc[i,0])

for j in range(n_stocks):
    flag1_per = (df_rankings_per.iloc[j,1]==df_ranking_1_per.iloc[j,0])

for k in range(n_stocks):
    flag129_per = (df_rankings_per.iloc[k,129]==df_ranking_129_per.iloc[k,0])

(flag0_per,flag1_per,flag129_per)


# Gracias al bloque anterior se puede verificar lo que se quería, que la escalabilidad dada al modelo es correcta.
# 
# Ahora bien, con el dataFrame de rankings y la función *seCruza* es momento de construir la matriz de adyacencia de este grafo de competitividad.

# In[94]:


#Definición de la matriz de adyacencia del grafo, donde sus filas y sus columnas son las acciones
adj_matrix_per = pd.DataFrame(columns=stocks,index=stocks)

#Dicha matriz se rellena de 0's para asegurarse de que posteriormente se puede rellenar de la forma que se desea en el estudio
for i in range(n_stocks):
    for j in range(n_stocks):
        adj_matrix_per.iloc[i,j]=0

#Iteraciones para completarla con el dataFrame de rankings: Se toma una acción y cada una de sus sucesivas a lo largo
#de todos los rankings, tomados de dos en dos de forma contigua
for k in range(n_sesions-2):
    for i in range(n_stocks):
        for j in range(i+1,n_stocks):
            if (seCruza(df_rankings_per.iloc[:,k],df_rankings_per.iloc[:,k+1],stocks[i],stocks[j])):
                adj_matrix_per.iloc[i,j] = adj_matrix_per.iloc[i,j]+1
                adj_matrix_per.iloc[j,i] = adj_matrix_per.iloc[j,i]+1
adj_matrix_per


# Con la matriz de adyacencia anterior, se puede hacer una representación de su grafo de competitividad asociado, que es el que se buscaba en esta perspectiva.
# 
# El procedimiento para su represntación es absolutamente análogo a los desarrollados anteriormente.

# In[95]:


#Creación del grafo
G_per = nx.Graph()
G_per.add_nodes_from(stocks)

for i in range(n_stocks):
    for j in range(i+1,n_stocks):
        if(adj_matrix_per.iloc[i,j]>0):
            G_per.add_edge(stocks[i],stocks[j],weight=adj_matrix_per.iloc[i,j])


# In[96]:


#Tipo de diseño del grafo
pos_per = nx.circular_layout(G_per)

#Grosor de las aristas
edgew_per = [0.01*G_per.get_edge_data(u, v)['weight'] for u, v in G_per.edges()]
#Espacio de representación
x_per, y_per = plt.subplots(figsize=(12, 12))
#Título del grafo
y_per.set_title("Competitivity graph: Perspective 3", dict(fontweight="bold",fontsize=22,color="black"),loc="center")

#Representación de los objetos del grafo
    #Aristas
nx.draw_networkx_edges(G_per, pos_per, width=edgew_per, edge_color="navy", style='-')
    #Nodos
nx.draw_networkx_nodes(G_per, pos_per, node_size=700, node_shape='o', node_color="gold", linewidths=1,edgecolors="black")
    #Etiquetas sobre nodos
nx.draw_networkx_labels(G_per, pos_per, font_size=11, bbox=dict(ec="black",boxstyle="round",facecolor="white",pad=0.3,alpha=0.6), font_weight='normal', font_family='Verdana', horizontalalignment='center', verticalalignment='center',clip_on=False)

#Modificaciones sobre el espacio de representación
x_per.tight_layout()
plt.axis("off")
y_per.margins(0.05,0.05)
plt.savefig("CG3.png")
plt.show()


# A simple vista y en comparación con los grafos representados anteriormente, este parece tener más competencia entre sus empresas. De nuevo, como pasaba en el segundo caso, esto puede ser debido a la naturaleza de los valores empleados para la creación de los rankings.
# 
# Como pasó anteriormente, esto lleva a desarrollar subvariantes de este grafo para poder tratar el problema tomando solamente las aristas más representativas.

# #### 3.3.1. Perspectiva 3.1: Estudio mediante el cálculo de la variación porcentual en el precio de cierre de la sesión de cada acción respecto de la sesión anterior para aquellas empresas que se crucen más que la media del total de pesos de las aristas del grafo

# Como se viene haciendo en perspectivas anteriores, esta subvariante es para considerar aquellas aristas cuyo peso es mayor que la media de las aristas cuyo peso es mayor que 0 en el grafo original. En ese caso, el peso de la arista se actualiza a la diferencia entre el peso original y la media de pesos.
# 
# En primer lugar, en el siguiente bloque se construye la matriz de adyacencia de esta subvariante del grafo original. 

# In[97]:


#Copia de la matriz original
adj_matrix_per_avg = pd.DataFrame.copy(adj_matrix_per)

#Cálculo de la media
aux_per_avg=[]
for i in range(0,n_stocks):
    for j in range(i+1,n_stocks):
        if(adj_matrix_per_avg.iloc[i,j]>0):
            aux_per_avg.append(adj_matrix_per_avg.iloc[i,j])
mean_aux_per_avg = np.mean(aux_per_avg)
        
#A continuación, se actualiza la matriz adj_matrix_per_avg
for i in range(0,n_stocks):
    for j in range(i+1,n_stocks):
        if(adj_matrix_per_avg.iloc[i,j] < mean_aux_per_avg):
            adj_matrix_per_avg.iloc[i,j] = 0
            adj_matrix_per_avg.iloc[j,i] = 0 
        else:
            adj_matrix_per_avg.iloc[i,j] = adj_matrix_per_avg.iloc[i,j] - mean_aux_per_avg
            adj_matrix_per_avg.iloc[j,i] = adj_matrix_per_avg.iloc[j,i] - mean_aux_per_avg
adj_matrix_per_avg


# Seguidamente, se genera la representación del grafo de competitividad asociado.

# In[98]:


#Creación del grafo
G_per_avg = nx.Graph()
G_per_avg.add_nodes_from(stocks)

for i in range(n_stocks):
    for j in range(i+1,n_stocks):
        if(adj_matrix_per_avg.iloc[i,j]>0):
            G_per_avg.add_edge(stocks[i],stocks[j],weight=adj_matrix_per_avg.iloc[i,j])


# In[99]:


#Tipo de diseño del grafo
pos_per_avg = nx.circular_layout(G_per_avg)

#Grosor de las aristas
edgew_per_avg = [0.2*G_per_avg.get_edge_data(u, v)['weight'] for u, v in G_per_avg.edges()]
#Espacio de representación
x_per_avg, y_per_avg = plt.subplots(figsize=(12, 12))
#Título del grafo
y_per_avg.set_title("Competitivity graph: Perspective 3.1", dict(fontweight="bold",fontsize=22,color="black"),loc="center")

#Representación de los objetos del grafo
    #Aristas
nx.draw_networkx_edges(G_per_avg, pos_per_avg, width=edgew_per_avg, edge_color="navy", style='-')
    #Nodos
nx.draw_networkx_nodes(G_per_avg, pos_per_avg, node_size=700, node_shape='o', node_color="gold", linewidths=1,edgecolors="black")
    #Etiquetas sobre nodos
nx.draw_networkx_labels(G_per_avg, pos_per_avg, font_size=11, bbox=dict(ec="black",boxstyle="round",facecolor="white",pad=0.3,alpha=0.6), font_weight='normal', font_family='Verdana', horizontalalignment='center', verticalalignment='center',clip_on=False)

#Modificaciones sobre el espacio de representación
x_per_avg.tight_layout()
plt.axis("off") 
y_per_avg.margins(0.05,0.05)
plt.savefig("CG3-1.png")
plt.show() 


# Aunque mejora un poco respecto del grafo original, la capacidad para poder extraer conclusiones del mismo es prácticamente nula debido a que sigue existiendo una alta competitividad. Se pasa a la siguiente subvariante.

# #### 3.3.2. Perspectiva 3.2: Estudio mediante el cálculo de la variación porcentual en el precio de cierre de la sesión de cada acción respecto de la sesión anterior para aquellas empresas que se crucen más que la medida 1 del total de pesos de las aristas del grafo

# Se repite el desarrollo del punto 3.3.1 pero estableciendo el límite criterio para considerar las aristas en el valor medida 1 cuya construcción es análoga a la de los apartados 3.1.2 y 3.2.2.
# 
# Se crea la matriz de adyacencia y la representación del grafo al que se asocia.

# In[100]:


#Copia de la matriz original
adj_matrix_per_ms1 = pd.DataFrame.copy(adj_matrix_per)

#Cálculo del valor medida 1
measure_1_per = mean_aux_per_avg + 0.5*(max(aux_per_avg)-mean_aux_per_avg) 

#A continuación, se actualiza la matriz adj_matrix_per_ms1
for i in range(0,n_stocks):
    for j in range(i+1,n_stocks):
        if(adj_matrix_per_ms1.iloc[i,j] < measure_1_per):
            adj_matrix_per_ms1.iloc[i,j] = 0
            adj_matrix_per_ms1.iloc[j,i] = 0 
        else:
            adj_matrix_per_ms1.iloc[i,j] = adj_matrix_per_ms1.iloc[i,j] - measure_1_per
            adj_matrix_per_ms1.iloc[j,i] = adj_matrix_per_ms1.iloc[j,i] - measure_1_per
adj_matrix_per_ms1


# In[101]:


#Creación del grafo
G_per_ms1 = nx.Graph()
G_per_ms1.add_nodes_from(stocks)

for i in range(n_stocks):
    for j in range(i+1,n_stocks):
        if(adj_matrix_per_ms1.iloc[i,j]>0):
            G_per_ms1.add_edge(stocks[i],stocks[j],weight=adj_matrix_per_ms1.iloc[i,j])


# In[102]:


#Tipo de diseño del grafo
pos_per_ms1 = nx.circular_layout(G_per_ms1)

#Grosor de las aristas
edgew_per_ms1 = [2*G_per_ms1.get_edge_data(u, v)['weight'] for u, v in G_per_ms1.edges()]
#Espacio de representación
x_per_ms1, y_per_ms1 = plt.subplots(figsize=(12, 12))
#Título del grafo
y_per_ms1.set_title("Competitivity graph: Perspective 3.2", dict(fontweight="bold",fontsize=22,color="black"),loc="center")

#Representación de los objetos del grafo
    #Aristas
nx.draw_networkx_edges(G_per_ms1, pos_per_ms1, width=edgew_per_ms1, edge_color="navy", style='-')
    #Nodos
nx.draw_networkx_nodes(G_per_ms1, pos_per_ms1, node_size=700, node_shape='o', node_color="gold", linewidths=1,edgecolors="black")
    #Etiquetas sobre nodos
nx.draw_networkx_labels(G_per_ms1, pos_per_ms1, font_size=11, bbox=dict(ec="black",boxstyle="round",facecolor="white",pad=0.3,alpha=0.6), font_weight='normal', font_family='Verdana', horizontalalignment='center', verticalalignment='center',clip_on=False)

#Modificaciones sobre el espacio de representación
x_per_ms1.tight_layout()
plt.axis("off") 
y_per_ms1.margins(0.05,0.05)
plt.savefig("CG3-2.png")
plt.show() 


# La situación aquí es similar a la del punto 3.1.2 donde el volumnen de aristas ya es suficiente. Sin embargo, se aplica la última subvariante.

# #### 3.3.3. Perspectiva 3.3: Estudio mediante el cálculo de la variación porcentual en el precio de cierre de la sesión de cada acción respecto de la sesión anterior para aquellas empresas que se crucen más que la medida 2 del total de pesos de las aristas del grafo

# Se procede a ejecutar los bloques de códigos análogos a las anteriores subvariantes pero tomando como límite para considerar las aristas el valor medida 2, que se contruye de manera análoga a los apartados anteriores en los que se empleaba.
# 
# Seguidamente de la matriz de adyacencia del grafo construido, se realizará su representación asociada.

# In[103]:


#Copia de la matriz original
adj_matrix_per_ms2 = pd.DataFrame.copy(adj_matrix_per)

#Cálculo del valor medida 2
measure_2_per = mean_aux_per_avg + 0.6*(max(aux_per_avg)-mean_aux_per_avg) 

#A continuación, se actualiza la matriz adj_matrix_per_ms2
for i in range(0,n_stocks):
    for j in range(i+1,n_stocks):
        if(adj_matrix_per_ms2.iloc[i,j] < measure_2_per):
            adj_matrix_per_ms2.iloc[i,j] = 0
            adj_matrix_per_ms2.iloc[j,i] = 0 
        else:
            adj_matrix_per_ms2.iloc[i,j] = adj_matrix_per_ms2.iloc[i,j] - measure_2_per
            adj_matrix_per_ms2.iloc[j,i] = adj_matrix_per_ms2.iloc[j,i] - measure_2_per
adj_matrix_per_ms2


# In[104]:


#Creación del grafo
G_per_ms2 = nx.Graph()
G_per_ms2.add_nodes_from(stocks)

for i in range(n_stocks):
    for j in range(i+1,n_stocks):
        if(adj_matrix_per_ms2.iloc[i,j]>0):
            G_per_ms2.add_edge(stocks[i],stocks[j],weight=adj_matrix_per_ms2.iloc[i,j])


# In[105]:


#Tipo de diseño del grafo
pos_per_ms2 = nx.circular_layout(G_per_ms2)

#Grosor de las aristas
edgew_per_ms2 = [2*G_per_ms2.get_edge_data(u, v)['weight'] for u, v in G_per_ms2.edges()]
#Espacio de representación
x_per_ms2, y_per_ms2 = plt.subplots(figsize=(12, 12))
#Título del grafo
y_per_ms2.set_title("Competitivity graph: Perspective 3.3", dict(fontweight="bold",fontsize=22,color="black"),loc="center")

#Representación de los objetos del grafo
    #Aristas
nx.draw_networkx_edges(G_per_ms2, pos_per_ms2, width=edgew_per_ms2, edge_color="navy", style='-')
    #Nodos
nx.draw_networkx_nodes(G_per_ms2, pos_per_ms2, node_size=700, node_shape='o', node_color="gold", linewidths=1,edgecolors="black")
    #Etiquetas sobre nodos
nx.draw_networkx_labels(G_per_ms2, pos_per_ms2, font_size=11, bbox=dict(ec="black",boxstyle="round",facecolor="white",pad=0.3,alpha=0.6), font_weight='normal', font_family='Verdana', horizontalalignment='center', verticalalignment='center',clip_on=False)

#Modificaciones sobre el espacio de representación
x_per_ms2.tight_layout()
plt.axis("off") 
y_per_ms2.margins(0.05,0.05)
plt.savefig("CG3-3.png")
plt.show() 


# Como ocurría en la perspectiva 1.3, es posible que al aumentar tanto el límite haya información que se esté perdiendo. Pese a ello, será en la última sección donde se verá si estas perspectivas permiten o no extraer conclusiones de la situación que se está estudiando.

# ## 4. Aplicación del coeficiente de correlación Kendall en el estudio

# En este apartado se aplica a las diferentes perspectivas desarrolladas anteriormente, y en concreto a su familia de rankings, el cálculo del coeficiente de correlación Kendall. Para ello, se implementa la función ***coefKendall*** que toma un par de rankings y una lista de nombres, la cual en este caso es la lista de nombres de empresas. Su resultado es devolver el valor del coeficiente de correlación de Kendall. Internamente, evalúa si para un par de empresas de la lista estas compiten o no para poder calcular el valor del coeficiente en cuestión.

# In[106]:


def coefKendall (data1,data2,listStocks):
    n = len(data1)
    n_compete = 0
    n_non_compete = 0

    for i in range(n):
        for j in range(i+1,n):
            if (seCruza(data1,data2,listStocks[i],listStocks[j])):
                n_compete = n_compete + 1
            else:
                n_non_compete = n_non_compete + 1

    coef = (n_non_compete - n_compete)/((n*(n-1))/2)
    return coef


# Para probar esta función, se recurre a los dos primeros rankings de la primera perspectiva. Con ellos y la lista *stocks* que contiene todos los nombres de las empresas, se calcula el coeficiente de correlación de Kendall para este caso. Un pequeño matiz para su aplicación es que solamente necesita la lista de nombres ordenados y no el valor de creación del ranking, por lo que habrá que coger exactamente los nombres de los rankings ordenados, lo que a nivel dataFrame de rankings son las columnas. Sin embargo, como se está recurriendo para crear el ejemplo a los rankings ejemplo, hay que tomar solo las primeras columnas de esos dataFrame.

# In[107]:


coefKendall(df_ranking_0_inv.iloc[:,0],df_ranking_1_inv.iloc[:,0],stocks)


# Para ese primer par de rankings de la primera perspectiva, el valor es 0.5262. En este momento, y puesto que la finalidad del cálculo de este coeficiente es para comparar las distintas perspectivas, simplemente se anota como que la prueba de la función se ejecuta de forma correcta. Si se quisiera analizar el valor obtenido habría que añadir que estos rankings no presentan una competitividad muy elevada.
# 
# Ahora sí, se calculan todos los coeficientes de Kendall para todos los pares de rankings contiguos para todas las perspectivas desarrolladas en el estudio.

# In[108]:


#Primera perspectiva
list_coefficients_inv = []

for k in range(n_sesions-2):
    aux_kendall_inv = coefKendall(df_rankings_inv.iloc[:,k],df_rankings_inv.iloc[:,k+1],stocks)
    list_coefficients_inv.append(aux_kendall_inv)
    
list_coefficients_inv


# In[109]:


#Segunda perspectiva
list_coefficients_inv_ac = []

for k in range(n_sesions-2):
    aux_kendall_inv_ac = coefKendall(df_rankings_inv_ac.iloc[:,k],df_rankings_inv_ac.iloc[:,k+1],stocks)
    list_coefficients_inv_ac.append(aux_kendall_inv_ac)
    
list_coefficients_inv_ac


# In[110]:


#Tercera perspectiva
list_coefficients_per = []

for k in range(n_sesions-2):
    aux_kendall_per = coefKendall(df_rankings_per.iloc[:,k],df_rankings_per.iloc[:,k+1],stocks)
    list_coefficients_per.append(aux_kendall_per)
    
list_coefficients_per


# Por último, con estas listas de coeficientes, se representan a lo largo de los pares de rankings contiguos para poder comparar la competitividad de las perspectivas desarrolladas.

# In[111]:


#Organización del tamaño del espacio
plt.subplots(figsize=(13, 7))

#Títulos en los ejes y del gráfico
plt.xlabel("Pares de rankings contiguos",size=12) 
plt.ylabel("Coeficiente de correlación Kendall",size=12)
plt.title("Coeficiente de correlación Kendall en las diferentes perspectivas",size=20)

#Plot de los coeficientes
plt.plot(list_coefficients_inv,'cyan',marker=',',label='Perspectiva 1')
plt.plot(list_coefficients_inv_ac,'blue',marker='.',label='Perspectiva 2')
plt.plot(list_coefficients_per,'orange',marker='x',label='Perspectiva 3')

#Leyenda
plt.legend(title="Perspectivas", title_fontsize=13)

plt.savefig("CoefKendallRep.png") #Para guardar la imagen para exportarla al documento de texto
plt.show()


# A vista de la gráfica y teniendo en cuenta que el criterio para la interpretación de este coeficiente es que a mayor valor del coeficiente menor competitividad en los rankings porque presentan una mayor correlación, las conclusiones son:
# 
#   * La primera perspectiva donde se trabajaba con el valor cambiante de las acciones que se habían comprado al cierre de la         primera sesión con un valor equivalente a 1000 € es la visión menos competitiva. De hecho, esto se refleja en que a medida     que se van desarrollando las subvariantes de este primer enfoque, los grafos asociados van disminuyendo el volumen en su       número de aristas en mayor cantidad respecto de las otras dos perspectivas.
#   * La segunda perspectiva, que tenía en cuenta lo anterior y trabajaba con la diferencia entre valores en sesiones contiguas,     y la tercera perspectiva, que estudiaba la variación porcentual entre el precio de cierre de sesiones, presentan, a vista       general, una misma tendencia en la evolución del coeficiente de correlación Kendall, pues avanzando en el eje X se observa     que hay momentos en los que una tiene un valor para el coeficiente mayor que la otra y otros momentos en los que es al         revés, pero, en líneas generales, van siempre a la par. Por ello, se puede concluir que ambas perspectivas presentan una       competitividad prácticamente idéntica y alta, con valores comprendidos entre -0.6 y 0.5, aproximadamente.    

# # 5. Aplicación del algoritmo de Girvan Newman

# En esta última sección se busca aplicar el algoritmo Girvan Newman explicado en teoría a las diferentes perspectivas y subvariantes desarrolladas en el estudio. La estructuración de esta sección va a ser análoga a la de la sección 3 y dentro de cada subsección se emplearán las mismas técnicas para la aplicación del algoritmo. Aunque existen diferentes métodos para la aplicación del algoritmo, en este apartado se va a escoger uno concreto y en el anexo se podrán incluir más métodos para aplicar el algoritmo que serán extrapolables a las diferentes perspectivas. Adicionalmente a los tres apartados, existe un cuarto donde se realizará la representación en un dendograma de las iteraciones del algoritmo para un caso concreto.
# 
# Para el primer caso de aplicación del algoritmo, la primera perspectiva, se va a explicar cómo se aplica el algoritmo, mientras que para el resto de subvariantes se harán simples comentarios de los resultados obtenidos. El objetivo inicial era iterar el algoritmo hasta que se obtuviesen 4-5 comunidades diferenciadas pero finalmente se iterará el algoritmo hasta siete veces en cada caso para observar qué ocurre en grafos con mayor y menor volumen de aristas.
# 
# Con el número de iteraciones anteriores se va a observar que dependiendo del volumen de arista del grafo habrá casos en los que en la primera iteración se obtengan varias comunidades y otros en los que solo se obtenga una. Además, en las últimas iteraciones se podrá ver cómo se llegan a obtener prácticamente comunidades con un solo nodo (hojas), para los casos de grafos con pocas aristas; mientras que para grafos con muchas aristas en las últimas iteraciones fijadas solamente se obtendrá comunidades pequeñas y una comunidad con la mayoría de los nodos. 
# 
# El fin último de esta sección es detectar las comunidades dentro de los grafos para poder extraer conclusiones de las mismas.

# ### 5.1. Aplicación del algoritmo G-N a la perspectiva 1: Bajo una inversión inicial de 1000 €, estudio de la evolución diaria del total de la inversión al cierre de la sesión

# Tanto para esta como para el resto de casos se va a emplear la siguiente sentencia que itera el algoritmo tantas veces como se desee. Hay que recordar que en este estudio se había fijado a siete iteraciones.

# In[112]:


#Con este bloque se consiguen las k primeras iteraciones del algoritmo
list_communities_inv = []
n_it_inv = 7
comp_inv = community.girvan_newman(G_inv)
for communities in itertools.islice(comp_inv, n_it_inv):
    print(tuple(sorted(c) for c in communities))
    list_communities_inv.append(tuple(sorted(c) for c in communities))


# El resultado es una lista con siete grandes familias donde cada una hace referencia a cada iteración, siendo la de la posición *i* referente a la iteración *i+1*. Dentro de cada familia hay subfamilias que son las comunidades de esa iteración.
# 
# En este caso, se puede observar que las comunidades se van generando una a una, con un solo nodo por cada empresa. Esto es debido a la cantidad de información que recoge este primer grafo. Se va a ir viendo su iteración de forma progresiva.

# In[113]:


#Iteración 1
color_communities_inv_1 = []
node_communities_inv_1 = list_communities_inv[0]
for node in G_inv:
    if node in node_communities_inv_1[0]:
        color_communities_inv_1.append('red')
    else:
        color_communities_inv_1.append('green')  
        
#Grosor de las aristas
edgew_inv_GN = [0.15*G_inv.get_edge_data(u, v)['weight'] for u, v in G_inv.edges()]
        
#Espacio de representación
x_inv_1, y_inv_1 = plt.subplots(figsize=(16, 16))
#Título del grafo
y_inv_1.set_title("Application of Girvan Newman algorithm: Perspective 1, iteration 1", dict(fontweight="bold",fontsize=22,color="black"),loc="center")

#Representación de los objetos del grafo
    #Aristas
nx.draw_networkx_edges(G_inv, pos_inv, width=edgew_inv_GN, edge_color="navy", style='-')
    #Nodos
nx.draw_networkx_nodes(G_inv, pos_inv, node_color=color_communities_inv_1, node_size=1300, node_shape='o', linewidths=1,edgecolors="black")
    #Etiquetas sobre nodos
nx.draw_networkx_labels(G_inv, pos_inv, font_size=16, bbox=dict(ec="black",boxstyle="round",facecolor="white",pad=0.3,alpha=0.6), font_weight='normal', font_family='Verdana', horizontalalignment='center', verticalalignment='center',clip_on=False)

#Modificaciones sobre el espacio de representación
x_inv_1.tight_layout()
plt.axis("off") 
y_inv_1.margins(0.05,0.05)
plt.savefig("GN-CG1-It1.png")
plt.show() 


# In[114]:


#Iteración 2
color_communities_inv_2 = []
node_communities_inv_2 = list_communities_inv[1]
for node in G_inv:
    if node in node_communities_inv_2[0]:
        color_communities_inv_2.append('red')
    elif node in node_communities_inv_2[1]:
        color_communities_inv_2.append('purple')
    else:
        color_communities_inv_2.append('green')  
        
#Espacio de representación
x_inv_2, y_inv_2 = plt.subplots(figsize=(16, 16))
#Título del grafo
y_inv_2.set_title("Application of Girvan Newman algorithm: Perspective 1, iteration 2", dict(fontweight="bold",fontsize=22,color="black"),loc="center")

#Representación de los objetos del grafo
    #Aristas
nx.draw_networkx_edges(G_inv, pos_inv, width=edgew_inv_GN, edge_color="navy", style='-')
    #Nodos
nx.draw_networkx_nodes(G_inv, pos_inv, node_color=color_communities_inv_2, node_size=1300, node_shape='o', linewidths=1,edgecolors="black")
    #Etiquetas sobre nodos
nx.draw_networkx_labels(G_inv, pos_inv, font_size=16, bbox=dict(ec="black",boxstyle="round",facecolor="white",pad=0.3,alpha=0.6), font_weight='normal', font_family='Verdana', horizontalalignment='center', verticalalignment='center',clip_on=False)

#Modificaciones sobre el espacio de representación
x_inv_2.tight_layout()
plt.axis("off") 
y_inv_2.margins(0.05,0.05)
plt.savefig("GN-CG1-It2.png")
plt.show() 


# In[115]:


#Iteración 3
color_communities_inv_3 = []
node_communities_inv_3 = list_communities_inv[2]
for node in G_inv:
    if node in node_communities_inv_3[0]:
        color_communities_inv_3.append('red')
    elif node in node_communities_inv_3[1]:
        color_communities_inv_3.append('yellow')
    elif node in node_communities_inv_3[2]:
        color_communities_inv_3.append('purple')
    else:
        color_communities_inv_3.append('green')  
        
#Espacio de representación
x_inv_3, y_inv_3 = plt.subplots(figsize=(16, 16))
#Título del grafo
y_inv_3.set_title("Application of Girvan Newman algorithm: Perspective 1, iteration 3", dict(fontweight="bold",fontsize=22,color="black"),loc="center")

#Representación de los objetos del grafo
    #Aristas
nx.draw_networkx_edges(G_inv, pos_inv, width=edgew_inv_GN, edge_color="navy", style='-')
    #Nodos
nx.draw_networkx_nodes(G_inv, pos_inv, node_color=color_communities_inv_3, node_size=1300, node_shape='o', linewidths=1,edgecolors="black")
    #Etiquetas sobre nodos
nx.draw_networkx_labels(G_inv, pos_inv, font_size=16, bbox=dict(ec="black",boxstyle="round",facecolor="white",pad=0.3,alpha=0.6), font_weight='normal', font_family='Verdana', horizontalalignment='center', verticalalignment='center',clip_on=False)

#Modificaciones sobre el espacio de representación
x_inv_3.tight_layout()
plt.axis("off") 
y_inv_3.margins(0.05,0.05)
plt.savefig("GN-CG1-It3.png")
plt.show() 


# In[116]:


#Iteración 4
color_communities_inv_4 = []
node_communities_inv_4 = list_communities_inv[3]
for node in G_inv:
    if node in node_communities_inv_4[0]:
        color_communities_inv_4.append('red')
    elif node in node_communities_inv_4[1]:
        color_communities_inv_4.append('yellow')
    elif node in node_communities_inv_4[2]:
        color_communities_inv_4.append('purple')
    elif node in node_communities_inv_4[3]:
        color_communities_inv_4.append('green')
    else:
        color_communities_inv_4.append('orange')  
        
#Espacio de representación
x_inv_4, y_inv_4 = plt.subplots(figsize=(16, 16))
#Título del grafo
y_inv_4.set_title("Application of Girvan Newman algorithm: Perspective 1, iteration 4", dict(fontweight="bold",fontsize=22,color="black"),loc="center")

#Representación de los objetos del grafo
    #Aristas
nx.draw_networkx_edges(G_inv, pos_inv, width=edgew_inv_GN, edge_color="navy", style='-')
    #Nodos
nx.draw_networkx_nodes(G_inv, pos_inv, node_color=color_communities_inv_4, node_size=1300, node_shape='o', linewidths=1,edgecolors="black")
    #Etiquetas sobre nodos
nx.draw_networkx_labels(G_inv, pos_inv, font_size=16, bbox=dict(ec="black",boxstyle="round",facecolor="white",pad=0.3,alpha=0.6), font_weight='normal', font_family='Verdana', horizontalalignment='center', verticalalignment='center',clip_on=False)

#Modificaciones sobre el espacio de representación
x_inv_4.tight_layout()
plt.axis("off") 
y_inv_4.margins(0.05,0.05)
plt.savefig("GN-CG1-It4.png")
plt.show() 


# In[117]:


#Iteración 5
color_communities_inv_5 = []
node_communities_inv_5 = list_communities_inv[4]
for node in G_inv:
    if node in node_communities_inv_5[0]:
        color_communities_inv_5.append('red')
    elif node in node_communities_inv_5[1]:
        color_communities_inv_5.append('deeppink')
    elif node in node_communities_inv_5[2]:
        color_communities_inv_5.append('yellow')
    elif node in node_communities_inv_5[3]:
        color_communities_inv_5.append('purple')
    elif node in node_communities_inv_5[4]:
        color_communities_inv_5.append('green')
    else:
        color_communities_inv_5.append('orange')  
        
#Espacio de representación
x_inv_5, y_inv_5 = plt.subplots(figsize=(16, 16))
#Título del grafo
y_inv_5.set_title("Application of Girvan Newman algorithm: Perspective 1, iteration 5", dict(fontweight="bold",fontsize=22,color="black"),loc="center")

#Representación de los objetos del grafo
    #Aristas
nx.draw_networkx_edges(G_inv, pos_inv, width=edgew_inv_GN, edge_color="navy", style='-')
    #Nodos
nx.draw_networkx_nodes(G_inv, pos_inv, node_color=color_communities_inv_5, node_size=1300, node_shape='o', linewidths=1,edgecolors="black")
    #Etiquetas sobre nodos
nx.draw_networkx_labels(G_inv, pos_inv, font_size=16, bbox=dict(ec="black",boxstyle="round",facecolor="white",pad=0.3,alpha=0.6), font_weight='normal', font_family='Verdana', horizontalalignment='center', verticalalignment='center',clip_on=False)

#Modificaciones sobre el espacio de representación
x_inv_5.tight_layout()
plt.axis("off") 
y_inv_5.margins(0.05,0.05)
plt.savefig("GN-CG1-It5.png")
plt.show() 


# In[118]:


#Iteración 6
color_communities_inv_6 = []
node_communities_inv_6 = list_communities_inv[5]
for node in G_inv:
    if node in node_communities_inv_6[0]:
        color_communities_inv_6.append('red')
    elif node in node_communities_inv_6[1]:
        color_communities_inv_6.append('deeppink')
    elif node in node_communities_inv_6[2]:
        color_communities_inv_6.append('yellow')
    elif node in node_communities_inv_6[3]:
        color_communities_inv_6.append('purple')
    elif node in node_communities_inv_6[4]:
        color_communities_inv_6.append('green')
    elif node in node_communities_inv_6[5]:
        color_communities_inv_6.append('orange')
    else:
        color_communities_inv_6.append('cyan')  

#Espacio de representación
x_inv_6, y_inv_6 = plt.subplots(figsize=(16, 16))
#Título del grafo
y_inv_6.set_title("Application of Girvan Newman algorithm: Perspective 1, iteration 6", dict(fontweight="bold",fontsize=22,color="black"),loc="center")

#Representación de los objetos del grafo
    #Aristas
nx.draw_networkx_edges(G_inv, pos_inv, width=edgew_inv_GN, edge_color="navy", style='-')
    #Nodos
nx.draw_networkx_nodes(G_inv, pos_inv, node_color=color_communities_inv_6, node_size=1300, node_shape='o', linewidths=1,edgecolors="black")
    #Etiquetas sobre nodos
nx.draw_networkx_labels(G_inv, pos_inv, font_size=16, bbox=dict(ec="black",boxstyle="round",facecolor="white",pad=0.3,alpha=0.6), font_weight='normal', font_family='Verdana', horizontalalignment='center', verticalalignment='center',clip_on=False)

#Modificaciones sobre el espacio de representación
x_inv_6.tight_layout()
plt.axis("off") 
y_inv_6.margins(0.05,0.05)
plt.savefig("GN-CG1-It6.png")
plt.show() 


# In[119]:


#Iteración 7
color_communities_inv_7 = []
node_communities_inv_7 = list_communities_inv[6]
for node in G_inv:
    if node in node_communities_inv_7[0]:
        color_communities_inv_7.append('red')
    elif node in node_communities_inv_7[1]:
        color_communities_inv_7.append('deeppink')
    elif node in node_communities_inv_7[2]:
        color_communities_inv_7.append('yellow')
    elif node in node_communities_inv_7[3]:
        color_communities_inv_7.append('purple')
    elif node in node_communities_inv_7[4]:
        color_communities_inv_7.append('green')
    elif node in node_communities_inv_7[5]:
        color_communities_inv_7.append('orange')
    elif node in node_communities_inv_7[6]:
        color_communities_inv_7.append('lime')
    else:
        color_communities_inv_7.append('cyan')  

#Espacio de representación
x_inv_7, y_inv_7 = plt.subplots(figsize=(16, 16))
#Título del grafo
y_inv_7.set_title("Application of Girvan Newman algorithm: Perspective 1, iteration 7", dict(fontweight="bold",fontsize=22,color="black"),loc="center")

#Representación de los objetos del grafo
    #Aristas
nx.draw_networkx_edges(G_inv, pos_inv, width=edgew_inv_GN, edge_color="navy", style='-')
    #Nodos
nx.draw_networkx_nodes(G_inv, pos_inv, node_color=color_communities_inv_7, node_size=1300, node_shape='o', linewidths=1,edgecolors="black")
    #Etiquetas sobre nodos
nx.draw_networkx_labels(G_inv, pos_inv, font_size=16, bbox=dict(ec="black",boxstyle="round",facecolor="white",pad=0.3,alpha=0.6), font_weight='normal', font_family='Verdana', horizontalalignment='center', verticalalignment='center',clip_on=False)

#Modificaciones sobre el espacio de representación
x_inv_7.tight_layout()
plt.axis("off") 
y_inv_7.margins(0.05,0.05)
plt.savefig("GN-CG1-It7.png")
plt.show() 


# Como se ha dicho anteriormente, el algoritmo va formando comunidades con un solo nodo, los cuales ya son nodos hoja del algoritmo.
# 
# Para poder estudiar un poco cómo va evolucionando el algoritmo, se ejecuta el siguiente bloque, el cual itera el algoritmo hasta obtener todas las comunidades con un solo nodo.

# In[120]:


#Aquí se recogen todas las comunidades que se pueden formar
communities_inv = list(community.girvan_newman(G_inv))
communities_inv


# Básicamente las iteraciones sucesivas del algoritmo van capturando solamente un nodo y forman una comunidad con ese nodo. Claramente este grafo no permite extraer conclusiones porque el desarrollo que hace el algoritmo sobre este es crear una comunidad inicial con todos los nodos salvo uno y, a partir de ahí, ir extrayendo nodo a nodo de esta "mega-comunidad" para crear comunidades con un solo nodo.
# 
# A continuación, se hace el mismo análisis para las siguientes subvariantes y perspectivas.

# #### 5.1.1. Aplicación del algoritmo G-N a la perspectiva 1.1: Bajo una inversión inicial de 1000 €, estudio de la evolución diaria del total de la inversión al cierre de la sesión para aquellas empresas que se crucen más que la media del total de pesos de las aristas del grafo

# In[121]:


list_communities_inv_avg = []
n_it_inv_avg = 7
comp_inv_avg = community.girvan_newman(G_inv_avg)
for communities in itertools.islice(comp_inv_avg, n_it_inv_avg):
    print(tuple(sorted(c) for c in communities))
    list_communities_inv_avg.append(tuple(sorted(c) for c in communities))


# In[122]:


#Iteración 1
color_communities_inv_avg_1 = []
node_communities_inv_avg_1 = list_communities_inv_avg[0]
for node in G_inv_avg:
    if node in node_communities_inv_avg_1[0]:
        color_communities_inv_avg_1.append('red')
    else:
        color_communities_inv_avg_1.append('green')  
        
#Grosor de las aristas
edgew_inv_avg_GN = [0.2*G_inv_avg.get_edge_data(u, v)['weight'] for u, v in G_inv_avg.edges()]
        
#Espacio de representación
x_inv_avg_1, y_inv_avg_1 = plt.subplots(figsize=(16, 16))
#Título del grafo
y_inv_avg_1.set_title("Application of Girvan Newman algorithm: Perspective 1.1, iteration 1", dict(fontweight="bold",fontsize=22,color="black"),loc="center")

#Representación de los objetos del grafo
    #Aristas
nx.draw_networkx_edges(G_inv_avg, pos_inv_avg, width=edgew_inv_avg_GN, edge_color="navy", style='-')
    #Nodos
nx.draw_networkx_nodes(G_inv_avg, pos_inv_avg, node_color=color_communities_inv_avg_1, node_size=1300, node_shape='o', linewidths=1,edgecolors="black")
    #Etiquetas sobre nodos
nx.draw_networkx_labels(G_inv_avg, pos_inv_avg, font_size=16, bbox=dict(ec="black",boxstyle="round",facecolor="white",pad=0.3,alpha=0.6), font_weight='normal', font_family='Verdana', horizontalalignment='center', verticalalignment='center',clip_on=False)

#Modificaciones sobre el espacio de representación
x_inv_avg_1.tight_layout()
plt.axis("off") 
y_inv_avg_1.margins(0.05,0.05)
plt.savefig("GN-CG11-It1.png")
plt.show() 


# In[123]:


#Iteración 2
color_communities_inv_avg_2 = []
node_communities_inv_avg_2 = list_communities_inv_avg[1]
for node in G_inv_avg:
    if node in node_communities_inv_avg_2[0]:
        color_communities_inv_avg_2.append('red')
    elif node in node_communities_inv_avg_2[1]:
        color_communities_inv_avg_2.append('purple')
    else:
        color_communities_inv_avg_2.append('green')  

#Espacio de representación
x_inv_avg_2, y_inv_avg_2 = plt.subplots(figsize=(16, 16))
#Título del grafo
y_inv_avg_2.set_title("Application of Girvan Newman algorithm: Perspective 1.1, iteration 2", dict(fontweight="bold",fontsize=22,color="black"),loc="center")

#Representación de los objetos del grafo
    #Aristas
nx.draw_networkx_edges(G_inv_avg, pos_inv_avg, width=edgew_inv_avg_GN, edge_color="navy", style='-')
    #Nodos
nx.draw_networkx_nodes(G_inv_avg, pos_inv_avg, node_color=color_communities_inv_avg_2, node_size=1300, node_shape='o', linewidths=1,edgecolors="black")
    #Etiquetas sobre nodos
nx.draw_networkx_labels(G_inv_avg, pos_inv_avg, font_size=16, bbox=dict(ec="black",boxstyle="round",facecolor="white",pad=0.3,alpha=0.6), font_weight='normal', font_family='Verdana', horizontalalignment='center', verticalalignment='center',clip_on=False)

#Modificaciones sobre el espacio de representación
x_inv_avg_2.tight_layout()
plt.axis("off") 
y_inv_avg_2.margins(0.05,0.05)
plt.savefig("GN-CG11-It2.png")
plt.show() 


# In[124]:


#Iteración 3
color_communities_inv_avg_3 = []
node_communities_inv_avg_3 = list_communities_inv_avg[2]
for node in G_inv_avg:
    if node in node_communities_inv_avg_3[0]:
        color_communities_inv_avg_3.append('red')
    elif node in node_communities_inv_avg_3[1]:
        color_communities_inv_avg_3.append('purple')
    elif node in node_communities_inv_avg_3[2]:
        color_communities_inv_avg_3.append('yellow')
    else:
        color_communities_inv_avg_3.append('green')  

#Espacio de representación
x_inv_avg_3, y_inv_avg_3 = plt.subplots(figsize=(16, 16))
#Título del grafo
y_inv_avg_3.set_title("Application of Girvan Newman algorithm: Perspective 1.1, iteration 3", dict(fontweight="bold",fontsize=22,color="black"),loc="center")

#Representación de los objetos del grafo
    #Aristas
nx.draw_networkx_edges(G_inv_avg, pos_inv_avg, width=edgew_inv_avg_GN, edge_color="navy", style='-')
    #Nodos
nx.draw_networkx_nodes(G_inv_avg, pos_inv_avg, node_color=color_communities_inv_avg_3, node_size=1300, node_shape='o', linewidths=1,edgecolors="black")
    #Etiquetas sobre nodos
nx.draw_networkx_labels(G_inv_avg, pos_inv_avg, font_size=16, bbox=dict(ec="black",boxstyle="round",facecolor="white",pad=0.3,alpha=0.6), font_weight='normal', font_family='Verdana', horizontalalignment='center', verticalalignment='center',clip_on=False)

#Modificaciones sobre el espacio de representación
x_inv_avg_3.tight_layout()
plt.axis("off") 
y_inv_avg_3.margins(0.05,0.05)
plt.savefig("GN-CG11-It3.png")
plt.show() 


# In[125]:


#Iteración 4
color_communities_inv_avg_4 = []
node_communities_inv_avg_4 = list_communities_inv_avg[3]
for node in G_inv_avg:
    if node in node_communities_inv_avg_4[0]:
        color_communities_inv_avg_4.append('red')
    elif node in node_communities_inv_avg_4[1]:
        color_communities_inv_avg_4.append('orange')
    elif node in node_communities_inv_avg_4[2]:
        color_communities_inv_avg_4.append('purple')
    elif node in node_communities_inv_avg_4[3]:
        color_communities_inv_avg_4.append('yellow')
    else:
        color_communities_inv_avg_4.append('green')  

#Espacio de representación
x_inv_avg_4, y_inv_avg_4 = plt.subplots(figsize=(16, 16))
#Título del grafo
y_inv_avg_4.set_title("Application of Girvan Newman algorithm: Perspective 1.1, iteration 4", dict(fontweight="bold",fontsize=22,color="black"),loc="center")

#Representación de los objetos del grafo
    #Aristas
nx.draw_networkx_edges(G_inv_avg, pos_inv_avg, width=edgew_inv_avg_GN, edge_color="navy", style='-')
    #Nodos
nx.draw_networkx_nodes(G_inv_avg, pos_inv_avg, node_color=color_communities_inv_avg_4, node_size=1300, node_shape='o', linewidths=1,edgecolors="black")
    #Etiquetas sobre nodos
nx.draw_networkx_labels(G_inv_avg, pos_inv_avg, font_size=16, bbox=dict(ec="black",boxstyle="round",facecolor="white",pad=0.3,alpha=0.6), font_weight='normal', font_family='Verdana', horizontalalignment='center', verticalalignment='center',clip_on=False)

#Modificaciones sobre el espacio de representación
x_inv_avg_4.tight_layout()
plt.axis("off") 
y_inv_avg_4.margins(0.05,0.05)
plt.savefig("GN-CG11-It4.png")
plt.show() 


# In[126]:


#Iteración 5
color_communities_inv_avg_5 = []
node_communities_inv_avg_5 = list_communities_inv_avg[4]
for node in G_inv_avg:
    if node in node_communities_inv_avg_5[0]:
        color_communities_inv_avg_5.append('red')
    elif node in node_communities_inv_avg_5[1]:
        color_communities_inv_avg_5.append('orange')
    elif node in node_communities_inv_avg_5[2]:
        color_communities_inv_avg_5.append('purple')
    elif node in node_communities_inv_avg_5[3]:
        color_communities_inv_avg_5.append('yellow')
    elif node in node_communities_inv_avg_5[4]:
        color_communities_inv_avg_5.append('deeppink')
    else:
        color_communities_inv_avg_5.append('green')  
        
#Espacio de representación
x_inv_avg_5, y_inv_avg_5 = plt.subplots(figsize=(16, 16))
#Título del grafo
y_inv_avg_5.set_title("Application of Girvan Newman algorithm: Perspective 1.1, iteration 5", dict(fontweight="bold",fontsize=22,color="black"),loc="center")

#Representación de los objetos del grafo
    #Aristas
nx.draw_networkx_edges(G_inv_avg, pos_inv_avg, width=edgew_inv_avg_GN, edge_color="navy", style='-')
    #Nodos
nx.draw_networkx_nodes(G_inv_avg, pos_inv_avg, node_color=color_communities_inv_avg_5, node_size=1300, node_shape='o', linewidths=1,edgecolors="black")
    #Etiquetas sobre nodos
nx.draw_networkx_labels(G_inv_avg, pos_inv_avg, font_size=16, bbox=dict(ec="black",boxstyle="round",facecolor="white",pad=0.3,alpha=0.6), font_weight='normal', font_family='Verdana', horizontalalignment='center', verticalalignment='center',clip_on=False)

#Modificaciones sobre el espacio de representación
x_inv_avg_5.tight_layout()
plt.axis("off") 
y_inv_avg_5.margins(0.05,0.05)
plt.savefig("GN-CG11-It5.png")
plt.show() 


# In[127]:


#Iteración 6
color_communities_inv_avg_6 = []
node_communities_inv_avg_6 = list_communities_inv_avg[5]
for node in G_inv_avg:
    if node in node_communities_inv_avg_6[0]:
        color_communities_inv_avg_6.append('red')
    elif node in node_communities_inv_avg_6[1]:
        color_communities_inv_avg_6.append('orange')
    elif node in node_communities_inv_avg_6[2]:
        color_communities_inv_avg_6.append('purple')
    elif node in node_communities_inv_avg_6[3]:
        color_communities_inv_avg_6.append('yellow')
    elif node in node_communities_inv_avg_6[4]:
        color_communities_inv_avg_6.append('deeppink')
    elif node in node_communities_inv_avg_6[5]:
        color_communities_inv_avg_6.append('cyan')
    else:
        color_communities_inv_avg_6.append('green')  
        
#Espacio de representación
x_inv_avg_6, y_inv_avg_6 = plt.subplots(figsize=(16, 16))
#Título del grafo
y_inv_avg_6.set_title("Application of Girvan Newman algorithm: Perspective 1.1, iteration 6", dict(fontweight="bold",fontsize=22,color="black"),loc="center")

#Representación de los objetos del grafo
    #Aristas
nx.draw_networkx_edges(G_inv_avg, pos_inv_avg, width=edgew_inv_avg_GN, edge_color="navy", style='-')
    #Nodos
nx.draw_networkx_nodes(G_inv_avg, pos_inv_avg, node_color=color_communities_inv_avg_6, node_size=1300, node_shape='o', linewidths=1,edgecolors="black")
    #Etiquetas sobre nodos
nx.draw_networkx_labels(G_inv_avg, pos_inv_avg, font_size=16, bbox=dict(ec="black",boxstyle="round",facecolor="white",pad=0.3,alpha=0.6), font_weight='normal', font_family='Verdana', horizontalalignment='center', verticalalignment='center',clip_on=False)

#Modificaciones sobre el espacio de representación
x_inv_avg_6.tight_layout()
plt.axis("off") 
y_inv_avg_6.margins(0.05,0.05)
plt.savefig("GN-CG11-It6.png")
plt.show() 


# In[128]:


#Iteración 7
color_communities_inv_avg_7 = []
node_communities_inv_avg_7 = list_communities_inv_avg[6]
for node in G_inv_avg:
    if node in node_communities_inv_avg_7[0]:
        color_communities_inv_avg_7.append('red')
    elif node in node_communities_inv_avg_7[1]:
        color_communities_inv_avg_7.append('orange')
    elif node in node_communities_inv_avg_7[2]:
        color_communities_inv_avg_7.append('purple')
    elif node in node_communities_inv_avg_7[3]:
        color_communities_inv_avg_7.append('yellow')
    elif node in node_communities_inv_avg_7[4]:
        color_communities_inv_avg_7.append('lime')
    elif node in node_communities_inv_avg_7[5]:
        color_communities_inv_avg_7.append('deeppink')
    elif node in node_communities_inv_avg_7[6]:
        color_communities_inv_avg_7.append('cyan')
    else:
        color_communities_inv_avg_7.append('green')  
        
#Espacio de representación
x_inv_avg_7, y_inv_avg_7 = plt.subplots(figsize=(16, 16))
#Título del grafo
y_inv_avg_7.set_title("Application of Girvan Newman algorithm: Perspective 1.1, iteration 7", dict(fontweight="bold",fontsize=22,color="black"),loc="center")

#Representación de los objetos del grafo
    #Aristas
nx.draw_networkx_edges(G_inv_avg, pos_inv_avg, width=edgew_inv_avg_GN, edge_color="navy", style='-')
    #Nodos
nx.draw_networkx_nodes(G_inv_avg, pos_inv_avg, node_color=color_communities_inv_avg_7, node_size=1300, node_shape='o', linewidths=1,edgecolors="black")
    #Etiquetas sobre nodos
nx.draw_networkx_labels(G_inv_avg, pos_inv_avg, font_size=16, bbox=dict(ec="black",boxstyle="round",facecolor="white",pad=0.3,alpha=0.6), font_weight='normal', font_family='Verdana', horizontalalignment='center', verticalalignment='center',clip_on=False)

#Modificaciones sobre el espacio de representación
x_inv_avg_7.tight_layout()
plt.axis("off") 
y_inv_avg_7.margins(0.05,0.05)
plt.savefig("GN-CG11-It7.png")
plt.show() 


# De nuevo, en la primera iteración surge una "mega-comunidad" y un nodo aislado, pero en la segunda aparece una comunidad que se separa de esta gran comunidad con 5 nodos. A partir de ahí, se siguen generando comunidades a partir de la "mega-comunidad" extrayendo un nodo en cada iteración.

# In[129]:


communities_inv_avg = list(community.girvan_newman(G_inv_avg))
communities_inv_avg


# Tras estudiar todas las iteraciones posibles del algoritmo, las conclusiones son las mismas que con las 7 iterciones primeras. Esa comunidad con 5 nodos se va desagregando en las iteraciones siguientes pero no de forma sucesiva, si no que en mayor medida son nodos de la "mega-comunidad" los que van formando comunidades por sí solos y en un par de iteraciones entre medias son los nodos de esa comunidad que se formó inicialmente los que van formando comunidades con un nodo. 
# 
# Para poder extraer información de este grafo, la única opción es enfocarse en la comunidad de 5 nodos, coloreada en morado en los grafos anteriores e intentar llegar a alguna conclusión.

# #### 5.1.2. Aplicación del algoritmo G-N a la perspectiva 1.2: Bajo una inversión inicial de 1000 €, estudio de la evolución diaria del total de la inversión al cierre de la sesión para aquellas empresas que se crucen más que la medida 1 del total de pesos de las aristas del grafo

# In[130]:


list_communities_inv_ms1 = []
n_it_inv_ms1 = 7
comp_inv_ms1 = community.girvan_newman(G_inv_ms1)
for communities in itertools.islice(comp_inv_ms1, n_it_inv_ms1):
    print(tuple(sorted(c) for c in communities))
    list_communities_inv_ms1.append(tuple(sorted(c) for c in communities))


# In[131]:


#Iteración 1
color_communities_inv_ms1_1 = []
node_communities_inv_ms1_1 = list_communities_inv_ms1[0]
for node in G_inv_ms1:
    if node in node_communities_inv_ms1_1[0]:
        color_communities_inv_ms1_1.append('red')
    elif node in node_communities_inv_ms1_1[3]:
        color_communities_inv_ms1_1.append('green')
    elif node in node_communities_inv_ms1_1[5]:
        color_communities_inv_ms1_1.append('purple')
    elif node in node_communities_inv_ms1_1[6]:
        color_communities_inv_ms1_1.append('yellow')
    else:
        color_communities_inv_ms1_1.append('white')  
        
#Grosor de las aristas
edgew_inv_ms1_GN = [0.9*G_inv_ms1.get_edge_data(u, v)['weight'] for u, v in G_inv_ms1.edges()]
        
#Espacio de representación
x_inv_ms1_1, y_inv_ms1_1 = plt.subplots(figsize=(16, 16))
#Título del grafo
y_inv_ms1_1.set_title("Application of Girvan Newman algorithm: Perspective 1.2, iteration 1", dict(fontweight="bold",fontsize=22,color="black"),loc="center")

#Representación de los objetos del grafo
    #Aristas
nx.draw_networkx_edges(G_inv_ms1, pos_inv_ms1, width=edgew_inv_ms1_GN, edge_color="navy", style='-')
    #Nodos
nx.draw_networkx_nodes(G_inv_ms1, pos_inv_ms1, node_color=color_communities_inv_ms1_1, node_size=1300, node_shape='o', linewidths=1,edgecolors="black")
    #Etiquetas sobre nodos
nx.draw_networkx_labels(G_inv_ms1, pos_inv_ms1, font_size=16, bbox=dict(ec="black",boxstyle="round",facecolor="white",pad=0.3,alpha=0.6), font_weight='normal', font_family='Verdana', horizontalalignment='center', verticalalignment='center',clip_on=False)

#Modificaciones sobre el espacio de representación
x_inv_ms1_1.tight_layout()
plt.axis("off") 
y_inv_ms1_1.margins(0.05,0.05)
plt.savefig("GN-CG12-It1.png")
plt.show() 


# In[132]:


#Iteración 2
color_communities_inv_ms1_2 = []
node_communities_inv_ms1_2 = list_communities_inv_ms1[1]
for node in G_inv_ms1:
    if node in node_communities_inv_ms1_2[0]:
        color_communities_inv_ms1_2.append('red')
    elif node in node_communities_inv_ms1_2[3]:
        color_communities_inv_ms1_2.append('green')
    elif node in node_communities_inv_ms1_2[5]:
        color_communities_inv_ms1_2.append('purple')
    elif node in node_communities_inv_ms1_2[6]:
        color_communities_inv_ms1_2.append('yellow')
    elif node in node_communities_inv_ms1_2[12]:
        color_communities_inv_ms1_2.append('orange')
    else:
        color_communities_inv_ms1_2.append('white')  
        
#Espacio de representación
x_inv_ms1_2, y_inv_ms1_2 = plt.subplots(figsize=(16, 16))
#Título del grafo
y_inv_ms1_2.set_title("Application of Girvan Newman algorithm: Perspective 1.2, iteration 2", dict(fontweight="bold",fontsize=22,color="black"),loc="center")

#Representación de los objetos del grafo
    #Aristas
nx.draw_networkx_edges(G_inv_ms1, pos_inv_ms1, width=edgew_inv_ms1_GN, edge_color="navy", style='-')
    #Nodos
nx.draw_networkx_nodes(G_inv_ms1, pos_inv_ms1, node_color=color_communities_inv_ms1_2, node_size=1300, node_shape='o', linewidths=1,edgecolors="black")
    #Etiquetas sobre nodos
nx.draw_networkx_labels(G_inv_ms1, pos_inv_ms1, font_size=16, bbox=dict(ec="black",boxstyle="round",facecolor="white",pad=0.3,alpha=0.6), font_weight='normal', font_family='Verdana', horizontalalignment='center', verticalalignment='center',clip_on=False)

#Modificaciones sobre el espacio de representación
x_inv_ms1_2.tight_layout()
plt.axis("off") 
y_inv_ms1_2.margins(0.05,0.05)
plt.savefig("GN-CG12-It2.png")
plt.show() 


# In[133]:


#Iteración 3
color_communities_inv_ms1_3 = []
node_communities_inv_ms1_3 = list_communities_inv_ms1[2]
for node in G_inv_ms1:
    if node in node_communities_inv_ms1_3[0]:
        color_communities_inv_ms1_3.append('red')
    elif node in node_communities_inv_ms1_3[3]:
        color_communities_inv_ms1_3.append('green')
    elif node in node_communities_inv_ms1_3[5]:
        color_communities_inv_ms1_3.append('purple')
    elif node in node_communities_inv_ms1_3[6]:
        color_communities_inv_ms1_3.append('yellow')
    elif node in node_communities_inv_ms1_3[12]:
        color_communities_inv_ms1_3.append('deeppink')
    elif node in node_communities_inv_ms1_3[13]:
        color_communities_inv_ms1_3.append('orange')
    else:
        color_communities_inv_ms1_3.append('white')  
        
#Espacio de representación
x_inv_ms1_3, y_inv_ms1_3 = plt.subplots(figsize=(16, 16))
#Título del grafo
y_inv_ms1_3.set_title("Application of Girvan Newman algorithm: Perspective 1.2, iteration 3", dict(fontweight="bold",fontsize=22,color="black"),loc="center")

#Representación de los objetos del grafo
    #Aristas
nx.draw_networkx_edges(G_inv_ms1, pos_inv_ms1, width=edgew_inv_ms1_GN, edge_color="navy", style='-')
    #Nodos
nx.draw_networkx_nodes(G_inv_ms1, pos_inv_ms1, node_color=color_communities_inv_ms1_3, node_size=1300, node_shape='o', linewidths=1,edgecolors="black")
    #Etiquetas sobre nodos
nx.draw_networkx_labels(G_inv_ms1, pos_inv_ms1, font_size=16, bbox=dict(ec="black",boxstyle="round",facecolor="white",pad=0.3,alpha=0.6), font_weight='normal', font_family='Verdana', horizontalalignment='center', verticalalignment='center',clip_on=False)

#Modificaciones sobre el espacio de representación
x_inv_ms1_3.tight_layout()
plt.axis("off") 
y_inv_ms1_3.margins(0.05,0.05)
plt.savefig("GN-CG12-It3.png")
plt.show() 


# In[134]:


#Iteración 4
color_communities_inv_ms1_4 = []
node_communities_inv_ms1_4 = list_communities_inv_ms1[3]
for node in G_inv_ms1:
    if node in node_communities_inv_ms1_4[0]:
        color_communities_inv_ms1_4.append('red')
    elif node in node_communities_inv_ms1_4[3]:
        color_communities_inv_ms1_4.append('green')
    elif node in node_communities_inv_ms1_4[5]:
        color_communities_inv_ms1_4.append('purple')
    elif node in node_communities_inv_ms1_4[6]:
        color_communities_inv_ms1_4.append('yellow')
    elif node in node_communities_inv_ms1_4[12]:
        color_communities_inv_ms1_4.append('cyan')
    elif node in node_communities_inv_ms1_4[13]:
        color_communities_inv_ms1_4.append('deeppink')
    elif node in node_communities_inv_ms1_4[14]:
        color_communities_inv_ms1_4.append('orange')
    else:
        color_communities_inv_ms1_4.append('white')  
        
#Espacio de representación
x_inv_ms1_4, y_inv_ms1_4 = plt.subplots(figsize=(16, 16))
#Título del grafo
y_inv_ms1_4.set_title("Application of Girvan Newman algorithm: Perspective 1.2, iteration 4", dict(fontweight="bold",fontsize=22,color="black"),loc="center")

#Representación de los objetos del grafo
    #Aristas
nx.draw_networkx_edges(G_inv_ms1, pos_inv_ms1, width=edgew_inv_ms1_GN, edge_color="navy", style='-')
    #Nodos
nx.draw_networkx_nodes(G_inv_ms1, pos_inv_ms1, node_color=color_communities_inv_ms1_4, node_size=1300, node_shape='o', linewidths=1,edgecolors="black")
    #Etiquetas sobre nodos
nx.draw_networkx_labels(G_inv_ms1, pos_inv_ms1, font_size=16, bbox=dict(ec="black",boxstyle="round",facecolor="white",pad=0.3,alpha=0.6), font_weight='normal', font_family='Verdana', horizontalalignment='center', verticalalignment='center',clip_on=False)

#Modificaciones sobre el espacio de representación
x_inv_ms1_4.tight_layout()
plt.axis("off") 
y_inv_ms1_4.margins(0.05,0.05)
plt.savefig("GN-CG12-It4.png")
plt.show() 


# In[135]:


#Iteración 5
color_communities_inv_ms1_5 = []
node_communities_inv_ms1_5 = list_communities_inv_ms1[4]
for node in G_inv_ms1:
    if node in node_communities_inv_ms1_5[0]:
        color_communities_inv_ms1_5.append('red')
    elif node in node_communities_inv_ms1_5[3]:
        color_communities_inv_ms1_5.append('green')
    elif node in node_communities_inv_ms1_5[5]:
        color_communities_inv_ms1_5.append('purple')
    elif node in node_communities_inv_ms1_5[6]:
        color_communities_inv_ms1_5.append('yellow')
    elif node in node_communities_inv_ms1_5[12]:
        color_communities_inv_ms1_5.append('cyan')
    elif node in node_communities_inv_ms1_5[13]:
        color_communities_inv_ms1_5.append('deeppink')
    elif node in node_communities_inv_ms1_5[14]:
        color_communities_inv_ms1_5.append('orange')
    elif node in node_communities_inv_ms1_5[18]:
        color_communities_inv_ms1_5.append('lime')
    else:
        color_communities_inv_ms1_5.append('white')  
        
#Espacio de representación
x_inv_ms1_5, y_inv_ms1_5 = plt.subplots(figsize=(16, 16))
#Título del grafo
y_inv_ms1_5.set_title("Application of Girvan Newman algorithm: Perspective 1.2, iteration 5", dict(fontweight="bold",fontsize=22,color="black"),loc="center")

#Representación de los objetos del grafo
    #Aristas
nx.draw_networkx_edges(G_inv_ms1, pos_inv_ms1, width=edgew_inv_ms1_GN, edge_color="navy", style='-')
    #Nodos
nx.draw_networkx_nodes(G_inv_ms1, pos_inv_ms1, node_color=color_communities_inv_ms1_5, node_size=1300, node_shape='o', linewidths=1,edgecolors="black")
    #Etiquetas sobre nodos
nx.draw_networkx_labels(G_inv_ms1, pos_inv_ms1, font_size=16, bbox=dict(ec="black",boxstyle="round",facecolor="white",pad=0.3,alpha=0.6), font_weight='normal', font_family='Verdana', horizontalalignment='center', verticalalignment='center',clip_on=False)

#Modificaciones sobre el espacio de representación
x_inv_ms1_5.tight_layout()
plt.axis("off") 
y_inv_ms1_5.margins(0.05,0.05)
plt.savefig("GN-CG12-It5.png")
plt.show() 


# In[136]:


#Iteración 6
color_communities_inv_ms1_6 = []
node_communities_inv_ms1_6 = list_communities_inv_ms1[5]
for node in G_inv_ms1:
    if node in node_communities_inv_ms1_6[0]:
        color_communities_inv_ms1_6.append('red')
    elif node in node_communities_inv_ms1_6[3]:
        color_communities_inv_ms1_6.append('green')
    elif node in node_communities_inv_ms1_6[5]:
        color_communities_inv_ms1_6.append('purple')
    elif node in node_communities_inv_ms1_6[6]:
        color_communities_inv_ms1_6.append('yellow')
    elif node in node_communities_inv_ms1_6[12]:
        color_communities_inv_ms1_6.append('cyan')
    elif node in node_communities_inv_ms1_6[13]:
        color_communities_inv_ms1_6.append('deeppink')
    elif node in node_communities_inv_ms1_6[14]:
        color_communities_inv_ms1_6.append('orange')
    elif node in node_communities_inv_ms1_6[18]:
        color_communities_inv_ms1_6.append('lime')
    elif node in node_communities_inv_ms1_6[26]:
        color_communities_inv_ms1_6.append('chocolate')
    else:
        color_communities_inv_ms1_6.append('white')  
        
#Espacio de representación
x_inv_ms1_6, y_inv_ms1_6 = plt.subplots(figsize=(16, 16))
#Título del grafo
y_inv_ms1_6.set_title("Application of Girvan Newman algorithm: Perspective 1.2, iteration 6", dict(fontweight="bold",fontsize=22,color="black"),loc="center")

#Representación de los objetos del grafo
    #Aristas
nx.draw_networkx_edges(G_inv_ms1, pos_inv_ms1, width=edgew_inv_ms1_GN, edge_color="navy", style='-')
    #Nodos
nx.draw_networkx_nodes(G_inv_ms1, pos_inv_ms1, node_color=color_communities_inv_ms1_6, node_size=1300, node_shape='o', linewidths=1,edgecolors="black")
    #Etiquetas sobre nodos
nx.draw_networkx_labels(G_inv_ms1, pos_inv_ms1, font_size=16, bbox=dict(ec="black",boxstyle="round",facecolor="white",pad=0.3,alpha=0.6), font_weight='normal', font_family='Verdana', horizontalalignment='center', verticalalignment='center',clip_on=False)

#Modificaciones sobre el espacio de representación
x_inv_ms1_6.tight_layout()
plt.axis("off") 
y_inv_ms1_6.margins(0.05,0.05)
plt.savefig("GN-CG12-It6.png")
plt.show() 


# In[137]:


#Iteración 7
color_communities_inv_ms1_7 = []
node_communities_inv_ms1_7 = list_communities_inv_ms1[6]
for node in G_inv_ms1:
    if node in node_communities_inv_ms1_7[0]:
        color_communities_inv_ms1_7.append('red')
    elif node in node_communities_inv_ms1_7[3]:
        color_communities_inv_ms1_7.append('green')
    elif node in node_communities_inv_ms1_7[5]:
        color_communities_inv_ms1_7.append('purple')
    elif node in node_communities_inv_ms1_7[6]:
        color_communities_inv_ms1_7.append('yellow')
    elif node in node_communities_inv_ms1_7[12]:
        color_communities_inv_ms1_7.append('cyan')
    elif node in node_communities_inv_ms1_7[13]:
        color_communities_inv_ms1_7.append('olive')
    elif node in node_communities_inv_ms1_7[14]:
        color_communities_inv_ms1_7.append('deeppink')
    elif node in node_communities_inv_ms1_7[15]:
        color_communities_inv_ms1_7.append('orange')
    elif node in node_communities_inv_ms1_7[19]:
        color_communities_inv_ms1_7.append('lime')
    elif node in node_communities_inv_ms1_7[27]:
        color_communities_inv_ms1_7.append('chocolate')
    else:
        color_communities_inv_ms1_7.append('white')  
        
#Espacio de representación
x_inv_ms1_7, y_inv_ms1_7 = plt.subplots(figsize=(16, 16))
#Título del grafo
y_inv_ms1_7.set_title("Application of Girvan Newman algorithm: Perspective 1.2, iteration 7", dict(fontweight="bold",fontsize=22,color="black"),loc="center")

#Representación de los objetos del grafo
    #Aristas
nx.draw_networkx_edges(G_inv_ms1, pos_inv_ms1, width=edgew_inv_ms1_GN, edge_color="navy", style='-')
    #Nodos
nx.draw_networkx_nodes(G_inv_ms1, pos_inv_ms1, node_color=color_communities_inv_ms1_7, node_size=1300, node_shape='o', linewidths=1,edgecolors="black")
    #Etiquetas sobre nodos
nx.draw_networkx_labels(G_inv_ms1, pos_inv_ms1, font_size=16, bbox=dict(ec="black",boxstyle="round",facecolor="white",pad=0.3,alpha=0.6), font_weight='normal', font_family='Verdana', horizontalalignment='center', verticalalignment='center',clip_on=False)

#Modificaciones sobre el espacio de representación
x_inv_ms1_7.tight_layout()
plt.axis("off") 
y_inv_ms1_7.margins(0.05,0.05)
plt.savefig("GN-CG12-It7.png")
plt.show() 


# Para este caso hay que tener en cuenta que hay nodos aislados debido a que en el grafo tienen grado 0. Es por ello que no hay que confundir estos nodos con comunidades. Adicionalmente, se puede observar que ahora sí hay comunidades bien diferenciadas al inicio, concretamente, cuatro y que a partir de estas se van formando comunidades más pequeñas desagregando nodos de las mismas. Para extraer conlcusiones bastará con fijarse en las iteraciones iniciales, debido a que las sucesivas comienzan a tener comunidades con un solo nodo.

# In[138]:


communities_inv_ms1 = list(community.girvan_newman(G_inv_ms1))
communities_inv_ms1


# Como se ha comentado anteriormente para las siete primeras iteraciones, las últimas no aportan mucho valor para poder extraer información porque son las en las que los nodos comienzan a aislarse en comunidades individuales.

# #### 5.1.3. Aplicación del algoritmo G-N a la perspectiva 1.3: Bajo una inversión inicial de 1000 €, estudio de la evolución diaria del total de la inversión al cierre de la sesión para aquellas empresas que se crucen más que la medida 2 del total de pesos de las aristas del grafo

# In[139]:


list_communities_inv_ms2 = []
n_it_inv_ms2 = 7
comp_inv_ms2 = community.girvan_newman(G_inv_ms2)
for communities in itertools.islice(comp_inv_ms2, n_it_inv_ms2):
    print(tuple(sorted(c) for c in communities))
    list_communities_inv_ms2.append(tuple(sorted(c) for c in communities))


# In[140]:


#Iteración 1
color_communities_inv_ms2_1 = []
node_communities_inv_ms2_1 = list_communities_inv_ms2[0]
for node in G_inv_ms2:
    if node in node_communities_inv_ms2_1[6]:
        color_communities_inv_ms2_1.append('red')
    elif node in node_communities_inv_ms2_1[14]:
        color_communities_inv_ms2_1.append('green')
    elif node in node_communities_inv_ms2_1[15]:
        color_communities_inv_ms2_1.append('purple')
    elif node in node_communities_inv_ms2_1[19]:
        color_communities_inv_ms2_1.append('yellow')
    else:
        color_communities_inv_ms2_1.append('white')  

#Grosor de las aristas
edgew_inv_ms2_GN = [G_inv_ms2.get_edge_data(u, v)['weight'] for u, v in G_inv_ms2.edges()]
        
#Espacio de representación
x_inv_ms2_1, y_inv_ms2_1 = plt.subplots(figsize=(16, 16))
#Título del grafo
y_inv_ms2_1.set_title("Application of Girvan Newman algorithm: Perspective 1.3, iteration 1", dict(fontweight="bold",fontsize=22,color="black"),loc="center")

#Representación de los objetos del grafo
    #Aristas
nx.draw_networkx_edges(G_inv_ms2, pos_inv_ms2, width=edgew_inv_ms2_GN, edge_color="navy", style='-')
    #Nodos
nx.draw_networkx_nodes(G_inv_ms2, pos_inv_ms2, node_color=color_communities_inv_ms2_1, node_size=1300, node_shape='o', linewidths=1,edgecolors="black")
    #Etiquetas sobre nodos
nx.draw_networkx_labels(G_inv_ms2, pos_inv_ms2, font_size=16, bbox=dict(ec="black",boxstyle="round",facecolor="white",pad=0.3,alpha=0.6), font_weight='normal', font_family='Verdana', horizontalalignment='center', verticalalignment='center',clip_on=False)

#Modificaciones sobre el espacio de representación
x_inv_ms2_1.tight_layout()
plt.axis("off") 
y_inv_ms2_1.margins(0.05,0.05)
plt.savefig("GN-CG13-It1.png")
plt.show() 


# In[141]:


#Iteración 2
color_communities_inv_ms2_2 = []
node_communities_inv_ms2_2 = list_communities_inv_ms2[1]
for node in G_inv_ms2:
    if node in node_communities_inv_ms2_2[6]:
        color_communities_inv_ms2_2.append('red')
    elif node in node_communities_inv_ms2_2[14]:
        color_communities_inv_ms2_2.append('green')
    elif node in node_communities_inv_ms2_2[15]:
        color_communities_inv_ms2_2.append('purple')
    elif node in node_communities_inv_ms2_2[19]:
        color_communities_inv_ms2_2.append('yellow')
    elif node in node_communities_inv_ms2_2[27]:
        color_communities_inv_ms2_2.append('orange')
    else:
        color_communities_inv_ms2_2.append('white')  
        
#Espacio de representación
x_inv_ms2_2, y_inv_ms2_2 = plt.subplots(figsize=(16, 16))
#Título del grafo
y_inv_ms2_2.set_title("Application of Girvan Newman algorithm: Perspective 1.3, iteration 2", dict(fontweight="bold",fontsize=22,color="black"),loc="center")

#Representación de los objetos del grafo
    #Aristas
nx.draw_networkx_edges(G_inv_ms2, pos_inv_ms2, width=edgew_inv_ms2_GN, edge_color="navy", style='-')
    #Nodos
nx.draw_networkx_nodes(G_inv_ms2, pos_inv_ms2, node_color=color_communities_inv_ms2_2, node_size=1300, node_shape='o', linewidths=1,edgecolors="black")
    #Etiquetas sobre nodos
nx.draw_networkx_labels(G_inv_ms2, pos_inv_ms2, font_size=16, bbox=dict(ec="black",boxstyle="round",facecolor="white",pad=0.3,alpha=0.6), font_weight='normal', font_family='Verdana', horizontalalignment='center', verticalalignment='center',clip_on=False)

#Modificaciones sobre el espacio de representación
x_inv_ms2_2.tight_layout()
plt.axis("off") 
y_inv_ms2_2.margins(0.05,0.05)
plt.savefig("GN-CG13-It2.png")
plt.show() 


# In[142]:


#Iteración 3
color_communities_inv_ms2_3 = []
node_communities_inv_ms2_3 = list_communities_inv_ms2[2]
for node in G_inv_ms2:
    if node in node_communities_inv_ms2_3[6]:
        color_communities_inv_ms2_3.append('red')
    elif node in node_communities_inv_ms2_3[14]:
        color_communities_inv_ms2_3.append('green')
    elif node in node_communities_inv_ms2_3[15]:
        color_communities_inv_ms2_3.append('purple')
    elif node in node_communities_inv_ms2_3[19]:
        color_communities_inv_ms2_3.append('yellow')
    elif node in node_communities_inv_ms2_3[27]:
        color_communities_inv_ms2_3.append('orange')
    elif node in node_communities_inv_ms2_3[28]:
        color_communities_inv_ms2_3.append('deeppink')
    else:
        color_communities_inv_ms2_3.append('white')  
        
#Espacio de representación
x_inv_ms2_3, y_inv_ms2_3 = plt.subplots(figsize=(16, 16))
#Título del grafo
y_inv_ms2_3.set_title("Application of Girvan Newman algorithm: Perspective 1.3, iteration 3", dict(fontweight="bold",fontsize=22,color="black"),loc="center")

#Representación de los objetos del grafo
    #Aristas
nx.draw_networkx_edges(G_inv_ms2, pos_inv_ms2, width=edgew_inv_ms2_GN, edge_color="navy", style='-')
    #Nodos
nx.draw_networkx_nodes(G_inv_ms2, pos_inv_ms2, node_color=color_communities_inv_ms2_3, node_size=1300, node_shape='o', linewidths=1,edgecolors="black")
    #Etiquetas sobre nodos
nx.draw_networkx_labels(G_inv_ms2, pos_inv_ms2, font_size=16, bbox=dict(ec="black",boxstyle="round",facecolor="white",pad=0.3,alpha=0.6), font_weight='normal', font_family='Verdana', horizontalalignment='center', verticalalignment='center',clip_on=False)

#Modificaciones sobre el espacio de representación
x_inv_ms2_3.tight_layout()
plt.axis("off") 
y_inv_ms2_3.margins(0.05,0.05)
plt.savefig("GN-CG13-It3.png")
plt.show() 


# In[143]:


#Iteración 4
color_communities_inv_ms2_4 = []
node_communities_inv_ms2_4 = list_communities_inv_ms2[3]
for node in G_inv_ms2:
    if node in node_communities_inv_ms2_4[6]:
        color_communities_inv_ms2_4.append('red')
    elif node in node_communities_inv_ms2_4[14]:
        color_communities_inv_ms2_4.append('green')
    elif node in node_communities_inv_ms2_4[15]:
        color_communities_inv_ms2_4.append('purple')
    elif node in node_communities_inv_ms2_4[19]:
        color_communities_inv_ms2_4.append('yellow')
    elif node in node_communities_inv_ms2_4[27]:
        color_communities_inv_ms2_4.append('orange')
    elif node in node_communities_inv_ms2_4[28]:
        color_communities_inv_ms2_4.append('deeppink')
    elif node in node_communities_inv_ms2_4[30]:
        color_communities_inv_ms2_4.append('cyan')
    else:
        color_communities_inv_ms2_4.append('white')  
        
#Espacio de representación
x_inv_ms2_4, y_inv_ms2_4 = plt.subplots(figsize=(16, 16))
#Título del grafo
y_inv_ms2_4.set_title("Application of Girvan Newman algorithm: Perspective 1.3, iteration 4", dict(fontweight="bold",fontsize=22,color="black"),loc="center")

#Representación de los objetos del grafo
    #Aristas
nx.draw_networkx_edges(G_inv_ms2, pos_inv_ms2, width=edgew_inv_ms2_GN, edge_color="navy", style='-')
    #Nodos
nx.draw_networkx_nodes(G_inv_ms2, pos_inv_ms2, node_color=color_communities_inv_ms2_4, node_size=1300, node_shape='o', linewidths=1,edgecolors="black")
    #Etiquetas sobre nodos
nx.draw_networkx_labels(G_inv_ms2, pos_inv_ms2, font_size=16, bbox=dict(ec="black",boxstyle="round",facecolor="white",pad=0.3,alpha=0.6), font_weight='normal', font_family='Verdana', horizontalalignment='center', verticalalignment='center',clip_on=False)

#Modificaciones sobre el espacio de representación
x_inv_ms2_4.tight_layout()
plt.axis("off") 
y_inv_ms2_4.margins(0.05,0.05)
plt.savefig("GN-CG13-It4.png")
plt.show() 


# In[144]:


#Iteración 5
color_communities_inv_ms2_5 = []
node_communities_inv_ms2_5 = list_communities_inv_ms2[4]
for node in G_inv_ms2:
    if node in node_communities_inv_ms2_5[6]:
        color_communities_inv_ms2_5.append('red')
    elif node in node_communities_inv_ms2_5[14]:
        color_communities_inv_ms2_5.append('green')
    elif node in node_communities_inv_ms2_5[15]:
        color_communities_inv_ms2_5.append('purple')
    elif node in node_communities_inv_ms2_5[19]:
        color_communities_inv_ms2_5.append('yellow')
    elif node in node_communities_inv_ms2_5[27]:
        color_communities_inv_ms2_5.append('orange')
    elif node in node_communities_inv_ms2_5[28]:
        color_communities_inv_ms2_5.append('deeppink')
    elif node in node_communities_inv_ms2_5[30]:
        color_communities_inv_ms2_5.append('cyan')
    elif node in node_communities_inv_ms2_5[31]:
        color_communities_inv_ms2_5.append('lime')
    else:
        color_communities_inv_ms2_5.append('white')  
        
#Espacio de representación
x_inv_ms2_5, y_inv_ms2_5 = plt.subplots(figsize=(16, 16))
#Título del grafo
y_inv_ms2_5.set_title("Application of Girvan Newman algorithm: Perspective 1.3, iteration 5", dict(fontweight="bold",fontsize=22,color="black"),loc="center")

#Representación de los objetos del grafo
    #Aristas
nx.draw_networkx_edges(G_inv_ms2, pos_inv_ms2, width=edgew_inv_ms2_GN, edge_color="navy", style='-')
    #Nodos
nx.draw_networkx_nodes(G_inv_ms2, pos_inv_ms2, node_color=color_communities_inv_ms2_5, node_size=1300, node_shape='o', linewidths=1,edgecolors="black")
    #Etiquetas sobre nodos
nx.draw_networkx_labels(G_inv_ms2, pos_inv_ms2, font_size=16, bbox=dict(ec="black",boxstyle="round",facecolor="white",pad=0.3,alpha=0.6), font_weight='normal', font_family='Verdana', horizontalalignment='center', verticalalignment='center',clip_on=False)

#Modificaciones sobre el espacio de representación
x_inv_ms2_5.tight_layout()
plt.axis("off") 
y_inv_ms2_5.margins(0.05,0.05)
plt.savefig("GN-CG13-It5.png")
plt.show() 


# In[145]:


#Iteración 6
color_communities_inv_ms2_6 = []
node_communities_inv_ms2_6 = list_communities_inv_ms2[5]
for node in G_inv_ms2:
    if node in node_communities_inv_ms2_6[6]:
        color_communities_inv_ms2_6.append('red')
    elif node in node_communities_inv_ms2_6[14]:
        color_communities_inv_ms2_6.append('green')
    elif node in node_communities_inv_ms2_6[15]:
        color_communities_inv_ms2_6.append('purple')
    elif node in node_communities_inv_ms2_6[19]:
        color_communities_inv_ms2_6.append('yellow')
    elif node in node_communities_inv_ms2_6[27]:
        color_communities_inv_ms2_6.append('orange')
    elif node in node_communities_inv_ms2_6[28]:
        color_communities_inv_ms2_6.append('deeppink')
    elif node in node_communities_inv_ms2_6[30]:
        color_communities_inv_ms2_6.append('cyan')
    elif node in node_communities_inv_ms2_6[31]:
        color_communities_inv_ms2_6.append('lime')
    elif node in node_communities_inv_ms2_6[33]:
        color_communities_inv_ms2_6.append('olive')
    else:
        color_communities_inv_ms2_6.append('white')  
        
#Espacio de representación
x_inv_ms2_6, y_inv_ms2_6 = plt.subplots(figsize=(16, 16))
#Título del grafo
y_inv_ms2_6.set_title("Application of Girvan Newman algorithm: Perspective 1.3, iteration 6", dict(fontweight="bold",fontsize=22,color="black"),loc="center")

#Representación de los objetos del grafo
    #Aristas
nx.draw_networkx_edges(G_inv_ms2, pos_inv_ms2, width=edgew_inv_ms2_GN, edge_color="navy", style='-')
    #Nodos
nx.draw_networkx_nodes(G_inv_ms2, pos_inv_ms2, node_color=color_communities_inv_ms2_6, node_size=1300, node_shape='o', linewidths=1,edgecolors="black")
    #Etiquetas sobre nodos
nx.draw_networkx_labels(G_inv_ms2, pos_inv_ms2, font_size=16, bbox=dict(ec="black",boxstyle="round",facecolor="white",pad=0.3,alpha=0.6), font_weight='normal', font_family='Verdana', horizontalalignment='center', verticalalignment='center',clip_on=False)

#Modificaciones sobre el espacio de representación
x_inv_ms2_6.tight_layout()
plt.axis("off") 
y_inv_ms2_6.margins(0.05,0.05)
plt.savefig("GN-CG13-It6.png")
plt.show() 


# El resultado es análogo a la aplicación del algoritmo para la perspectiva 1.3 debido a que sólo aporta información las primeras iteraciones. Es más, para este caso, no ha sido posible llegar a la iteración 7 porque en la iteración 6 todos los nodos estaban ya aislados en una sola comunidad.

# In[146]:


communities_inv_ms2 = list(community.girvan_newman(G_inv_ms2))
communities_inv_ms2


# En este caso el resultado es el mismo que con la sentencia anterior pero se quería verificar que en ambos casos se obtenía el mismo resultado de aplicación del algoritmo.

# ### 5.2. Aplicación del algoritmo G-N a la perspectiva 2: Bajo una inversión inicial de 1000 €, estudio de la diferencia diaria del total de la inversión al cierre de la sesión

# In[147]:


list_communities_inv_ac = []
n_it_inv_ac = 7
comp_inv_ac = community.girvan_newman(G_inv_ac)
for communities in itertools.islice(comp_inv_ac, n_it_inv_ac):
    print(tuple(sorted(c) for c in communities))
    list_communities_inv_ac.append(tuple(sorted(c) for c in communities))


# In[148]:


#Iteración 1
color_communities_inv_ac_1 = []
node_communities_inv_ac_1 = list_communities_inv_ac[0]
for node in G_inv_ac:
    if node in node_communities_inv_ac_1[0]:
        color_communities_inv_ac_1.append('green')
    else:
        color_communities_inv_ac_1.append('red')  

#Grosor de las aristas
edgew_inv_ac_GN = [0.005*G_inv_ac.get_edge_data(u, v)['weight'] for u, v in G_inv_ac.edges()]
        
#Espacio de representación
x_inv_ac_1, y_inv_ac_1 = plt.subplots(figsize=(16, 16))
#Título del grafo
y_inv_ac_1.set_title("Application of Girvan Newman algorithm: Perspective 2, iteration 1", dict(fontweight="bold",fontsize=22,color="black"),loc="center")

#Representación de los objetos del grafo
    #Aristas
nx.draw_networkx_edges(G_inv_ac, pos_inv_ac, width=edgew_inv_ac_GN, edge_color="navy", style='-')
    #Nodos
nx.draw_networkx_nodes(G_inv_ac, pos_inv_ac, node_color=color_communities_inv_ac_1, node_size=1300, node_shape='o', linewidths=1,edgecolors="black")
    #Etiquetas sobre nodos
nx.draw_networkx_labels(G_inv_ac, pos_inv_ac, font_size=16, bbox=dict(ec="black",boxstyle="round",facecolor="white",pad=0.3,alpha=0.6), font_weight='normal', font_family='Verdana', horizontalalignment='center', verticalalignment='center',clip_on=False)

#Modificaciones sobre el espacio de representación
x_inv_ac_1.tight_layout()
plt.axis("off") 
y_inv_ac_1.margins(0.05,0.05)
plt.savefig("GN-CG2-It1.png")
plt.show() 


# In[149]:


#Iteración 2
color_communities_inv_ac_2 = []
node_communities_inv_ac_2 = list_communities_inv_ac[1]
for node in G_inv_ac:
    if node in node_communities_inv_ac_2[0]:
        color_communities_inv_ac_2.append('green')
    elif node in node_communities_inv_ac_2[1]:
        color_communities_inv_ac_2.append('purple')
    else:
        color_communities_inv_ac_2.append('red')  
        
#Espacio de representación
x_inv_ac_2, y_inv_ac_2 = plt.subplots(figsize=(16, 16))
#Título del grafo
y_inv_ac_2.set_title("Application of Girvan Newman algorithm: Perspective 2, iteration 2", dict(fontweight="bold",fontsize=22,color="black"),loc="center")

#Representación de los objetos del grafo
    #Aristas
nx.draw_networkx_edges(G_inv_ac, pos_inv_ac, width=edgew_inv_ac_GN, edge_color="navy", style='-')
    #Nodos
nx.draw_networkx_nodes(G_inv_ac, pos_inv_ac, node_color=color_communities_inv_ac_2, node_size=1300, node_shape='o', linewidths=1,edgecolors="black")
    #Etiquetas sobre nodos
nx.draw_networkx_labels(G_inv_ac, pos_inv_ac, font_size=16, bbox=dict(ec="black",boxstyle="round",facecolor="white",pad=0.3,alpha=0.6), font_weight='normal', font_family='Verdana', horizontalalignment='center', verticalalignment='center',clip_on=False)

#Modificaciones sobre el espacio de representación
x_inv_ac_2.tight_layout()
plt.axis("off") 
y_inv_ac_2.margins(0.05,0.05)
plt.savefig("GN-CG2-It2.png")
plt.show() 


# In[150]:


#Iteración 3
color_communities_inv_ac_3 = []
node_communities_inv_ac_3 = list_communities_inv_ac[2]
for node in G_inv_ac:
    if node in node_communities_inv_ac_3[0]:
        color_communities_inv_ac_3.append('green')
    elif node in node_communities_inv_ac_3[1]:
        color_communities_inv_ac_3.append('purple')
    elif node in node_communities_inv_ac_3[2]:
        color_communities_inv_ac_3.append('yellow')
    else:
        color_communities_inv_ac_3.append('red')  
        
#Espacio de representación
x_inv_ac_3, y_inv_ac_3 = plt.subplots(figsize=(16, 16))
#Título del grafo
y_inv_ac_3.set_title("Application of Girvan Newman algorithm: Perspective 2, iteration 3", dict(fontweight="bold",fontsize=22,color="black"),loc="center")

#Representación de los objetos del grafo
    #Aristas
nx.draw_networkx_edges(G_inv_ac, pos_inv_ac, width=edgew_inv_ac_GN, edge_color="navy", style='-')
    #Nodos
nx.draw_networkx_nodes(G_inv_ac, pos_inv_ac, node_color=color_communities_inv_ac_3, node_size=1300, node_shape='o', linewidths=1,edgecolors="black")
    #Etiquetas sobre nodos
nx.draw_networkx_labels(G_inv_ac, pos_inv_ac, font_size=16, bbox=dict(ec="black",boxstyle="round",facecolor="white",pad=0.3,alpha=0.6), font_weight='normal', font_family='Verdana', horizontalalignment='center', verticalalignment='center',clip_on=False)

#Modificaciones sobre el espacio de representación
x_inv_ac_3.tight_layout()
plt.axis("off") 
y_inv_ac_3.margins(0.05,0.05)
plt.savefig("GN-CG2-It3.png")
plt.show() 


# In[151]:


#Iteración 4
color_communities_inv_ac_4 = []
node_communities_inv_ac_4 = list_communities_inv_ac[3]
for node in G_inv_ac:
    if node in node_communities_inv_ac_4[0]:
        color_communities_inv_ac_4.append('green')
    elif node in node_communities_inv_ac_4[1]:
        color_communities_inv_ac_4.append('purple')
    elif node in node_communities_inv_ac_4[2]:
        color_communities_inv_ac_4.append('yellow')
    elif node in node_communities_inv_ac_4[3]:
        color_communities_inv_ac_4.append('orange')
    else:
        color_communities_inv_ac_4.append('red')  
        
#Espacio de representación
x_inv_ac_4, y_inv_ac_4 = plt.subplots(figsize=(16, 16))
#Título del grafo
y_inv_ac_4.set_title("Application of Girvan Newman algorithm: Perspective 2, iteration 4", dict(fontweight="bold",fontsize=22,color="black"),loc="center")

#Representación de los objetos del grafo
    #Aristas
nx.draw_networkx_edges(G_inv_ac, pos_inv_ac, width=edgew_inv_ac_GN, edge_color="navy", style='-')
    #Nodos
nx.draw_networkx_nodes(G_inv_ac, pos_inv_ac, node_color=color_communities_inv_ac_4, node_size=1300, node_shape='o', linewidths=1,edgecolors="black")
    #Etiquetas sobre nodos
nx.draw_networkx_labels(G_inv_ac, pos_inv_ac, font_size=16, bbox=dict(ec="black",boxstyle="round",facecolor="white",pad=0.3,alpha=0.6), font_weight='normal', font_family='Verdana', horizontalalignment='center', verticalalignment='center',clip_on=False)

#Modificaciones sobre el espacio de representación
x_inv_ac_4.tight_layout()
plt.axis("off") 
y_inv_ac_4.margins(0.05,0.05)
plt.savefig("GN-CG2-It4.png")
plt.show() 


# In[152]:


#Iteración 5
color_communities_inv_ac_5 = []
node_communities_inv_ac_5 = list_communities_inv_ac[4]
for node in G_inv_ac:
    if node in node_communities_inv_ac_5[0]:
        color_communities_inv_ac_5.append('green')
    elif node in node_communities_inv_ac_5[1]:
        color_communities_inv_ac_5.append('purple')
    elif node in node_communities_inv_ac_5[2]:
        color_communities_inv_ac_5.append('yellow')
    elif node in node_communities_inv_ac_5[3]:
        color_communities_inv_ac_5.append('orange')
    elif node in node_communities_inv_ac_5[4]:
        color_communities_inv_ac_5.append('deeppink')
    else:
        color_communities_inv_ac_5.append('red')  
        
#Espacio de representación
x_inv_ac_5, y_inv_ac_5 = plt.subplots(figsize=(16, 16))
#Título del grafo
y_inv_ac_5.set_title("Application of Girvan Newman algorithm: Perspective 2, iteration 5", dict(fontweight="bold",fontsize=22,color="black"),loc="center")

#Representación de los objetos del grafo
    #Aristas
nx.draw_networkx_edges(G_inv_ac, pos_inv_ac, width=edgew_inv_ac_GN, edge_color="navy", style='-')
    #Nodos
nx.draw_networkx_nodes(G_inv_ac, pos_inv_ac, node_color=color_communities_inv_ac_5, node_size=1300, node_shape='o', linewidths=1,edgecolors="black")
    #Etiquetas sobre nodos
nx.draw_networkx_labels(G_inv_ac, pos_inv_ac, font_size=16, bbox=dict(ec="black",boxstyle="round",facecolor="white",pad=0.3,alpha=0.6), font_weight='normal', font_family='Verdana', horizontalalignment='center', verticalalignment='center',clip_on=False)

#Modificaciones sobre el espacio de representación
x_inv_ac_5.tight_layout()
plt.axis("off") 
y_inv_ac_5.margins(0.05,0.05)
plt.savefig("GN-CG2-It5.png")
plt.show() 


# In[153]:


#Iteración 6
color_communities_inv_ac_6 = []
node_communities_inv_ac_6 = list_communities_inv_ac[5]
for node in G_inv_ac:
    if node in node_communities_inv_ac_6[0]:
        color_communities_inv_ac_6.append('green')
    elif node in node_communities_inv_ac_6[1]:
        color_communities_inv_ac_6.append('purple')
    elif node in node_communities_inv_ac_6[2]:
        color_communities_inv_ac_6.append('yellow')
    elif node in node_communities_inv_ac_6[3]:
        color_communities_inv_ac_6.append('orange')
    elif node in node_communities_inv_ac_6[4]:
        color_communities_inv_ac_6.append('deeppink')
    elif node in node_communities_inv_ac_6[5]:
        color_communities_inv_ac_6.append('cyan')
    else:
        color_communities_inv_ac_6.append('red')  
        
#Espacio de representación
x_inv_ac_6, y_inv_ac_6 = plt.subplots(figsize=(16, 16))
#Título del grafo
y_inv_ac_6.set_title("Application of Girvan Newman algorithm: Perspective 2, iteration 6", dict(fontweight="bold",fontsize=22,color="black"),loc="center")

#Representación de los objetos del grafo
    #Aristas
nx.draw_networkx_edges(G_inv_ac, pos_inv_ac, width=edgew_inv_ac_GN, edge_color="navy", style='-')
    #Nodos
nx.draw_networkx_nodes(G_inv_ac, pos_inv_ac, node_color=color_communities_inv_ac_6, node_size=1300, node_shape='o', linewidths=1,edgecolors="black")
    #Etiquetas sobre nodos
nx.draw_networkx_labels(G_inv_ac, pos_inv_ac, font_size=16, bbox=dict(ec="black",boxstyle="round",facecolor="white",pad=0.3,alpha=0.6), font_weight='normal', font_family='Verdana', horizontalalignment='center', verticalalignment='center',clip_on=False)

#Modificaciones sobre el espacio de representación
x_inv_ac_6.tight_layout()
plt.axis("off") 
y_inv_ac_6.margins(0.05,0.05)
plt.savefig("GN-CG2-It6.png")
plt.show() 


# In[154]:


#Iteración 7
color_communities_inv_ac_7 = []
node_communities_inv_ac_7 = list_communities_inv_ac[6]
for node in G_inv_ac:
    if node in node_communities_inv_ac_7[0]:
        color_communities_inv_ac_7.append('green')
    elif node in node_communities_inv_ac_7[1]:
        color_communities_inv_ac_7.append('purple')
    elif node in node_communities_inv_ac_7[2]:
        color_communities_inv_ac_7.append('yellow')
    elif node in node_communities_inv_ac_7[3]:
        color_communities_inv_ac_7.append('orange')
    elif node in node_communities_inv_ac_7[4]:
        color_communities_inv_ac_7.append('deeppink')
    elif node in node_communities_inv_ac_7[5]:
        color_communities_inv_ac_7.append('cyan')
    elif node in node_communities_inv_ac_7[6]:
        color_communities_inv_ac_7.append('lime')
    else:
        color_communities_inv_ac_7.append('red')  
        
#Espacio de representación
x_inv_ac_7, y_inv_ac_7 = plt.subplots(figsize=(16, 16))
#Título del grafo
y_inv_ac_7.set_title("Application of Girvan Newman algorithm: Perspective 2, iteration 7", dict(fontweight="bold",fontsize=22,color="black"),loc="center")

#Representación de los objetos del grafo
    #Aristas
nx.draw_networkx_edges(G_inv_ac, pos_inv_ac, width=edgew_inv_ac_GN, edge_color="navy", style='-')
    #Nodos
nx.draw_networkx_nodes(G_inv_ac, pos_inv_ac, node_color=color_communities_inv_ac_7, node_size=1300, node_shape='o', linewidths=1,edgecolors="black")
    #Etiquetas sobre nodos
nx.draw_networkx_labels(G_inv_ac, pos_inv_ac, font_size=16, bbox=dict(ec="black",boxstyle="round",facecolor="white",pad=0.3,alpha=0.6), font_weight='normal', font_family='Verdana', horizontalalignment='center', verticalalignment='center',clip_on=False)

#Modificaciones sobre el espacio de representación
x_inv_ac_7.tight_layout()
plt.axis("off") 
y_inv_ac_7.margins(0.05,0.05)
plt.savefig("GN-CG2-It7.png")
plt.show() 


# Tras la aplicación del algoritmo, las iteraciones realizan el mismo funcionamiento, van generando comunidades de nodos aislados. En este caso, además, las comunidades se van generando en el orden de los nodos por lo que, unido al hecho anterior, este grafo no permite extraer información concluyente de la situación.

# In[155]:


communities_inv_ac = list(community.girvan_newman(G_inv_ac))
communities_inv_ac


# Las iteraciones sucesivas del algoritmo son las comentadas anteriormente, por lo que este caso no aporta información al estudio.

# #### 5.2.1. Aplicación del algoritmo G-N a la perspectiva 2.1:  Bajo una inversión inicial de 1000 €, estudio de la diferencia diaria del total de la inversión al cierre de la sesión para aquellas empresas que se crucen más que la media del total de pesos de las aristas del grafo

# In[156]:


list_communities_inv_ac_avg = []
n_it_inv_ac_avg = 7
comp_inv_ac_avg = community.girvan_newman(G_inv_ac_avg)
for communities in itertools.islice(comp_inv_ac_avg, n_it_inv_ac_avg):
    print(tuple(sorted(c) for c in communities))
    list_communities_inv_ac_avg.append(tuple(sorted(c) for c in communities))


# In[157]:


#Iteración 1
color_communities_inv_ac_avg_1 = []
node_communities_inv_ac_avg_1 = list_communities_inv_ac_avg[0]
for node in G_inv_ac_avg:
    if node in node_communities_inv_ac_avg_1[0]:
        color_communities_inv_ac_avg_1.append('red')
    else:
        color_communities_inv_ac_avg_1.append('green')  

#Grosor de las aristas
edgew_inv_ac_avg_GN = [0.2*G_inv_ac_avg.get_edge_data(u, v)['weight'] for u, v in G_inv_ac_avg.edges()]
        
#Espacio de representación
x_inv_ac_avg_1, y_inv_ac_avg_1 = plt.subplots(figsize=(16, 16))
#Título del grafo
y_inv_ac_avg_1.set_title("Application of Girvan Newman algorithm: Perspective 2.1, iteration 1", dict(fontweight="bold",fontsize=22,color="black"),loc="center")

#Representación de los objetos del grafo
    #Aristas
nx.draw_networkx_edges(G_inv_ac_avg, pos_inv_ac_avg, width=edgew_inv_ac_avg_GN, edge_color="navy", style='-')
    #Nodos
nx.draw_networkx_nodes(G_inv_ac_avg, pos_inv_ac_avg, node_color=color_communities_inv_ac_avg_1, node_size=1300, node_shape='o', linewidths=1,edgecolors="black")
    #Etiquetas sobre nodos
nx.draw_networkx_labels(G_inv_ac_avg, pos_inv_ac_avg, font_size=16, bbox=dict(ec="black",boxstyle="round",facecolor="white",pad=0.3,alpha=0.6), font_weight='normal', font_family='Verdana', horizontalalignment='center', verticalalignment='center',clip_on=False)

#Modificaciones sobre el espacio de representación
x_inv_ac_avg_1.tight_layout()
plt.axis("off") 
y_inv_ac_avg_1.margins(0.05,0.05)
plt.savefig("GN-CG21-It1.png")
plt.show() 


# In[158]:


#Iteración 2
color_communities_inv_ac_avg_2 = []
node_communities_inv_ac_avg_2 = list_communities_inv_ac_avg[1]
for node in G_inv_ac_avg:
    if node in node_communities_inv_ac_avg_2[0]:
        color_communities_inv_ac_avg_2.append('red')
    elif node in node_communities_inv_ac_avg_2[1]:
        color_communities_inv_ac_avg_2.append('green')
    else:
        color_communities_inv_ac_avg_2.append('purple')  
        
#Espacio de representación
x_inv_ac_avg_2, y_inv_ac_avg_2 = plt.subplots(figsize=(16, 16))
#Título del grafo
y_inv_ac_avg_2.set_title("Application of Girvan Newman algorithm: Perspective 2.1, iteration 2", dict(fontweight="bold",fontsize=22,color="black"),loc="center")

#Representación de los objetos del grafo
    #Aristas
nx.draw_networkx_edges(G_inv_ac_avg, pos_inv_ac_avg, width=edgew_inv_ac_avg_GN, edge_color="navy", style='-')
    #Nodos
nx.draw_networkx_nodes(G_inv_ac_avg, pos_inv_ac_avg, node_color=color_communities_inv_ac_avg_2, node_size=1300, node_shape='o', linewidths=1,edgecolors="black")
    #Etiquetas sobre nodos
nx.draw_networkx_labels(G_inv_ac_avg, pos_inv_ac_avg, font_size=16, bbox=dict(ec="black",boxstyle="round",facecolor="white",pad=0.3,alpha=0.6), font_weight='normal', font_family='Verdana', horizontalalignment='center', verticalalignment='center',clip_on=False)

#Modificaciones sobre el espacio de representación
x_inv_ac_avg_2.tight_layout()
plt.axis("off") 
y_inv_ac_avg_2.margins(0.05,0.05)
plt.savefig("GN-CG21-It2.png")
plt.show() 


# In[159]:


#Iteración 3
color_communities_inv_ac_avg_3 = []
node_communities_inv_ac_avg_3 = list_communities_inv_ac_avg[2]
for node in G_inv_ac_avg:
    if node in node_communities_inv_ac_avg_3[0]:
        color_communities_inv_ac_avg_3.append('red')
    elif node in node_communities_inv_ac_avg_3[1]:
        color_communities_inv_ac_avg_3.append('green')
    elif node in node_communities_inv_ac_avg_3[2]:
        color_communities_inv_ac_avg_3.append('yellow')
    else:
        color_communities_inv_ac_avg_3.append('purple')  
        
#Espacio de representación
x_inv_ac_avg_3, y_inv_ac_avg_3 = plt.subplots(figsize=(16, 16))
#Título del grafo
y_inv_ac_avg_3.set_title("Application of Girvan Newman algorithm: Perspective 2.1, iteration 3", dict(fontweight="bold",fontsize=22,color="black"),loc="center")

#Representación de los objetos del grafo
    #Aristas
nx.draw_networkx_edges(G_inv_ac_avg, pos_inv_ac_avg, width=edgew_inv_ac_avg_GN, edge_color="navy", style='-')
    #Nodos
nx.draw_networkx_nodes(G_inv_ac_avg, pos_inv_ac_avg, node_color=color_communities_inv_ac_avg_3, node_size=1300, node_shape='o', linewidths=1,edgecolors="black")
    #Etiquetas sobre nodos
nx.draw_networkx_labels(G_inv_ac_avg, pos_inv_ac_avg, font_size=16, bbox=dict(ec="black",boxstyle="round",facecolor="white",pad=0.3,alpha=0.6), font_weight='normal', font_family='Verdana', horizontalalignment='center', verticalalignment='center',clip_on=False)

#Modificaciones sobre el espacio de representación
x_inv_ac_avg_3.tight_layout()
plt.axis("off") 
y_inv_ac_avg_3.margins(0.05,0.05)
plt.savefig("GN-CG21-It3.png")
plt.show() 


# In[160]:


#Iteración 4
color_communities_inv_ac_avg_4 = []
node_communities_inv_ac_avg_4 = list_communities_inv_ac_avg[3]
for node in G_inv_ac_avg:
    if node in node_communities_inv_ac_avg_4[0]:
        color_communities_inv_ac_avg_4.append('red')
    elif node in node_communities_inv_ac_avg_4[1]:
        color_communities_inv_ac_avg_4.append('green')
    elif node in node_communities_inv_ac_avg_4[2]:
        color_communities_inv_ac_avg_4.append('yellow')
    elif node in node_communities_inv_ac_avg_4[3]:
        color_communities_inv_ac_avg_4.append('orange')
    else:
        color_communities_inv_ac_avg_4.append('purple')  
        
#Espacio de representación
x_inv_ac_avg_4, y_inv_ac_avg_4 = plt.subplots(figsize=(16, 16))
#Título del grafo
y_inv_ac_avg_4.set_title("Application of Girvan Newman algorithm: Perspective 2.1, iteration 4", dict(fontweight="bold",fontsize=22,color="black"),loc="center")

#Representación de los objetos del grafo
    #Aristas
nx.draw_networkx_edges(G_inv_ac_avg, pos_inv_ac_avg, width=edgew_inv_ac_avg_GN, edge_color="navy", style='-')
    #Nodos
nx.draw_networkx_nodes(G_inv_ac_avg, pos_inv_ac_avg, node_color=color_communities_inv_ac_avg_4, node_size=1300, node_shape='o', linewidths=1,edgecolors="black")
    #Etiquetas sobre nodos
nx.draw_networkx_labels(G_inv_ac_avg, pos_inv_ac_avg, font_size=16, bbox=dict(ec="black",boxstyle="round",facecolor="white",pad=0.3,alpha=0.6), font_weight='normal', font_family='Verdana', horizontalalignment='center', verticalalignment='center',clip_on=False)

#Modificaciones sobre el espacio de representación
x_inv_ac_avg_4.tight_layout()
plt.axis("off") 
y_inv_ac_avg_4.margins(0.05,0.05)
plt.savefig("GN-CG21-It4.png")
plt.show() 


# In[161]:


#Iteración 5
color_communities_inv_ac_avg_5 = []
node_communities_inv_ac_avg_5 = list_communities_inv_ac_avg[4]
for node in G_inv_ac_avg:
    if node in node_communities_inv_ac_avg_5[0]:
        color_communities_inv_ac_avg_5.append('red')
    elif node in node_communities_inv_ac_avg_5[1]:
        color_communities_inv_ac_avg_5.append('green')
    elif node in node_communities_inv_ac_avg_5[2]:
        color_communities_inv_ac_avg_5.append('deeppink')
    elif node in node_communities_inv_ac_avg_5[3]:
        color_communities_inv_ac_avg_5.append('yellow')
    elif node in node_communities_inv_ac_avg_5[4]:
        color_communities_inv_ac_avg_5.append('orange')
    else:
        color_communities_inv_ac_avg_5.append('purple')  
        
#Espacio de representación
x_inv_ac_avg_5, y_inv_ac_avg_5 = plt.subplots(figsize=(16, 16))
#Título del grafo
y_inv_ac_avg_5.set_title("Application of Girvan Newman algorithm: Perspective 2.1, iteration 5", dict(fontweight="bold",fontsize=22,color="black"),loc="center")

#Representación de los objetos del grafo
    #Aristas
nx.draw_networkx_edges(G_inv_ac_avg, pos_inv_ac_avg, width=edgew_inv_ac_avg_GN, edge_color="navy", style='-')
    #Nodos
nx.draw_networkx_nodes(G_inv_ac_avg, pos_inv_ac_avg, node_color=color_communities_inv_ac_avg_5, node_size=1300, node_shape='o', linewidths=1,edgecolors="black")
    #Etiquetas sobre nodos
nx.draw_networkx_labels(G_inv_ac_avg, pos_inv_ac_avg, font_size=16, bbox=dict(ec="black",boxstyle="round",facecolor="white",pad=0.3,alpha=0.6), font_weight='normal', font_family='Verdana', horizontalalignment='center', verticalalignment='center',clip_on=False)

#Modificaciones sobre el espacio de representación
x_inv_ac_avg_5.tight_layout()
plt.axis("off") 
y_inv_ac_avg_5.margins(0.05,0.05)
plt.savefig("GN-CG21-It5.png")
plt.show() 


# In[162]:


#Iteración 6
color_communities_inv_ac_avg_6 = []
node_communities_inv_ac_avg_6 = list_communities_inv_ac_avg[5]
for node in G_inv_ac_avg:
    if node in node_communities_inv_ac_avg_6[0]:
        color_communities_inv_ac_avg_6.append('red')
    elif node in node_communities_inv_ac_avg_6[1]:
        color_communities_inv_ac_avg_6.append('green')
    elif node in node_communities_inv_ac_avg_6[2]:
        color_communities_inv_ac_avg_6.append('deeppink')
    elif node in node_communities_inv_ac_avg_6[3]:
        color_communities_inv_ac_avg_6.append('cyan')
    elif node in node_communities_inv_ac_avg_6[4]:
        color_communities_inv_ac_avg_6.append('yellow')
    elif node in node_communities_inv_ac_avg_6[5]:
        color_communities_inv_ac_avg_6.append('orange')
    else:
        color_communities_inv_ac_avg_6.append('purple')  
        
#Espacio de representación
x_inv_ac_avg_6, y_inv_ac_avg_6 = plt.subplots(figsize=(16, 16))
#Título del grafo
y_inv_ac_avg_6.set_title("Application of Girvan Newman algorithm: Perspective 2.1, iteration 6", dict(fontweight="bold",fontsize=22,color="black"),loc="center")

#Representación de los objetos del grafo
    #Aristas
nx.draw_networkx_edges(G_inv_ac_avg, pos_inv_ac_avg, width=edgew_inv_ac_avg_GN, edge_color="navy", style='-')
    #Nodos
nx.draw_networkx_nodes(G_inv_ac_avg, pos_inv_ac_avg, node_color=color_communities_inv_ac_avg_6, node_size=1300, node_shape='o', linewidths=1,edgecolors="black")
    #Etiquetas sobre nodos
nx.draw_networkx_labels(G_inv_ac_avg, pos_inv_ac_avg, font_size=16, bbox=dict(ec="black",boxstyle="round",facecolor="white",pad=0.3,alpha=0.6), font_weight='normal', font_family='Verdana', horizontalalignment='center', verticalalignment='center',clip_on=False)

#Modificaciones sobre el espacio de representación
x_inv_ac_avg_6.tight_layout()
plt.axis("off") 
y_inv_ac_avg_6.margins(0.05,0.05)
plt.savefig("GN-CG21-It6.png")
plt.show() 


# In[163]:


#Iteración 7
color_communities_inv_ac_avg_7 = []
node_communities_inv_ac_avg_7 = list_communities_inv_ac_avg[6]
for node in G_inv_ac_avg:
    if node in node_communities_inv_ac_avg_7[0]:
        color_communities_inv_ac_avg_7.append('red')
    elif node in node_communities_inv_ac_avg_7[1]:
        color_communities_inv_ac_avg_7.append('green')
    elif node in node_communities_inv_ac_avg_7[2]:
        color_communities_inv_ac_avg_7.append('deeppink')
    elif node in node_communities_inv_ac_avg_7[3]:
        color_communities_inv_ac_avg_7.append('cyan')
    elif node in node_communities_inv_ac_avg_7[4]:
        color_communities_inv_ac_avg_7.append('lime')
    elif node in node_communities_inv_ac_avg_7[5]:
        color_communities_inv_ac_avg_7.append('yellow')
    elif node in node_communities_inv_ac_avg_7[6]:
        color_communities_inv_ac_avg_7.append('orange')
    else:
        color_communities_inv_ac_avg_7.append('purple')  
        
#Espacio de representación
x_inv_ac_avg_7, y_inv_ac_avg_7 = plt.subplots(figsize=(16, 16))
#Título del grafo
y_inv_ac_avg_7.set_title("Application of Girvan Newman algorithm: Perspective 2.1, iteration 7", dict(fontweight="bold",fontsize=22,color="black"),loc="center")

#Representación de los objetos del grafo
    #Aristas
nx.draw_networkx_edges(G_inv_ac_avg, pos_inv_ac_avg, width=edgew_inv_ac_avg_GN, edge_color="navy", style='-')
    #Nodos
nx.draw_networkx_nodes(G_inv_ac_avg, pos_inv_ac_avg, node_color=color_communities_inv_ac_avg_7, node_size=1300, node_shape='o', linewidths=1,edgecolors="black")
    #Etiquetas sobre nodos
nx.draw_networkx_labels(G_inv_ac_avg, pos_inv_ac_avg, font_size=16, bbox=dict(ec="black",boxstyle="round",facecolor="white",pad=0.3,alpha=0.6), font_weight='normal', font_family='Verdana', horizontalalignment='center', verticalalignment='center',clip_on=False)

#Modificaciones sobre el espacio de representación
x_inv_ac_avg_7.tight_layout()
plt.axis("off") 
y_inv_ac_avg_7.margins(0.05,0.05)
plt.savefig("GN-CG21-It7.png")
plt.show() 


# Tras las representaciones, el funcionamiento del algoritmo es el mimso que para el caso 2 pero las comunidades no se forman de manera ordenada. De nuevo, esta situación no permite extraer información concluyente.

# In[164]:


communities_inv_ac_avg = list(community.girvan_newman(G_inv_ac_avg))
communities_inv_ac_avg


# Comentarios análogos a las primeras iteraciones.

# #### 5.2.2. Aplicación del algoritmo G-N a la perspectiva 2.2:  Bajo una inversión inicial de 1000 €, estudio de la diferencia diaria del total de la inversión al cierre de la sesión para aquellas empresas que se crucen más que la medida 1 del total de pesos de las aristas del grafo

# In[165]:


list_communities_inv_ac_ms1 = []
n_it_inv_ac_ms1 = 7
comp_inv_ac_ms1 = community.girvan_newman(G_inv_ac_ms1)
for communities in itertools.islice(comp_inv_ac_ms1, n_it_inv_ac_ms1):
    print(tuple(sorted(c) for c in communities))
    list_communities_inv_ac_ms1.append(tuple(sorted(c) for c in communities))


# In[166]:


#Iteración 1
color_communities_inv_ac_ms1_1 = []
node_communities_inv_ac_ms1_1 = list_communities_inv_ac_ms1[0]
for node in G_inv_ac_ms1:
    if node in node_communities_inv_ac_ms1_1[0]:
        color_communities_inv_ac_ms1_1.append('red')
    elif node in node_communities_inv_ac_ms1_1[2]:
        color_communities_inv_ac_ms1_1.append('green')
    else:
        color_communities_inv_ac_ms1_1.append('white')  

#Grosor de las aristas
edgew_inv_ac_ms1_GN = [0.8*G_inv_ac_ms1.get_edge_data(u, v)['weight'] for u, v in G_inv_ac_ms1.edges()]
        
#Espacio de representación
x_inv_ac_ms1_1, y_inv_ac_ms1_1 = plt.subplots(figsize=(16, 16))
#Título del grafo
y_inv_ac_ms1_1.set_title("Application of Girvan Newman algorithm: Perspective 2.2, iteration 1", dict(fontweight="bold",fontsize=22,color="black"),loc="center")

#Representación de los objetos del grafo
    #Aristas
nx.draw_networkx_edges(G_inv_ac_ms1, pos_inv_ac_ms1, width=edgew_inv_ac_ms1_GN, edge_color="navy", style='-')
    #Nodos
nx.draw_networkx_nodes(G_inv_ac_ms1, pos_inv_ac_ms1, node_color=color_communities_inv_ac_ms1_1, node_size=1300, node_shape='o', linewidths=1,edgecolors="black")
    #Etiquetas sobre nodos
nx.draw_networkx_labels(G_inv_ac_ms1, pos_inv_ac_ms1, font_size=16, bbox=dict(ec="black",boxstyle="round",facecolor="white",pad=0.3,alpha=0.6), font_weight='normal', font_family='Verdana', horizontalalignment='center', verticalalignment='center',clip_on=False)

#Modificaciones sobre el espacio de representación
x_inv_ac_ms1_1.tight_layout()
plt.axis("off") 
y_inv_ac_ms1_1.margins(0.05,0.05)
plt.savefig("GN-CG22-It1.png")
plt.show() 


# In[167]:


#Iteración 2
color_communities_inv_ac_ms1_2 = []
node_communities_inv_ac_ms1_2 = list_communities_inv_ac_ms1[1]
for node in G_inv_ac_ms1:
    if node in node_communities_inv_ac_ms1_2[0]:
        color_communities_inv_ac_ms1_2.append('red')
    elif node in node_communities_inv_ac_ms1_2[2]:
        color_communities_inv_ac_ms1_2.append('green')
    elif node in node_communities_inv_ac_ms1_2[3]:
        color_communities_inv_ac_ms1_2.append('purple')
    else:
        color_communities_inv_ac_ms1_2.append('white')  
        
#Espacio de representación
x_inv_ac_ms1_2, y_inv_ac_ms1_2 = plt.subplots(figsize=(16, 16))
#Título del grafo
y_inv_ac_ms1_2.set_title("Application of Girvan Newman algorithm: Perspective 2.2, iteration 2", dict(fontweight="bold",fontsize=22,color="black"),loc="center")

#Representación de los objetos del grafo
    #Aristas
nx.draw_networkx_edges(G_inv_ac_ms1, pos_inv_ac_ms1, width=edgew_inv_ac_ms1_GN, edge_color="navy", style='-')
    #Nodos
nx.draw_networkx_nodes(G_inv_ac_ms1, pos_inv_ac_ms1, node_color=color_communities_inv_ac_ms1_2, node_size=1300, node_shape='o', linewidths=1,edgecolors="black")
    #Etiquetas sobre nodos
nx.draw_networkx_labels(G_inv_ac_ms1, pos_inv_ac_ms1, font_size=16, bbox=dict(ec="black",boxstyle="round",facecolor="white",pad=0.3,alpha=0.6), font_weight='normal', font_family='Verdana', horizontalalignment='center', verticalalignment='center',clip_on=False)

#Modificaciones sobre el espacio de representación
x_inv_ac_ms1_2.tight_layout()
plt.axis("off") 
y_inv_ac_ms1_2.margins(0.05,0.05)
plt.savefig("GN-CG22-It2.png")
plt.show() 


# In[168]:


#Iteración 3
color_communities_inv_ac_ms1_3 = []
node_communities_inv_ac_ms1_3 = list_communities_inv_ac_ms1[2]
for node in G_inv_ac_ms1:
    if node in node_communities_inv_ac_ms1_3[0]:
        color_communities_inv_ac_ms1_3.append('red')
    elif node in node_communities_inv_ac_ms1_3[2]:
        color_communities_inv_ac_ms1_3.append('green')
    elif node in node_communities_inv_ac_ms1_3[3]:
        color_communities_inv_ac_ms1_3.append('yellow')
    elif node in node_communities_inv_ac_ms1_3[4]:
        color_communities_inv_ac_ms1_3.append('purple')
    else:
        color_communities_inv_ac_ms1_3.append('white')  
        
#Espacio de representación
x_inv_ac_ms1_3, y_inv_ac_ms1_3 = plt.subplots(figsize=(16, 16))
#Título del grafo
y_inv_ac_ms1_3.set_title("Application of Girvan Newman algorithm: Perspective 2.2, iteration 3", dict(fontweight="bold",fontsize=22,color="black"),loc="center")

#Representación de los objetos del grafo
    #Aristas
nx.draw_networkx_edges(G_inv_ac_ms1, pos_inv_ac_ms1, width=edgew_inv_ac_ms1_GN, edge_color="navy", style='-')
    #Nodos
nx.draw_networkx_nodes(G_inv_ac_ms1, pos_inv_ac_ms1, node_color=color_communities_inv_ac_ms1_3, node_size=1300, node_shape='o', linewidths=1,edgecolors="black")
    #Etiquetas sobre nodos
nx.draw_networkx_labels(G_inv_ac_ms1, pos_inv_ac_ms1, font_size=16, bbox=dict(ec="black",boxstyle="round",facecolor="white",pad=0.3,alpha=0.6), font_weight='normal', font_family='Verdana', horizontalalignment='center', verticalalignment='center',clip_on=False)

#Modificaciones sobre el espacio de representación
x_inv_ac_ms1_3.tight_layout()
plt.axis("off") 
y_inv_ac_ms1_3.margins(0.05,0.05)
plt.savefig("GN-CG22-It3.png")
plt.show() 


# In[169]:


#Iteración 4
color_communities_inv_ac_ms1_4 = []
node_communities_inv_ac_ms1_4 = list_communities_inv_ac_ms1[3]
for node in G_inv_ac_ms1:
    if node in node_communities_inv_ac_ms1_4[0]:
        color_communities_inv_ac_ms1_4.append('red')
    elif node in node_communities_inv_ac_ms1_4[2]:
        color_communities_inv_ac_ms1_4.append('green')
    elif node in node_communities_inv_ac_ms1_4[3]:
        color_communities_inv_ac_ms1_4.append('yellow')
    elif node in node_communities_inv_ac_ms1_4[4]:
        color_communities_inv_ac_ms1_4.append('purple')
    elif node in node_communities_inv_ac_ms1_4[6]:
        color_communities_inv_ac_ms1_4.append('orange')
    else:
        color_communities_inv_ac_ms1_4.append('white')  
        
#Espacio de representación
x_inv_ac_ms1_4, y_inv_ac_ms1_4 = plt.subplots(figsize=(16, 16))
#Título del grafo
y_inv_ac_ms1_4.set_title("Application of Girvan Newman algorithm: Perspective 2.2, iteration 4", dict(fontweight="bold",fontsize=22,color="black"),loc="center")

#Representación de los objetos del grafo
    #Aristas
nx.draw_networkx_edges(G_inv_ac_ms1, pos_inv_ac_ms1, width=edgew_inv_ac_ms1_GN, edge_color="navy", style='-')
    #Nodos
nx.draw_networkx_nodes(G_inv_ac_ms1, pos_inv_ac_ms1, node_color=color_communities_inv_ac_ms1_4, node_size=1300, node_shape='o', linewidths=1,edgecolors="black")
    #Etiquetas sobre nodos
nx.draw_networkx_labels(G_inv_ac_ms1, pos_inv_ac_ms1, font_size=16, bbox=dict(ec="black",boxstyle="round",facecolor="white",pad=0.3,alpha=0.6), font_weight='normal', font_family='Verdana', horizontalalignment='center', verticalalignment='center',clip_on=False)

#Modificaciones sobre el espacio de representación
x_inv_ac_ms1_4.tight_layout()
plt.axis("off") 
y_inv_ac_ms1_4.margins(0.05,0.05)
plt.savefig("GN-CG22-It4.png")
plt.show() 


# In[170]:


#Iteración 5
color_communities_inv_ac_ms1_5 = []
node_communities_inv_ac_ms1_5 = list_communities_inv_ac_ms1[4]
for node in G_inv_ac_ms1:
    if node in node_communities_inv_ac_ms1_5[0]:
        color_communities_inv_ac_ms1_5.append('red')
    elif node in node_communities_inv_ac_ms1_5[2]:
        color_communities_inv_ac_ms1_5.append('green')
    elif node in node_communities_inv_ac_ms1_5[3]:
        color_communities_inv_ac_ms1_5.append('yellow')
    elif node in node_communities_inv_ac_ms1_5[4]:
        color_communities_inv_ac_ms1_5.append('purple')
    elif node in node_communities_inv_ac_ms1_5[6]:
        color_communities_inv_ac_ms1_5.append('deeppink')
    elif node in node_communities_inv_ac_ms1_5[7]:
        color_communities_inv_ac_ms1_5.append('orange')
    else:
        color_communities_inv_ac_ms1_5.append('white')  
        
#Espacio de representación
x_inv_ac_ms1_5, y_inv_ac_ms1_5 = plt.subplots(figsize=(16, 16))
#Título del grafo
y_inv_ac_ms1_5.set_title("Application of Girvan Newman algorithm: Perspective 2.2, iteration 5", dict(fontweight="bold",fontsize=22,color="black"),loc="center")

#Representación de los objetos del grafo
    #Aristas
nx.draw_networkx_edges(G_inv_ac_ms1, pos_inv_ac_ms1, width=edgew_inv_ac_ms1_GN, edge_color="navy", style='-')
    #Nodos
nx.draw_networkx_nodes(G_inv_ac_ms1, pos_inv_ac_ms1, node_color=color_communities_inv_ac_ms1_5, node_size=1300, node_shape='o', linewidths=1,edgecolors="black")
    #Etiquetas sobre nodos
nx.draw_networkx_labels(G_inv_ac_ms1, pos_inv_ac_ms1, font_size=16, bbox=dict(ec="black",boxstyle="round",facecolor="white",pad=0.3,alpha=0.6), font_weight='normal', font_family='Verdana', horizontalalignment='center', verticalalignment='center',clip_on=False)

#Modificaciones sobre el espacio de representación
x_inv_ac_ms1_5.tight_layout()
plt.axis("off") 
y_inv_ac_ms1_5.margins(0.05,0.05)
plt.savefig("GN-CG22-It5.png")
plt.show() 


# In[171]:


#Iteración 6
color_communities_inv_ac_ms1_6 = []
node_communities_inv_ac_ms1_6 = list_communities_inv_ac_ms1[5]
for node in G_inv_ac_ms1:
    if node in node_communities_inv_ac_ms1_6[0]:
        color_communities_inv_ac_ms1_6.append('red')
    elif node in node_communities_inv_ac_ms1_6[2]:
        color_communities_inv_ac_ms1_6.append('green')
    elif node in node_communities_inv_ac_ms1_6[3]:
        color_communities_inv_ac_ms1_6.append('yellow')
    elif node in node_communities_inv_ac_ms1_6[4]:
        color_communities_inv_ac_ms1_6.append('purple')
    elif node in node_communities_inv_ac_ms1_6[5]:
        color_communities_inv_ac_ms1_6.append('cyan')
    elif node in node_communities_inv_ac_ms1_6[7]:
        color_communities_inv_ac_ms1_6.append('deeppink')
    elif node in node_communities_inv_ac_ms1_6[8]:
        color_communities_inv_ac_ms1_6.append('orange')
    else:
        color_communities_inv_ac_ms1_6.append('white')  
        
#Espacio de representación
x_inv_ac_ms1_6, y_inv_ac_ms1_6 = plt.subplots(figsize=(16, 16))
#Título del grafo
y_inv_ac_ms1_6.set_title("Application of Girvan Newman algorithm: Perspective 2.2, iteration 6", dict(fontweight="bold",fontsize=22,color="black"),loc="center")

#Representación de los objetos del grafo
    #Aristas
nx.draw_networkx_edges(G_inv_ac_ms1, pos_inv_ac_ms1, width=edgew_inv_ac_ms1_GN, edge_color="navy", style='-')
    #Nodos
nx.draw_networkx_nodes(G_inv_ac_ms1, pos_inv_ac_ms1, node_color=color_communities_inv_ac_ms1_6, node_size=1300, node_shape='o', linewidths=1,edgecolors="black")
    #Etiquetas sobre nodos
nx.draw_networkx_labels(G_inv_ac_ms1, pos_inv_ac_ms1, font_size=16, bbox=dict(ec="black",boxstyle="round",facecolor="white",pad=0.3,alpha=0.6), font_weight='normal', font_family='Verdana', horizontalalignment='center', verticalalignment='center',clip_on=False)

#Modificaciones sobre el espacio de representación
x_inv_ac_ms1_6.tight_layout()
plt.axis("off") 
y_inv_ac_ms1_6.margins(0.05,0.05)
plt.savefig("GN-CG22-It6.png")
plt.show() 


# In[172]:


#Iteración 7
color_communities_inv_ac_ms1_7 = []
node_communities_inv_ac_ms1_7 = list_communities_inv_ac_ms1[6]
for node in G_inv_ac_ms1:
    if node in node_communities_inv_ac_ms1_7[0]:
        color_communities_inv_ac_ms1_7.append('red')
    elif node in node_communities_inv_ac_ms1_7[2]:
        color_communities_inv_ac_ms1_7.append('green')
    elif node in node_communities_inv_ac_ms1_7[3]:
        color_communities_inv_ac_ms1_7.append('yellow')
    elif node in node_communities_inv_ac_ms1_7[4]:
        color_communities_inv_ac_ms1_7.append('purple')
    elif node in node_communities_inv_ac_ms1_7[5]:
        color_communities_inv_ac_ms1_7.append('cyan')
    elif node in node_communities_inv_ac_ms1_7[7]:
        color_communities_inv_ac_ms1_7.append('lime')
    elif node in node_communities_inv_ac_ms1_7[8]:
        color_communities_inv_ac_ms1_7.append('deeppink')
    elif node in node_communities_inv_ac_ms1_7[9]:
        color_communities_inv_ac_ms1_7.append('orange')
    else:
        color_communities_inv_ac_ms1_7.append('white')  
        
#Espacio de representación
x_inv_ac_ms1_7, y_inv_ac_ms1_7 = plt.subplots(figsize=(16, 16))
#Título del grafo
y_inv_ac_ms1_7.set_title("Application of Girvan Newman algorithm: Perspective 2.2, iteration 7", dict(fontweight="bold",fontsize=22,color="black"),loc="center")

#Representación de los objetos del grafo
    #Aristas
nx.draw_networkx_edges(G_inv_ac_ms1, pos_inv_ac_ms1, width=edgew_inv_ac_ms1_GN, edge_color="navy", style='-')
    #Nodos
nx.draw_networkx_nodes(G_inv_ac_ms1, pos_inv_ac_ms1, node_color=color_communities_inv_ac_ms1_7, node_size=1300, node_shape='o', linewidths=1,edgecolors="black")
    #Etiquetas sobre nodos
nx.draw_networkx_labels(G_inv_ac_ms1, pos_inv_ac_ms1, font_size=16, bbox=dict(ec="black",boxstyle="round",facecolor="white",pad=0.3,alpha=0.6), font_weight='normal', font_family='Verdana', horizontalalignment='center', verticalalignment='center',clip_on=False)

#Modificaciones sobre el espacio de representación
x_inv_ac_ms1_7.tight_layout()
plt.axis("off") 
y_inv_ac_ms1_7.margins(0.05,0.05)
plt.savefig("GN-CG22-It7.png")
plt.show() 


# Para esta subvariante sí que aparecen aspectos interesantes. En un primer momento aparecen dos grandes comunidades con aproximadamente el mismo número de nodos y a partir de entonces se forman comunidades sucesivamente con comunidades bien diferenciadas y con varios nodos cada una. Habrá que ver qué información aporta este grafo pero hasta el momento es el más atractivo para su estudio.

# In[173]:


communities_inv_ac_ms1 = list(community.girvan_newman(G_inv_ac_ms1))
communities_inv_ac_ms1


# A partir de las representaciones anteriores, las siguientes iteeraciones del algoritmo se basan en la creación de comunidades con un solo nodo a partir de las generadas en las primeras iteraciones.

# #### 5.2.3. Aplicación del algoritmo G-N a la perspectiva 2.3:  Bajo una inversión inicial de 1000 €, estudio de la diferencia diaria del total de la inversión al cierre de la sesión para aquellas empresas que se crucen más que la medida 2 del total de pesos de las aristas del grafo

# In[174]:


list_communities_inv_ac_ms2 = []
n_it_inv_ac_ms2 = 7
comp_inv_ac_ms2 = community.girvan_newman(G_inv_ac_ms2)
for communities in itertools.islice(comp_inv_ac_ms2, n_it_inv_ac_ms2):
    print(tuple(sorted(c) for c in communities))
    list_communities_inv_ac_ms2.append(tuple(sorted(c) for c in communities))


# In[175]:


#Iteración 1
color_communities_inv_ac_ms2_1 = []
node_communities_inv_ac_ms2_1 = list_communities_inv_ac_ms2[0]
for node in G_inv_ac_ms2:
    if node in node_communities_inv_ac_ms2_1[0]:
        color_communities_inv_ac_ms2_1.append('red')
    elif node in node_communities_inv_ac_ms2_1[4]:
        color_communities_inv_ac_ms2_1.append('green')
    else:
        color_communities_inv_ac_ms2_1.append('white')  

#Grosor de las aristas
edgew_inv_ac_ms2_GN = [2*G_inv_ac_ms2.get_edge_data(u, v)['weight'] for u, v in G_inv_ac_ms2.edges()]
        
#Espacio de representación
x_inv_ac_ms2_1, y_inv_ac_ms2_1 = plt.subplots(figsize=(16, 16))
#Título del grafo
y_inv_ac_ms2_1.set_title("Application of Girvan Newman algorithm: Perspective 2.3, iteration 1", dict(fontweight="bold",fontsize=22,color="black"),loc="center")

#Representación de los objetos del grafo
    #Aristas
nx.draw_networkx_edges(G_inv_ac_ms2, pos_inv_ac_ms2, width=edgew_inv_ac_ms2_GN, edge_color="navy", style='-')
    #Nodos
nx.draw_networkx_nodes(G_inv_ac_ms2, pos_inv_ac_ms2, node_color=color_communities_inv_ac_ms2_1, node_size=1300, node_shape='o', linewidths=1,edgecolors="black")
    #Etiquetas sobre nodos
nx.draw_networkx_labels(G_inv_ac_ms2, pos_inv_ac_ms2, font_size=16, bbox=dict(ec="black",boxstyle="round",facecolor="white",pad=0.3,alpha=0.6), font_weight='normal', font_family='Verdana', horizontalalignment='center', verticalalignment='center',clip_on=False)

#Modificaciones sobre el espacio de representación
x_inv_ac_ms2_1.tight_layout()
plt.axis("off") 
y_inv_ac_ms2_1.margins(0.05,0.05)
plt.savefig("GN-CG23-It1.png")
plt.show() 


# In[176]:


#Iteración 2
color_communities_inv_ac_ms2_2 = []
node_communities_inv_ac_ms2_2 = list_communities_inv_ac_ms2[1]
for node in G_inv_ac_ms2:
    if node in node_communities_inv_ac_ms2_2[0]:
        color_communities_inv_ac_ms2_2.append('red')
    elif node in node_communities_inv_ac_ms2_2[2]:
        color_communities_inv_ac_ms2_2.append('purple')
    elif node in node_communities_inv_ac_ms2_2[5]:
        color_communities_inv_ac_ms2_2.append('green')
    else:
        color_communities_inv_ac_ms2_2.append('white')  

#Espacio de representación
x_inv_ac_ms2_2, y_inv_ac_ms2_2 = plt.subplots(figsize=(16, 16))
#Título del grafo
y_inv_ac_ms2_2.set_title("Application of Girvan Newman algorithm: Perspective 2.3, iteration 2", dict(fontweight="bold",fontsize=22,color="black"),loc="center")

#Representación de los objetos del grafo
    #Aristas
nx.draw_networkx_edges(G_inv_ac_ms2, pos_inv_ac_ms2, width=edgew_inv_ac_ms2_GN, edge_color="navy", style='-')
    #Nodos
nx.draw_networkx_nodes(G_inv_ac_ms2, pos_inv_ac_ms2, node_color=color_communities_inv_ac_ms2_2, node_size=1300, node_shape='o', linewidths=1,edgecolors="black")
    #Etiquetas sobre nodos
nx.draw_networkx_labels(G_inv_ac_ms2, pos_inv_ac_ms2, font_size=16, bbox=dict(ec="black",boxstyle="round",facecolor="white",pad=0.3,alpha=0.6), font_weight='normal', font_family='Verdana', horizontalalignment='center', verticalalignment='center',clip_on=False)

#Modificaciones sobre el espacio de representación
x_inv_ac_ms2_2.tight_layout()
plt.axis("off") 
y_inv_ac_ms2_2.margins(0.05,0.05)
plt.savefig("GN-CG23-It2.png")
plt.show() 


# In[177]:


#Iteración 3
color_communities_inv_ac_ms2_3 = []
node_communities_inv_ac_ms2_3 = list_communities_inv_ac_ms2[2]
for node in G_inv_ac_ms2:
    if node in node_communities_inv_ac_ms2_3[0]:
        color_communities_inv_ac_ms2_3.append('red')
    elif node in node_communities_inv_ac_ms2_3[2]:
        color_communities_inv_ac_ms2_3.append('purple')
    elif node in node_communities_inv_ac_ms2_3[3]:
        color_communities_inv_ac_ms2_3.append('yellow')
    elif node in node_communities_inv_ac_ms2_3[6]:
        color_communities_inv_ac_ms2_3.append('green')
    else:
        color_communities_inv_ac_ms2_3.append('white')  

#Espacio de representación
x_inv_ac_ms2_3, y_inv_ac_ms2_3 = plt.subplots(figsize=(16, 16))
#Título del grafo
y_inv_ac_ms2_3.set_title("Application of Girvan Newman algorithm: Perspective 2.3, iteration 3", dict(fontweight="bold",fontsize=22,color="black"),loc="center")

#Representación de los objetos del grafo
    #Aristas
nx.draw_networkx_edges(G_inv_ac_ms2, pos_inv_ac_ms2, width=edgew_inv_ac_ms2_GN, edge_color="navy", style='-')
    #Nodos
nx.draw_networkx_nodes(G_inv_ac_ms2, pos_inv_ac_ms2, node_color=color_communities_inv_ac_ms2_3, node_size=1300, node_shape='o', linewidths=1,edgecolors="black")
    #Etiquetas sobre nodos
nx.draw_networkx_labels(G_inv_ac_ms2, pos_inv_ac_ms2, font_size=16, bbox=dict(ec="black",boxstyle="round",facecolor="white",pad=0.3,alpha=0.6), font_weight='normal', font_family='Verdana', horizontalalignment='center', verticalalignment='center',clip_on=False)

#Modificaciones sobre el espacio de representación
x_inv_ac_ms2_3.tight_layout()
plt.axis("off") 
y_inv_ac_ms2_3.margins(0.05,0.05)
plt.savefig("GN-CG23-It3.png")
plt.show() 


# In[178]:


#Iteración 4
color_communities_inv_ac_ms2_4 = []
node_communities_inv_ac_ms2_4 = list_communities_inv_ac_ms2[3]
for node in G_inv_ac_ms2:
    if node in node_communities_inv_ac_ms2_4[0]:
        color_communities_inv_ac_ms2_4.append('red')
    elif node in node_communities_inv_ac_ms2_4[2]:
        color_communities_inv_ac_ms2_4.append('purple')
    elif node in node_communities_inv_ac_ms2_4[3]:
        color_communities_inv_ac_ms2_4.append('orange')
    elif node in node_communities_inv_ac_ms2_4[4]:
        color_communities_inv_ac_ms2_4.append('yellow')
    elif node in node_communities_inv_ac_ms2_4[7]:
        color_communities_inv_ac_ms2_4.append('green')
    else:
        color_communities_inv_ac_ms2_4.append('white')  

#Espacio de representación
x_inv_ac_ms2_4, y_inv_ac_ms2_4 = plt.subplots(figsize=(16, 16))
#Título del grafo
y_inv_ac_ms2_4.set_title("Application of Girvan Newman algorithm: Perspective 2.3, iteration 4", dict(fontweight="bold",fontsize=22,color="black"),loc="center")

#Representación de los objetos del grafo
    #Aristas
nx.draw_networkx_edges(G_inv_ac_ms2, pos_inv_ac_ms2, width=edgew_inv_ac_ms2_GN, edge_color="navy", style='-')
    #Nodos
nx.draw_networkx_nodes(G_inv_ac_ms2, pos_inv_ac_ms2, node_color=color_communities_inv_ac_ms2_4, node_size=1300, node_shape='o', linewidths=1,edgecolors="black")
    #Etiquetas sobre nodos
nx.draw_networkx_labels(G_inv_ac_ms2, pos_inv_ac_ms2, font_size=16, bbox=dict(ec="black",boxstyle="round",facecolor="white",pad=0.3,alpha=0.6), font_weight='normal', font_family='Verdana', horizontalalignment='center', verticalalignment='center',clip_on=False)

#Modificaciones sobre el espacio de representación
x_inv_ac_ms2_4.tight_layout()
plt.axis("off") 
y_inv_ac_ms2_4.margins(0.05,0.05)
plt.savefig("GN-CG23-It4.png")
plt.show() 


# In[179]:


#Iteración 5
color_communities_inv_ac_ms2_5 = []
node_communities_inv_ac_ms2_5 = list_communities_inv_ac_ms2[4]
for node in G_inv_ac_ms2:
    if node in node_communities_inv_ac_ms2_5[0]:
        color_communities_inv_ac_ms2_5.append('red')
    elif node in node_communities_inv_ac_ms2_5[2]:
        color_communities_inv_ac_ms2_5.append('purple')
    elif node in node_communities_inv_ac_ms2_5[3]:
        color_communities_inv_ac_ms2_5.append('orange')
    elif node in node_communities_inv_ac_ms2_5[4]:
        color_communities_inv_ac_ms2_5.append('yellow')
    elif node in node_communities_inv_ac_ms2_5[7]:
        color_communities_inv_ac_ms2_5.append('green')
    elif node in node_communities_inv_ac_ms2_5[8]:
        color_communities_inv_ac_ms2_5.append('deeppink')
    else:
        color_communities_inv_ac_ms2_5.append('white')  

#Espacio de representación
x_inv_ac_ms2_5, y_inv_ac_ms2_5 = plt.subplots(figsize=(16, 16))
#Título del grafo
y_inv_ac_ms2_5.set_title("Application of Girvan Newman algorithm: Perspective 2.3, iteration 5", dict(fontweight="bold",fontsize=22,color="black"),loc="center")

#Representación de los objetos del grafo
    #Aristas
nx.draw_networkx_edges(G_inv_ac_ms2, pos_inv_ac_ms2, width=edgew_inv_ac_ms2_GN, edge_color="navy", style='-')
    #Nodos
nx.draw_networkx_nodes(G_inv_ac_ms2, pos_inv_ac_ms2, node_color=color_communities_inv_ac_ms2_5, node_size=1300, node_shape='o', linewidths=1,edgecolors="black")
    #Etiquetas sobre nodos
nx.draw_networkx_labels(G_inv_ac_ms2, pos_inv_ac_ms2, font_size=16, bbox=dict(ec="black",boxstyle="round",facecolor="white",pad=0.3,alpha=0.6), font_weight='normal', font_family='Verdana', horizontalalignment='center', verticalalignment='center',clip_on=False)

#Modificaciones sobre el espacio de representación
x_inv_ac_ms2_5.tight_layout()
plt.axis("off") 
y_inv_ac_ms2_5.margins(0.05,0.05)
plt.savefig("GN-CG23-It5.png")
plt.show() 


# In[180]:


#Iteración 6
color_communities_inv_ac_ms2_6 = []
node_communities_inv_ac_ms2_6 = list_communities_inv_ac_ms2[5]
for node in G_inv_ac_ms2:
    if node in node_communities_inv_ac_ms2_6[0]:
        color_communities_inv_ac_ms2_6.append('red')
    elif node in node_communities_inv_ac_ms2_6[2]:
        color_communities_inv_ac_ms2_6.append('purple')
    elif node in node_communities_inv_ac_ms2_6[3]:
        color_communities_inv_ac_ms2_6.append('orange')
    elif node in node_communities_inv_ac_ms2_6[4]:
        color_communities_inv_ac_ms2_6.append('yellow')
    elif node in node_communities_inv_ac_ms2_6[6]:
        color_communities_inv_ac_ms2_6.append('cyan')
    elif node in node_communities_inv_ac_ms2_6[8]:
        color_communities_inv_ac_ms2_6.append('green')
    elif node in node_communities_inv_ac_ms2_6[9]:
        color_communities_inv_ac_ms2_6.append('deeppink')
    else:
        color_communities_inv_ac_ms2_6.append('white')  

#Espacio de representación
x_inv_ac_ms2_6, y_inv_ac_ms2_6 = plt.subplots(figsize=(16, 16))
#Título del grafo
y_inv_ac_ms2_6.set_title("Application of Girvan Newman algorithm: Perspective 2.3, iteration 6", dict(fontweight="bold",fontsize=22,color="black"),loc="center")

#Representación de los objetos del grafo
    #Aristas
nx.draw_networkx_edges(G_inv_ac_ms2, pos_inv_ac_ms2, width=edgew_inv_ac_ms2_GN, edge_color="navy", style='-')
    #Nodos
nx.draw_networkx_nodes(G_inv_ac_ms2, pos_inv_ac_ms2, node_color=color_communities_inv_ac_ms2_6, node_size=1300, node_shape='o', linewidths=1,edgecolors="black")
    #Etiquetas sobre nodos
nx.draw_networkx_labels(G_inv_ac_ms2, pos_inv_ac_ms2, font_size=16, bbox=dict(ec="black",boxstyle="round",facecolor="white",pad=0.3,alpha=0.6), font_weight='normal', font_family='Verdana', horizontalalignment='center', verticalalignment='center',clip_on=False)

#Modificaciones sobre el espacio de representación
x_inv_ac_ms2_6.tight_layout()
plt.axis("off") 
y_inv_ac_ms2_6.margins(0.05,0.05)
plt.savefig("GN-CG23-It6.png")
plt.show() 


# In[181]:


#Iteración 7
color_communities_inv_ac_ms2_7 = []
node_communities_inv_ac_ms2_7 = list_communities_inv_ac_ms2[6]
for node in G_inv_ac_ms2:
    if node in node_communities_inv_ac_ms2_7[0]:
        color_communities_inv_ac_ms2_7.append('red')
    elif node in node_communities_inv_ac_ms2_7[2]:
        color_communities_inv_ac_ms2_7.append('purple')
    elif node in node_communities_inv_ac_ms2_7[3]:
        color_communities_inv_ac_ms2_7.append('orange')
    elif node in node_communities_inv_ac_ms2_7[4]:
        color_communities_inv_ac_ms2_7.append('yellow')
    elif node in node_communities_inv_ac_ms2_7[6]:
        color_communities_inv_ac_ms2_7.append('cyan')
    elif node in node_communities_inv_ac_ms2_7[8]:
        color_communities_inv_ac_ms2_7.append('green')
    elif node in node_communities_inv_ac_ms2_7[9]:
        color_communities_inv_ac_ms2_7.append('deeppink')
    elif node in node_communities_inv_ac_ms2_7[13]:
        color_communities_inv_ac_ms2_7.append('lime')
    else:
        color_communities_inv_ac_ms2_7.append('white')  

#Espacio de representación
x_inv_ac_ms2_7, y_inv_ac_ms2_7 = plt.subplots(figsize=(16, 16))
#Título del grafo
y_inv_ac_ms2_7.set_title("Application of Girvan Newman algorithm: Perspective 2.3, iteration 7", dict(fontweight="bold",fontsize=22,color="black"),loc="center")

#Representación de los objetos del grafo
    #Aristas
nx.draw_networkx_edges(G_inv_ac_ms2, pos_inv_ac_ms2, width=edgew_inv_ac_ms2_GN, edge_color="navy", style='-')
    #Nodos
nx.draw_networkx_nodes(G_inv_ac_ms2, pos_inv_ac_ms2, node_color=color_communities_inv_ac_ms2_7, node_size=1300, node_shape='o', linewidths=1,edgecolors="black")
    #Etiquetas sobre nodos
nx.draw_networkx_labels(G_inv_ac_ms2, pos_inv_ac_ms2, font_size=16, bbox=dict(ec="black",boxstyle="round",facecolor="white",pad=0.3,alpha=0.6), font_weight='normal', font_family='Verdana', horizontalalignment='center', verticalalignment='center',clip_on=False)

#Modificaciones sobre el espacio de representación
x_inv_ac_ms2_7.tight_layout()
plt.axis("off") 
y_inv_ac_ms2_7.margins(0.05,0.05)
plt.savefig("GN-CG23-It7.png")
plt.show() 


# La situación es prácticamente similar a la de la subvariante 2.2 pero con un volumen menor de aristas. Habrá que estudiar este caso en las conclusiones de cara a extraer información del mismo.

# In[182]:


communities_inv_ac_ms2 = list(community.girvan_newman(G_inv_ac_ms2))
communities_inv_ac_ms2


# Aunque se genera alguna comunidad más pequeña a partir de las generadas en las iteraciones primeras, unas pocas iteraciones más tarde el algoritmo ya está emepzando a separar nodos en comunidades individuales, por lo que para extraer conclusiones habría que estudiar las primeras comunidades.

# ### 5.3. Aplicación del algoritmo G-N a la perspectiva 3: Estudio mediante el cálculo de la variación porcentual en el precio de cierre de la sesión de cada acción respecto de la sesión anterior

# In[183]:


list_communities_per = []
n_it_per = 7
comp_per = community.girvan_newman(G_per)
for communities in itertools.islice(comp_per, n_it_per):
    print(tuple(sorted(c) for c in communities))
    list_communities_per.append(tuple(sorted(c) for c in communities))


# In[184]:


#Iteración 1
color_communities_per_1 = []
node_communities_per_1 = list_communities_per[0]
for node in G_per:
    if node in node_communities_per_1[0]:
        color_communities_per_1.append('green')
    else:
        color_communities_per_1.append('red')  

#Grosor de las aristas
edgew_per_GN = [0.01*G_per.get_edge_data(u, v)['weight'] for u, v in G_per.edges()]
        
#Espacio de representación
x_per_1, y_per_1 = plt.subplots(figsize=(16, 16))
#Título del grafo
y_per_1.set_title("Application of Girvan Newman algorithm: Perspective 3, iteration 1", dict(fontweight="bold",fontsize=22,color="black"),loc="center")

#Representación de los objetos del grafo
    #Aristas
nx.draw_networkx_edges(G_per, pos_per, width=edgew_per_GN, edge_color="navy", style='-')
    #Nodos
nx.draw_networkx_nodes(G_per, pos_per, node_color=color_communities_per_1, node_size=1300, node_shape='o', linewidths=1,edgecolors="black")
    #Etiquetas sobre nodos
nx.draw_networkx_labels(G_per, pos_per, font_size=16, bbox=dict(ec="black",boxstyle="round",facecolor="white",pad=0.3,alpha=0.6), font_weight='normal', font_family='Verdana', horizontalalignment='center', verticalalignment='center',clip_on=False)

#Modificaciones sobre el espacio de representación
x_per_1.tight_layout()
plt.axis("off") 
y_per_1.margins(0.05,0.05)
plt.savefig("GN-CG3-It1.png")
plt.show() 


# In[185]:


#Iteración 2
color_communities_per_2 = []
node_communities_per_2 = list_communities_per[1]
for node in G_per:
    if node in node_communities_per_2[0]:
        color_communities_per_2.append('green')
    elif node in node_communities_per_2[1]:
        color_communities_per_2.append('purple')
    else:
        color_communities_per_2.append('red')  
        
#Espacio de representación
x_per_2, y_per_2 = plt.subplots(figsize=(16, 16))
#Título del grafo
y_per_2.set_title("Application of Girvan Newman algorithm: Perspective 3, iteration 2", dict(fontweight="bold",fontsize=22,color="black"),loc="center")

#Representación de los objetos del grafo
    #Aristas
nx.draw_networkx_edges(G_per, pos_per, width=edgew_per_GN, edge_color="navy", style='-')
    #Nodos
nx.draw_networkx_nodes(G_per, pos_per, node_color=color_communities_per_2, node_size=1300, node_shape='o', linewidths=1,edgecolors="black")
    #Etiquetas sobre nodos
nx.draw_networkx_labels(G_per, pos_per, font_size=16, bbox=dict(ec="black",boxstyle="round",facecolor="white",pad=0.3,alpha=0.6), font_weight='normal', font_family='Verdana', horizontalalignment='center', verticalalignment='center',clip_on=False)

#Modificaciones sobre el espacio de representación
x_per_2.tight_layout()
plt.axis("off") 
y_per_2.margins(0.05,0.05)
plt.savefig("GN-CG3-It2.png")
plt.show() 


# In[186]:


#Iteración 3
color_communities_per_3 = []
node_communities_per_3 = list_communities_per[2]
for node in G_per:
    if node in node_communities_per_3[0]:
        color_communities_per_3.append('green')
    elif node in node_communities_per_3[1]:
        color_communities_per_3.append('purple')
    elif node in node_communities_per_3[2]:
        color_communities_per_3.append('yellow')
    else:
        color_communities_per_3.append('red')  
        
#Espacio de representación
x_per_3, y_per_3 = plt.subplots(figsize=(16, 16))
#Título del grafo
y_per_3.set_title("Application of Girvan Newman algorithm: Perspective 3, iteration 3", dict(fontweight="bold",fontsize=22,color="black"),loc="center")

#Representación de los objetos del grafo
    #Aristas
nx.draw_networkx_edges(G_per, pos_per, width=edgew_per_GN, edge_color="navy", style='-')
    #Nodos
nx.draw_networkx_nodes(G_per, pos_per, node_color=color_communities_per_3, node_size=1300, node_shape='o', linewidths=1,edgecolors="black")
    #Etiquetas sobre nodos
nx.draw_networkx_labels(G_per, pos_per, font_size=16, bbox=dict(ec="black",boxstyle="round",facecolor="white",pad=0.3,alpha=0.6), font_weight='normal', font_family='Verdana', horizontalalignment='center', verticalalignment='center',clip_on=False)

#Modificaciones sobre el espacio de representación
x_per_3.tight_layout()
plt.axis("off") 
y_per_3.margins(0.05,0.05)
plt.savefig("GN-CG3-It3.png")
plt.show() 


# In[187]:


#Iteración 4
color_communities_per_4 = []
node_communities_per_4 = list_communities_per[3]
for node in G_per:
    if node in node_communities_per_4[0]:
        color_communities_per_4.append('green')
    elif node in node_communities_per_4[1]:
        color_communities_per_4.append('purple')
    elif node in node_communities_per_4[2]:
        color_communities_per_4.append('yellow')
    elif node in node_communities_per_4[3]:
        color_communities_per_4.append('orange')
    else:
        color_communities_per_4.append('red')  
        
#Espacio de representación
x_per_4, y_per_4 = plt.subplots(figsize=(16, 16))
#Título del grafo
y_per_4.set_title("Application of Girvan Newman algorithm: Perspective 3, iteration 4", dict(fontweight="bold",fontsize=22,color="black"),loc="center")

#Representación de los objetos del grafo
    #Aristas
nx.draw_networkx_edges(G_per, pos_per, width=edgew_per_GN, edge_color="navy", style='-')
    #Nodos
nx.draw_networkx_nodes(G_per, pos_per, node_color=color_communities_per_4, node_size=1300, node_shape='o', linewidths=1,edgecolors="black")
    #Etiquetas sobre nodos
nx.draw_networkx_labels(G_per, pos_per, font_size=16, bbox=dict(ec="black",boxstyle="round",facecolor="white",pad=0.3,alpha=0.6), font_weight='normal', font_family='Verdana', horizontalalignment='center', verticalalignment='center',clip_on=False)

#Modificaciones sobre el espacio de representación
x_per_4.tight_layout()
plt.axis("off") 
y_per_4.margins(0.05,0.05)
plt.savefig("GN-CG3-It4.png")
plt.show() 


# In[188]:


#Iteración 5
color_communities_per_5 = []
node_communities_per_5 = list_communities_per[4]
for node in G_per:
    if node in node_communities_per_5[0]:
        color_communities_per_5.append('green')
    elif node in node_communities_per_5[1]:
        color_communities_per_5.append('purple')
    elif node in node_communities_per_5[2]:
        color_communities_per_5.append('yellow')
    elif node in node_communities_per_5[3]:
        color_communities_per_5.append('orange')
    elif node in node_communities_per_5[4]:
        color_communities_per_5.append('deeppink')
    else:
        color_communities_per_5.append('red')  
        
#Espacio de representación
x_per_5, y_per_5 = plt.subplots(figsize=(16, 16))
#Título del grafo
y_per_5.set_title("Application of Girvan Newman algorithm: Perspective 3, iteration 5", dict(fontweight="bold",fontsize=22,color="black"),loc="center")

#Representación de los objetos del grafo
    #Aristas
nx.draw_networkx_edges(G_per, pos_per, width=edgew_per_GN, edge_color="navy", style='-')
    #Nodos
nx.draw_networkx_nodes(G_per, pos_per, node_color=color_communities_per_5, node_size=1300, node_shape='o', linewidths=1,edgecolors="black")
    #Etiquetas sobre nodos
nx.draw_networkx_labels(G_per, pos_per, font_size=16, bbox=dict(ec="black",boxstyle="round",facecolor="white",pad=0.3,alpha=0.6), font_weight='normal', font_family='Verdana', horizontalalignment='center', verticalalignment='center',clip_on=False)

#Modificaciones sobre el espacio de representación
x_per_5.tight_layout()
plt.axis("off") 
y_per_5.margins(0.05,0.05)
plt.savefig("GN-CG3-It5.png")
plt.show() 


# In[189]:


#Iteración 6
color_communities_per_6 = []
node_communities_per_6 = list_communities_per[5]
for node in G_per:
    if node in node_communities_per_6[0]:
        color_communities_per_6.append('green')
    elif node in node_communities_per_6[1]:
        color_communities_per_6.append('purple')
    elif node in node_communities_per_6[2]:
        color_communities_per_6.append('yellow')
    elif node in node_communities_per_6[3]:
        color_communities_per_6.append('orange')
    elif node in node_communities_per_6[4]:
        color_communities_per_6.append('deeppink')
    elif node in node_communities_per_6[5]:
        color_communities_per_6.append('cyan')
    else:
        color_communities_per_6.append('red')  
        
#Espacio de representación
x_per_6, y_per_6 = plt.subplots(figsize=(16, 16))
#Título del grafo
y_per_6.set_title("Application of Girvan Newman algorithm: Perspective 3, iteration 6", dict(fontweight="bold",fontsize=22,color="black"),loc="center")

#Representación de los objetos del grafo
    #Aristas
nx.draw_networkx_edges(G_per, pos_per, width=edgew_per_GN, edge_color="navy", style='-')
    #Nodos
nx.draw_networkx_nodes(G_per, pos_per, node_color=color_communities_per_6, node_size=1300, node_shape='o', linewidths=1,edgecolors="black")
    #Etiquetas sobre nodos
nx.draw_networkx_labels(G_per, pos_per, font_size=16, bbox=dict(ec="black",boxstyle="round",facecolor="white",pad=0.3,alpha=0.6), font_weight='normal', font_family='Verdana', horizontalalignment='center', verticalalignment='center',clip_on=False)

#Modificaciones sobre el espacio de representación
x_per_6.tight_layout()
plt.axis("off") 
y_per_6.margins(0.05,0.05)
plt.savefig("GN-CG3-It6.png")
plt.show() 


# In[190]:


#Iteración 7
color_communities_per_7 = []
node_communities_per_7 = list_communities_per[6]
for node in G_per:
    if node in node_communities_per_7[0]:
        color_communities_per_7.append('green')
    elif node in node_communities_per_7[1]:
        color_communities_per_7.append('purple')
    elif node in node_communities_per_7[2]:
        color_communities_per_7.append('yellow')
    elif node in node_communities_per_7[3]:
        color_communities_per_7.append('orange')
    elif node in node_communities_per_7[4]:
        color_communities_per_7.append('deeppink')
    elif node in node_communities_per_7[5]:
        color_communities_per_7.append('cyan')
    elif node in node_communities_per_7[6]:
        color_communities_per_7.append('lime')
    else:
        color_communities_per_7.append('red')  
        
#Espacio de representación
x_per_7, y_per_7 = plt.subplots(figsize=(16, 16))
#Título del grafo
y_per_7.set_title("Application of Girvan Newman algorithm: Perspective 3, iteration 7", dict(fontweight="bold",fontsize=22,color="black"),loc="center")

#Representación de los objetos del grafo
    #Aristas
nx.draw_networkx_edges(G_per, pos_per, width=edgew_per_GN, edge_color="navy", style='-')
    #Nodos
nx.draw_networkx_nodes(G_per, pos_per, node_color=color_communities_per_7, node_size=1300, node_shape='o', linewidths=1,edgecolors="black")
    #Etiquetas sobre nodos
nx.draw_networkx_labels(G_per, pos_per, font_size=16, bbox=dict(ec="black",boxstyle="round",facecolor="white",pad=0.3,alpha=0.6), font_weight='normal', font_family='Verdana', horizontalalignment='center', verticalalignment='center',clip_on=False)

#Modificaciones sobre el espacio de representación
x_per_7.tight_layout()
plt.axis("off") 
y_per_7.margins(0.05,0.05)
plt.savefig("GN-CG3-It7.png")
plt.show() 


# In[191]:


communities_per = list(community.girvan_newman(G_per))
communities_per


# En este caso, a vista de las representaciones y de este último bloque, el algoritmo realiza la misma segmentación que en el caso 2, por lo que esta variante se descarta para poder extraer conclusiones.

# #### 5.3.1. Aplicación del algoritmo G-N a la perspectiva 3.1: Estudio mediante el cálculo de la variación porcentual en el precio de cierre de la sesión de cada acción respecto de la sesión anterior para aquellas empresas que se crucen más que la media del total de pesos de las aristas del grafo

# In[192]:


list_communities_per_avg = []
n_it_per_avg = 7
comp_per_avg = community.girvan_newman(G_per_avg)
for communities in itertools.islice(comp_per_avg, n_it_per_avg):
    print(tuple(sorted(c) for c in communities))
    list_communities_per_avg.append(tuple(sorted(c) for c in communities))


# In[193]:


#Iteración 1
color_communities_per_avg_1 = []
node_communities_per_avg_1 = list_communities_per_avg[0]
for node in G_per_avg:
    if node in node_communities_per_avg_1[1]:
        color_communities_per_avg_1.append('green')
    else:
        color_communities_per_avg_1.append('red')  

#Grosor de las aristas
edgew_per_avg_GN = [0.2*G_per_avg.get_edge_data(u, v)['weight'] for u, v in G_per_avg.edges()]
        
#Espacio de representación
x_per_avg_1, y_per_avg_1 = plt.subplots(figsize=(16, 16))
#Título del grafo
y_per_avg_1.set_title("Application of Girvan Newman algorithm: Perspective 3.1, iteration 1", dict(fontweight="bold",fontsize=22,color="black"),loc="center")

#Representación de los objetos del grafo
    #Aristas
nx.draw_networkx_edges(G_per_avg, pos_per_avg, width=edgew_per_avg_GN, edge_color="navy", style='-')
    #Nodos
nx.draw_networkx_nodes(G_per_avg, pos_per_avg, node_color=color_communities_per_avg_1, node_size=1300, node_shape='o', linewidths=1,edgecolors="black")
    #Etiquetas sobre nodos
nx.draw_networkx_labels(G_per_avg, pos_per_avg, font_size=16, bbox=dict(ec="black",boxstyle="round",facecolor="white",pad=0.3,alpha=0.6), font_weight='normal', font_family='Verdana', horizontalalignment='center', verticalalignment='center',clip_on=False)

#Modificaciones sobre el espacio de representación
x_per_avg_1.tight_layout()
plt.axis("off") 
y_per_avg_1.margins(0.05,0.05)
plt.savefig("GN-CG31-It1.png")
plt.show() 


# In[194]:


#Iteración 2
color_communities_per_avg_2 = []
node_communities_per_avg_2 = list_communities_per_avg[1]
for node in G_per_avg:
    if node in node_communities_per_avg_2[1]:
        color_communities_per_avg_2.append('green')
    elif node in node_communities_per_avg_2[2]:
        color_communities_per_avg_2.append('purple')
    else:
        color_communities_per_avg_2.append('red')  

#Espacio de representación
x_per_avg_2, y_per_avg_2 = plt.subplots(figsize=(16, 16))
#Título del grafo
y_per_avg_2.set_title("Application of Girvan Newman algorithm: Perspective 3.1, iteration 2", dict(fontweight="bold",fontsize=22,color="black"),loc="center")

#Representación de los objetos del grafo
    #Aristas
nx.draw_networkx_edges(G_per_avg, pos_per_avg, width=edgew_per_avg_GN, edge_color="navy", style='-')
    #Nodos
nx.draw_networkx_nodes(G_per_avg, pos_per_avg, node_color=color_communities_per_avg_2, node_size=1300, node_shape='o', linewidths=1,edgecolors="black")
    #Etiquetas sobre nodos
nx.draw_networkx_labels(G_per_avg, pos_per_avg, font_size=16, bbox=dict(ec="black",boxstyle="round",facecolor="white",pad=0.3,alpha=0.6), font_weight='normal', font_family='Verdana', horizontalalignment='center', verticalalignment='center',clip_on=False)

#Modificaciones sobre el espacio de representación
x_per_avg_2.tight_layout()
plt.axis("off") 
y_per_avg_2.margins(0.05,0.05)
plt.savefig("GN-CG31-It2.png")
plt.show() 


# In[195]:


#Iteración 3
color_communities_per_avg_3 = []
node_communities_per_avg_3 = list_communities_per_avg[2]
for node in G_per_avg:
    if node in node_communities_per_avg_3[1]:
        color_communities_per_avg_3.append('green')
    elif node in node_communities_per_avg_3[2]:
        color_communities_per_avg_3.append('yellow')
    elif node in node_communities_per_avg_3[3]:
        color_communities_per_avg_3.append('purple')
    else:
        color_communities_per_avg_3.append('red')  

#Espacio de representación
x_per_avg_3, y_per_avg_3 = plt.subplots(figsize=(16, 16))
#Título del grafo
y_per_avg_3.set_title("Application of Girvan Newman algorithm: Perspective 3.1, iteration 3", dict(fontweight="bold",fontsize=22,color="black"),loc="center")

#Representación de los objetos del grafo
    #Aristas
nx.draw_networkx_edges(G_per_avg, pos_per_avg, width=edgew_per_avg_GN, edge_color="navy", style='-')
    #Nodos
nx.draw_networkx_nodes(G_per_avg, pos_per_avg, node_color=color_communities_per_avg_3, node_size=1300, node_shape='o', linewidths=1,edgecolors="black")
    #Etiquetas sobre nodos
nx.draw_networkx_labels(G_per_avg, pos_per_avg, font_size=16, bbox=dict(ec="black",boxstyle="round",facecolor="white",pad=0.3,alpha=0.6), font_weight='normal', font_family='Verdana', horizontalalignment='center', verticalalignment='center',clip_on=False)

#Modificaciones sobre el espacio de representación
x_per_avg_3.tight_layout()
plt.axis("off") 
y_per_avg_3.margins(0.05,0.05)
plt.savefig("GN-CG31-It3.png")
plt.show() 


# In[196]:


#Iteración 4
color_communities_per_avg_4 = []
node_communities_per_avg_4 = list_communities_per_avg[3]
for node in G_per_avg:
    if node in node_communities_per_avg_4[1]:
        color_communities_per_avg_4.append('green')
    elif node in node_communities_per_avg_4[2]:
        color_communities_per_avg_4.append('orange')
    elif node in node_communities_per_avg_4[3]:
        color_communities_per_avg_4.append('yellow')
    elif node in node_communities_per_avg_4[4]:
        color_communities_per_avg_4.append('purple')
    else:
        color_communities_per_avg_4.append('red')  

#Espacio de representación
x_per_avg_4, y_per_avg_4 = plt.subplots(figsize=(16, 16))
#Título del grafo
y_per_avg_4.set_title("Application of Girvan Newman algorithm: Perspective 3.1, iteration 4", dict(fontweight="bold",fontsize=22,color="black"),loc="center")

#Representación de los objetos del grafo
    #Aristas
nx.draw_networkx_edges(G_per_avg, pos_per_avg, width=edgew_per_avg_GN, edge_color="navy", style='-')
    #Nodos
nx.draw_networkx_nodes(G_per_avg, pos_per_avg, node_color=color_communities_per_avg_4, node_size=1300, node_shape='o', linewidths=1,edgecolors="black")
    #Etiquetas sobre nodos
nx.draw_networkx_labels(G_per_avg, pos_per_avg, font_size=16, bbox=dict(ec="black",boxstyle="round",facecolor="white",pad=0.3,alpha=0.6), font_weight='normal', font_family='Verdana', horizontalalignment='center', verticalalignment='center',clip_on=False)

#Modificaciones sobre el espacio de representación
x_per_avg_4.tight_layout()
plt.axis("off") 
y_per_avg_4.margins(0.05,0.05)
plt.savefig("GN-CG31-It4.png")
plt.show() 


# In[197]:


#Iteración 5
color_communities_per_avg_5 = []
node_communities_per_avg_5 = list_communities_per_avg[4]
for node in G_per_avg:
    if node in node_communities_per_avg_5[1]:
        color_communities_per_avg_5.append('green')
    elif node in node_communities_per_avg_5[2]:
        color_communities_per_avg_5.append('orange')
    elif node in node_communities_per_avg_5[3]:
        color_communities_per_avg_5.append('deeppink')
    elif node in node_communities_per_avg_5[4]:
        color_communities_per_avg_5.append('yellow')
    elif node in node_communities_per_avg_5[5]:
        color_communities_per_avg_5.append('purple')
    else:
        color_communities_per_avg_5.append('red')  

#Espacio de representación
x_per_avg_5, y_per_avg_5 = plt.subplots(figsize=(16, 16))
#Título del grafo
y_per_avg_5.set_title("Application of Girvan Newman algorithm: Perspective 3.1, iteration 5", dict(fontweight="bold",fontsize=22,color="black"),loc="center")

#Representación de los objetos del grafo
    #Aristas
nx.draw_networkx_edges(G_per_avg, pos_per_avg, width=edgew_per_avg_GN, edge_color="navy", style='-')
    #Nodos
nx.draw_networkx_nodes(G_per_avg, pos_per_avg, node_color=color_communities_per_avg_5, node_size=1300, node_shape='o', linewidths=1,edgecolors="black")
    #Etiquetas sobre nodos
nx.draw_networkx_labels(G_per_avg, pos_per_avg, font_size=16, bbox=dict(ec="black",boxstyle="round",facecolor="white",pad=0.3,alpha=0.6), font_weight='normal', font_family='Verdana', horizontalalignment='center', verticalalignment='center',clip_on=False)

#Modificaciones sobre el espacio de representación
x_per_avg_5.tight_layout()
plt.axis("off") 
y_per_avg_5.margins(0.05,0.05)
plt.savefig("GN-CG31-It5.png")
plt.show() 


# In[198]:


#Iteración 6
color_communities_per_avg_6 = []
node_communities_per_avg_6 = list_communities_per_avg[5]
for node in G_per_avg:
    if node in node_communities_per_avg_6[1]:
        color_communities_per_avg_6.append('green')
    elif node in node_communities_per_avg_6[2]:
        color_communities_per_avg_6.append('orange')
    elif node in node_communities_per_avg_6[3]:
        color_communities_per_avg_6.append('cyan')
    elif node in node_communities_per_avg_6[4]:
        color_communities_per_avg_6.append('deeppink')
    elif node in node_communities_per_avg_6[5]:
        color_communities_per_avg_6.append('yellow')
    elif node in node_communities_per_avg_6[6]:
        color_communities_per_avg_6.append('purple')
    else:
        color_communities_per_avg_6.append('red')  

#Espacio de representación
x_per_avg_6, y_per_avg_6 = plt.subplots(figsize=(16, 16))
#Título del grafo
y_per_avg_6.set_title("Application of Girvan Newman algorithm: Perspective 3.1, iteration 6", dict(fontweight="bold",fontsize=22,color="black"),loc="center")

#Representación de los objetos del grafo
    #Aristas
nx.draw_networkx_edges(G_per_avg, pos_per_avg, width=edgew_per_avg_GN, edge_color="navy", style='-')
    #Nodos
nx.draw_networkx_nodes(G_per_avg, pos_per_avg, node_color=color_communities_per_avg_6, node_size=1300, node_shape='o', linewidths=1,edgecolors="black")
    #Etiquetas sobre nodos
nx.draw_networkx_labels(G_per_avg, pos_per_avg, font_size=16, bbox=dict(ec="black",boxstyle="round",facecolor="white",pad=0.3,alpha=0.6), font_weight='normal', font_family='Verdana', horizontalalignment='center', verticalalignment='center',clip_on=False)

#Modificaciones sobre el espacio de representación
x_per_avg_6.tight_layout()
plt.axis("off") 
y_per_avg_6.margins(0.05,0.05)
plt.savefig("GN-CG31-It6.png")
plt.show() 


# In[199]:


#Iteración 7
color_communities_per_avg_7 = []
node_communities_per_avg_7 = list_communities_per_avg[6]
for node in G_per_avg:
    if node in node_communities_per_avg_7[1]:
        color_communities_per_avg_7.append('green')
    elif node in node_communities_per_avg_7[2]:
        color_communities_per_avg_7.append('lime')
    elif node in node_communities_per_avg_7[3]:
        color_communities_per_avg_7.append('orange')
    elif node in node_communities_per_avg_7[4]:
        color_communities_per_avg_7.append('cyan')
    elif node in node_communities_per_avg_7[5]:
        color_communities_per_avg_7.append('deeppink')
    elif node in node_communities_per_avg_7[6]:
        color_communities_per_avg_7.append('yellow')
    elif node in node_communities_per_avg_7[7]:
        color_communities_per_avg_7.append('purple')
    else:
        color_communities_per_avg_7.append('red')  

#Espacio de representación
x_per_avg_7, y_per_avg_7 = plt.subplots(figsize=(16, 16))
#Título del grafo
y_per_avg_7.set_title("Application of Girvan Newman algorithm: Perspective 3.1, iteration 7", dict(fontweight="bold",fontsize=22,color="black"),loc="center")

#Representación de los objetos del grafo
    #Aristas
nx.draw_networkx_edges(G_per_avg, pos_per_avg, width=edgew_per_avg_GN, edge_color="navy", style='-')
    #Nodos
nx.draw_networkx_nodes(G_per_avg, pos_per_avg, node_color=color_communities_per_avg_7, node_size=1300, node_shape='o', linewidths=1,edgecolors="black")
    #Etiquetas sobre nodos
nx.draw_networkx_labels(G_per_avg, pos_per_avg, font_size=16, bbox=dict(ec="black",boxstyle="round",facecolor="white",pad=0.3,alpha=0.6), font_weight='normal', font_family='Verdana', horizontalalignment='center', verticalalignment='center',clip_on=False)

#Modificaciones sobre el espacio de representación
x_per_avg_7.tight_layout()
plt.axis("off") 
y_per_avg_7.margins(0.05,0.05)
plt.savefig("GN-CG31-It7.png")
plt.show() 


# In[200]:


communities_per_avg = list(community.girvan_newman(G_per_avg))
communities_per_avg


# Para esta subvariante ocurre lo mismo que para la 2.1. Es más, debido a su relación en la naturaleza de los valores para establecer los rankings, las primeras iteraciones son totalmente análogas y a partir de estas se generan "mono-comunidades" pero con distintos nodos. Aún así, el algoritmo actúa de forma análoga a la visión 2.1 y esto no permite extraer conclusiones para el estudio.

# #### 5.3.2. Aplicación del algoritmo G-N a la perspectiva 3.2: Estudio mediante el cálculo de la variación porcentual en el precio de cierre de la sesión de cada acción respecto de la sesión anterior para aquellas empresas que se crucen más que la medida 1 del total de pesos de las aristas del grafo

# In[201]:


list_communities_per_ms1 = []
n_it_per_ms1 = 7
comp_per_ms1 = community.girvan_newman(G_per_ms1)
for communities in itertools.islice(comp_per_ms1, n_it_per_ms1):
    print(tuple(sorted(c) for c in communities))
    list_communities_per_ms1.append(tuple(sorted(c) for c in communities))


# In[202]:


#Iteración 1
color_communities_per_ms1_1 = []
node_communities_per_ms1_1 = list_communities_per_ms1[0]
for node in G_per_ms1:
    if node in node_communities_per_ms1_1[0]:
        color_communities_per_ms1_1.append('red')
    elif node in node_communities_per_ms1_1[2]:
        color_communities_per_ms1_1.append('green')
    elif node in node_communities_per_ms1_1[7]:
        color_communities_per_ms1_1.append('purple')
    else:
        color_communities_per_ms1_1.append('white')  

#Grosor de las aristas
edgew_per_ms1_GN = [2*G_per_ms1.get_edge_data(u, v)['weight'] for u, v in G_per_ms1.edges()]
        
#Espacio de representación
x_per_ms1_1, y_per_ms1_1 = plt.subplots(figsize=(16, 16))
#Título del grafo
y_per_ms1_1.set_title("Application of Girvan Newman algorithm: Perspective 3.2, iteration 1", dict(fontweight="bold",fontsize=22,color="black"),loc="center")

#Representación de los objetos del grafo
    #Aristas
nx.draw_networkx_edges(G_per_ms1, pos_per_ms1, width=edgew_per_ms1_GN, edge_color="navy", style='-')
    #Nodos
nx.draw_networkx_nodes(G_per_ms1, pos_per_ms1, node_color=color_communities_per_ms1_1, node_size=1300, node_shape='o', linewidths=1,edgecolors="black")
    #Etiquetas sobre nodos
nx.draw_networkx_labels(G_per_ms1, pos_per_ms1, font_size=16, bbox=dict(ec="black",boxstyle="round",facecolor="white",pad=0.3,alpha=0.6), font_weight='normal', font_family='Verdana', horizontalalignment='center', verticalalignment='center',clip_on=False)

#Modificaciones sobre el espacio de representación
x_per_ms1_1.tight_layout()
plt.axis("off") 
y_per_ms1_1.margins(0.05,0.05)
plt.savefig("GN-CG32-It1.png")
plt.show() 


# In[203]:


#Iteración 2
color_communities_per_ms1_2 = []
node_communities_per_ms1_2 = list_communities_per_ms1[1]
for node in G_per_ms1:
    if node in node_communities_per_ms1_2[0]:
        color_communities_per_ms1_2.append('red')
    elif node in node_communities_per_ms1_2[2]:
        color_communities_per_ms1_2.append('green')
    elif node in node_communities_per_ms1_2[3]:
        color_communities_per_ms1_2.append('yellow')
    elif node in node_communities_per_ms1_2[8]:
        color_communities_per_ms1_2.append('purple')
    else:
        color_communities_per_ms1_2.append('white')  
        
#Espacio de representación
x_per_ms1_2, y_per_ms1_2 = plt.subplots(figsize=(16, 16))
#Título del grafo
y_per_ms1_2.set_title("Application of Girvan Newman algorithm: Perspective 3.2, iteration 2", dict(fontweight="bold",fontsize=22,color="black"),loc="center")

#Representación de los objetos del grafo
    #Aristas
nx.draw_networkx_edges(G_per_ms1, pos_per_ms1, width=edgew_per_ms1_GN, edge_color="navy", style='-')
    #Nodos
nx.draw_networkx_nodes(G_per_ms1, pos_per_ms1, node_color=color_communities_per_ms1_2, node_size=1300, node_shape='o', linewidths=1,edgecolors="black")
    #Etiquetas sobre nodos
nx.draw_networkx_labels(G_per_ms1, pos_per_ms1, font_size=16, bbox=dict(ec="black",boxstyle="round",facecolor="white",pad=0.3,alpha=0.6), font_weight='normal', font_family='Verdana', horizontalalignment='center', verticalalignment='center',clip_on=False)

#Modificaciones sobre el espacio de representación
x_per_ms1_2.tight_layout()
plt.axis("off") 
y_per_ms1_2.margins(0.05,0.05)
plt.savefig("GN-CG32-It2.png")
plt.show() 


# In[204]:


#Iteración 3
color_communities_per_ms1_3 = []
node_communities_per_ms1_3 = list_communities_per_ms1[2]
for node in G_per_ms1:
    if node in node_communities_per_ms1_3[0]:
        color_communities_per_ms1_3.append('red')
    elif node in node_communities_per_ms1_3[2]:
        color_communities_per_ms1_3.append('green')
    elif node in node_communities_per_ms1_3[3]:
        color_communities_per_ms1_3.append('yellow')
    elif node in node_communities_per_ms1_3[4]:
        color_communities_per_ms1_3.append('orange')
    elif node in node_communities_per_ms1_3[9]:
        color_communities_per_ms1_3.append('purple')
    else:
        color_communities_per_ms1_3.append('white')  
        
#Espacio de representación
x_per_ms1_3, y_per_ms1_3 = plt.subplots(figsize=(16, 16))
#Título del grafo
y_per_ms1_3.set_title("Application of Girvan Newman algorithm: Perspective 3.2, iteration 3", dict(fontweight="bold",fontsize=22,color="black"),loc="center")

#Representación de los objetos del grafo
    #Aristas
nx.draw_networkx_edges(G_per_ms1, pos_per_ms1, width=edgew_per_ms1_GN, edge_color="navy", style='-')
    #Nodos
nx.draw_networkx_nodes(G_per_ms1, pos_per_ms1, node_color=color_communities_per_ms1_3, node_size=1300, node_shape='o', linewidths=1,edgecolors="black")
    #Etiquetas sobre nodos
nx.draw_networkx_labels(G_per_ms1, pos_per_ms1, font_size=16, bbox=dict(ec="black",boxstyle="round",facecolor="white",pad=0.3,alpha=0.6), font_weight='normal', font_family='Verdana', horizontalalignment='center', verticalalignment='center',clip_on=False)

#Modificaciones sobre el espacio de representación
x_per_ms1_3.tight_layout()
plt.axis("off") 
y_per_ms1_3.margins(0.05,0.05)
plt.savefig("GN-CG32-It3.png")
plt.show()


# In[205]:


#Iteración 4
color_communities_per_ms1_4 = []
node_communities_per_ms1_4 = list_communities_per_ms1[3]
for node in G_per_ms1:
    if node in node_communities_per_ms1_4[0]:
        color_communities_per_ms1_4.append('red')
    elif node in node_communities_per_ms1_4[2]:
        color_communities_per_ms1_4.append('green')
    elif node in node_communities_per_ms1_4[3]:
        color_communities_per_ms1_4.append('yellow')
    elif node in node_communities_per_ms1_4[4]:
        color_communities_per_ms1_4.append('orange')
    elif node in node_communities_per_ms1_4[8]:
        color_communities_per_ms1_4.append('deeppink')
    elif node in node_communities_per_ms1_4[10]:
        color_communities_per_ms1_4.append('purple')
    else:
        color_communities_per_ms1_4.append('white')  
        
#Espacio de representación
x_per_ms1_4, y_per_ms1_4 = plt.subplots(figsize=(16, 16))
#Título del grafo
y_per_ms1_4.set_title("Application of Girvan Newman algorithm: Perspective 3.2, iteration 4", dict(fontweight="bold",fontsize=22,color="black"),loc="center")

#Representación de los objetos del grafo
    #Aristas
nx.draw_networkx_edges(G_per_ms1, pos_per_ms1, width=edgew_per_ms1_GN, edge_color="navy", style='-')
    #Nodos
nx.draw_networkx_nodes(G_per_ms1, pos_per_ms1, node_color=color_communities_per_ms1_4, node_size=1300, node_shape='o', linewidths=1,edgecolors="black")
    #Etiquetas sobre nodos
nx.draw_networkx_labels(G_per_ms1, pos_per_ms1, font_size=16, bbox=dict(ec="black",boxstyle="round",facecolor="white",pad=0.3,alpha=0.6), font_weight='normal', font_family='Verdana', horizontalalignment='center', verticalalignment='center',clip_on=False)

#Modificaciones sobre el espacio de representación
x_per_ms1_4.tight_layout()
plt.axis("off") 
y_per_ms1_4.margins(0.05,0.05)
plt.savefig("GN-CG32-It4.png")
plt.show()


# In[206]:


#Iteración 5
color_communities_per_ms1_5 = []
node_communities_per_ms1_5 = list_communities_per_ms1[4]
for node in G_per_ms1:
    if node in node_communities_per_ms1_5[0]:
        color_communities_per_ms1_5.append('red')
    elif node in node_communities_per_ms1_5[2]:
        color_communities_per_ms1_5.append('green')
    elif node in node_communities_per_ms1_5[3]:
        color_communities_per_ms1_5.append('yellow')
    elif node in node_communities_per_ms1_5[4]:
        color_communities_per_ms1_5.append('orange')
    elif node in node_communities_per_ms1_5[8]:
        color_communities_per_ms1_5.append('cyan')
    elif node in node_communities_per_ms1_5[9]:
        color_communities_per_ms1_5.append('deeppink')
    elif node in node_communities_per_ms1_5[11]:
        color_communities_per_ms1_5.append('purple')
    else:
        color_communities_per_ms1_5.append('white')  
        
#Espacio de representación
x_per_ms1_5, y_per_ms1_5 = plt.subplots(figsize=(16, 16))
#Título del grafo
y_per_ms1_5.set_title("Application of Girvan Newman algorithm: Perspective 3.2, iteration 5", dict(fontweight="bold",fontsize=22,color="black"),loc="center")

#Representación de los objetos del grafo
    #Aristas
nx.draw_networkx_edges(G_per_ms1, pos_per_ms1, width=edgew_per_ms1_GN, edge_color="navy", style='-')
    #Nodos
nx.draw_networkx_nodes(G_per_ms1, pos_per_ms1, node_color=color_communities_per_ms1_5, node_size=1300, node_shape='o', linewidths=1,edgecolors="black")
    #Etiquetas sobre nodos
nx.draw_networkx_labels(G_per_ms1, pos_per_ms1, font_size=16, bbox=dict(ec="black",boxstyle="round",facecolor="white",pad=0.3,alpha=0.6), font_weight='normal', font_family='Verdana', horizontalalignment='center', verticalalignment='center',clip_on=False)

#Modificaciones sobre el espacio de representación
x_per_ms1_5.tight_layout()
plt.axis("off") 
y_per_ms1_5.margins(0.05,0.05)
plt.savefig("GN-CG32-It5.png")
plt.show()


# In[207]:


#Iteración 6
color_communities_per_ms1_6 = []
node_communities_per_ms1_6 = list_communities_per_ms1[5]
for node in G_per_ms1:
    if node in node_communities_per_ms1_6[0]:
        color_communities_per_ms1_6.append('red')
    elif node in node_communities_per_ms1_6[2]:
        color_communities_per_ms1_6.append('green')
    elif node in node_communities_per_ms1_6[3]:
        color_communities_per_ms1_6.append('yellow')
    elif node in node_communities_per_ms1_6[4]:
        color_communities_per_ms1_6.append('orange')
    elif node in node_communities_per_ms1_6[5]:
        color_communities_per_ms1_6.append('lime')
    elif node in node_communities_per_ms1_6[9]:
        color_communities_per_ms1_6.append('cyan')
    elif node in node_communities_per_ms1_6[10]:
        color_communities_per_ms1_6.append('deeppink')
    elif node in node_communities_per_ms1_6[12]:
        color_communities_per_ms1_6.append('purple')
    else:
        color_communities_per_ms1_6.append('white')  
        
#Espacio de representación
x_per_ms1_6, y_per_ms1_6 = plt.subplots(figsize=(16, 16))
#Título del grafo
y_per_ms1_6.set_title("Application of Girvan Newman algorithm: Perspective 3.2, iteration 6", dict(fontweight="bold",fontsize=22,color="black"),loc="center")

#Representación de los objetos del grafo
    #Aristas
nx.draw_networkx_edges(G_per_ms1, pos_per_ms1, width=edgew_per_ms1_GN, edge_color="navy", style='-')
    #Nodos
nx.draw_networkx_nodes(G_per_ms1, pos_per_ms1, node_color=color_communities_per_ms1_6, node_size=1300, node_shape='o', linewidths=1,edgecolors="black")
    #Etiquetas sobre nodos
nx.draw_networkx_labels(G_per_ms1, pos_per_ms1, font_size=16, bbox=dict(ec="black",boxstyle="round",facecolor="white",pad=0.3,alpha=0.6), font_weight='normal', font_family='Verdana', horizontalalignment='center', verticalalignment='center',clip_on=False)

#Modificaciones sobre el espacio de representación
x_per_ms1_6.tight_layout()
plt.axis("off") 
y_per_ms1_6.margins(0.05,0.05)
plt.savefig("GN-CG32-It6.png")
plt.show()


# In[208]:


#Iteración 7
color_communities_per_ms1_7 = []
node_communities_per_ms1_7 = list_communities_per_ms1[6]
for node in G_per_ms1:
    if node in node_communities_per_ms1_7[0]:
        color_communities_per_ms1_7.append('red')
    elif node in node_communities_per_ms1_7[2]:
        color_communities_per_ms1_7.append('green')
    elif node in node_communities_per_ms1_7[3]:
        color_communities_per_ms1_7.append('yellow')
    elif node in node_communities_per_ms1_7[4]:
        color_communities_per_ms1_7.append('orange')
    elif node in node_communities_per_ms1_7[5]:
        color_communities_per_ms1_7.append('lime')
    elif node in node_communities_per_ms1_7[9]:
        color_communities_per_ms1_7.append('cyan')
    elif node in node_communities_per_ms1_7[10]:
        color_communities_per_ms1_7.append('deeppink')
    elif node in node_communities_per_ms1_7[12]:
        color_communities_per_ms1_7.append('chocolate')
    elif node in node_communities_per_ms1_7[13]:
        color_communities_per_ms1_7.append('purple')
    else:
        color_communities_per_ms1_7.append('white')  
        
#Espacio de representación
x_per_ms1_7, y_per_ms1_7 = plt.subplots(figsize=(16, 16))
#Título del grafo
y_per_ms1_7.set_title("Application of Girvan Newman algorithm: Perspective 3.2, iteration 7", dict(fontweight="bold",fontsize=22,color="black"),loc="center")

#Representación de los objetos del grafo
    #Aristas
nx.draw_networkx_edges(G_per_ms1, pos_per_ms1, width=edgew_per_ms1_GN, edge_color="navy", style='-')
    #Nodos
nx.draw_networkx_nodes(G_per_ms1, pos_per_ms1, node_color=color_communities_per_ms1_7, node_size=1300, node_shape='o', linewidths=1,edgecolors="black")
    #Etiquetas sobre nodos
nx.draw_networkx_labels(G_per_ms1, pos_per_ms1, font_size=16, bbox=dict(ec="black",boxstyle="round",facecolor="white",pad=0.3,alpha=0.6), font_weight='normal', font_family='Verdana', horizontalalignment='center', verticalalignment='center',clip_on=False)

#Modificaciones sobre el espacio de representación
x_per_ms1_7.tight_layout()
plt.axis("off") 
y_per_ms1_7.margins(0.05,0.05)
plt.savefig("GN-CG32-It7.png")
plt.show()


# In[209]:


communities_per_ms1 = list(community.girvan_newman(G_per_ms1))
communities_per_ms1


# Mismos comentarios que para la subvariante 2.2 pero las comunidades que se forman están compuestas por otras empresas. Aún así, funcionamiento del algoritmo sobre el grafo similar.

# #### 5.3.3. Aplicación del algoritmo G-N a la perspectiva 3.3: Estudio mediante el cálculo de la variación porcentual en el precio de cierre de la sesión de cada acción respecto de la sesión anterior para aquellas empresas que se crucen más que la medida 2 del total de pesos de las aristas del grafo

# In[210]:


list_communities_per_ms2 = []
n_it_per_ms2 = 7
comp_per_ms2 = community.girvan_newman(G_per_ms2)
for communities in itertools.islice(comp_per_ms2, n_it_per_ms2):
    print(tuple(sorted(c) for c in communities))
    list_communities_per_ms2.append(tuple(sorted(c) for c in communities))


# In[211]:


#Iteración 1
color_communities_per_ms2_1 = []
node_communities_per_ms2_1 = list_communities_per_ms2[0]
for node in G_per_ms2:
    if node in node_communities_per_ms2_1[0]:
        color_communities_per_ms2_1.append('red')
    elif node in node_communities_per_ms2_1[2]:
        color_communities_per_ms2_1.append('green')
    elif node in node_communities_per_ms2_1[4]:
        color_communities_per_ms2_1.append('purple')
    elif node in node_communities_per_ms2_1[6]:
        color_communities_per_ms2_1.append('yellow')
    elif node in node_communities_per_ms2_1[11]:
        color_communities_per_ms2_1.append('orange')
    elif node in node_communities_per_ms2_1[12]:
        color_communities_per_ms2_1.append('deeppink')
    elif node in node_communities_per_ms2_1[14]:
        color_communities_per_ms2_1.append('cyan')
    else:
        color_communities_per_ms2_1.append('white')  

#Grosor de las aristas
edgew_per_ms2_GN = [2*G_per_ms2.get_edge_data(u, v)['weight'] for u, v in G_per_ms2.edges()]
        
#Espacio de representación
x_per_ms2_1, y_per_ms2_1 = plt.subplots(figsize=(16, 16))
#Título del grafo
y_per_ms2_1.set_title("Application of Girvan Newman algorithm: Perspective 3.3, iteration 1", dict(fontweight="bold",fontsize=22,color="black"),loc="center")

#Representación de los objetos del grafo
    #Aristas
nx.draw_networkx_edges(G_per_ms2, pos_per_ms2, width=edgew_per_ms2_GN, edge_color="navy", style='-')
    #Nodos
nx.draw_networkx_nodes(G_per_ms2, pos_per_ms2, node_color=color_communities_per_ms2_1, node_size=1300, node_shape='o', linewidths=1,edgecolors="black")
    #Etiquetas sobre nodos
nx.draw_networkx_labels(G_per_ms2, pos_per_ms2, font_size=16, bbox=dict(ec="black",boxstyle="round",facecolor="white",pad=0.3,alpha=0.6), font_weight='normal', font_family='Verdana', horizontalalignment='center', verticalalignment='center',clip_on=False)

#Modificaciones sobre el espacio de representación
x_per_ms2_1.tight_layout()
plt.axis("off") 
y_per_ms2_1.margins(0.05,0.05)
plt.savefig("GN-CG33-It1.png")
plt.show() 


# In[212]:


#Iteración 2
color_communities_per_ms2_2 = []
node_communities_per_ms2_2 = list_communities_per_ms2[1]
for node in G_per_ms2:
    if node in node_communities_per_ms2_2[0]:
        color_communities_per_ms2_2.append('red')
    elif node in node_communities_per_ms2_2[2]:
        color_communities_per_ms2_2.append('green')
    elif node in node_communities_per_ms2_2[4]:
        color_communities_per_ms2_2.append('purple')
    elif node in node_communities_per_ms2_2[6]:
        color_communities_per_ms2_2.append('yellow')
    elif node in node_communities_per_ms2_2[11]:
        color_communities_per_ms2_2.append('orange')
    elif node in node_communities_per_ms2_2[12]:
        color_communities_per_ms2_2.append('deeppink')
    elif node in node_communities_per_ms2_2[14]:
        color_communities_per_ms2_2.append('cyan')
    elif node in node_communities_per_ms2_2[19]:
        color_communities_per_ms2_2.append('lime')
    else:
        color_communities_per_ms2_2.append('white')  

#Espacio de representación
x_per_ms2_2, y_per_ms2_2 = plt.subplots(figsize=(16, 16))
#Título del grafo
y_per_ms2_2.set_title("Application of Girvan Newman algorithm: Perspective 3.3, iteration 2", dict(fontweight="bold",fontsize=22,color="black"),loc="center")

#Representación de los objetos del grafo
    #Aristas
nx.draw_networkx_edges(G_per_ms2, pos_per_ms2, width=edgew_per_ms2_GN, edge_color="navy", style='-')
    #Nodos
nx.draw_networkx_nodes(G_per_ms2, pos_per_ms2, node_color=color_communities_per_ms2_2, node_size=1300, node_shape='o', linewidths=1,edgecolors="black")
    #Etiquetas sobre nodos
nx.draw_networkx_labels(G_per_ms2, pos_per_ms2, font_size=16, bbox=dict(ec="black",boxstyle="round",facecolor="white",pad=0.3,alpha=0.6), font_weight='normal', font_family='Verdana', horizontalalignment='center', verticalalignment='center',clip_on=False)

#Modificaciones sobre el espacio de representación
x_per_ms2_2.tight_layout()
plt.axis("off") 
y_per_ms2_2.margins(0.05,0.05)
plt.savefig("GN-CG33-It2.png")
plt.show() 


# In[213]:


#Iteración 3
color_communities_per_ms2_3 = []
node_communities_per_ms2_3 = list_communities_per_ms2[2]
for node in G_per_ms2:
    if node in node_communities_per_ms2_3[0]:
        color_communities_per_ms2_3.append('red')
    elif node in node_communities_per_ms2_3[2]:
        color_communities_per_ms2_3.append('green')
    elif node in node_communities_per_ms2_3[4]:
        color_communities_per_ms2_3.append('purple')
    elif node in node_communities_per_ms2_3[6]:
        color_communities_per_ms2_3.append('yellow')
    elif node in node_communities_per_ms2_3[11]:
        color_communities_per_ms2_3.append('orange')
    elif node in node_communities_per_ms2_3[12]:
        color_communities_per_ms2_3.append('deeppink')
    elif node in node_communities_per_ms2_3[14]:
        color_communities_per_ms2_3.append('cyan')
    elif node in node_communities_per_ms2_3[17]:
        color_communities_per_ms2_3.append('chocolate')
    elif node in node_communities_per_ms2_3[20]:
        color_communities_per_ms2_3.append('lime')
    else:
        color_communities_per_ms2_3.append('white')  

#Espacio de representación
x_per_ms2_3, y_per_ms2_3 = plt.subplots(figsize=(16, 16))
#Título del grafo
y_per_ms2_3.set_title("Application of Girvan Newman algorithm: Perspective 3.3, iteration 3", dict(fontweight="bold",fontsize=22,color="black"),loc="center")

#Representación de los objetos del grafo
    #Aristas
nx.draw_networkx_edges(G_per_ms2, pos_per_ms2, width=edgew_per_ms2_GN, edge_color="navy", style='-')
    #Nodos
nx.draw_networkx_nodes(G_per_ms2, pos_per_ms2, node_color=color_communities_per_ms2_3, node_size=1300, node_shape='o', linewidths=1,edgecolors="black")
    #Etiquetas sobre nodos
nx.draw_networkx_labels(G_per_ms2, pos_per_ms2, font_size=16, bbox=dict(ec="black",boxstyle="round",facecolor="white",pad=0.3,alpha=0.6), font_weight='normal', font_family='Verdana', horizontalalignment='center', verticalalignment='center',clip_on=False)

#Modificaciones sobre el espacio de representación
x_per_ms2_3.tight_layout()
plt.axis("off") 
y_per_ms2_3.margins(0.05,0.05)
plt.savefig("GN-CG33-It3.png")
plt.show() 


# In[214]:


#Iteración 4
color_communities_per_ms2_4 = []
node_communities_per_ms2_4 = list_communities_per_ms2[3]
for node in G_per_ms2:
    if node in node_communities_per_ms2_4[0]:
        color_communities_per_ms2_4.append('red')
    elif node in node_communities_per_ms2_4[2]:
        color_communities_per_ms2_4.append('green')
    elif node in node_communities_per_ms2_4[4]:
        color_communities_per_ms2_4.append('purple')
    elif node in node_communities_per_ms2_4[6]:
        color_communities_per_ms2_4.append('yellow')
    elif node in node_communities_per_ms2_4[11]:
        color_communities_per_ms2_4.append('orange')
    elif node in node_communities_per_ms2_4[12]:
        color_communities_per_ms2_4.append('deeppink')
    elif node in node_communities_per_ms2_4[14]:
        color_communities_per_ms2_4.append('cyan')
    elif node in node_communities_per_ms2_4[17]:
        color_communities_per_ms2_4.append('chocolate')
    elif node in node_communities_per_ms2_4[20]:
        color_communities_per_ms2_4.append('lime')
    elif node in node_communities_per_ms2_4[25]:
        color_communities_per_ms2_4.append('olive')
    else:
        color_communities_per_ms2_4.append('white')  

#Espacio de representación
x_per_ms2_4, y_per_ms2_4 = plt.subplots(figsize=(16, 16))
#Título del grafo
y_per_ms2_4.set_title("Application of Girvan Newman algorithm: Perspective 3.3, iteration 4", dict(fontweight="bold",fontsize=22,color="black"),loc="center")

#Representación de los objetos del grafo
    #Aristas
nx.draw_networkx_edges(G_per_ms2, pos_per_ms2, width=edgew_per_ms2_GN, edge_color="navy", style='-')
    #Nodos
nx.draw_networkx_nodes(G_per_ms2, pos_per_ms2, node_color=color_communities_per_ms2_4, node_size=1300, node_shape='o', linewidths=1,edgecolors="black")
    #Etiquetas sobre nodos
nx.draw_networkx_labels(G_per_ms2, pos_per_ms2, font_size=16, bbox=dict(ec="black",boxstyle="round",facecolor="white",pad=0.3,alpha=0.6), font_weight='normal', font_family='Verdana', horizontalalignment='center', verticalalignment='center',clip_on=False)

#Modificaciones sobre el espacio de representación
x_per_ms2_4.tight_layout()
plt.axis("off") 
y_per_ms2_4.margins(0.05,0.05)
plt.savefig("GN-CG33-It4.png")
plt.show() 


# In[215]:


#Iteración 5
color_communities_per_ms2_5 = []
node_communities_per_ms2_5 = list_communities_per_ms2[4]
for node in G_per_ms2:
    if node in node_communities_per_ms2_5[0]:
        color_communities_per_ms2_5.append('red')
    elif node in node_communities_per_ms2_5[2]:
        color_communities_per_ms2_5.append('green')
    elif node in node_communities_per_ms2_5[4]:
        color_communities_per_ms2_5.append('tan')
    elif node in node_communities_per_ms2_5[5]:
        color_communities_per_ms2_5.append('purple')
    elif node in node_communities_per_ms2_5[7]:
        color_communities_per_ms2_5.append('yellow')
    elif node in node_communities_per_ms2_5[12]:
        color_communities_per_ms2_5.append('orange')
    elif node in node_communities_per_ms2_5[13]:
        color_communities_per_ms2_5.append('deeppink')
    elif node in node_communities_per_ms2_5[15]:
        color_communities_per_ms2_5.append('cyan')
    elif node in node_communities_per_ms2_5[18]:
        color_communities_per_ms2_5.append('chocolate')
    elif node in node_communities_per_ms2_5[21]:
        color_communities_per_ms2_5.append('lime')
    elif node in node_communities_per_ms2_5[26]:
        color_communities_per_ms2_5.append('olive')
    else:
        color_communities_per_ms2_5.append('white')  

#Espacio de representación
x_per_ms2_5, y_per_ms2_5 = plt.subplots(figsize=(16, 16))
#Título del grafo
y_per_ms2_5.set_title("Application of Girvan Newman algorithm: Perspective 3.3 iteration 5", dict(fontweight="bold",fontsize=22,color="black"),loc="center")

#Representación de los objetos del grafo
    #Aristas
nx.draw_networkx_edges(G_per_ms2, pos_per_ms2, width=edgew_per_ms2_GN, edge_color="navy", style='-')
    #Nodos
nx.draw_networkx_nodes(G_per_ms2, pos_per_ms2, node_color=color_communities_per_ms2_5, node_size=1300, node_shape='o', linewidths=1,edgecolors="black")
    #Etiquetas sobre nodos
nx.draw_networkx_labels(G_per_ms2, pos_per_ms2, font_size=16, bbox=dict(ec="black",boxstyle="round",facecolor="white",pad=0.3,alpha=0.6), font_weight='normal', font_family='Verdana', horizontalalignment='center', verticalalignment='center',clip_on=False)

#Modificaciones sobre el espacio de representación
x_per_ms2_5.tight_layout()
plt.axis("off") 
y_per_ms2_5.margins(0.05,0.05)
plt.savefig("GN-CG33-It5.png")
plt.show() 


# In[216]:


#Iteración 6
color_communities_per_ms2_6 = []
node_communities_per_ms2_6 = list_communities_per_ms2[5]
for node in G_per_ms2:
    if node in node_communities_per_ms2_6[0]:
        color_communities_per_ms2_6.append('red')
    elif node in node_communities_per_ms2_6[2]:
        color_communities_per_ms2_6.append('green')
    elif node in node_communities_per_ms2_6[4]:
        color_communities_per_ms2_6.append('tan')
    elif node in node_communities_per_ms2_6[5]:
        color_communities_per_ms2_6.append('purple')
    elif node in node_communities_per_ms2_6[7]:
        color_communities_per_ms2_6.append('yellow')
    elif node in node_communities_per_ms2_6[12]:
        color_communities_per_ms2_6.append('orange')
    elif node in node_communities_per_ms2_6[13]:
        color_communities_per_ms2_6.append('deeppink')
    elif node in node_communities_per_ms2_6[15]:
        color_communities_per_ms2_6.append('cyan')
    elif node in node_communities_per_ms2_6[18]:
        color_communities_per_ms2_6.append('chocolate')
    elif node in node_communities_per_ms2_6[20]:
        color_communities_per_ms2_6.append('palegreen')
    elif node in node_communities_per_ms2_6[22]:
        color_communities_per_ms2_6.append('lime')
    elif node in node_communities_per_ms2_6[27]:
        color_communities_per_ms2_6.append('olive')
    else:
        color_communities_per_ms2_6.append('white')  

#Espacio de representación
x_per_ms2_6, y_per_ms2_6 = plt.subplots(figsize=(16, 16))
#Título del grafo
y_per_ms2_6.set_title("Application of Girvan Newman algorithm: Perspective 3.3 iteration 6", dict(fontweight="bold",fontsize=22,color="black"),loc="center")

#Representación de los objetos del grafo
    #Aristas
nx.draw_networkx_edges(G_per_ms2, pos_per_ms2, width=edgew_per_ms2_GN, edge_color="navy", style='-')
    #Nodos
nx.draw_networkx_nodes(G_per_ms2, pos_per_ms2, node_color=color_communities_per_ms2_6, node_size=1300, node_shape='o', linewidths=1,edgecolors="black")
    #Etiquetas sobre nodos
nx.draw_networkx_labels(G_per_ms2, pos_per_ms2, font_size=16, bbox=dict(ec="black",boxstyle="round",facecolor="white",pad=0.3,alpha=0.6), font_weight='normal', font_family='Verdana', horizontalalignment='center', verticalalignment='center',clip_on=False)

#Modificaciones sobre el espacio de representación
x_per_ms2_6.tight_layout()
plt.axis("off") 
y_per_ms2_6.margins(0.05,0.05)
plt.savefig("GN-CG33-It6.png")
plt.show() 


# In[217]:


#Iteración 7
color_communities_per_ms2_7 = []
node_communities_per_ms2_7 = list_communities_per_ms2[6]
for node in G_per_ms2:
    if node in node_communities_per_ms2_7[0]:
        color_communities_per_ms2_7.append('red')
    elif node in node_communities_per_ms2_7[2]:
        color_communities_per_ms2_7.append('green')
    elif node in node_communities_per_ms2_7[4]:
        color_communities_per_ms2_7.append('tan')
    elif node in node_communities_per_ms2_7[5]:
        color_communities_per_ms2_7.append('purple')
    elif node in node_communities_per_ms2_7[7]:
        color_communities_per_ms2_7.append('yellow')
    elif node in node_communities_per_ms2_7[12]:
        color_communities_per_ms2_7.append('orange')
    elif node in node_communities_per_ms2_7[13]:
        color_communities_per_ms2_7.append('deeppink')
    elif node in node_communities_per_ms2_7[15]:
        color_communities_per_ms2_7.append('cyan')
    elif node in node_communities_per_ms2_7[18]:
        color_communities_per_ms2_7.append('chocolate')
    elif node in node_communities_per_ms2_7[20]:
        color_communities_per_ms2_7.append('palegreen')
    elif node in node_communities_per_ms2_7[22]:
        color_communities_per_ms2_7.append('lime')
    elif node in node_communities_per_ms2_7[27]:
        color_communities_per_ms2_7.append('olive')
    elif node in node_communities_per_ms2_7[28]:
        color_communities_per_ms2_7.append('skyblue')
    else:
        color_communities_per_ms2_7.append('white')  

#Espacio de representación
x_per_ms2_7, y_per_ms2_7 = plt.subplots(figsize=(16, 16))
#Título del grafo
y_per_ms2_7.set_title("Application of Girvan Newman algorithm: Perspective 3.3 iteration 7", dict(fontweight="bold",fontsize=22,color="black"),loc="center")

#Representación de los objetos del grafo
    #Aristas
nx.draw_networkx_edges(G_per_ms2, pos_per_ms2, width=edgew_per_ms2_GN, edge_color="navy", style='-')
    #Nodos
nx.draw_networkx_nodes(G_per_ms2, pos_per_ms2, node_color=color_communities_per_ms2_7, node_size=1300, node_shape='o', linewidths=1,edgecolors="black")
    #Etiquetas sobre nodos
nx.draw_networkx_labels(G_per_ms2, pos_per_ms2, font_size=16, bbox=dict(ec="black",boxstyle="round",facecolor="white",pad=0.3,alpha=0.6), font_weight='normal', font_family='Verdana', horizontalalignment='center', verticalalignment='center',clip_on=False)

#Modificaciones sobre el espacio de representación
x_per_ms2_7.tight_layout()
plt.axis("off") 
y_per_ms2_7.margins(0.05,0.05)
plt.savefig("GN-CG33-It7.png")
plt.show() 


# Para este último caso, ya en la primera iteración aparecen siete comunidades con entre 2 y 3 nodos cada una. A partir de entonces, se construyen comunidades de dos nodos y finalmente estas se van separando en "mono-comunidades" como se va a ver en el siguiente bloque.
# 
# Este caso también es interesante para el estudio. Es más, debido a su rápida división en un alto número de comunidades se representarán las iteraciones del grafo en un dendograma.

# In[218]:


communities_per_ms2 = list(community.girvan_newman(G_per_ms2))
communities_per_ms2


# ###  5.4. Representación del dendograma asociado a la aplicación del algoritmo G-N a la subvariante 3.3

# Por último, en este subapartado se va a realizar la representación del dendograma asociado a la aplicación del algoritmo de Girvan - Newman a la perspectiva 3.3. 

# In[220]:


Image.open('Dendograma GN-33.JPG')

