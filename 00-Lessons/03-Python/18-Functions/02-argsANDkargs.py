def exibir_poema(data_estenso, *args, **kargs):
    text = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kargs.items()])
    mensagem = f"{data_estenso}\n\n{text}\n\n{meta_dados}"
    print(mensagem)

exibir_poema(
    "25 de Dezembro de 2023",
    "No meio do caminho tinha uma pedra",
    "Tinha uma pedra no meio do caminho",
    autor="Carlos Drummond de Andrade",
    obra="Alguma Poesia",
    ano=1930)