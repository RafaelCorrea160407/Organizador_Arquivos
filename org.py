from pathlib import Path

arquivos = {".png": "Imagens",
            ".jpg": "Imagens",
            ".jpeg": "Imagens",
            ".gif": "Imagens",
            ".bmp": "Imagens",
            ".webp": "Imagens",
            ".svg": "Imagens",
            ".ico": "Imagens",
            ".tiff": "Imagens",
            ".pdf": "PDFs",
            ".doc": "Documentos",
            ".docx": "Documentos",
            ".txt": "Documentos",
            ".rtf": "Documentos",
            ".odt": "Documentos",
            ".xls": "Planilhas",
            ".xlsx": "Planilhas",
            ".csv": "Planilhas",
            ".ods": "Planilhas",
            ".mp3": "Áudios",
            ".wav": "Áudios",
            ".aac": "Áudios",
            ".flac": "Áudios",
            ".ogg": "Áudios",
            ".m4a": "Áudios",
            ".mp4": "Vídeos",
            ".avi": "Vídeos",
            ".mov": "Vídeos",
            ".mkv": "Vídeos",
            ".wmv": "Vídeos",
            ".webm": "Vídeos",
            ".flv": "Vídeos",
            ".zip": "Compactados",
            ".rar": "Compactados",
            ".7z": "Compactados",
            ".tar": "Compactados",
            ".gz": "Compactados",
            ".py": "Python",
            ".java": "Java",
            ".js": "JavaScript",
            ".ts": "TypeScript",
            ".html": "HTML",
            ".css": "CSS",
            ".cpp": "C++",
            ".c": "C",
            ".cs": "C#",
            ".php": "PHP",
            ".json": "JSON",
            ".xml": "XML",
            ".sql": "SQL",
            ".md": "Markdown",
            ".exe": "Executáveis",
            ".msi": "Executáveis",
            ".bat": "Executáveis",}

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
def descobrir_destino(arquivo, arquivos):

        if arquivo.is_file():
       
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



for arquivo in pasta.glob("*"):
        destino = descobrir_destino(arquivo, arquivos)
        pasta_destino = pasta / destino

        arquivo_destino = gerar_nome_duplicados(arquivo, pasta_destino)
        pasta_destino.mkdir(exist_ok=True, parents=True)
        arquivo.rename(arquivo_destino)

        atualizar_resumo(destino)

        mostrar_mensagem(arquivo, destino)

mostrar_resumo()
        


    
        
    
       
       
       
       
        
        
               


