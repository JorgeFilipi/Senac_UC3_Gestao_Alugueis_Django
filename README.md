# SENAC UC3 - Sistema de Gestão de Aluguéis (Django)

## 📖 Sobre o Projeto

Este projeto foi desenvolvido como parte da Unidade Curricular 3 (UC3) do curso [Nome do Curso] no SENAC [Localidade do SENAC, se aplicável]. O objetivo é um sistema de gestão de aluguéis construído com o framework Django, permitindo [Descreva aqui as principais funcionalidades, por exemplo: cadastrar imóveis para aluguel, gerenciar inquilinos, registrar contratos de aluguel, controlar pagamentos, etc.].

## ✨ Funcionalidades Principais

* **Cadastro de Imóveis:** Permite registrar imóveis disponíveis para aluguel com detalhes (endereço, tipo, valor do aluguel, número de quartos, etc.).
* **Gerenciamento de Inquilinos:** Funcionalidades para cadastrar informações de inquilinos.
* **Gestão de Contratos:** Criação e acompanhamento de contratos de aluguel, vinculando imóveis e inquilinos.
* **Controle de Pagamentos:** Registro e acompanhamento de pagamentos de aluguel.


## 🛠️ Tecnologias Utilizadas

* **Linguagem de Programação:** Python ([Versão, ex: 3.8+])
* **Framework Backend:** Django ([Versão, ex: 3.2+])
* **Framework Frontend:** [Ex: Templates Django (HTML, CSS, JavaScript), ou algum framework JS como React/Vue se integrado]
* **Banco de Dados:** [Ex: SQLite (padrão Django para desenvolvimento), PostgreSQL, MySQL]
* **Gerenciamento de Dependências:** Pip com `requirements.txt`
* **Outras Ferramentas/Bibliotecas:** [Ex: Django REST framework (para APIs), Celery (para tarefas assíncronas), Git]

## ⚙️ Pré-requisitos

Antes de executar o projeto, certifique-se de ter instalado:

* [Python X.X ou superior](https://www.python.org/downloads/) (verifique a versão usada no projeto)
* [Git](https://git-scm.com/downloads)
* (Opcional, mas recomendado) Um ambiente virtual Python (ex: `venv` ou `conda`)

## 🚀 Instalação e Execução

Siga os passos abaixo para configurar e executar o projeto localmente:

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/JorgeFilipi/Senac_UC3_Gestao_Alugueis_Django.git](https://github.com/JorgeFilipi/Senac_UC3_Gestao_Alugueis_Django.git)
    cd Senac_UC3_Gestao_Alugueis_Django
    ```

2.  **Crie e Ative um Ambiente Virtual (Recomendado):**
    ```bash
    python -m venv venv
    # No Windows:
    venv\Scripts\activate
    # No macOS/Linux:
    source venv/bin/activate
    ```

3.  **Instale as Dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure as Variáveis de Ambiente (se houver):**
    * Verifique se há um arquivo `.env.example` ou instruções no código sobre variáveis de ambiente necessárias (ex: `SECRET_KEY`, configurações de banco de dados se não for SQLite).
    * Se necessário, crie um arquivo `.env` e adicione as configurações.

5.  **Aplique as Migrações do Banco de Dados:**
    ```bash
    python manage.py migrate
    ```

6.  **Crie um Superusuário (para acessar o Admin do Django):**
    ```bash
    python manage.py createsuperuser
    ```
    (Siga as instruções no terminal para definir nome de usuário, email e senha)

7.  **Execute o Servidor de Desenvolvimento:**
    ```bash
    python manage.py runserver
    ```

8.  Acesse a aplicação em: `http://localhost:8000`
    * Acesse o painel de administração do Django em: `http://localhost:8000/admin` (usando as credenciais do superusuário criado).

## 📋 Estrutura do Projeto (Simplificada)
```bash
gestao_de_alugueis/
│
├ manage.py                  # Interface de linha de comando (CLI)
├── gestao_de_alugueis/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── imoveis/
│   ├── migrations/
│   │   └── __init__.py
│   ├── static/imoveis/css/
│   │   └── style.css
|   ├── templates/imoveis/
│   │   |── base.html
│   │   |── editar_imovel.html
│   │   |── excluir_imovel.html
│   │   |── index.html
│   │   |── list_imoveis.html
│   │   |── list_inquilinos.html
│   │   └── login.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py/


```

## 📄 Licença

Este projeto é distribuído sob a licença [Nome da Licença, ex: MIT]. Veja o arquivo `LICENSE` para mais detalhes (se você adicionar um).

### 📞 Conecte-se Comigo

<p align="left">
  <a href="https://linkedin.com/in/jfdias" target="_blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="jfdias" height="30" width="40" /></a>
  <a href="mailto:jorgefelipe1986@gmail.com" target="_blank"><img align="center" src="https://img.icons8.com/color/48/000000/gmail-new.png" alt="jorgefelipe1986@gmail.com" height="30" width="40" /></a>
  <a href="https://discord.gg/jorgefelipe1986" target="_blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/discord.svg" alt="jorgefelipe1986" height="30" width="40" /></a>
  </p>
