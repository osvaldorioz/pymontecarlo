import pi_montecarlo
from fastapi import FastAPI
import time

app = FastAPI()

@app.get("/montecarlo")
async def montecarlo(total_points: int, num_threads: int):
    start = time.time()
    # Calcular Pi usando el método de Monte Carlo y concurrencia
    pi_estimate = pi_montecarlo.concurrent_monte_carlo_pi(total_points, num_threads)

    end = time.time()

    var1 = 'Time taken in seconds: '
    var2 = end - start

    str = f'{var1}{var2}\n'.format(var1=var1, var2=var2)
    str1= f"Estimación de Pi con {total_points} puntos y {num_threads} hilos: {pi_estimate}"
    
    return str + str1