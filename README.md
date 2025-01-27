# Guia para Configurar e Executar um Projeto Django

Este guia descreve as etapas para configurar e executar um projeto Django em sistemas Windows e Linux (Arch).

---

## Pré-requisitos

1. **Python**
   - Versão recomendada: 3.10 ou superior
2. **Git**
   - Para clonar o repositório do projeto
3. **Visual Studio Code (VS Code)**
   - Para edição e depuração de código
4. **Virtualenv**
   - Para isolar o ambiente Python

---

## Passos no Windows

### 1. Baixar e Instalar Dependências

#### Python
1. Acesse o site oficial do Python: https://www.python.org/downloads/
2. Baixe o instalador para Windows.
3. Durante a instalação, habilite a opção **"Add Python to PATH"**.

#### Git
1. Acesse o site oficial do Git: https://git-scm.com/
2. Baixe e instale o Git.

#### VS Code
1. Baixe o Visual Studio Code em: https://code.visualstudio.com/
2. Instale o software normalmente.

#### Virtualenv
Abra o terminal do Windows (cmd ou PowerShell) e instale o virtualenv:
```bash
pip install virtualenv
```

---

### 2. Configurar o Ambiente

#### Clonar o Repositório
1. Abra o terminal.
2. Clone o repositório do projeto:
   ```bash
   git clone https://github.com/JVM3L0/PIAF
   ```
3. Navegue até o diretório do projeto:
   ```bash
   cd PIAF
   ```

#### Criar e Ativar o Ambiente Virtual
1. Crie o ambiente virtual:
   ```bash
   virtualenv venv
   ```
2. Ative o ambiente virtual:
   ```bash
   venv\Scripts\activate
   ```

#### Instalar Dependências do Projeto
1. Instale as dependências listadas no arquivo `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

---

### 3. Executar o Projeto

1. Realize as migrações do banco de dados:
   ```bash
   python manage.py migrate
   ```
2. Inicie o servidor de desenvolvimento:
   ```bash
   python manage.py runserver
   ```
3. Acesse o projeto no navegador em: http://127.0.0.1:8000/

---

## Passos no Linux (Arch)

### 1. Instalar Dependências

#### Python
1. Abra o terminal e instale o Python:
   ```bash
   sudo pacman -S python
   ```

#### Git
1. Instale o Git:
   ```bash
   sudo pacman -S git
   ```

#### VS Code
1. Instale o VS Code via AUR ou repositório oficial:
   ```bash
   sudo pacman -S code
   ```

#### Virtualenv
1. Instale o virtualenv usando `pip`:
   ```bash
   pip install virtualenv
   ```

---

### 2. Configurar o Ambiente

#### Clonar o Repositório
1. Clone o repositório do projeto:
   ```bash
   git clone https://github.com/JVM3L0/PIAF
   ```
2. Navegue até o diretório do projeto:
   ```bash
   cd PIAF
   ```

#### Criar e Ativar o Ambiente Virtual
1. Crie o ambiente virtual:
   ```bash
   virtualenv venv
   ```
2. Ative o ambiente virtual:
   ```bash
   source venv/bin/activate
   ```

#### Instalar Dependências do Projeto
1. Instale as dependências listadas no arquivo `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

---

### 3. Executar o Projeto

1. Realize as migrações do banco de dados:
   ```bash
   python manage.py migrate
   ```
2. Inicie o servidor de desenvolvimento:
   ```bash
   python manage.py runserver
   ```
3. Acesse o projeto no navegador em: http://127.0.0.1:8000/

---

## Sugestões de Extensões para VS Code

1. **Python** (Microsoft): Suporte completo para desenvolvimento em Python.
2. **Django**: Extensão para facilitar o desenvolvimento com Django.
3. **GitLens**: Ferramenta para integrar Git no VS Code.

