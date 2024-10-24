import requests
import tkinter as tk
from tkinter import messagebox


# Función para obtener el último registro de la API
def obtener_ultimo_estudiante():
    url = 'https://66db3d98f47a05d55be77b70.mockapi.io/api/v1/estudiante'
    try:
        # Hacemos una solicitud GET a la API
        respuesta = requests.get(url)
        respuesta.raise_for_status()  # Verifica si hubo algún error
        estudiantes = respuesta.json()

        if estudiantes:
            # Obtener el último estudiante de la lista
            ultimo_estudiante = estudiantes[-1]
            return ultimo_estudiante
        else:
            return None
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Hubo un problema al obtener los datos: {e}")
        return None


# Función para mostrar los datos del estudiante en la interfaz
def mostrar_estudiante():
    estudiante = obtener_ultimo_estudiante()

    if estudiante:
        # Extraemos los datos del estudiante
        id_ = estudiante['id']
        nombre = estudiante['nombre']
        apellido = estudiante['apellido']
        ciudad = estudiante['ciudad']
        calle = estudiante['calle']

        # Mostrar los datos en la ventana
        datos_label.config(text=f"ID: {id_}\n"
                                f"Nombre: {nombre}\n"
                                f"Apellido: {apellido}\n"
                                f"Ciudad: {ciudad}\n"
                                f"Calle: {calle}")
    else:
        datos_label.config(text="No se encontró ningún estudiante")


# Crear la ventana de la aplicación con Tkinter
root = tk.Tk()
root.title("Último Estudiante")
root.geometry("300x200")

# Título
titulo_label = tk.Label(root, text="Datos del Último Estudiante", font=("Helvetica", 14))
titulo_label.pack(pady=10)

# Etiqueta para mostrar los datos
datos_label = tk.Label(root, text="", font=("Helvetica", 12), justify="left")
datos_label.pack(pady=10)

# Botón para actualizar y obtener los datos del estudiante
actualizar_btn = tk.Button(root, text="Actualizar", command=mostrar_estudiante)
actualizar_btn.pack(pady=10)

# Llamamos a la función para mostrar los datos al iniciar la aplicación
mostrar_estudiante()

# Ejecutar la aplicación
root.mainloop()
