import tkinter as tk
from tkinter import messagebox, ttk
import requests

def abrirCategorias(root):
    def list_categorias():
        # Limpa os itens atuais na tabela
        for row in tree.get_children():
            tree.delete(row)

        try:
            response = requests.get("http://localhost:8080/api/categorias")
            response.raise_for_status()
            categorias = response.json()
            
            # Insere os dados das categorias na tabela
            for categoria in categorias:
                tree.insert("", "end", values=(
                    categoria['id'],
                    categoria['nome'],
                    categoria.get('descricao', 'N/A')
                ))
        except requests.RequestException as e:
            messagebox.showerror("Erro", f"Erro ao listar categorias: {e}")

    def save_categoria():
        try:
            id = entry_id.get()
            nome = entry_nome.get()
            descricao = entry_descricao.get() if entry_descricao.get() else None

            data = {
                "id": id,
                "nome": nome,
                "descricao": descricao
            }

            response = requests.post("http://localhost:8080/api/categorias", data=data)
            response.raise_for_status()
            
            # Atualiza a lista de categorias
            list_categorias()
            messagebox.showinfo("Sucesso", "Categoria salva com sucesso!")
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores válidos.")
        except requests.RequestException as e:
            messagebox.showerror("Erro", f"Erro ao salvar categoria: {e}")

    def delete_categoria():
        try:
            selected_item = tree.selection()
            if not selected_item:
                messagebox.showwarning("Aviso", "Selecione uma categoria para excluir.")
                return

            id = tree.item(selected_item[0], "values")[0]  # Obtém o ID da linha selecionada

            response = requests.delete(f"http://localhost:8080/api/categoria/{id}")
            response.raise_for_status()

            # Atualiza a lista de categorias
            list_categorias()
            messagebox.showinfo("Sucesso", "Categoria excluída com sucesso!")
        except requests.RequestException as e:
            messagebox.showerror("Erro", f"Erro ao excluir categoria: {e}")

    def update_categoria():
        try:
            selected_item = tree.selection()
            if not selected_item:
                messagebox.showwarning("Aviso", "Selecione uma categoria para atualizar.")
                return

            id = tree.item(selected_item[0], "values")[0]  # Obtém o ID da linha selecionada
            nome = entry_nome.get()
            descricao = entry_descricao.get() if entry_descricao.get() else None

            data = {
                "nome": nome,
                "descricao": descricao
            }

            response = requests.put(f"http://localhost:8080/api/categoria/{id}", data=data)
            response.raise_for_status()
            
            # Atualiza a lista de categorias
            list_categorias()
            messagebox.showinfo("Sucesso", "Categoria atualizada com sucesso!")
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores válidos.")
        except requests.RequestException as e:
            messagebox.showerror("Erro", f"Erro ao atualizar categoria: {e}")

    def on_select(event):
        # Preenche os campos com os dados da linha selecionada
        selected_item = tree.selection()
        if selected_item:
            values = tree.item(selected_item[0], "values")
            entry_id.delete(0, tk.END)
            entry_nome.delete(0, tk.END)
            entry_descricao.delete(0, tk.END)

            entry_id.insert(0, values[0])
            entry_nome.insert(0, values[1])
            entry_descricao.insert(0, values[2] if values[2] != "N/A" else "")

    root = tk.Tk()
    root.title("Gerenciar Categorias")

    tk.Label(root, text="ID:").grid(row=0, column=0, padx=10, pady=5)
    entry_id = tk.Entry(root)  # a ideia era deixa bloqueado
    entry_id.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(root, text="Nome:").grid(row=1, column=0, padx=10, pady=5)
    entry_nome = tk.Entry(root)
    entry_nome.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(root, text="Descrição:").grid(row=2, column=0, padx=10, pady=5)
    entry_descricao = tk.Entry(root)
    entry_descricao.grid(row=2, column=1, padx=10, pady=5)

    save_button = tk.Button(root, text="Salvar Categoria", command=save_categoria)
    save_button.grid(row=3, column=0, pady=10)

    delete_button = tk.Button(root, text="Excluir Categoria", command=delete_categoria)
    delete_button.grid(row=3, column=2, pady=10)

    update_button = tk.Button(root, text="Atualizar Categoria", command=update_categoria)
    update_button.grid(row=3, column=1, pady=10)

    tree = ttk.Treeview(root, columns=("ID", "Nome", "Descrição"), show="headings")
    tree.heading("ID", text="ID")
    tree.heading("Nome", text="Nome")
    tree.heading("Descrição", text="Descrição")
    tree.grid(row=4, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

    tree.bind("<<TreeviewSelect>>", on_select)  # Vincula a seleção da linha

    root.grid_rowconfigure(4, weight=1)
    root.grid_columnconfigure(1, weight=1)

    list_categorias()

    root.mainloop()
