# ==========================
# IMPORTAÇÕES
# ==========================

# Manipulação de caminhos e arquivos de forma multiplataforma
from pathlib import Path

# Utilizado para registrar data e hora no arquivo de log
from datetime import datetime

# Interface gráfica para selecionar pastas e exibir mensagens
from tkinter import filedialog, messagebox

# Leitura do arquivo config.json
import json

# Utilizado para descobrir se o programa está rodando como .py ou .exe
# e também para encerrar o programa quando necessário
import sys


# ==========================================================
# DESCOBRIR A PASTA ONDE O PROGRAMA ESTÁ LOCALIZADO
# ==========================================================
#
# Quando executamos o programa como .py, usamos __file__.
#
# Quando executamos como .exe (PyInstaller),
# usamos sys.executable.
#
# Isso permite encontrar corretamente:
#
# - config.json
# - .orgignore
#
# independentemente da forma como o programa foi iniciado.
# ==========================================================

def obter_pasta_script():
    if getattr(sys, "frozen", False):
        return Path(sys.executable).parent

    return Path(__file__).parent


# Pasta onde o programa está localizado
pasta_script = obter_pasta_script()


# Caminhos para os arquivos de configuração
caminho_dict = pasta_script / "config.json"
caminhos_ignorados = pasta_script / ".orgignore"


# ==========================================================
# CARREGA O DICIONÁRIO DE EXTENSÕES
# ==========================================================
#
# Lê o config.json contendo o mapeamento:
#
# ".png" -> "Imagens"
# ".pdf" -> "PDFs"
#
# Assim é possível alterar categorias sem modificar o código.
# ==========================================================

with open(caminho_dict, "r", encoding="utf-8") as arquivo:
    arquivos = json.load(arquivo)


# ==========================================================
# SELEÇÃO DA PASTA
# ==========================================================
#
# Abre uma janela para o usuário escolher qual pasta
# deseja organizar.
#
# Caso nenhuma pasta seja escolhida,
# o programa é encerrado.
# ==========================================================

caminho = filedialog.askdirectory(
    title="Selecione a Pasta que deseja organizar"
)

if not caminho:
    print("Você nao escolheu nenhuma Pasta")
    sys.exit()

pasta = Path(caminho)


# ==========================================================
# LEITURA DO .ORGIGNORE
# ==========================================================
#
# Arquivos listados neste arquivo NÃO serão organizados.
#
# Exemplo:
#
# config.json
# log.txt
# .orgignore
#
# Os nomes são armazenados em um set
# por possuir busca extremamente rápida.
# ==========================================================

with open(caminhos_ignorados, "r", encoding="utf-8") as arq:
    arquivos_ignorados = set(arq.read().splitlines())


# ==========================================================
# VARIÁVEIS GLOBAIS
# ==========================================================

# Guarda quantos arquivos foram organizados por categoria
contador_categorias = {}

# Caminho onde será salvo o log
caminho_log = pasta / "log.txt"


# ==========================================================
# DESCOBRIR DESTINO
# ==========================================================
#
# Recebe um arquivo e verifica sua extensão.
#
# Exemplo:
#
# foto.png
#
# procura ".png" no config.json
#
# Se encontrar:
#
# retorna "Imagens"
#
# Caso contrário:
#
# retorna "Outros"
# ==========================================================

def descobrir_destino(arquivo, arquivos):

    sufixo = arquivo.suffix

    destino = arquivos.get(sufixo)

    if destino is None:
        destino = "Outros"

    return destino


# ==========================================================
# TRATAMENTO DE DUPLICATAS
# ==========================================================
#
# Evita sobrescrever arquivos.
#
# Exemplo:
#
# foto.png
#
# Já existe?
#
# cria:
#
# foto (1).png
#
# Se também existir:
#
# foto (2).png
#
# E assim sucessivamente.
# ==========================================================

def gerar_nome_duplicados(arquivo, pasta_destino):

    arquivo_destino = pasta_destino / arquivo.name

    numero = 1

    while arquivo_destino.exists():

        arquivo_novo = (
            f"{arquivo.stem} ({numero}){arquivo.suffix}"
        )

        arquivo_destino = pasta_destino / arquivo_novo

        numero += 1

    return arquivo_destino


# ==========================================================
# MENSAGEM NO TERMINAL
# ==========================================================
#
# Exibe qual arquivo acabou de ser organizado.
#
# Durante o desenvolvimento foi muito útil
# para acompanhar o funcionamento do programa.
# ==========================================================

def mostrar_mensagem(arquivo, destino):

    print("✔ Arquivo Organizado com Sucesso!")

    print(f"Arquivo: {arquivo.name}")

    print(f"Pasta: {destino}")


# ==========================================================
# RESUMO POR CATEGORIA
# ==========================================================
#
# Conta quantos arquivos foram enviados
# para cada categoria.
#
# Exemplo:
#
# Imagens -> 5
# PDFs -> 2
# ==========================================================

def atualizar_resumo(destino):

    contador_categorias[destino] = (
        contador_categorias.get(destino, 0) + 1
    )


# ==========================================================
# RESUMO FINAL
# ==========================================================
#
# Exibe uma janela informando:
#
# - categorias
# - quantidade
# - total de arquivos
# - local do log
# ==========================================================

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

    messagebox.showinfo(
        "Organizador de Arquivos",
        resumo
    )


# ==========================================================
# REGISTRO DE LOG
# ==========================================================
#
# Salva um histórico de todas as operações.
#
# Cada linha contém:
#
# - Caminho original
# - Data
# - Hora
# - Nome do arquivo
# - Tipo
# - Destino
# - Status
#
# Isso permite identificar problemas
# ou consultar organizações antigas.
# ==========================================================

def registrar_log(arquivo, destino, caminho_log, status):

    agora = datetime.now()

    data = agora.strftime("%Y-%m-%d")

    hora = agora.strftime("%H:%M:%S")

    arquivo_log = (
        f"Caminho original: {arquivo.parent}"
        f" | {data} {hora}"
        f" | Arquivo: {arquivo.name}"
        f" | Tipo: {arquivo.suffix}"
        f" | Destino: {destino}"
        f" | Status: {status}\n"
    )

    with open(caminho_log, "a") as log:

        log.write(arquivo_log)


# ==========================================================
# LOOP PRINCIPAL
# ==========================================================
#
# Percorre TODOS os arquivos da pasta,
# incluindo subpastas.
#
# Fluxo:
#
# 1 - Ignora diretórios
# 2 - Ignora arquivos do .orgignore
# 3 - Descobre categoria
# 4 - Evita reorganizar arquivos já organizados
# 5 - Trata duplicatas
# 6 - Cria pasta se necessário
# 7 - Move arquivo
# 8 - Atualiza resumo
# 9 - Registra log
# 10 - Trata possíveis erros
# ==========================================================

for arquivo in pasta.rglob("*"):

    # Ignora pastas
    if arquivo.is_dir():
        continue

    # Ignora arquivos definidos pelo usuário
    if arquivo.name in arquivos_ignorados:
        continue

    destino = descobrir_destino(arquivo, arquivos)

    pasta_destino = pasta / destino

    # Evita mover novamente um arquivo
    # que já está na pasta correta.
    if arquivo.parent == pasta_destino:
        continue

    arquivo_destino = gerar_nome_duplicados(
        arquivo,
        pasta_destino
    )

    # Cria a pasta caso ela ainda não exista
    pasta_destino.mkdir(
        exist_ok=True,
        parents=True
    )

    try:

        # Move o arquivo
        arquivo.rename(arquivo_destino)

        # Atualiza estatísticas
        atualizar_resumo(destino)

        # Mostra mensagem no terminal
        mostrar_mensagem(arquivo, destino)

        # Registra sucesso
        registrar_log(
            arquivo,
            destino,
            caminho_log,
            "Sucesso"
        )

    except PermissionError:

        registrar_log(
            arquivo,
            destino,
            caminho_log,
            "Erro de Permissão"
        )

    except FileNotFoundError:

        registrar_log(
            arquivo,
            destino,
            caminho_log,
            "Erro de arquivo não encontrado"
        )


# ==========================================================
# FINALIZAÇÃO
# ==========================================================
#
# Exibe o resumo final da organização.
# ==========================================================

mostrar_resumo()