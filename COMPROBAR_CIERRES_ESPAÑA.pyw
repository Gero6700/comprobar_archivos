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
    '0010': 'PLAYA CAPRICHO',
    '0020': 'SENATOR CASTELLANA',
    '0030': 'PLAYA DULCE',
    '0040': 'DRIVER AGUADULCE',
    '0050': 'PLAYA SOL',
    '0060': 'DIVER ROQUETAS',
    '0080': 'VERA PLAYA',
    '0090': 'ZIMBALI PLAYA',
    '0130': 'SENATOR MAR MENOR',
    '0150': 'SENATOR BARAJAS',
    '0180': 'PLAYA BALLENA',
    '0200': 'PLAYA LINDA',
    '0260': 'SENATOR CALAMILLOR',
    '0270': 'PLAYA CANELA',
    '0280': 'SENATOR HUELVA',
    '0290': 'MOJACAR PLAYA',
    '0340': 'VIRGEN DE LOS REYES',
    '0350': 'SENATOR MARBELLA',
    '0360': 'SENATOR PARQUE CENTRAL',
    '0410': 'PLAYA MARINA',
    '0420': 'PLAYA CARTAYA',
    '0440': 'SENATOR CADIZ',
    '0450': 'SENATOR GRANADA',
    '0460': 'CALEIA TALAYOT',   
    '0470': 'SENATOR BANUS',    
    '0480': 'APT PARAISO [VERA]', 
    '0610': 'SENATOR GANDIA',
    '0650': 'CLUB SIMO',
    '0660': 'IBIZA',
    '0700': 'MONTANYA',
    '0750': 'GUADACORTE', 
    '2520': 'OASYS MINIHOLLYWOOD', 
    '2510': 'AQUARIUM', 
    # Agrega más números y nombres aquí
}

comprobar_archivos_c(carpeta, unidad_hotel)
