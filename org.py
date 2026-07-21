from pathlib import Path
from datetime import datetime
from tkinter import filedialog, messagebox
import json
import sys
def obter_pasta_script():
    if getattr(sys, "frozen", False):
        return Path(sys.executable).parent
    return Path(__file__).parent

pasta_script = obter_pasta_script()
caminho_dict = pasta_script / "config.json"
caminhos_ignorados = pasta_script / ".orgignore"

with open(caminho_dict, "r", encoding="utf-8") as arquivo:
     arquivos = json.load(arquivo)

caminho = filedialog.askdirectory(title="Selecione a Pasta que deseja organizar")
if not caminho:
    print("Você nao escolheu nenhuma Pasta")
    sys.exit()

pasta = Path(caminho)

with open(caminhos_ignorados, "r", encoding="utf-8") as arq:    
    arquivos_ignorados = set(arq.read().splitlines())


contador_categorias = {}
caminho_log = pasta / "log.txt"
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
        messagebox.showinfo(
            "Organizador de Arquivos",
            "Nenhum arquivo encontrado para organizar."
        )
        return

    total = sum(contador_categorias.values())

    resumo = "Organização concluída com sucesso!\n\n"
    resumo += "Resumo por categoria:\n\n"

    for categoria, quantidade in contador_categorias.items():
        resumo += f"{categoria}: {quantidade}\n"

    resumo += f"\nTotal de arquivos organizados: {total}"
    resumo += f"\n\nLog salvo em:\n{caminho_log}"

    messagebox.showinfo("Organizador de Arquivos", resumo)

def registrar_log(arquivo,destino, caminho_log, status):
     agora = datetime.now()
     data = agora.strftime("%Y-%m-%d")
     hora = agora.strftime("%H:%M:%S")

     arquivo_log = f" Caminho original: {arquivo.parent} | {data} {hora}| Arquivo: {arquivo.name}| Tipo: {arquivo.suffix}| Destino: {destino}| Status: {status}\n"
     with open(caminho_log, "a") as log:
          log.write(arquivo_log)  

for arquivo in pasta.rglob("*"):
    if arquivo.is_dir():
        continue
    if arquivo.name in arquivos_ignorados:
         continue
    destino = descobrir_destino(arquivo, arquivos)
    pasta_destino = pasta / destino
    if arquivo.parent == pasta_destino:
         continue

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
        


    
        
    
       
       
       
       
        
        
               


