import tkinter as tk
from tkinter import messagebox, ttk
import requests

def abrirJuizes(root):
    def list_juizes():
        for row in tree.get_children():
            tree.delete(row)

        try:
            response = requests.get("http://localhost:8080/api/juizes")
            response.raise_for_status()
            juizes = response.json()
            
            for juiz in juizes:
                tree.insert("", "end", values=(juiz['id'], juiz['nome']))
        except requests.RequestException as e:
            messagebox.showerror("Erro", f"Erro ao listar juízes: {e}")

    def save_juiz():
        try:
            id = int(entry_id.get())
            nome = entry_nome.get()

            data = {"id": id, "nome": nome}
            response = requests.post("http://localhost:8080/api/juizes", data=data)
            response.raise_for_status()
            list_juizes()
            messagebox.showinfo("Sucesso", "Juiz salvo com sucesso!")
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores válidos.")
        except requests.RequestException as e:
            messagebox.showerror("Erro", f"Erro ao salvar juiz: {e}")

    def delete_juiz():
        try:
            selected_item = tree.selection()
            if not selected_item:
                messagebox.showwarning("Aviso", "Selecione um juiz para excluir.")
                return

            id = tree.item(selected_item[0], "values")[0]
            response = requests.delete(f"http://localhost:8080/api/juiz/{id}")
            response.raise_for_status()
            list_juizes()
            messagebox.showinfo("Sucesso", "Juiz excluído com sucesso!")
        except requests.RequestException as e:
            messagebox.showerror("Erro", f"Erro ao excluir juiz: {e}")

    def update_juiz():
        try:
            selected_item = tree.selection()
            if not selected_item:
                messagebox.showwarning("Aviso", "Selecione um juiz para atualizar.")
                return

            id = tree.item(selected_item[0], "values")[0]
            nome = entry_nome.get()

            data = {"nome": nome}
            response = requests.put(f"http://localhost:8080/api/juiz/{id}", data=data)
            response.raise_for_status()
            list_juizes()
            messagebox.showinfo("Sucesso", "Juiz atualizado com sucesso!")
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores válidos.")
        except requests.RequestException as e:
            messagebox.showerror("Erro", f"Erro ao atualizar juiz: {e}")

    def on_select(event):
        selected_item = tree.selection()
        if selected_item:
            values = tree.item(selected_item[0], "values")
            entry_id.delete(0, tk.END)
            entry_nome.delete(0, tk.END)

            entry_id.insert(0, values[0])
            entry_nome.insert(0, values[1])

    root = tk.Tk()
    root.title("Gerenciar Juízes")

    tk.Label(root, text="ID:").grid(row=0, column=0, padx=10, pady=5)
    entry_id = tk.Entry(root)
    entry_id.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(root, text="Nome:").grid(row=1, column=0, padx=10, pady=5)
    entry_nome = tk.Entry(root)
    entry_nome.grid(row=1, column=1, padx=10, pady=5)

    save_button = tk.Button(root, text="Salvar Juiz", command=save_juiz)
    save_button.grid(row=2, column=0, pady=10)

    update_button = tk.Button(root, text="Atualizar Juiz", command=update_juiz)
    update_button.grid(row=2, column=1, pady=10)

    delete_button = tk.Button(root, text="Excluir Juiz", command=delete_juiz)
    delete_button.grid(row=2, column=2, pady=10)

    tree = ttk.Treeview(root, columns=("ID", "Nome"), show="headings")
    tree.heading("ID", text="ID")
    tree.heading("Nome", text="Nome")
    tree.grid(row=3, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

    tree.bind("<<TreeviewSelect>>", on_select)

    root.grid_rowconfigure(3, weight=1)
    root.grid_columnconfigure(1, weight=1)

    list_juizes()

    root.mainloop()
