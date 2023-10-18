import os
import pygame

pygame.mixer.init()

class Musicas():
    def __init__(self) -> None:
        pass

    def procurar(pasta):
        '''
        Está função procura as musicas na pasta 
        args:
            param:Você coloca o nome da pasta
        Returns:
            Ele retorna uma lista com o nome das musicas
        '''
        musicas = []
        arquivo = os.listdir(pasta)
        for m in arquivo:
            musicas.append(m[:])

        return musicas
    
    def volume(volume):
        '''
        A função volume define a altura do play de 0.0 a 1.0
        args:
            param:Você diz a altura do som
        '''
        pygame.mixer.music.set_volume(volume)

    def add_musicas(pasta, musica):
        '''
        Está função adiciona as musicas para tocar
        args:
            param1: pasta de musica
            param: musica
        Returns:
            ele vai carregar as musicas
        '''
        pygame.mixer.music.load(f'{pasta}/{musica}')


    def play(cont=1):
        from time import sleep
        '''
        Está função começa a tocar a musica
        Args:
            param:cont recebe um numero para ver se está tocand a musica ou não
        '''
        if cont == 1:
            pygame.mixer.music.play()
        if cont == 2:
            pygame.mixer.music.pause()



