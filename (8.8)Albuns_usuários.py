def make_albun(artist, albun):
    music_albun = {'artista': artist, 'album': albun
                   }
    return music_albun

while True:
    print('Por favor digite o nome de um artista e um album dele: ')
    print('Pressione q para sair a qualquer momento\n')
    artist_name = input('Nome do artista: ')
    if artist_name == 'q':
        break
    albun_name = input('Nome do albun: ')
    if albun_name == 'q':
        break
    albun = make_albun(artist_name, albun_name)
    print(albun)