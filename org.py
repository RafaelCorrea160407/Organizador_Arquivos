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
    if destino == None:
        pasta_destino = pasta / "Outros"
    else:
        pasta_destino = pasta / destino
        
    arquivo_destino = pasta_destino / arquivo.name
    pasta_destino.mkdir(exist_ok=True, parents=True)
    arquivo.rename(arquivo_destino)
      
       
       
       
       
        
        
               


