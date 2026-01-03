# 📁 Visualizador de Directorios

**Visualizador de Directorios** es un proyecto en Python para **explorar carpetas y ver su estructura en forma de árbol**, mostrando **archivos, subcarpetas y tamaños**. Incluye versiones por consola y una versión más completa con **interfaz gráfica (Tkinter)**.

Repo: https://github.com/piero7ov/Visualizador-de-directorios/tree/main

---

## ✨ Qué hace

- Muestra el árbol de una carpeta con iconos tipo:
  - 📁 carpetas
  - 📄 archivos
- Calcula tamaños:
  - Tamaño de archivos
  - Tamaño total por carpeta (sumando contenido)
- Maneja casos comunes:
  - carpetas sin permisos (`PermissionError`)
  - rutas inválidas
  - evita seguir symlinks (en varias partes usa `follow_symlinks=False`)

---

## ✅ Versión recomendada (más “proyecto”)

### 🖥️ GUI (Tkinter)
**`007-tkinter mas visual.py`**  
Permite elegir una carpeta con botón **Examinar…** y verla en un **TreeView** con una columna de **Tamaño**.

### ⌨️ CLI (Consola)
**`006-recorre carpeta concreta.py`**  
Permite generar el árbol desde terminal y opcionalmente guardarlo en un archivo `.txt`.

> Los scripts `003-005` son iteraciones/pruebas (os.walk, árbol más limpio, tamaños en consola).

---

## 🧰 Requisitos

- **Python 3.8+**
- No requiere librerías externas (solo estándar: `os`, `sys`, `tkinter`)

### Nota sobre Tkinter
- En **Windows** suele venir incluido con Python.
- En **Linux** puede que necesites:
  ```bash
  sudo apt install python3-tk

---

## ▶️ Cómo usar

### 1) Interfaz gráfica (recomendado)

Ejecuta:

```bash
python "007-tkinter mas visual.py"
```

Pasos:

1. Click en **Examinar…**
2. Elige una carpeta
3. Click en **Escanear**
4. Navega el árbol y revisa tamaños

✅ Extra: el script intenta mejorar el escalado en Windows (DPI) con `SetProcessDpiAwareness`.

---

### 2) Consola (árbol + tamaños + exportación)

Ejecuta:

```bash
python "006-recorre carpeta concreta.py" "RUTA_DE_LA_CARPETA"
```

Ejemplo (Windows):

```bash
python "006-recorre carpeta concreta.py" "C:\xampp\htdocs"
```

Guardar salida en un archivo:

```bash
python "006-recorre carpeta concreta.py" "C:\xampp\htdocs" "arbol.txt"
```

---

## 🧠 Cómo funciona (resumen)

* Recorre carpetas de forma recursiva.
* Va acumulando tamaños en bytes y los convierte a formato legible (`KB`, `MB`, `GB`).
* Ordena entradas para mostrar primero **directorios** y luego **archivos**.
* Si no hay permisos en una ruta, la marca y sigue con el resto.

---

## 📁 Estructura del proyecto (archivos principales)

* `003-libreria os.py` → recorrido básico con `os.walk`
* `004-mas ordenado arbol.py` → árbol visual con conectores (`├──`, `└──`)
* `005-cuanto ocupa.py` → árbol + tamaños por consola (recursivo)
* `006-recorre carpeta concreta.py` → ✅ CLI parametrizable + exportación a archivo
* `007-tkinter mas visual.py` → ✅ GUI con TreeView (carpetas/archivos + tamaños)

---

## ⚠️ Cosas a tener en cuenta

* En carpetas **muy grandes** (Windows o Linux), el cálculo de tamaños puede tardar.
* Si hay carpetas protegidas, verás algo como **“Acceso Denegado”** o **“Permiso denegado”**.
* Si quieres máximo rendimiento, una mejora típica sería:

  * calcular tamaños “lazy” (cuando expandes una carpeta)
  * o cachear tamaños ya calculados

---

## 🛣️ Ideas de mejora (si lo quieres subir de nivel)

* Barra de progreso mientras escanea
* Botón “Exportar a TXT” desde la GUI
* Filtro por extensiones (`.log`, `.png`, etc.)
* Mostrar “Top 10 archivos más pesados”
* Opción de ignorar carpetas (ej: `node_modules`, `.git`)

---

## 👤 Autor

**Piero Olivares**
GitHub: [https://github.com/piero7ov](https://github.com/piero7ov)

