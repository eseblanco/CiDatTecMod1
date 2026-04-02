import json
import random

def generate_data(num_files=5, min_trips=10, max_trips=15):
    distritos = ["11504", "11501", "10101", "60101", "20101", "30101", "40101"]
    
    for i in range(1, num_files + 1):
        identificador = str(random.randint(10000, 99999))
        viajes = []
        num_trips = random.randint(min_trips, max_trips)
        
        for _ in range(num_trips):
            origen = random.choice(distritos)
            destino = random.choice(distritos)
            while destino == origen:
                destino = random.choice(distritos)
                
            kilometros = f"{round(random.uniform(1.0, 100.0), 1)}"
            precio_kilometro = f"{random.choice([300, 400, 500, 550, 600])}"
            
            viajes.append({
                "codigo_postal_origen": origen,
                "codigo_postal_destino": destino,
                "kilometros": kilometros,
                "precio_kilometro": precio_kilometro
            })
            
        data = {
            "identificador": identificador,
            "viajes": viajes
        }
        
        filename = f"persona{i}.json"
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"Generated {filename} with {num_trips} trips.")

if __name__ == "__main__":
    generate_data()
