import os
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

def format_size(size_bytes: int) -> str:
    """Devuelve el tamaño con la unidad más conveniente."""
    units = ["B", "KB", "MB", "GB", "TB"]
    size = float(size_bytes)
    for unit in units:
        if size < 1024 or unit == units[-1]:
            if unit == "B":
                return f"{size:.0f} {unit}"
            else:
                return f"{size:.2f} {unit}"
        size /= 1024
    return f"{size_bytes} B"

class DirectoryTreeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Visualizador de Directorios")
        self.root.geometry("800x600")

        # Frame superior para la entrada de ruta
        top_frame = ttk.Frame(root, padding="10")
        top_frame.pack(fill=tk.X)

        ttk.Label(top_frame, text="Ruta:").pack(side=tk.LEFT)
        
        self.path_var = tk.StringVar()
        self.entry = ttk.Entry(top_frame, textvariable=self.path_var)
        self.entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        
        btn_browse = ttk.Button(top_frame, text="Examinar...", command=self.browse_folder)
        btn_browse.pack(side=tk.LEFT)

        btn_scan = ttk.Button(top_frame, text="Escanear", command=self.scan_folder)
        btn_scan.pack(side=tk.LEFT, padx=5)

        # Treeview para mostrar el árbol
        self.tree = ttk.Treeview(root, columns=("size",), selectmode="browse")
        self.tree.heading("#0", text="Nombre", anchor=tk.W)
        self.tree.heading("size", text="Tamaño", anchor=tk.E)
        self.tree.column("#0", stretch=True, width=400)
        self.tree.column("size", width=100, anchor=tk.E)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y, pady=10)

        # Iconos (emojis simples para no depender de imágenes externas)
        self.folder_icon = "📁"
        self.file_icon = "📄"

    def browse_folder(self):
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            self.path_var.set(folder_selected)

    def scan_folder(self):
        path = self.path_var.get()
        if not os.path.isdir(path):
            messagebox.showerror("Error", "La ruta especificada no es válida.")
            return

        # Limpiar árbol existente
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Iniciar escaneo
        root_node = self.tree.insert("", "end", text=f"{self.folder_icon} {os.path.basename(path) or path}", open=True)
        self.process_directory(path, root_node)

    def process_directory(self, path, parent_node):
        try:
            # Obtener lista ordenada (directorios primero)
            entries = os.scandir(path)
            entries = sorted(entries, key=lambda e: (not e.is_dir(), e.name.lower()))
        except PermissionError:
            self.tree.insert(parent_node, "end", text="⚠️ Acceso Denegado")
            return 0

        total_size = 0
        
        for entry in entries:
            try:
                if entry.is_dir(follow_symlinks=False):
                    # Insertar nodo de carpeta (vacío inicialmente para el tamaño)
                    node = self.tree.insert(parent_node, "end", text=f"{self.folder_icon} {entry.name}", open=False)
                    
                    # Recursividad
                    dir_size = self.process_directory(entry.path, node)
                    total_size += dir_size
                    
                    # Actualizar tamaño de la carpeta en el árbol
                    self.tree.set(node, "size", format_size(dir_size))
                    
                else:
                    file_size = entry.stat(follow_symlinks=False).st_size
                    total_size += file_size
                    self.tree.insert(parent_node, "end", text=f"{self.file_icon} {entry.name}", values=(format_size(file_size),))
            except Exception:
                continue

        # Actualizar tamaño del nodo padre (si es la raíz)
        if self.tree.parent(parent_node) == "":
             self.tree.set(parent_node, "size", format_size(total_size))

        return total_size

if __name__ == "__main__":
    root = tk.Tk()
    # Intentar mejorar la resolución en Windows
    try:
        from ctypes import windll
        windll.shcore.SetProcessDpiAwareness(1)
    except:
        pass
        
    app = DirectoryTreeApp(root)
    root.mainloop()
