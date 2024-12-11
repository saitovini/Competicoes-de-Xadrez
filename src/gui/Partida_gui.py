import tkinter as tk
from tkinter import messagebox, ttk
import requests

def abrirPartidas(root):

    def list_partidas():
        for row in tree.get_children():
            tree.delete(row)

        try:
            response = requests.get("http://localhost:8080/api/partidas")
            response.raise_for_status()
            partidas = response.json()
            
            for partida in partidas:
                tree.insert("", "end", values=(
                    partida['id'],
                    partida['torneio_id'],
                    partida['jogador1_id'],
                    partida['jogador2_id'],
                    partida['data_partida'],
                    partida['juiz_id'],
                    partida.get('tipo', 'N/A'),
                    partida.get('resultado', 'N/A'),
                    partida.get('vencedor_id', 'N/A')
                ))
        except requests.RequestException as e:
            messagebox.showerror("Erro", f"Erro ao listar partidas: {e}")

    def save_partida():
        try:
            id = int(entry_id.get())
            torneio_id = int(entry_torneio_id.get()) if entry_torneio_id.get() else None
            jogador1_id = int(entry_jogador1_id.get())
            jogador2_id = int(entry_jogador2_id.get())
            data_partida = entry_data_partida.get()
            juiz_id = int(entry_juiz_id.get())
            tipo = entry_tipo.get() if entry_tipo.get() else None
            resultado = entry_resultado.get() if entry_resultado.get() else None
            vencedor_id = int(entry_vencedor_id.get()) if entry_vencedor_id.get() else None

            data = {
                "id": id,
                "torneio_id": torneio_id,
                "jogador1_id": jogador1_id,
                "jogador2_id": jogador2_id,
                "data_partida": data_partida,
                "juiz_id": juiz_id,
                "tipo": tipo,
                "resultado": resultado,
                "vencedor_id": vencedor_id
            }

            response = requests.post("http://localhost:8080/api/partidas", data=data)
            response.raise_for_status()

            list_partidas()
            messagebox.showinfo("Sucesso", "Partida salva com sucesso!")
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores válidos.")
        except requests.RequestException as e:
            messagebox.showerror("Erro", f"Erro ao salvar partida: {e}")

    def delete_partida():
        try:
            selected_item = tree.selection()
            if not selected_item:
                messagebox.showwarning("Aviso", "Selecione uma partida para excluir.")
                return

            id = tree.item(selected_item[0], "values")[0]  # Obtém o ID da linha selecionada
            response = requests.delete(f"http://localhost:8080/api/partida/{id}")
            response.raise_for_status()

            list_partidas()
            messagebox.showinfo("Sucesso", "Partida excluída com sucesso!")
        except requests.RequestException as e:
            messagebox.showerror("Erro", f"Erro ao excluir partida: {e}")

    def update_partida():
        try:
            selected_item = tree.selection()
            if not selected_item:
                messagebox.showwarning("Aviso", "Selecione uma partida para atualizar.")
                return

            id = tree.item(selected_item[0], "values")[0]  # Obtém o ID da linha selecionada
            torneio_id = int(entry_torneio_id.get()) if entry_torneio_id.get() else None
            jogador1_id = int(entry_jogador1_id.get())
            jogador2_id = int(entry_jogador2_id.get())
            data_partida = entry_data_partida.get()
            juiz_id = int(entry_juiz_id.get())
            tipo = entry_tipo.get() if entry_tipo.get() else None
            resultado = entry_resultado.get() if entry_resultado.get() else None
            vencedor_id = int(entry_vencedor_id.get()) if entry_vencedor_id.get() else None

            data = {
                "torneio_id": torneio_id,
                "jogador1_id": jogador1_id,
                "jogador2_id": jogador2_id,
                "data_partida": data_partida,
                "juiz_id": juiz_id,
                "tipo": tipo,
                "resultado": resultado,
                "vencedor_id": vencedor_id
            }

            response = requests.put(f"http://localhost:8080/api/partida/{id}", data=data)
            response.raise_for_status()

            list_partidas()
            messagebox.showinfo("Sucesso", "Partida atualizada com sucesso!")
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores válidos.")
        except requests.RequestException as e:
            messagebox.showerror("Erro", f"Erro ao atualizar partida: {e}")

    def on_select(event):
        selected_item = tree.selection()
        if selected_item:
            values = tree.item(selected_item[0], "values")
            entry_id.delete(0, tk.END)
            entry_torneio_id.delete(0, tk.END)
            entry_jogador1_id.delete(0, tk.END)
            entry_jogador2_id.delete(0, tk.END)
            entry_data_partida.delete(0, tk.END)
            entry_juiz_id.delete(0, tk.END)
            entry_tipo.delete(0, tk.END)
            entry_resultado.delete(0, tk.END)
            entry_vencedor_id.delete(0, tk.END)

            entry_id.insert(0, values[0])
            entry_torneio_id.insert(0, values[1])
            entry_jogador1_id.insert(0, values[2])
            entry_jogador2_id.insert(0, values[3])
            entry_data_partida.insert(0, values[4])
            entry_juiz_id.insert(0, values[5])
            entry_tipo.insert(0, values[6] if values[6] != "N/A" else "")
            entry_resultado.insert(0, values[7] if values[7] != "N/A" else "")
            entry_vencedor_id.insert(0, values[8] if values[8] != "N/A" else "")

    root = tk.Tk()
    root.title("Gerenciar Partidas")

    # Campos de entrada
    tk.Label(root, text="ID:").grid(row=0, column=0, padx=10, pady=5)
    entry_id = tk.Entry(root)
    entry_id.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(root, text="Torneio ID:").grid(row=1, column=0, padx=5, pady=5)
    entry_torneio_id = tk.Entry(root)
    entry_torneio_id.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(root, text="Jogador 1 ID:").grid(row=2, column=0, padx=10, pady=5)
    entry_jogador1_id = tk.Entry(root)
    entry_jogador1_id.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(root, text="Jogador 2 ID:").grid(row=3, column=0, padx=10, pady=5)
    entry_jogador2_id = tk.Entry(root)
    entry_jogador2_id.grid(row=3, column=1, padx=10, pady=5)

    tk.Label(root, text="Data Partida (YYYY-MM-DD):").grid(row=4, column=0, padx=10, pady=5)
    entry_data_partida = tk.Entry(root)
    entry_data_partida.grid(row=4, column=1, padx=10, pady=5)

    tk.Label(root, text="Juiz ID:").grid(row=5, column=0, padx=10, pady=5)
    entry_juiz_id = tk.Entry(root)
    entry_juiz_id.grid(row=5, column=1, padx=10, pady=5)

    tk.Label(root, text="Tipo:").grid(row=6, column=0, padx=10, pady=5)
    entry_tipo = tk.Entry(root)
    entry_tipo.grid(row=6, column=1, padx=10, pady=5)

    tk.Label(root, text="Resultado:").grid(row=7, column=0, padx=10, pady=5)
    entry_resultado = tk.Entry(root)
    entry_resultado.grid(row=7, column=1, padx=10, pady=5)

    tk.Label(root, text="Vencedor ID:").grid(row=8, column=0, padx=10, pady=5)
    entry_vencedor_id = tk.Entry(root)
    entry_vencedor_id.grid(row=8, column=1, padx=10, pady=5)

    # Botões
    save_button = tk.Button(root, text="Salvar Partida", command=save_partida)
    save_button.grid(row=9, column=0, pady=10)

    update_button = tk.Button(root, text="Atualizar Partida", command=update_partida)
    update_button.grid(row=9, column=1, pady=10)

    delete_button = tk.Button(root, text="Excluir Partida", command=delete_partida)
    delete_button.grid(row=9, column=2, pady=10)

    # Treeview
    tree = ttk.Treeview(root, columns=("ID", "Torneio ID", "Jogador 1 ID", "Jogador 2 ID", "Data Partida", "Juiz ID", "Tipo", "Resultado", "Vencedor ID"), show="headings")
    tree.heading("ID", text="ID")
    tree.heading("Torneio ID", text="Torneio ID")
    tree.heading("Jogador 1 ID", text="Jogador 1 ID")
    tree.heading("Jogador 2 ID", text="Jogador 2 ID")
    tree.heading("Data Partida", text="Data Partida")
    tree.heading("Juiz ID", text="Juiz ID")
    tree.heading("Tipo", text="Tipo")
    tree.heading("Resultado", text="Resultado")
    tree.heading("Vencedor ID", text="Vencedor ID")
    tree.grid(row=10, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

    tree.bind("<<TreeviewSelect>>", on_select)

    root.grid_rowconfigure(10, weight=1)
    root.grid_columnconfigure(1, weight=1)

    list_partidas()

    root.mainloop()
