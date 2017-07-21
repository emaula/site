# GUIA PARA DESENVOLVIMENTO

Para fazer download do projeto, navegue até o diretório onde quer colocá-lo e clone o projeto (assume que você tem Git instalado):
```
$ git clone https://github.com/emaula/site.git
```

Para fazer download de um branch específico do projeto:
```
$ git clone -b NOME_DO_BRANCH https://github.com/emaula/site.git
```

## Instalando e rodando

### Criar virtualenv na pasta
Entre na pasta do repositório e crie um ambiente virtual (virtualenv). Se você não sabe como criar uma virtualenv, é altamente recomendado que leia o [tutorial DjangoGirls](http://tutorial.djangogirls.org/pt/django_installation/). Ative a virtualenv.
 
Linux/BSD
```
$ python3 -m venv myvenv
```

Windows
```
C:\DIRETORIO_COM_PYTHON\python -m venv myvenv
```

Ubuntu
```
$ sudo apt-get install python-virtualenv
$ virtualenv --python=python3.4 myvenv
```

### Se / quando virtual env já estiver criada, ativar:
```
$ source myvenv/bin/activate
```
OU
```
C:\USUARIO\PASTA\projeto> myvenv\Scripts\activate
```

NOTA: virtual env *ativa* aparece como (myvenv) no começo da linha de comando.


### Atualize o pip (gerenciador de pacotes Python)
```
(myvenv)$ pip install --upgrade pip
```

### Python-dev
Antes de instalar as dependências do projeto, pode ser necessário instalar o pacote Python-dev para lidar com o Pillow:
```
(myvenv)$ sudo apt-get install python3-dev python3-setuptools
```


### Instalar as dependências requeridas (Django) via pip:
```
(myvenv)$ pip install -r requirements.txt
```

### Crie um banco de dados e um superusuário
Entre na pasta onde está o arquivo manage.py (site/emaula).
```
(myvenv)$ python manage.py migrate --settings=website.settings.dev
(myvenv)$ python manage.py createsuperuser --settings=website.settings.dev
```

Esse superusuário que você vai usar para logar localmente na interface administrativa.

Atenção: se você estiver usando um MacOS X para desenvolver, você provavelmente precisará exportar algumas variáveis locale do Python. Siga esse link: [Fix unknown locale](http://patrick.arminio.info/fix-valueerror-unknown-locale-utf8/)

### Inicialize o servidor com as configurações de desenvolvimento:
```
(myvenv)$ python manage.py runserver --settings=website.settings.dev
```
Abra seu navegador em localhost:8000

OU: abra seu navegador em localhost:8000/APP_QUE_VOCÊ_QUER

Ex:

Para vermos a administração:
```
localhost:8000/admin
```

Para vermos a app da escola:
```
localhost:8000/school
```

Para vermos a app de aulas:
```
localhost:8000/lessons
```


### Para commitar as mudanças que você fez:

Crie um novo branch para a funcionalidade desenvolvida:
```
$ git checkout -b NOME_DO_NOVO_BRANCH
```

Adicione os arquivos alterados. Por exemplo:
```
$ git add --all .
```

Faça o commit com a mensagem:
```
$ git commit -m "altera tal e tal coisa"

```

Envie para o repositório original, criando branch novo lá:
```
$ git push origin NOME_DO_NOVO_BRANCH
```


Estrutura das pastas:
```
.
├── README.md                           # Esse arquivo que você está lendo
├── emaula
│   ├── lessons                         # Aplicação das aulas
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── migrations                  # Banco de dados aula
│   │   ├── models.py
│   │   ├── tests.py                    # Testes da app
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
│   │   ├── tests.py                    # Testes da app
│   │   ├── urls.py                     # Redirecionamentos páginas internas da app
│   │   └── views.py                    # Processa request/response
│   ├── templates                       # Templates da interface de admin
│   │   └── admin
│   │       ├── base_site.html
│   │       └── index.html
│   └── website                         # Configurações do site
│       ├── __init__.py
│       ├── index.html
│       ├── media
│       │   └── python.png
│       ├── settings
│       │   ├── __init__.py
│       │   ├── base.py                 # Configuração base para as outras
│       │   ├── dev.py                  # Configuração para ambiente local
│       │   ├── production.py
│       │   ├── secrets.json
│       │   └── settings.py
│       ├── urls.py                     # Redirecionamentos do projeto
│       └── wsgi.py                     # Chamável para o servidor
└── requirements.txt                    # Dependências do projeto
```
