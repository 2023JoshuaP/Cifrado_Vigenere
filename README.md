# Cifrado Vigenère

## Descripción

El **cifrado de Vigenère** es un método clásico de criptografía por sustitución polialfabética.  
A diferencia del cifrado César (monoalfabético), Vigenère emplea una **clave de varias letras** que determina cómo se cifran los caracteres del texto original, alternando distintos alfabetos.  

Este proyecto implementa el cifrado de Vigenère en **Python**, con una interfaz gráfica desarrollada en **Tkinter**, y también cuenta con una versión en **C++** en consola.  

---

## Características

- Soporte para dos alfabetos:  
    - **27 caracteres** (alfabeto español: A–Z + Ñ).  
    - **191 caracteres** (ASCII extendido del 32 al 222).  

- Entrada desde archivo `.txt` o directamente desde la interfaz.  
- Normalización de texto (conversión a mayúsculas, eliminación de acentos y filtrado según el alfabeto).  
- Interfaz gráfica con Tkinter (Python).  
- Resultados mostrados en pantalla y opción de exportar a archivo (opcional).  

---

## Proceso del cifrado Vigenère

1. **Definir alfabeto:**  
El conjunto de caracteres válidos, por ejemplo:  
- `ABCDEFGHIJKLMNÑOPQRSTUVWXYZ` (27 letras).  
- `chr(32) ... chr(222)` (ASCII extendido).  

2. **Normalizar el texto y la clave:**  
- Convertir todo a mayúsculas.  
- Eliminar tildes (`Á → A`, `É → E`, etc.).  
- Eliminar caracteres que no pertenecen al alfabeto seleccionado.  

3. **Expansión de la clave:**  
La clave se repite tantas veces como sea necesario para cubrir la longitud del texto.  
Ejemplo:

    ```
    Texto: HOLA MUNDO
    Clave: LLAVE
    Exp: LLAVELLLA
    ```

4. **Aplicar el cifrado:**  
Para cada letra:

```
C[i] = (P[i] + K[i]) mod N
```

Donde:  
- `C[i]` = carácter cifrado en la posición `i`.  
- `P[i]` = posición del carácter plano en el alfabeto.  
- `K[i]` = posición del carácter de la clave en el alfabeto.  
- `N` = tamaño del alfabeto.  

5. **Resultado:**  
Se obtiene el texto cifrado concatenando los `C[i]`.

---

## 🧩 Algoritmos principales

- **Normalización (`normalize`)**  
Convierte texto a mayúsculas, elimina tildes y descarta caracteres fuera del alfabeto.

- **Función de índice**  
Determina la posición de cada carácter en el alfabeto.  

- **Cifrado (`vigenere_cipher`)**  
Recorre el texto carácter por carácter, suma la posición de la clave y aplica módulo con la longitud del alfabeto.

---

## Ejemplo de uso

### Entrada
```
Texto: HOLA MUNDO
Clave: LLAVE
Alfabeto: 27 letras
```

### Salida
```
RZLVPFXDK
```

---

## Tecnologías

- **Python 3.10+**  
- **Tkinter** para la interfaz gráfica.  
- **C++17** (versión de consola alternativa).  

---