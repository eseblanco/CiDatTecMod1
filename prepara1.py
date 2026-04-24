"""

    genere un programa en python en el archivo prepara1.py en el cual  habra el archivo bank-full.csv y recorra el archivo realizando lo siguiente:
    
    1- Codifique el atributo job por numeración y crea un archivo jobs.csv donde este el codigo del job y la descripción. 
    2- Codifique el atributo education por numeración y crea un archivo education.csv donde este el codigo del education y la descripción.
"""

import csv

def main():
    input_file = 'bank-full.csv'
    output_file = 'bank-full-encoded.csv'
    jobs_file = 'jobs.csv'
    education_file = 'education.csv'

    # Diccionarios para guardar los mapeos {descripción: código}
    job_map = {}
    education_map = {}

    # Contadores para asignar los códigos numéricos
    job_counter = 1
    education_counter = 1

    # Lista para almacenar los datos codificados
    encoded_data = []
    headers = []

    try:
        # Recorrer el archivo original
        with open(input_file, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f, delimiter=';')
            headers = reader.fieldnames
            
            for row in reader:
                # 1- Codificar job
                job_desc = row.get('job', '')
                if job_desc and job_desc not in job_map:
                    job_map[job_desc] = job_counter
                    job_counter += 1
                if job_desc:
                    row['job'] = job_map[job_desc]

                # 2- Codificar education
                edu_desc = row.get('education', '')
                if edu_desc and edu_desc not in education_map:
                    education_map[edu_desc] = education_counter
                    education_counter += 1
                if edu_desc:
                    row['education'] = education_map[edu_desc]

                encoded_data.append(row)

        # Crear jobs.csv
        with open(jobs_file, mode='w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['codigo', 'descripcion'])
            # Ordenar por código
            for desc, code in sorted(job_map.items(), key=lambda item: item[1]):
                writer.writerow([code, desc])

        # Crear education.csv
        with open(education_file, mode='w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['codigo', 'descripcion'])
            for desc, code in sorted(education_map.items(), key=lambda item: item[1]):
                writer.writerow([code, desc])

        # Guardar los datos con las columnas codificadas en un nuevo archivo
        with open(output_file, mode='w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=headers, delimiter=';')
            writer.writeheader()
            writer.writerows(encoded_data)

        print("Procesamiento completado exitosamente.")
        print(f"Se han generado los siguientes archivos:")
        print(f"- {jobs_file}: Catálogo de códigos y descripciones de 'job'")
        print(f"- {education_file}: Catálogo de códigos y descripciones de 'education'")
        print(f"- {output_file}: Archivo de datos original con los atributos codificados")

    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{input_file}'. Asegúrese de que exista en el directorio actual.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

if __name__ == '__main__':
    main()
