from PySimpleGUI import Window, Button, Text, Image
import music

musicas = music.Musicas.procurar('sons')
index = 0
cont = 1

widgets = [
    [Image(filename='vini.png', background_color='gray')],
    [Text(' ' * 10, background_color='gray')],
    [Text(f'{musicas[index][:-4]}', background_color='gray', font=('Arial', 10, 'underline'), key='texto')], 
    [Text(' ' * 10, background_color='gray')],   
    [Button(image_filename='back.png', button_color='gray', border_width=0, key='back', ),
     Button(image_filename='play.png', button_color='gray', border_width=0, key='play'),
     Button(image_filename='skip.png', button_color='gray', border_width=0, key='skip')]
]

tela = Window('Kr Music', size=(300,450), layout=widgets, element_justification='c', background_color='gray')

while True:
    events, values = tela.read()
    if events == 'back':
        index -= 1
        if index < 0:
            index = len(musicas) - 1
        music.Musicas.add_musicas('sons', musicas[index])
        music.Musicas.play()
        tela['texto'].update(musicas[index][:-4])

    if events == 'play':
        if cont >= 3:
            cont = 1
        music.Musicas.add_musicas('sons', musicas[index])
        music.Musicas.play(cont)
        cont += 1
        tela['texto'].update(musicas[index][:-4])


    if events == 'skip':
        index += 1
        if index >= len(musicas):
            index = 0
        music.Musicas.add_musicas('sons', musicas[index])
        music.Musicas.play()
        tela['texto'].update(musicas[index][:-4])

        print(len(musicas))

    if events == Window.close:
        break

tela.close()