import random
from datetime import datetime, timedelta

def generar_simulacion(n):
    productos = ["iphone","samsung","xiaomi","laptop","audifonos"]
    categorias = ["tech","audio","computo"]

    data = []
    for i in range(n):
        data.append({
            "id": i+1,
            "producto": random.choice(productos),
            "categoria": random.choice(categorias),
            "costo": random.randint(10000, 500000),
            "stock": random.randint(0,50),
            "fecha": datetime.now() - timedelta(days=random.randint(0,100))
        })
    return data