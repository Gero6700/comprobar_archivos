import tkinter as tk
from tkinter import messagebox
import os
import datetime

def comprobar_archivos_c(carpeta, unidad_hotel):
    # Obtener fecha actual
    fecha_actual = datetime.datetime.now()

    # Restar un día
    un_dia = datetime.timedelta(days=1)
    fecha_anterior = fecha_actual - un_dia

    # Obtener los últimos dos dígitos del año
    anio = fecha_anterior.strftime("%y")

    # Formatear fecha
    fecha_formateada = fecha_anterior.strftime("%d%m%y")

    # Comprobar archivos faltantes
    archivos_faltantes = []
    for numero, nombre in unidad_hotel.items():
        nombre_archivo = 'C' + fecha_formateada + '.' + numero
        ruta_archivo = os.path.join(carpeta, nombre_archivo)

        if not os.path.isfile(ruta_archivo):
            archivos_faltantes.append(f"{numero}: {nombre}")

    # Mostrar el mensaje correspondiente
    if archivos_faltantes:
        mensaje = "C faltantes:\n\n" + "\n".join(archivos_faltantes)
        messagebox.showerror("Faltan C", mensaje)
    else:
        messagebox.showinfo("Todos los C han llegado", "¡Han llegado todos los C!")

# CARPETA DE C
carpeta = 'C:\\Users\\gero6\\Desktop\\hoteles'

unidad_hotel = {
    '0510': 'PLAYA BACHATA',
    '0520': 'PUERTO PLATA',
    # Agrega más números y nombres aquí
}

comprobar_archivos_c(carpeta, unidad_hotel)
