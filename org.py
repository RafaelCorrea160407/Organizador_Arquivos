from pathlib import Path
from datetime import datetime
import json

pasta_script = Path(__file__).parent
caminho_dict = pasta_script / "config.json"

with open(caminho_dict, "r") as arquivo:
     arquivos = json.load(arquivo)

caminho = input("Digite o caminho da pasta que deseja organizar: ")
pasta = Path(caminho)
while not pasta.exists() or not pasta.is_dir():
    if not pasta.exists():
        print("O caminho informado não existe.")
    elif not pasta.is_dir():
        print("O caminho informado não é uma pasta.")
    caminho = input("Digite o caminho da pasta que deseja organizar: ")
    pasta = Path(caminho)
     


contador_categorias = {}
caminho_log = pasta_script / "log.txt"
def descobrir_destino(arquivo, arquivos):
        sufixo = arquivo.suffix
        destino = arquivos.get(sufixo)

        if destino is None:
            destino = "Outros"
        return destino

def gerar_nome_duplicados(arquivo, pasta_destino):
    arquivo_destino = pasta_destino / arquivo.name
    numero = 1
    while arquivo_destino.exists():
        arquivo_novo = f"{arquivo.stem} ({numero}){arquivo.suffix}"
        arquivo_destino = pasta_destino / arquivo_novo

        numero += 1
    return arquivo_destino

def mostrar_mensagem(arquivo, destino):
        print("✔ Arquivo Organizado com Sucesso!")
        print(f"Arquivo: {arquivo.name}")
        print(f"Pasta:{destino}")

def atualizar_resumo(destino):
    contador_categorias[destino] = contador_categorias.get(destino, 0) + 1

def mostrar_resumo():
    if not contador_categorias:
        print("Nenhum arquivo encontrado para organizar.")
        return

    print("\nResumo por categoria:")

    for categoria, quantidade in contador_categorias.items():
        print(f"{categoria}: {quantidade}")

def registrar_log(arquivo,destino, caminho_log, status):
     agora = datetime.now()
     data = agora.strftime("%Y-%m-%d")
     hora = agora.strftime("%H:%M:%S")

     arquivo_log = f" Caminho original: {arquivo.parent} | {data} {hora}| Arquivo: {arquivo.name}| Tipo: {arquivo.suffix}| Destino: {destino}| Status: {status}\n"
     with open(caminho_log, "a") as log:
          log.write(arquivo_log)  

for arquivo in pasta.glob("*"):
    if arquivo.is_dir():
        continue
    destino = descobrir_destino(arquivo, arquivos)
    pasta_destino = pasta / destino

    arquivo_destino = gerar_nome_duplicados(arquivo, pasta_destino)
    pasta_destino.mkdir(exist_ok=True, parents=True)
    try:
        arquivo.rename(arquivo_destino)
        atualizar_resumo(destino)

        mostrar_mensagem(arquivo, destino)

        registrar_log(arquivo, destino, caminho_log, "Sucesso")

    except PermissionError:
        registrar_log(arquivo, destino, caminho_log, "Erro de Permissão")
    except FileNotFoundError:
        registrar_log(arquivo, destino, caminho_log, "Erro de arquivo não encontrado")
mostrar_resumo()
        


    
        
    
       
       
       
       
        
        
               


