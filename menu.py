from classes import *
from metodos import *
from cores import *

def menu():
    Animes.limparTela()
    print(f"{azulclaro}-------- Cadastro de Animes --------")
    print(f"{verde}1 - Cadastrar Anime")
    print(f"2 - Editar informações")
    print(f"3 - Excluir Anime")
    print(f"4 - Selecionar Anime")
    print("5 - Listar Animes")
    print("6 - Sair")
    print(f"{azulclaro}----------------------------------")
    opcao = int(input("Digite a opção desejada: "))
    return opcao


while True:
    opcao = menu()

    if opcao == 1:
        anime = Animes.cadastrarAnime()
        criarAnime(anime)
        Animes.exibirMsg("Anime cadastrado!")
    elif opcao == 2:
        anime = Animes.editarAnime()
        editarAnime(anime)
        Animes.exibirMsg("Anime editado!")
    elif opcao == 3:
        Animes.limparTela()
        id = Animes.excluirAnime()
        excluirAnime(id)
        Animes.exibirMsg("Anime excluído!")
    elif opcao == 4:
        id = Animes.selecionarAnime()
        anime = selecionarAnime(id)
        if anime == None:
            Animes.exibirMsg("Anime não encontrado")
        else:
            Animes.exibirAnime(anime)
            Animes.travarTela()
    elif opcao == 5:
        animes = selecionarTodos()
        Animes.exibirAnimes(animes)
    elif opcao == 6:
        break