import os

class Animes:
    def cadastrarAnime():
        Animes.limparTela()
        print("-------- Cadastro de Animes --------")
        anime = {}
        anime['nome'] = input('Nome do anime: ')
        anime['episodios'] = int(input('Numero de Episodios: '))
        anime['anoLancamento'] = int(input('Ano de Lancamento: '))
        anime['autor'] = input('Autor da Obra: ')
        anime['genero'] = input('Genero do anime: ')
        anime['classificacao'] = input('Classificacao: ')

        return anime


    def editarAnime():
        Animes.limparTela()
        print("-------- Edição de Animes --------")
        anime = {}
        anime['id'] = int(input('ID do anime: '))
        anime['nome'] = input('nome: ')
        anime['episodios'] = input('episodios: ')
        anime['anoLancamento'] = input('Ano de Lancamento: ')
        anime['autor'] = input('Autor da Obra: ')
        anime['genero'] = input('Genero do anime: ')
        anime['classificacao'] = input('Classificação do anime: ')
        return anime


    def excluirAnime():
        print("-------- Exclusão de Animes --------")
        Animes.limparTela()
        id = int(input('ID do anime: '))
        return id


    def selecionarAnime():
        Animes.limparTela()
        print("-------- Seleção de Animes --------")
        id = int(input('ID do anime: '))
        return id


    def exibirAnime(anime):
        print("-------- Animes --------")
        print(f"ID: {anime['id']}")
        print(f"Nome do anime: {anime['nome']}")
        print(f"Quantidade de episodios: {anime['episodios']}")
        print(f"Ano de lancamento: {anime['anoLancamento']}")
        print(f"Autor da obra: {anime['autor']}")
        print(f"Genero do anime: {anime['genero']}")
        print(f"Classificação do anime: {anime['classificacao']}")    
        


    def exibirAnimes(animes):
        Animes.limparTela()
        print("---------------- Animes ----------------")
        for anime in animes:
            Animes.exibirAnime(anime)
        Animes.travarTela()


    def limparTela():
        os.system('clear' if os.name == 'posix' else 'cls')


    def travarTela():
        input('Pressione ENTER para continuar...')


    def exibirMsg(msg):
        print(msg)
        Animes.travarTela()