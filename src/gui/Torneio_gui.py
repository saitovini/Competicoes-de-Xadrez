import tkinter as tk
from tkinter import messagebox, ttk
import requests

def abrirTorneios(root):
    def list_torneios():
        for row in tree.get_children():
            tree.delete(row)

        try:
            response = requests.get("http://localhost:8080/api/torneios")
            response.raise_for_status()
            torneios = response.json()
            
            for torneio in torneios:
                tree.insert("", "end", values=(
                    torneio['id'],
                    torneio['nome'],
                    torneio.get('vencedor_id', 'N/A'),
                    torneio['local']
                ))
        except requests.RequestException as e:
            messagebox.showerror("Erro", f"Erro ao listar torneios: {e}")

    def save_torneio():
        try:
            id = int(entry_id.get())
            nome = entry_nome.get()
            vencedor_id = int(entry_vencedor_id.get()) if entry_vencedor_id.get() else None
            local = entry_local.get()

            data = {
                "id": id,
                "nome": nome,
                "vencedor_id": vencedor_id,
                "local": local
            }

            response = requests.post("http://localhost:8080/api/torneios", data=data)
            response.raise_for_status()
            list_torneios()
            messagebox.showinfo("Sucesso", "Torneio salvo com sucesso!")
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores válidos.")
        except requests.RequestException as e:
            messagebox.showerror("Erro", f"Erro ao salvar torneio: {e}")

    def delete_torneio():
        try:
            selected_item = tree.selection()
            if not selected_item:
                messagebox.showwarning("Aviso", "Selecione um torneio para excluir.")
                return

            id = tree.item(selected_item[0], "values")[0]
            response = requests.delete(f"http://localhost:8080/api/torneio/{id}")
            response.raise_for_status()
            list_torneios()
            messagebox.showinfo("Sucesso", "Torneio excluído com sucesso!")
        except requests.RequestException as e:
            messagebox.showerror("Erro", f"Erro ao excluir torneio: {e}")

    def update_torneio():
        try:
            selected_item = tree.selection()
            if not selected_item:
                messagebox.showwarning("Aviso", "Selecione um torneio para atualizar.")
                return

            id = tree.item(selected_item[0], "values")[0]
            nome = entry_nome.get()
            vencedor_id = int(entry_vencedor_id.get()) if entry_vencedor_id.get() else None
            local = entry_local.get()

            data = {
                "nome": nome,
                "vencedor_id": vencedor_id,
                "local": local
            }

            response = requests.put(f"http://localhost:8080/api/torneio/{id}", data=data)
            response.raise_for_status()
            list_torneios()
            messagebox.showinfo("Sucesso", "Torneio atualizado com sucesso!")
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores válidos.")
        except requests.RequestException as e:
            messagebox.showerror("Erro", f"Erro ao atualizar torneio: {e}")

    def on_select(event):
        selected_item = tree.selection()
        if selected_item:
            values = tree.item(selected_item[0], "values")
            entry_id.delete(0, tk.END)
            entry_nome.delete(0, tk.END)
            entry_vencedor_id.delete(0, tk.END)
            entry_local.delete(0, tk.END)

            entry_id.insert(0, values[0])
            entry_nome.insert(0, values[1])
            entry_vencedor_id.insert(0, values[2] if values[2] != "N/A" else "")
            entry_local.insert(0, values[3])

    root = tk.Tk()
    root.title("Gerenciar Torneios")

    tk.Label(root, text="ID:").grid(row=0, column=0, padx=10, pady=5)
    entry_id = tk.Entry(root)
    entry_id.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(root, text="Nome:").grid(row=1, column=0, padx=10, pady=5)
    entry_nome = tk.Entry(root)
    entry_nome.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(root, text="Vencedor ID:").grid(row=2, column=0, padx=10, pady=5)
    entry_vencedor_id = tk.Entry(root)
    entry_vencedor_id.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(root, text="Local:").grid(row=3, column=0, padx=10, pady=5)
    entry_local = tk.Entry(root)
    entry_local.grid(row=3, column=1, padx=10, pady=5)

    save_button = tk.Button(root, text="Salvar Torneio", command=save_torneio)
    save_button.grid(row=4, column=0, pady=10)

    update_button = tk.Button(root, text="Atualizar Torneio", command=update_torneio)
    update_button.grid(row=4, column=1, pady=10)

    delete_button = tk.Button(root, text="Excluir Torneio", command=delete_torneio)
    delete_button.grid(row=4, column=2, pady=10)

    tree = ttk.Treeview(root, columns=("ID", "Nome", "Vencedor ID", "Local"), show="headings")
    tree.heading("ID", text="ID")
    tree.heading("Nome", text="Nome")
    tree.heading("Vencedor ID", text="Vencedor ID")
    tree.heading("Local", text="Local")
    tree.grid(row=5, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

    tree.bind("<<TreeviewSelect>>", on_select)

    root.grid_rowconfigure(5, weight=1)
    root.grid_columnconfigure(1, weight=1)

    list_torneios()

    root.mainloop()
