# EmAula

[![Actions Status](https://github.com/emaula/site/workflows/Em%20Aula%20CI/badge.svg)](https://github.com/emaula/site/actions)

**[en]**

A free software Django web application made for teachers to create and virtually share content with their students.

**Contributing with the project**

See [CONTRIBUTING.md](/CONTRIBUTING.md).

---

**[pt-br]**

Uma aplicação web feita em software livre para professoras e professores criarem e compartilharem virtualmente conteúdos de suas aulas.

**Contribuindo com o projeto**

Veja [CONTRIBUTING.md](/CONTRIBUTING_pt-br.md).

---

## Guia para Desenvolvimento
<!-- MDTOC maxdepth:2 firsth1:0 numbering:0 flatten:0 bullets:1 updateOnSave:1 -->

- [Guia para Desenvolvimento](#guia-para-desenvolvimento)   
- [Instalando e rodando](#instalando-e-rodando)   
   - [Localmente, sem Docker](#localmente-sem-docker)   
   - [Remoto, no PythonAnywhere:](#remoto-no-pythonanywhere)   
   - [Remoto, no CodeAnywhere:](#remoto-no-codeanywhere)   
   - [Docker](#docker)   
- [Testes](#testes)   
   - [Testes funcionais](#testes-funcionais)   
   - [Testes das apps](#testes-das-apps)   
- [Estrutura das pastas:](#estrutura-das-pastas)   

<!-- /MDTOC -->
Para baixar o projeto, navegue até o diretório onde quer colocá-lo e clone o projeto (assumindo que você tem [Git instalado](https://docs.github.com/pt/github/getting-started-with-github/set-up-git)):

```sh
$ git clone https://github.com/emaula/site.git
```

Para baixar um branch específico do projeto:

```sh
$ git clone -b NOME_DO_BRANCH https://github.com/emaula/site.git
```

---

## Instalando e rodando

### Localmente, sem Docker

#### Criar virtualenv na pasta

Entre na pasta do repositório e crie um ambiente virtual (virtualenv). Se você não sabe como criar uma virtualenv, é altamente recomendado que leia o [tutorial DjangoGirls](http://tutorial.djangogirls.org/pt/django_installation/). Ative a virtualenv.

Linux/BSD

```sh
$ python3 -m venv myvenv
```

Windows

```bat
C:\DIRETORIO_COM_PYTHON\python -m venv myvenv
```

Ubuntu

```sh
$ sudo apt-get install python-virtualenv
$ virtualenv --python=python3.6 myvenv
```

#### Se / quando virtual env já estiver criada, ativar:

```sh
$ source myvenv/bin/activate
```

OU

```bat
C:\USUARIO\PASTA\projeto> myvenv\Scripts\activate
```

NOTA: virtual env *ativa* aparece como (myvenv) no começo da linha de comando.

---

#### Atualize o pip (gerenciador de pacotes Python)

Presumindo que o [pip](https://pip.pypa.io/) já está instalado.

##### Instalando pip (se não estiver instalado)

###### Linux

```sh
$ python3 -m ensurepip
```

###### Windows

```bat
C:\Python -m ensurepip
```

###### Debian (ou distribuições Linux sem ensurepip)

```sh
$ sudo apt install python3-{pip,setuptools,wheel}
$ sudo python3 -m pip install --upgrade pip
```

##### Somente atualizar

Se pip já estiver instalado e o virtualenv já configurado:

```sh
(myvenv)$ pip install --upgrade pip
```

OU

```bat
C:\pip install --upgrade pip
```

---

#### Python-dev

Antes de instalar as dependências do projeto, pode ser necessário instalar o pacote Python-dev para lidar com o Pillow:

```sh
$ sudo apt-get install python3-{dev,setuptools}
```

---

#### Instalar as dependências requeridas (Django) para desenvolvimento, via pip requirements:

```sh
(myvenv)$ pip install -r requirements/dev.txt
```

##### Pipenv

Somente necessário se [pipenv](https://pipenv.pypa.io/) estiver sendo usado

```sh
(myenv)$ pipenv install
```

---

#### Configuração das variáveis de ambiente

Crie arquivo .env no diretório raiz do projeto (emaula/site/emaula/.env) com as seguintes variáveis:

```
SECRET_KEY=COLOQUE_ALGO_AQUI
DEBUG=True
```

---

#### Crie um banco de dados e um superusuário

Entre na pasta onde está o arquivo manage.py (site/emaula).

```sh
(myvenv)$ python manage.py migrate
(myvenv)$ python manage.py createsuperuser
```

Esse superusuário que você vai usar para entrar localmente na interface administrativa.

Atenção: se você estiver usando um MacOS X para desenvolver, você provavelmente precisará exportar algumas variáveis locale do Python. Siga esse link: [Fix unknown locale](http://patrick.arminio.info/fix-valueerror-unknown-locale-utf8/)

---

####  Inicialize o servidor com as configurações base:

```sh
(myvenv)$ python manage.py runserver
```

Abra seu navegador em <http://localhost:8000> (mude "8000" para a porta alternativa caso tenha usado outra)

![Página inicial do site](/imagens/home.png)

OU: abra seu navegador em **localhost:8000/APP_QUE_VOCÊ_QUER**

Ex:

Para vermos a administração:

> <http://localhost:8000/admin>

Para vermos a app da escola:

> <http://localhost:8000/school>

Para vermos a app de aulas:

> <http://localhost:8000/lessons>

**(fim da instruções para instalação local)**

---

### Remoto, no PythonAnywhere:

[Instruções para o PythonAnywhere](/deploy%20python%20anywhere.md)

---

### Remoto, no CodeAnywhere:

Faça os procedimentos descritos acima, clonando o repositório, criando virtualenv, criando banco de dados e superusuário.

Edite o arquivo `site/emaula/website/settings.py` para colocar o endereço do seu container em **ALLOWED_HOSTS**, por exemplo:

```py
ALLOWED_HOSTS = ['emaula-rsip22207208.codeanyapp.com']
```

Inicialize o servidor com as configurações de desenvolvimento e com a porta 3000, para poder acessar a app por HTTPS:

```sh
$ python3 manage.py runserver 0.0.0.0:3000 --settings=website.settings
```

---

### Docker

Dentro do diretório em que está o docker-compose.yml:

Criar a imagem.

```sh
$ docker build -t emaula:latest .
```

Se estiver utilizando um servidor, é necessário editar o arquivo `site/emaula/website/settings.py` para colocar o endereço do servidor em **ALLOWED_HOSTS**, por exemplo:

```py
ALLOWED_HOSTS = ['192.168.0.1']
```

Se quiser apenas rodar o container, mapeando a porta **3000** (container) para porta **8001** (do host) é necessário definir ao menos duas variáveis de ambiente: **DEBUG** e **SECRET_KEY**.

```sh
$ docker build -t emaula:latest . && docker run -e DEBUG=True -e SECRET_KEY="MUDE_AQUI" -it --rm -p 8001:3000 --name emaula1 emaula:latest bash
```

Para inicializar o servidor com as configurações de desenvolvimento e com a porta 3000:

```sh
$ python3 manage.py runserver 0.0.0.0:3000 --settings=website.settings
```

Inicializar os containers:

```sh
$ docker-compose up -d --build
```

Parar os containers:

```sh
$ docker-compose down
```

---

## Testes

### Testes funcionais
Você vai precisar ter o Geckodriver instalado e disponível no PATH para utilizar o Selenium.

- Baixe o geckodriver:
[https://github.com/mozilla/geckodriver/releases](https://github.com/mozilla/geckodriver/releases)

- OU com wget:

```sh
$ wget -cv https://github.com/mozilla/geckodriver/releases/download/v0.27.0/geckodriver-v0.27.0-linux64.tar.gz
```

- Extraia, mova para o diretório bin e coloque no PATH:

```sh
$ tar -xvzf geckodriver-v0.27.0-linux64.tar.gz
$ sudo cp -r geckodriver /usr/local/bin
$ sudo chmod a+x /usr/local/bin/geckodriver
$ export PATH=$PATH:/usr/local/bin/geckodriver
```

Rodar os testes funcionais:

```sh
(myvenv)$ python manage.py test functional_tests
```

### Testes das apps

Rodar os testes:

```sh
(myvenv)$ python manage.py test school
(myvenv)$ python manage.py test lessons
```

---

## Estrutura das pastas:

```
.
├── README.md                           # Esse arquivo que você está lendo
├── emaula
│   ├── functional_tests                
│   │   ├── __init__.py
│   │   └── tests.py                    # Testes funcionais (teste de aceitação)
│   ├── lessons                         # Aplicação das aulas
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── migrations                  # Banco de dados aula
│   │   ├── models.py
│   │   ├── tests.py                    # Testes da app lessons
│   │   ├── urls.py                     # Redirecionamentos páginas internas da app
│   │   └── views.py                    # Processa request/response
│   ├── manage.py                       # Arquivo importante que roda tudo
│   ├── school                          # Aplicação da escola
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── migrations                  # Banco de dados escola
│   │   ├── models.py
│   │   ├── static                      # Arquivos estáticos: css, js e img
│   │   │   ├── css                     # Arquivos de estilo da app
│   │   │   │   ├── bootstrap.min.css
│   │   │   │   ├── carousel.css
│   │   │   │   └── styles.css
│   │   │   ├── images                  # Imagens da app
│   │   │   │   └── picjumbo5096.jpg
│   │   │   └── js                      # Javascripts pra app funcionar
│   │   │       ├── bootstrap.min.js
│   │   │       └── jquery.js
│   │   ├── templates                   # Templates da app
│   │   │   ├── registration
│   │   │   │   ├── login.html
│   │   │   │   └── register.html
│   │   │   └── school
│   │   │       ├── about.html
│   │   │       ├── base.html               # Base todos templates
│   │   │       ├── classroom_detail.html   # Detalhe aula
│   │   │       ├── classroom_list.html     # Lista de aulas
│   │   │       ├── colaborate.html         # Colabore com o site
│   │   │       ├── index.html              # Página inicial do site
│   │   │       ├── professor_detail.html   # Detalhe do professor
│   │   │       ├── professor_list.html     # Lista de prof
│   │   │       ├── sitestatus.html         # Status do site
│   │   │       └── team.html               # Equipe
│   │   │       └── tos.html                # Termos de uso
│   │   ├── tests.py                    # Testes da app school
│   │   ├── urls.py                     # Redirecionamentos páginas internas da app
│   │   └── views.py                    # Processa request/response
│   ├── templates                       # Templates da interface de admin
│   │   └── admin
│   │       ├── base_site.html
│   │       └── index.html
│   └── website                         # Configurações do site
│       ├── __init__.py
│       ├── index.html
│       ├── settings.py                 # Configuração do projeto
│       ├── urls.py                     # Redirecionamentos do projeto
│       └── wsgi.py                     # Chamável para o servidor
├── nginx                               # Configurações para servidor
│   ├── Dockerfile                      # Configuração Docker para NGINX
│   └── emaula.conf                     # Configuração do servidor Django
├── docker-compose.yaml                 # Configuração containers aplicação
├── Dockerfile                          # Configuração Docker para Django
├── entrypoint.sh                       # Inicialização da app no servidor
└── requirements.txt                    # Dependências do projeto
```
