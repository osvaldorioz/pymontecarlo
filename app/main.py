import pi_montecarlo
from fastapi import FastAPI
import time

import random

app = FastAPI()

@app.get("/pymontecarlo")
async def pymontecarlo(total_points: int):
    #RANGO
    start = time.time()
    INTERVAL= total_points
    
    circle_points= 0 #PUNTOS DENTRO DEL CÍRCULO 
    square_points= 0 #PUNTOS DENTRO DEL CUADRADO
    
    for i in range(INTERVAL**2):

        #GENERACIÓN DE PUNTOS
        rand_x= random.uniform(-1, 1)
        rand_y= random.uniform(-1, 1)
    
        #DISTANCIA DE CADA PUNTO DEL ORIGEN
        origin_dist= (rand_x**2 + rand_y**2)**0.5
    
        #COMPROBAR SI EL PUNTO ESTÁ DENTRO DEL CÍRCULO.
        if origin_dist<= 1:
            circle_points+= 1
    
        square_points+= 1

        #OBTENCIÓN DEL VALOR DE PI.
        pi = 4* circle_points/ square_points

    #ESTIMACIÓN FINAL.
    print("PI ESTIMATION: ", pi)
    print('TOTAL POINTS: ',square_points)
    end = time.time()
    var1 = 'Time taken in seconds in python: '
    var2 = end - start

    str = f'{var1}{var2}\n'.format(var1=var1, var2=var2)
    str1= f"Estimación de Pi con {square_points} puntos : {pi}"
    
    return str + str1


@app.get("/cppmontecarlo")
async def cppmontecarlo(square_points: int, num_threads: int):
    start = time.time()
    # Calcular Pi usando el método de Monte Carlo y concurrencia
    pi_estimate = pi_montecarlo.concurrent_monte_carlo_pi(square_points, num_threads)

    end = time.time()

    var1 = 'Time taken in seconds: '
    var2 = end - start

    str = f'{var1}{var2}\n'.format(var1=var1, var2=var2)
    str1= f"Estimación de Pi con {square_points} puntos y {num_threads} hilos: {pi_estimate}"
    
    return str + str1
