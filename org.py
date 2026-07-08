from pathlib import Path

arquivos = {".png": "Imagens", 
            ".jpg": "Imagens", 
            ".jpeg": "Imagens", 
            ".gif": "Imagens", 
            ".pdf": "PDFs", 
            ".xlsx": "Planilhas"}

pasta = Path("C:/Users/Usuário/Documents/Organizador_Arquivos/testes")



for arquivo in pasta.glob("*"):
    if arquivo.is_file():
       sufixo = arquivo.suffix
       destino = arquivos.get(sufixo)
       
       
        
        
               


