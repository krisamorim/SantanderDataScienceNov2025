choiceLang = input("Escolha o idioma / Choose the language\nPT para português\nEN to English): ").strip().upper()
if choiceLang == 'PT':
    print("Este é um arquivo para praticar a aula de git")
elif choiceLang == 'EN':
    print("This is a file to practice the git class")
else:
    print("Idioma não reconhecido / Language not recognized")