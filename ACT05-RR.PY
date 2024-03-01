#Hernandez Chavez Isaac Alberto
#215769734
#seminario de solucion de sistemas operativos
import tkinter as tk
import time
import threading
import random
from tkinter import ttk
import queue  

#para hacer un programa que simule el funcionamiento de un algoritmo de planificacion FCFS'
#se hace uso de una cola en python
#se declara la cola de caracter global
cola_de_procesos=queue.Queue()
cola_de_procesos_terminados=queue.Queue()
quantum = 5
#reloj
clock=0

#configuracion de ventana
ventana = tk.Tk()
ventana.title("Hernandez chavez isaac alberto")
ventana.geometry("600x300")
#ventana.configure(bg="#C300C9")
ventana.configure(relief="ridge")

# Variables globales para pausar y detener los procesos
pausar_proceso_A = threading.Event()
pausar_proceso_B = threading.Event()
pausar_proceso_C = threading.Event()
pausar_proceso_D = threading.Event()

detener_proceso = threading.Event()

#semaforos
semaphore_general= threading.Semaphore(1) # ESTA PARTE ES DE SUMA IMPORTANCIA PARA  QUE NO SE EJECUTEN MAS DE DOS HILOS A LA VEZ, ESTA LIMITADO A UN PROCESO A LA VEZ

#procesos
class proceso_objet:
     def __init__(self,nombre,tiempo,hilo) -> None:
        self.nombre=nombre
        self.tiempo=tiempo
        self.hilo=hilo
        


# Función para iniciar el proceso de actualización de la barra de progreso
# en esta seccion del codigo se detienen cada una de las secciones del mismo (barras de progreso)
def actualizar_barra_de_progreso(progress_bar, nombre_proceso):
    semaphore_general.acquire() # ESTA PARTE ES DE SUMA IMPORTANCIA PARA  QUE NO SE EJECUTEN MAS DE DOS HILOS A LA VEZ
    valor = 0
    #labels
    label_A=tk.Label(ventana,text='A',fg="green")
    label_B=tk.Label(ventana,text='B',fg="green")
    label_C=tk.Label(ventana,text='C',fg="green")
    label_D=tk.Label(ventana,text='D',fg="green")
    #LABELS TERMINADO
    label_A_terminado=tk.Label(ventana,text='A',fg="red")
    label_B_terminado=tk.Label(ventana,text='B',fg="red")
    label_C_terminado=tk.Label(ventana,text='C',fg="red")
    label_D_terminado=tk.Label(ventana,text='D',fg="red")
    

    
    while valor < 100:                                                      #proceso A
        if nombre_proceso=="A":
            if not pausar_proceso_A.is_set():
                    
                    valor +=random.uniform(1,5)
                    if valor<100 and clock%2==0:
                        ventana.after(100, lambda p=progress_bar, v=valor: p.configure(value=v))
                        ventana.update_idletasks()
                        #ceracion de tabla
                        label_A.grid(row=8,column=2)
                        labelCola_A.grid_forget()
                        
                        
                    else:
                        #destruccion de label
                        label_A.grid_forget()
                        label_A.destroy()
                        #NUEVO LABEL
                        label_A_terminado.grid(row=11,column=2)
                        ventana.after(100, lambda p=progress_bar, v=valor: p.configure(value=100))

                        ventana.update_idletasks()
        ventana.update()                 
    
        if nombre_proceso=="B":                                                      #proceso B
            if not pausar_proceso_B.is_set():
                    valor +=random.uniform(1,7)
                    if valor<=100:
                        ventana.after(100, lambda p=progress_bar, v=valor: p.configure(value=v))
                        ventana.update_idletasks()

                        label_B.grid(row=8,column=3)
                        labelCola_B.grid_forget()
                        
                    if valor>100:
                        #destruccion de label
                        label_B.grid_forget()
                        label_B.destroy()
                        #NUEVO LABEL
                        label_B_terminado.grid(row=11,column=3)
                        ventana.after(100, lambda p=progress_bar, v=valor: p.configure(value=100))
                        ventana.update_idletasks()
                        
                        
        if nombre_proceso=="C":                                                      #proceso C
            if not pausar_proceso_C.is_set():
                    valor +=random.uniform(1,10)
                    if valor<=100:
                        ventana.after(100, lambda p=progress_bar, v=valor: p.configure(value=v))
                        ventana.update_idletasks()
                        
                        label_C.grid(row=8,column=5)
                        labelCola_C.grid_forget()
                        
                    if valor>100:
                        #destruccion de label
                        label_C.grid_forget()
                        label_C.destroy()
                        #NUEVO LABEL
                        label_C_terminado.grid(row=11,column=5)
                        ventana.after(100, lambda p=progress_bar, v=valor: p.configure(value=100))
                        ventana.update_idletasks()
                        
                        
        if nombre_proceso=="D":                                                      #proceso D
            if not pausar_proceso_D.is_set():
                    valor +=random.uniform(1,3)
                    if valor<=100:
                        ventana.after(100, lambda p=progress_bar, v=valor: p.configure(value=v))
                        ventana.update_idletasks()
                        
                        label_D.grid(row=8,column=7)
                        labelCola_D.grid_forget()
                        
                    if valor>100:
                        #destruccion de label
                        label_D.grid_forget()
                        label_D.destroy()
                        #NUEVO LABEL
                        label_D_terminado.grid(row=11,column=7)
                        ventana.after(100, lambda p=progress_bar, v=valor: p.configure(value=100))
                        ventana.update_idletasks()
                        
                        
        time.sleep(0.1)
        if valor % quantum == 0:
            break
        
        if detener_proceso.is_set():
            progress_bar.configure(value=0)
            break
    semaphore_general.release()
# Función que representa una fase de ejecución de un proceso
def fase_ejecucion(nombre_proceso, progress_bar):
    print(f"Fase de Ejecución del Proceso {nombre_proceso}: El proceso se está ejecutando")
    
        

# Función que inicia un proceso
def iniciar_proceso(nombre_proceso, progress_bar):
    progress_bar.start()
    actualizar_barra_de_progreso(progress_bar, nombre_proceso)
    
    progress_bar.stop()
    #t_actualizacion_1 = threading.Thread(target=actualizar_barra_de_progreso, args=(progress_bar, nombre_proceso))
    #t_ejecucion = threading.Thread(target=fase_ejecucion, args=(nombre_proceso, progress_bar))
    
    #semaphore_general.acquire()
    #t_actualizacion_1.start()
    #t_actualizacion_2.start()
    #t_actualizacion_3.start()
    #t_actualizacion_4.start()
    #t_ejecucion.start()
    #t_ejecucion.join()
    
    progress_bar.stop()

# Crear una barra de progreso determinada para cada proceso
progress_bars = []
for i, proceso in enumerate(["A", "B", "C", "D"]):
    progress_bar = ttk.Progressbar(ventana, orient="horizontal", length=200, mode="determinate")
    progress_bar.grid(row=i+1, column=1, columnspan=3, padx=10, pady=10)
    letra=tk.Label(ventana,text=proceso)
    letra.grid(row=i+1, column=0)
    progress_bars.append(progress_bar)

#labels***********************************************************************
enTerminacion = tk.Label(ventana, text="terminado:", font=("Arial", 9, "bold"))
enTerminacion.grid(row=11, column=0,rowspan=2)

enEjecucion = tk.Label(ventana, text="ejecutandose:", font=("Arial", 9, "bold"))
enEjecucion.grid(row=8, column=0,rowspan=2)

#labels esteticos
linea = tk.Label(ventana, text="--------------------------------------------------------------------------------------------------------", font=("Arial", 9, "bold"))
linea.grid(row=11, column=1,columnspan=8)

linea2 = tk.Label(ventana, text="-------------------------------------------------------------------------------------------------------", font=("Arial", 9, "bold"))
linea2.grid(row=8, column=1,columnspan=8)

linea3 = tk.Label(ventana, text="-------------------------------------------------------------------------------------------------------", font=("Arial", 9, "bold"))
linea3.grid(row=7, column=1,columnspan=8)


# label de cola****************************************************************
labelCola = tk.Label(ventana, text=" En cola:", font=("Arial", 9, "bold"))
labelCola.grid(row=7, column=0)
#labels de cola****************************************************************
labelCola_A = tk.Label(ventana, text="A")
labelCola_A.grid(row=7, column=2)
labelCola_B= tk.Label(ventana, text="B")
labelCola_B.grid(row=7, column=3)
labelCola_C = tk.Label(ventana, text="C")
labelCola_C.grid(row=7, column=5)
labelCola_D= tk.Label(ventana, text="D")
labelCola_D.grid(row=7, column=7)

# Botón para pausar A
boton_pausarA = tk.Button(ventana, text="Pausar/Reanudar", command=lambda: pausar_proceso_A.set() if not pausar_proceso_A.is_set() else pausar_proceso_A.clear())
boton_pausarA.grid(row=1, column=5, columnspan=3, padx=10, pady=10)
# Botón para pausar B
boton_pausarB = tk.Button(ventana, text="Pausar/Reanudar", command=lambda: pausar_proceso_B.set() if not pausar_proceso_B.is_set() else pausar_proceso_B.clear())
boton_pausarB.grid(row=2, column=5, columnspan=3, padx=10, pady=10)
# Botón para pausar C
boton_pausarC = tk.Button(ventana, text="Pausar/Reanudar", command=lambda: pausar_proceso_C.set() if not pausar_proceso_C.is_set() else pausar_proceso_C.clear())
boton_pausarC.grid(row=3, column=5, columnspan=3, padx=10, pady=10)
# Botón para pausar D
boton_pausarD = tk.Button(ventana, text="Pausar/Reanudar", command=lambda: pausar_proceso_D.set() if not pausar_proceso_D.is_set() else pausar_proceso_D.clear())
boton_pausarD.grid(row=4, column=5, columnspan=3, padx=10, pady=10)


# Botón para detener los procesos
boton_detener = tk.Button(ventana, text="Detener", command=lambda: detener_proceso.set())
boton_detener.grid(row=3, column=9, columnspan=3, padx=10, pady=10)




def desencolar():
    while not cola_de_procesos.empty():
        proceso = cola_de_procesos.get()

        proceso.hilo.start()

        
        
    
    
    
        
         
#se crea esta funcion para evitar hacer uso de demasiadas variables globales
def inicio():
    # Iniciar los procesos en hilos separados
    procesos_a_alternar=[]
    for i, proceso in enumerate(["A", "B", "C", "D"]):
        print(proceso)
        
        t_proceso = threading.Thread(target=iniciar_proceso, args=(proceso, progress_bars[i]))
        
        newProceso=proceso_objet(proceso,random.randint(0,10),t_proceso)
        procesos_a_alternar.append(newProceso)
        

        
    #simplemente para hacer mas divertida la ejecucion del programa
    random.shuffle(procesos_a_alternar)
    for i in procesos_a_alternar:
        cola_de_procesos.put(i)#se "encolan" los procesos
    desencolar()


inicio()
ventana.mainloop()
