while True:
    choiceLang = input("Escolha o idioma / Choose the language\nPT para português\nEN to English): ").strip().upper()
    if choiceLang == 'PT':
        print("Este é um arquivo para praticar a aula de git")
        break
    elif choiceLang == 'EN':
        print("This is a file to practice the git class")
        break
    else:
        print("Idioma não reconhecido / Language not recognized. Tente novamente.")