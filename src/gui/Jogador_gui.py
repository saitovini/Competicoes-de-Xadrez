import tkinter as tk
from tkinter import messagebox, ttk
import requests

def abrirJogadores(root):

    def list_jogadores():
        for row in tree.get_children():
            tree.delete(row)

        try:
            response = requests.get("http://localhost:8080/api/jogadores")
            response.raise_for_status()
            jogadores = response.json()
            
            for jog in jogadores:
                tree.insert("", "end", values=(jog['id'], jog['nome'], jog['idade'], jog['categoria_id']))
        except requests.RequestException as e:
            messagebox.showerror("Erro", f"Erro ao listar jogadores: {e}")

    def save_jogador():
        try:
            id = int(entry_id.get())
            nome = entry_nome.get()
            idade = int(entry_idade.get())
            categoria_id = int(entry_categoria.get()) if entry_categoria.get() else None

            data = {
                "id": id,
                "nome": nome,
                "idade": idade,
                "categoria_id": categoria_id
            }

            response = requests.post("http://localhost:8080/api/jogadores", data=data)
            response.raise_for_status()
            list_jogadores()
            messagebox.showinfo("Sucesso", "Jogador salvo com sucesso!")
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores válidos.")
        except requests.RequestException as e:
            messagebox.showerror("Erro", f"Erro ao salvar jogador: {e}")

    def delete_jogador():
        try:
            selected_item = tree.selection()
            if not selected_item:
                messagebox.showwarning("Aviso", "Selecione um jogador para excluir.")
                return

            id = tree.item(selected_item[0], "values")[0]
            response = requests.delete(f"http://localhost:8080/api/jogador/{id}")
            response.raise_for_status()
            list_jogadores()
            messagebox.showinfo("Sucesso", "Jogador excluído com sucesso!")
        except requests.RequestException as e:
            messagebox.showerror("Erro", f"Erro ao excluir jogador: {e}")

    def update_jogador():
        try:
            selected_item = tree.selection()
            if not selected_item:
                messagebox.showwarning("Aviso", "Selecione um jogador para atualizar.")
                return

            id = tree.item(selected_item[0], "values")[0]
            nome = entry_nome.get()
            idade = int(entry_idade.get())
            categoria_id = int(entry_categoria.get()) if entry_categoria.get() else None

            data = {
                "nome": nome,
                "idade": idade,
                "categoria_id": categoria_id
            }

            response = requests.put(f"http://localhost:8080/api/jogador/{id}", data=data)
            response.raise_for_status()
            list_jogadores()
            messagebox.showinfo("Sucesso", "Jogador atualizado com sucesso!")
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores válidos.")
        except requests.RequestException as e:
            messagebox.showerror("Erro", f"Erro ao atualizar jogador: {e}")

    def on_select(event):
        selected_item = tree.selection()
        if selected_item:
            values = tree.item(selected_item[0], "values")
            entry_id.delete(0, tk.END)
            entry_nome.delete(0, tk.END)
            entry_idade.delete(0, tk.END)
            entry_categoria.delete(0, tk.END)

            entry_id.insert(0, values[0])
            entry_nome.insert(0, values[1])
            entry_idade.insert(0, values[2])
            entry_categoria.insert(0, values[3])

    root = tk.Tk()
    root.title("Gerenciar Jogadores")

    tk.Label(root, text="ID:").grid(row=0, column=0, padx=10, pady=5)
    entry_id = tk.Entry(root)
    entry_id.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(root, text="Nome:").grid(row=1, column=0, padx=10, pady=5)
    entry_nome = tk.Entry(root)
    entry_nome.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(root, text="Idade:").grid(row=2, column=0, padx=10, pady=5)
    entry_idade = tk.Entry(root)
    entry_idade.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(root, text="Categoria:").grid(row=3, column=0, padx=10, pady=5)
    entry_categoria = tk.Entry(root)
    entry_categoria.grid(row=3, column=1, padx=10, pady=5)

    save_button = tk.Button(root, text="Salvar Jogador", command=save_jogador)
    save_button.grid(row=4, column=0, pady=10)

    update_button = tk.Button(root, text="Atualizar Jogador", command=update_jogador)
    update_button.grid(row=4, column=1, pady=10)

    delete_button = tk.Button(root, text="Excluir Jogador", command=delete_jogador)
    delete_button.grid(row=4, column=2, pady=10)

    tree = ttk.Treeview(root, columns=("ID", "Nome", "Idade", "Categoria"), show="headings")
    tree.heading("ID", text="ID")
    tree.heading("Nome", text="Nome")
    tree.heading("Idade", text="Idade")
    tree.heading("Categoria", text="Categoria")
    tree.grid(row=5, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

    tree.bind("<<TreeviewSelect>>", on_select)

    root.grid_rowconfigure(5, weight=1)
    root.grid_columnconfigure(1, weight=1)

    list_jogadores()

    root.mainloop()
