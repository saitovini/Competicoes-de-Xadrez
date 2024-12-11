from src.controller.JogadoresController import JogadorItem, JogadorList
from src.controller.TorneiosController import TorneioItem, TorneioList
from src.controller.PartidasController import PartidaItem, PartidaList
from src.controller.CategoriasController import CategoriaItem, CategoriaList
from src.controller.JuizesController import JuizItem, JuizList

def initialize_endpoints(api):
    # Jogador
    api.add_resource(JogadorItem, "/jogador/<int:jogador_id>")
    api.add_resource(JogadorList, "/jogadores")

    # Torneios
    api.add_resource(TorneioItem, "/torneio/<int:torneio_id>")
    api.add_resource(TorneioList, "/torneios")

    # Partidas
    api.add_resource(PartidaItem, "/partida/<int:partida_id>")
    api.add_resource(PartidaList, "/partidas")
    
    # Categorias
    api.add_resource(CategoriaItem, "/categoria/<int:categoria_id>")
    api.add_resource(CategoriaList, "/categorias")

    #juizes
    api.add_resource(JuizItem, "/juiz/<int:juiz_id>")
    api.add_resource(JuizList, "/juizes")

