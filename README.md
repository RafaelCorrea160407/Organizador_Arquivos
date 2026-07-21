# 📂 Organizador de Arquivos

> Um organizador de arquivos desenvolvido em **Python** que classifica automaticamente arquivos por categoria, cria pastas, evita arquivos duplicados e gera um relatório da organização.

## 🎬 Demonstração

![Demonstração](images/demo.gif)

---

[![Download](https://img.shields.io/badge/Download-v1.0.0-blue?style=for-the-badge)](https://github.com/RafaelCorrea160407/Organizador_Arquivos/releases/tag/v1.0.0)

---

## ⚠️ Aviso do Windows Defender

Como este é um projeto independente e o executável não possui assinatura digital, o Windows pode exibir um aviso de segurança na primeira execução.

Para executar:

1. Clique em **Mais informações**.
2. Clique em **Executar assim mesmo**.

O código-fonte está disponível neste repositório para consulta.

---

## ✨ Funcionalidades

- 📁 Seleção da pasta por interface gráfica.
- 🔄 Organização automática dos arquivos por extensão.
- 📂 Organização recursiva (incluindo subpastas).
- 🗂️ Criação automática das pastas de destino.
- ⚙️ Configuração personalizada através do `config.json`.
- 🚫 Suporte ao arquivo `.orgignore` para ignorar arquivos específicos.
- 📄 Geração automática de logs da organização.
- 🔢 Tratamento de arquivos duplicados.
- 📊 Resumo da organização ao final do processo.

---

## 🛠️ Tecnologias utilizadas

- Python 3.14
- pathlib
- tkinter
- json
- PyInstaller

---

## 📁 Estrutura do projeto

```text
Organizador_Arquivos/
│
├── dist/
│   ├── org.exe
│   ├── config.json
│   ├── .orgignore
│   └── log.txt
│
├── org.py
├── README.md
├── requirements.txt
└── testes/
```

---

## 🚀 Como utilizar

### Opção 1 — Executável

1. Baixe a versão mais recente na página de **Releases**.
2. Execute `org.exe`.
3. Selecione a pasta que deseja organizar.
4. Aguarde a conclusão da organização.

---

### Opção 2 — Código fonte

Clone o repositório:

```bash
git clone https://github.com/SEU-USUARIO/Organizador_Arquivos.git
```

Entre na pasta:

```bash
cd Organizador_Arquivos
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute:

```bash
python org.py
```

---

## ⚙️ Configuração

O comportamento do programa pode ser personalizado através do arquivo `config.json`.

Exemplo:

```json
{
    ".png": "Imagens",
    ".jpg": "Imagens",
    ".jpeg": "Imagens",
    ".gif": "Imagens",

    ".pdf": "PDFs",

    ".mp4": "Vídeos",
    ".avi": "Vídeos",

    ".mp3": "Músicas"
}
```

Basta adicionar novas extensões ou criar novas categorias.

---

## 🚫 Arquivos ignorados

Arquivos presentes no `.orgignore` não serão organizados.

Exemplo:

```text
config.json
.orgignore
log.txt
```

---

## 📸 Exemplo

### Antes

```text
Downloads/
│
├── foto.png
├── contrato.pdf
├── video.mp4
└── musica.mp3
```

### Depois

```text
Downloads/
│
├── Imagens/
│   └── foto.png
│
├── PDFs/
│   └── contrato.pdf
│
├── Vídeos/
│   └── video.mp4
│
└── Músicas/
    └── musica.mp3
```

---

## 📚 Aprendizados

Durante o desenvolvimento deste projeto foram praticados diversos conceitos importantes da linguagem Python, como:

- Manipulação de arquivos e diretórios.
- Uso da biblioteca `pathlib`.
- Estruturas de dados.
- Manipulação de arquivos JSON.
- Tratamento de exceções.
- Organização de código em funções.
- Interface gráfica utilizando Tkinter.
- Geração de executáveis com PyInstaller.
- Boas práticas de organização de projetos.

---

## 👨‍💻 Autor

**Rafael Correa Soares Nogueira**

- GitHub: https://github.com/RafaelCorrea160407
- LinkedIn: https://www.linkedin.com/in/rafaelcorreasoaresnogueira

---

⭐ Se este projeto foi útil para você, deixe uma estrela no repositório!
