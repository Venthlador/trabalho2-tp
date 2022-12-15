from json_storage import *
from classes import *

def criarAnime(anime: dict) -> dict:
    animes = lerJson()
    anime['id'] = gerarId()
    animes.append(anime)
    gravarJson(animes)


def editarAnime(anime: dict) -> None:
    animes = lerJson()
    for i, data in enumerate(animes):
        if data['id'] == anime['id']:
            animes[i] = anime
            
    gravarJson(animes)


def excluirAnime(id: int) -> None:
    animes = lerJson()
    for anime in animes:
        if anime['id'] == id:
            animes.remove(anime)
            
    gravarJson(animes)


def selecionarAnime(id: int) -> dict | None:
    animes = lerJson()
    for anime in animes:
        if anime['id'] == id:
            return anime
    return None


def selecionarTodos() -> list:
    return lerJson()

def gerarId() -> int:
    animes = lerJson()
    if len(animes) == 0:
        return 1
    return animes[-1]['id'] + 1