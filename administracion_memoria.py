import tkinter as tk
from tkinter import messagebox

class MemoryPartition:
    def __init__(self, name, size):
        self.name = name
        self.size = size

class MemoryManager:
    def __init__(self, total_memory, system_percent):
        self.total_memory = total_memory
        self.system_memory = total_memory * system_percent / 100
        self.available_memory = total_memory - self.system_memory
        self.partitions = []
        self.unused_partitions = [MemoryPartition("Free", self.available_memory)]

    def allocate_partition(self, name, size):
        if size > self.available_memory:
            messagebox.showerror("Error", "No hay suficiente memoria disponible para asignar esta partición.")
            return

        # Algoritmo de primer ajuste
        for partition in self.unused_partitions:
            if partition.size >= size:
                partition_index = self.unused_partitions.index(partition)
                self.partitions.append(MemoryPartition(name, size))
                self.unused_partitions[partition_index].size -= size
                if self.unused_partitions[partition_index].size == 0:
                    self.unused_partitions.pop(partition_index)
                self.available_memory -= size
                messagebox.showinfo("Asignación exitosa", f"Partición '{name}' asignada correctamente.")
                return

        messagebox.showerror("Error", "No hay suficiente memoria contigua disponible para asignar esta partición.")

    def deallocate_partition(self, name):
        for partition in self.partitions:
            if partition.name == name:
                self.available_memory += partition.size
                self.partitions.remove(partition)
                self.unused_partitions.append(MemoryPartition("Free", partition.size))
                messagebox.showinfo("Desasignación exitosa", f"Partición '{name}' desasignada correctamente.")
                return

        messagebox.showerror("Error", f"No se encontró una partición con el nombre '{name}'.")

class MemoryApp:
    def __init__(self, master, total_memory, system_percent):
        self.master = master
        master.title("Administración de Memoria")

        self.memory_manager = MemoryManager(total_memory, system_percent)

        self.allocate_button = tk.Button(master, text="Asignar Trabajo", command=self.open_allocate_window)
        self.allocate_button.pack()

        self.deallocate_button = tk.Button(master, text="Desasignar Trabajo", command=self.open_deallocate_window)
        self.deallocate_button.pack()

    def open_allocate_window(self):
        allocate_window = tk.Toplevel(self.master)
        AllocateWindow(allocate_window, self.memory_manager)

    def open_deallocate_window(self):
        deallocate_window = tk.Toplevel(self.master)
        DeallocateWindow(deallocate_window, self.memory_manager)

class AllocateWindow:
    def __init__(self, master, memory_manager):
        self.master = master
        self.memory_manager = memory_manager
        master.title("Asignar Trabajo")

        self.job_name_label = tk.Label(master, text="Nombre del trabajo:")
        self.job_name_label.grid(row=0, column=0)
        self.job_name_entry = tk.Entry(master)
        self.job_name_entry.grid(row=0, column=1)

        self.job_size_label = tk.Label(master, text="Tamaño del trabajo:")
        self.job_size_label.grid(row=1, column=0)
        self.job_size_entry = tk.Entry(master)
        self.job_size_entry.grid(row=1, column=1)

        self.allocate_button = tk.Button(master, text="Asignar", command=self.allocate_job)
        self.allocate_button.grid(row=2, columnspan=2)

    def allocate_job(self):
        job_name = self.job_name_entry.get()
        job_size = int(self.job_size_entry.get())
        self.memory_manager.allocate_partition(job_name, job_size)
        self.master.destroy()

class DeallocateWindow:
    def __init__(self, master, memory_manager):
        self.master = master
        self.memory_manager = memory_manager
        master.title("Desasignar Trabajo")

        self.job_name_label = tk.Label(master, text="Nombre del trabajo:")
        self.job_name_label.grid(row=0, column=0)
        self.job_name_entry = tk.Entry(master)
        self.job_name_entry.grid(row=0, column=1)

        self.deallocate_button = tk.Button(master, text="Desasignar", command=self.deallocate_job)
        self.deallocate_button.grid(row=1, columnspan=2)

    def deallocate_job(self):
        job_name = self.job_name_entry.get()
        self.memory_manager.deallocate_partition(job_name)
        self.master.destroy()

def main():
    root = tk.Tk()
    total_memory = 1024  # Ejemplo de tamaño total de memoria
    system_percent = 30  # Ejemplo de porcentaje de memoria dedicado al sistema
    app = MemoryApp(root, total_memory, system_percent)
    root.mainloop()

if __name__ == "__main__":
    main()
