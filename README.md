# 📂 Organizador de Arquivos

Projeto desenvolvido em **Python** com o objetivo de praticar lógica de programação, manipulação de arquivos e uso da biblioteca `pathlib`.

O programa organiza automaticamente os arquivos de uma pasta, separando-os em categorias de acordo com suas extensões e criando as pastas necessárias quando elas ainda não existem.

---

## ✨ Funcionalidades

- Organiza arquivos automaticamente por categoria.
- Cria as pastas de destino automaticamente.
- Move cada arquivo para sua respectiva pasta.
- Arquivos com extensões desconhecidas são enviados para a pasta **Outros**.
- Exibe mensagens informando cada arquivo organizado.
- Exibe um resumo da quantidade de arquivos organizados por categoria.

---

## 📁 Categorias suportadas

- 🖼️ Imagens
- 📄 Documentos
- 📕 PDFs
- 📊 Planilhas
- 🎵 Áudios
- 🎥 Vídeos
- 📦 Compactados
- 🐍 Python
- ☕ Java
- 📜 JavaScript
- 🔷 TypeScript
- 🌐 HTML
- 🎨 CSS
- ➕ C++
- ⚙️ C
- 💜 C#
- 🐘 PHP
- 🔧 JSON
- 🧩 XML
- 🗄️ SQL
- 📝 Markdown
- 💻 Executáveis
- 📂 Outros

---

## 🛠️ Tecnologias utilizadas

- Python 3
- pathlib

---

## ▶️ Como executar

1. Clone este repositório:

```bash
git clone https://github.com/seu-usuario/Organizador_Arquivos.git
```

2. Entre na pasta do projeto:

```bash
cd Organizador_Arquivos
```

3. Abra o arquivo `org.py`.

4. Altere o caminho da variável:

```python
pasta = Path("CAMINHO_DA_PASTA")
```

para a pasta que deseja organizar.

5. Execute o programa:

```bash
python org.py
```

---

## 📷 Exemplo de saída

```text
✔ Arquivo Organizado com Sucesso!
Arquivo: foto.png
Pasta: Imagens

✔ Arquivo Organizado com Sucesso!
Arquivo: currículo.pdf
Pasta: PDFs

✔ Arquivo Organizado com Sucesso!
Arquivo: música.mp3
Pasta: Áudios

Resumo por categoria:

Imagens: 3
PDFs: 2
Áudios: 1
Outros: 1
```

---

## 🎯 Objetivo do projeto

Este projeto foi desenvolvido para fortalecer meus conhecimentos em Python, praticando conceitos fundamentais como:

- Manipulação de arquivos
- Dicionários
- Estruturas condicionais
- Estruturas de repetição
- Contadores
- Organização de código
- Biblioteca `pathlib`

Além disso, este projeto faz parte do meu plano de estudos para me preparar para oportunidades de estágio em desenvolvimento Backend.

---

⭐ Este projeto faz parte da minha jornada de estudos em Python e Desenvolvimento Backend. Sugestões e feedbacks são sempre bem-vindos!
