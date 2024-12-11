import tkinter as tk
from Categoria_gui import abrirCategorias  
from Jogador_gui import abrirJogadores
from Juiz_gui import abrirJuizes
from Partida_gui import abrirPartidas
from Torneio_gui import abrirTorneios

def centralizar(janela, largura, altura):   
    # Define a geometria da janela
    janela.geometry(f"{largura}x{altura}")


# Janela principal
root = tk.Tk()
root.title("Sistema de Gerenciamento")
centralizar(root, 500, 500)


categorias_button = tk.Button(root, text="Gerenciar Categorias", command=lambda: abrirCategorias(root))
categorias_button.pack(pady=5)

categorias_button = tk.Button(root, text="Gerenciar Jogadores", command=lambda: abrirJogadores(root))
categorias_button.pack(pady=5)

categorias_button = tk.Button(root, text="Gerenciar Juizes", command=lambda: abrirJuizes(root))
categorias_button.pack(pady=5)

categorias_button = tk.Button(root, text="Gerenciar Partidas", command=lambda: abrirPartidas(root))
categorias_button.pack(pady=5)

categorias_button = tk.Button(root, text="Gerenciar Torneios", command=lambda: abrirTorneios(root))
categorias_button.pack(pady=5)

root.mainloop()
