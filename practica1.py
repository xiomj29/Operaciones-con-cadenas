"""
    Aplicación para realizar operaciones básicas con cadenas - Teoría de la Computación (v1)
    
    Compilación y ejecución:
    
    linux:
    
    op 1 (terminal):
    cd ruta/practica1.py
    python3 practica1.py 
    
    op 2 (terminal):
    python3 "ruta/practica1.py"
    

"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import os

class OperacionesApp:
    """
    Esta clase implementa una interfaz gráfica con dos pestañas:
    1. Subcadenas, Prefijos y Sufijos: Para analizar una cadena de texto
    2. Cerradura de Kleene y Positiva: Para generar combinaciones de un alfabeto
    """
    def __init__(self, root):
        """
        Constructor de la aplicación.
        
        Parámetros:
        - root: La ventana principal de tkinter donde se dibujará la aplicación
        """
        # Configuración inicial de la ventana
        self.root = root
        self.root.title("Operaciones Básicas con cadenas - Teoría de la Computación")
        self.root.geometry("800x600")  # Ancho x Alto de la ventana
        
        # Crear notebook (sistema de pestañas para organizar la interfaz)
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Crear los marcos para cada pestaña
        self.tab1 = ttk.Frame(self.notebook)  # Pestaña 1
        self.tab2 = ttk.Frame(self.notebook)  # Pestaña 2
        
        # Añadir las pestañas al notebook con sus títulos
        self.notebook.add(self.tab1, text="Subcadenas, Prefijos y Sufijos")
        self.notebook.add(self.tab2, text="Cerradura de Kleene y Positiva")
        
        # Llamar a los métodos que configuran cada pestaña
        self.setup_tab1()  # Primera pestaña
        self.setup_tab2()  # Segunda pestaña
    
    def setup_tab1(self):
        """
        Configura la interfaz de la primera pestaña para subcadenas, prefijos y sufijos.
        Esta pestaña permite al usuario ingresar una cadena de texto y calcular todas las
        subcadenas, prefijos y sufijos posibles.
        """
        # Título principal de la pestaña
        ttk.Label(self.tab1, text="Subcadenas, Prefijos y Sufijos", font=("Arial", 16, "bold")).pack(pady=10)
        ttk.Label(self.tab1, text="Ingrese una cadena para calcular todas sus subcadenas, prefijos y sufijos").pack(pady=5)
        
        # Frame para la entrada de texto
        # Un frame es un contenedor que ayuda a organizar elementos
        input_frame = ttk.Frame(self.tab1)
        input_frame.pack(fill='x', padx=20, pady=10)  # fill='x' hace que se expanda horizontalmente
        
        # Etiqueta y campo de entrada para la cadena de texto
        ttk.Label(input_frame, text="Ingrese una cadena:").pack(side=tk.LEFT, padx=5)
        self.input_text = ttk.Entry(input_frame, width=40)  # Campo de entrada de texto
        self.input_text.pack(side=tk.LEFT, fill='x', expand=True, padx=5)
        
        # Frame para los botones de acción
        btn_frame = ttk.Frame(self.tab1)
        btn_frame.pack(pady=10)
        
        # Botones para calcular y guardar resultados
        ttk.Button(btn_frame, text="Calcular", command=self.calcular_subcadenas).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Guardar Resultados", command=self.guardar_subcadenas).pack(side=tk.LEFT, padx=5)
        
        # Frame para mostrar los resultados
        result_frame = ttk.Frame(self.tab1)
        result_frame.pack(fill='both', expand=True, padx=20, pady=10)
        
        # Área de texto con scroll para mostrar los resultados
        ttk.Label(result_frame, text="Resultados:").pack(anchor='w')  # 'w' = oeste (alineado a la izquierda)
        self.result_text = scrolledtext.ScrolledText(result_frame, wrap=tk.WORD, width=70, height=15)
        self.result_text.pack(fill='both', expand=True, pady=5)
    
    def setup_tab2(self):
        """
        Configura la interfaz de la segunda pestaña para cerraduras de Kleene y positiva.
        Esta pestaña permite al usuario ingresar un alfabeto y generar todas las posibles
        combinaciones hasta una longitud máxima especificada.
        """
        # Título principal de la pestaña
        ttk.Label(self.tab2, text="Cerradura de Kleene y Positiva", font=("Arial", 16, "bold")).pack(pady=10)
        ttk.Label(self.tab2, text="Ingrese un alfabeto y elija la longitud máxima para generar las cerraduras").pack(pady=5)
        
        # Frame para la entrada del alfabeto
        alfabeto_frame = ttk.Frame(self.tab2)
        alfabeto_frame.pack(fill='x', padx=20, pady=10)
        
        # Etiqueta y campo de entrada para el alfabeto
        ttk.Label(alfabeto_frame, text="Alfabeto (sin espacios):").pack(side=tk.LEFT, padx=5)
        self.alfabeto_input = ttk.Entry(alfabeto_frame, width=40)
        self.alfabeto_input.pack(side=tk.LEFT, fill='x', expand=True, padx=5)
        
        # Frame para el control deslizante de longitud
        longitud_frame = ttk.Frame(self.tab2)
        longitud_frame.pack(fill='x', padx=20, pady=10)
        
        # Etiqueta, slider y valor numérico para la longitud máxima
        ttk.Label(longitud_frame, text="Longitud máxima:").pack(side=tk.LEFT, padx=5)
        self.longitud_var = tk.IntVar(value=3)  # Variable que almacena el valor del slider, inicia en 3
        self.longitud_slider = ttk.Scale(longitud_frame, from_=1, to=10, variable=self.longitud_var, orient='horizontal')
        self.longitud_slider.pack(side=tk.LEFT, fill='x', expand=True, padx=5)
        self.longitud_label = ttk.Label(longitud_frame, text="3")  # Muestra el valor actual del slider
        self.longitud_label.pack(side=tk.LEFT, padx=5)
        
        # Configurar que la etiqueta se actualice cuando el valor del slider cambie
        # trace_add registra una función que se ejecutará cuando la variable cambie
        self.longitud_var.trace_add("write", self.update_longitud_label)
        
        # Frame para los botones de acción
        btn_frame = ttk.Frame(self.tab2)
        btn_frame.pack(pady=10)
        
        # Botones para calcular y guardar resultados
        ttk.Button(btn_frame, text="Calcular Cerraduras", command=self.calcular_cerraduras).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Guardar Resultados", command=self.guardar_cerraduras).pack(side=tk.LEFT, padx=5)
        
        # Frame para mostrar los resultados
        result_frame = ttk.Frame(self.tab2)
        result_frame.pack(fill='both', expand=True, padx=20, pady=10)
        
        # Área de texto con scroll para mostrar los resultados
        ttk.Label(result_frame, text="Resultados:").pack(anchor='w')
        self.cerraduras_text = scrolledtext.ScrolledText(result_frame, wrap=tk.WORD, width=70, height=15)
        self.cerraduras_text.pack(fill='both', expand=True, pady=5)
    
    def update_longitud_label(self, *args):
        """
        Actualiza la etiqueta que muestra el valor del slider de longitud.
        
        Parámetros:
        - *args: Argumentos variables que son pasados por el sistema de eventos de tkinter
                (no los usamos directamente)
        """
        self.longitud_label.config(text=str(self.longitud_var.get()))
    
    def calcular_subcadenas(self):
        """
        Calcula y muestra todas las subcadenas, prefijos y sufijos de la cadena ingresada.
        Esta función se ejecuta cuando el usuario hace clic en "Calcular" en la primera pestaña.
        """
        # Obtener el texto ingresado y eliminar espacios al inicio y final
        text = self.input_text.get().strip()
        if not text:
            # Mostrar advertencia si no se ingresó texto
            messagebox.showwarning("Advertencia", "Por favor ingrese una cadena")
            return
        
        # Calcular subcadenas, prefijos y sufijos usando las funciones auxiliares
        subcadenas = self.get_subcadenas(text)
        prefijos = self.get_prefijos(text)
        sufijos = self.get_sufijos(text)
        
        # Mostrar resultados en el área de texto
        # Primero borrar el contenido actual (desde el principio hasta el final)
        self.result_text.delete(1.0, tk.END)
        # Insertar la cadena original
        self.result_text.insert(tk.END, f"Cadena original: {text}\n\n")
        
        # Insertar subcadenas
        self.result_text.insert(tk.END, "SUBCADENAS:\n")
        self.result_text.insert(tk.END, ", ".join(f"'{s}'" for s in subcadenas))
        
        # Insertar prefijos
        self.result_text.insert(tk.END, "\n\nPREFIJOS:\n")
        self.result_text.insert(tk.END, ", ".join(f"'{s}'" for s in prefijos))
        
        # Insertar sufijos
        self.result_text.insert(tk.END, "\n\nSUFIJOS:\n")
        self.result_text.insert(tk.END, ", ".join(f"'{s}'" for s in sufijos))
    
    def guardar_subcadenas(self):
        """
        Guarda los resultados de subcadenas, prefijos y sufijos en un archivo de texto.
        Esta función se ejecuta cuando el usuario hace clic en "Guardar Resultados" en la primera pestaña.
        """
        # Obtener el texto ingresado
        text = self.input_text.get().strip()
        if not text:
            # Mostrar advertencia si no hay resultados para guardar
            messagebox.showwarning("Advertencia", "No hay resultados para guardar")
            return
        
        try:
            # Abrir archivo en modo escritura ('w')
            # encoding="utf-8" asegura que los caracteres especiales se guarden correctamente
            with open("resultados_subcadenas.txt", "w", encoding="utf-8") as f:
                # Calcular los resultados
                subcadenas = self.get_subcadenas(text)
                prefijos = self.get_prefijos(text)
                sufijos = self.get_sufijos(text)
                
                # Escribir los resultados en el archivo
                f.write(f"Cadena original: {text}\n\n")
                f.write("SUBCADENAS:\n")
                f.write(", ".join(f"'{s}'" for s in subcadenas))
                
                f.write("\n\nPREFIJOS:\n")
                f.write(", ".join(f"'{s}'" for s in prefijos))
                
                f.write("\n\nSUFIJOS:\n")
                f.write(", ".join(f"'{s}'" for s in sufijos))
            
            # Mostrar mensaje de éxito
            messagebox.showinfo("Éxito", "Resultados guardados en 'resultados_subcadenas.txt'")
        except Exception as e:
            # Capturar y mostrar cualquier error que ocurra
            messagebox.showerror("Error", f"Error al guardar: {str(e)}")
    
    def calcular_cerraduras(self):
        """
        Calcula y muestra las cerraduras de Kleene y positiva del alfabeto ingresado.
        Esta función se ejecuta cuando el usuario hace clic en "Calcular Cerraduras" en la segunda pestaña.
        """
        # Obtener el alfabeto ingresado
        alfabeto = self.alfabeto_input.get().strip()
        if not alfabeto:
            # Mostrar advertencia si no se ingresó un alfabeto
            messagebox.showwarning("Advertencia", "Por favor ingrese un alfabeto")
            return
        
        # Obtener la longitud máxima seleccionada
        longitud_max = self.longitud_var.get()
        # Generar las cerraduras
        kleene, positiva = self.generar_cerraduras(alfabeto, longitud_max)
        
        # Mostrar resultados en el área de texto
        self.cerraduras_text.delete(1.0, tk.END)  # Borrar contenido actual
        self.cerraduras_text.insert(tk.END, f"Alfabeto: {alfabeto}\n")
        self.cerraduras_text.insert(tk.END, f"Longitud máxima: {longitud_max}\n\n")
        
        # Insertar cerradura de Kleene (incluye la cadena vacía)
        self.cerraduras_text.insert(tk.END, "CERRADURA DE KLEENE (Σ*):\n")
        self.cerraduras_text.insert(tk.END, ", ".join(kleene))
        
        # Insertar cerradura positiva (no incluye la cadena vacía)
        self.cerraduras_text.insert(tk.END, "\n\nCERRADURA POSITIVA (Σ+):\n")
        self.cerraduras_text.insert(tk.END, ", ".join(positiva))
    
    def guardar_cerraduras(self):
        """
        Guarda los resultados de las cerraduras en un archivo de texto.
        Esta función se ejecuta cuando el usuario hace clic en "Guardar Resultados" en la segunda pestaña.
        """
        # Obtener el alfabeto ingresado
        alfabeto = self.alfabeto_input.get().strip()
        if not alfabeto:
            # Mostrar advertencia si no hay resultados para guardar
            messagebox.showwarning("Advertencia", "No hay resultados para guardar")
            return
        
        try:
            # Obtener la longitud máxima y generar las cerraduras
            longitud_max = self.longitud_var.get()
            kleene, positiva = self.generar_cerraduras(alfabeto, longitud_max)
            
            # Guardar los resultados en un archivo
            with open("resultados_cerraduras.txt", "w", encoding="utf-8") as f:
                f.write(f"Alfabeto: {alfabeto}\n")
                f.write(f"Longitud máxima: {longitud_max}\n\n")
                
                f.write("CERRADURA DE KLEENE (Σ*):\n")
                f.write(", ".join(kleene))
                
                f.write("\n\nCERRADURA POSITIVA (Σ+):\n")
                f.write(", ".join(positiva))
            
            # Mostrar mensaje de éxito
            messagebox.showinfo("Éxito", "Resultados guardados en 'resultados_cerraduras.txt'")
        except Exception as e:
            # Capturar y mostrar cualquier error que ocurra
            messagebox.showerror("Error", f"Error al guardar: {str(e)}")
    
    # Funciones auxiliares para operaciones de teoría de lenguajes
    def get_subcadenas(self, text):
        """
        Calcula todas las subcadenas posibles de una cadena.
        Una subcadena es cualquier secuencia contigua de caracteres de la cadena original.
        
        Parámetros:
        - text: La cadena de texto a analizar
        
        Retorna:
        - Una lista ordenada de todas las subcadenas (ordenadas por longitud)
        """
        result = []
        # Para cada posición inicial posible
        for i in range(len(text)):
            # Para cada posición final posible después de la inicial
            for j in range(i + 1, len(text) + 1):
                # Añadir la subcadena extraída a la lista
                result.append(text[i:j])
        # Ordenar las subcadenas por longitud y retornar
        return sorted(result, key=len)
    
    def get_prefijos(self, text):
        """
        Calcula todos los prefijos posibles de una cadena.
        Un prefijo es cualquier subcadena que comienza en el primer carácter de la cadena original.
        
        Parámetros:
        - text: La cadena de texto a analizar
        
        Retorna:
        - Una lista de todos los prefijos (ordenados por longitud)
        """
        # List comprehension que genera todos los prefijos
        # text[:i] extrae los primeros i caracteres
        return [text[:i] for i in range(1, len(text) + 1)]
    
    def get_sufijos(self, text):
        """
        Calcula todos los sufijos posibles de una cadena.
        Un sufijo es cualquier subcadena que termina en el último carácter de la cadena original.
        
        Parámetros:
        - text: La cadena de texto a analizar
        
        Retorna:
        - Una lista de todos los sufijos (ordenados por longitud inversa)
        """
        # List comprehension que genera todos los sufijos
        # text[i:] extrae los caracteres desde la posición i hasta el final
        return [text[i:] for i in range(len(text))]

    def generar_cerraduras(self, alfabeto, longitud_max):
        """
        Genera las cerraduras de Kleene y positiva de un alfabeto hasta una longitud máxima.
        - Cerradura de Kleene (Σ*): Todas las cadenas posibles incluyendo la cadena vacía
        - Cerradura Positiva (Σ+): Todas las cadenas posibles excluyendo la cadena vacía
        
        Parámetros:
        - alfabeto: Cadena que contiene los símbolos del alfabeto
        - longitud_max: Longitud máxima de las cadenas a generar
        
        Retorna:
        - Tupla (kleene, positiva) con las listas de cadenas generadas
        """
        # Cerradura de Kleene (incluye cadena vacía)
        kleene = ["ε"]  # Cadena vacía representada como epsilon (ε)
        positiva = []  # Cerradura positiva (no incluye la cadena vacía)
        
        # Generar cadenas para cada longitud desde 1 hasta longitud_max
        for longitud in range(1, longitud_max + 1):
            # Obtener todas las cadenas de la longitud actual
            nuevas_cadenas = self.generar_cadenas(alfabeto, longitud)
            # Añadir a ambas cerraduras
            kleene.extend(nuevas_cadenas)
            positiva.extend(nuevas_cadenas)
        
        return kleene, positiva
    
    def generar_cadenas(self, alfabeto, longitud):
        """
        Genera todas las cadenas posibles de una longitud específica usando un alfabeto dado.
        
        Parámetros:
        - alfabeto: Cadena que contiene los símbolos del alfabeto
        - longitud: Longitud exacta de las cadenas a generar
        
        Retorna:
        - Lista de todas las cadenas posibles de la longitud especificada
        """
        # Caso base: longitud 0 (cadena vacía)
        if longitud == 0:
            return [""]
        
        # Caso base: longitud 1 (solo los símbolos del alfabeto)
        if longitud == 1:
            return list(alfabeto)
        
        # Caso recursivo para longitud > 1
        result = []
        # Obtener todas las cadenas de longitud (longitud-1)
        subcadenas = self.generar_cadenas(alfabeto, longitud - 1)
        # Para cada subcadena anterior
        for subcadena in subcadenas:
            # Añadir cada símbolo del alfabeto al final
            for simbolo in alfabeto:
                # Concatenar y añadir a los resultados
                result.append(subcadena + simbolo)
        
        return result

# Punto de entrada del programa
if __name__ == "__main__":
    """
    Código que se ejecuta cuando se corre el script directamente.
    Crea la ventana principal y inicia la aplicación.
    """
    root = tk.Tk()  # Crear la ventana principal de tkinter
    app = OperacionesApp(root)  # Inicializar nuestra aplicación
    root.mainloop()  # Iniciar el ciclo principal de eventos de la interfaz gráfica