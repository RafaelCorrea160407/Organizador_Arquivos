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

pasta = Path("C:/Users/Usuário/Documents/Organizador_Arquivos/testes")




contador_categorias = {}
for arquivo in pasta.glob("*"):
    if arquivo.is_file():
       
        sufixo = arquivo.suffix
        destino = arquivos.get(sufixo)

        if destino is None:
            destino = "Outros"
            pasta_destino = pasta / destino
        else:
            pasta_destino = pasta / destino

        contador_categorias[destino] = contador_categorias.get(destino, 0) + 1
        arquivo_destino = pasta_destino / arquivo.name
        pasta_destino.mkdir(exist_ok=True, parents=True)


        arquivo.rename(arquivo_destino)
    
        print("✔ Arquivo Organizado com Sucesso!")
        print(f"Arquivo: {arquivo.name}")
        print(f"Pasta:{destino}")

print("\nResumo por categoria:")

for categoria, quantidade in contador_categorias.items():
    print(f"{categoria}: {quantidade}")


if not contador_categorias:
    print("Nenhum arquivo encontrado para organizar.")
    
       
       
       
       
        
        
               


