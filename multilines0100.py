import matplotlib.pyplot as plt
from matplotlib import pyplot
import numpy as np
import random
import time

NUMERODELINEAS  = 25

def crea_graph():
   # Create the vectors X and Y
   plotf = []
   
   for i in range(NUMERODELINEAS):
      plotf.append('plot%d,' %i)
   
      
      
   for i in range(4):
      time.sleep(0)
          
      a = random.randint(-5,5)
      b = random.randint(a+1, 55)
      print(a)
      x = np.arange((a+1), 10 , 0.01)
      print('this is x' +str(x))
      print('este es super ' + str(x))
      y = np.sin(x)
          
      
   #for i in range(4):
   #    print("plot{}".format(i))   
   
   
   # for i in range(4):
   #    print('plot%d,' %i)
      
      
      # genera random para hacer la curva de sin o onda mas amplia (c = random.randrange)
      c = random.randrange(-5,7)
      print('this is c random' + str(c))
      
      for j in range(NUMERODELINEAS):
         print(str(j)+'este es i')
         plotf[j] = plt.plot(x*a,y*b)
         time.sleep(0)
       
         #= plt.plot(x,y)
           
           
         #plot2 = plt.plot(x+1,y)
         #plot2 = plt.plot(x*2,y)
       
         # Show the plot
         plt.show()
         plt.ylabel('titulo en y')
crea_graph()



#//crea loop for el codigo de generar funciones 
#for i in range(3):
#    crea_graph()