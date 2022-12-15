from classes import *
from metodos import *

def menu():
    Animes.limparTela()
    print("-------- Cadastro de Animes --------")
    print("1 - Cadastrar Anime")
    print("2 - Editar informações")
    print("3 - Excluir Anime")
    print("4 - Selecionar Anime")
    print("5 - Listar Animes")
    print("6 - Sair")
    print("----------------------------------")
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