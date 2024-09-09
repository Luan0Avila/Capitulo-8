def make_albun(artist, albun):
    music_albun = {'artista': artist, 'album': albun
    }
    return music_albun

supercombo = make_albun('Supercombo', 'This is Supercombo')
print(supercombo)

ogrilo = make_albun('O Grilo', 'O Grilo: As Essenciais')
print(ogrilo)

yunglixo =make_albun('Yung Lixo', 'Bons Tempos')
print(yunglixo)