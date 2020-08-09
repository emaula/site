# Instalação no Python Anywhere (modo desenvolvimento)

## Criar uma conta no Python Anywhere

1. Plano básico no [Python Anywhere](https://www.pythonanywhere.com/) é gratuito, e mantém app rodando por três meses para testar. Crie uma conta lá, em "Pricing & signup" / "Create a Beginner account".

2. Valide seu e-mail.

## Abrir novo console e instalar o EmAula

1. Em "Consoles\", "Start a new console" com Bash.

2. Crie um ambiente virtual com o seguinte comando:

```
$ mkvirtualenv myvenv --python=/usr/bin/python3.6
```

3. Clone o projeto do GitHub, conforme o "Guia para desenvolvimento".

```
$ git clone https://github.com/emaula/site.git

```

4. Entre na pasta do projeto.
```
(myvenv)$ cd site
```

5. Instale as dependências.

```
(myvenv)$ pip install -r requirements/dev.txt
```

6. Entre na pasta do manage.py

```
$ cd emaula
```

7. Crie um banco de dados e um superusuário
Entre na pasta onde está o arquivo manage.py (site/emaula).
```
(myvenv)$ python manage.py migrate
(myvenv)$ python manage.py createsuperuser
```

10. Crie uma web app com configuração manual

Na tab "Web", selecione "Add a new web app". Selecione "next" para não usar domínio personalizado (o que tem custo) e, então, "Manual configuration". Versão do Python, selecione "Python 3.6". Clique em "next".

11. Configurações de caminhos:

- Volte para a aba "Web". Nas configurações, defina o caminho da virtualenv, em "Virtualenv", coloque:

```
/home/USERNAME/.virtualenvs/myvenv
```

- Configure os diretórios do código.

```
Source code:

/home/USERNAME/site/emaula


Working directory:

/home/USERNAME/site/emaula
```


12. Edite seu arquivo WSGI.

Na tab "Web", busque o link para seu arquivo WSGI, vai ser algo como '/var/www/USERNAME_pythonanywhere_com_wsgi.py'. Coloque as configurações abaixo:

```
import os
import sys

# Supondo que as configurações do Django estão como no repositório, o que se
# traduz para '/home/USERNAME/site/emaula/website'
path = os.path.expanduser('~/site/emaula/website')

if path not in sys.path:
    sys.path.insert(0, path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'website.settings'

from django.core.wsgi import get_wsgi_application
from django.contrib.staticfiles.handlers import StaticFilesHandler
application = StaticFilesHandler(get_wsgi_application())
```

13. Usando 'browse files', navegue até '/home/USERNAME/site/emaula/website' e edite settings.py. Adicione o seu endereço no Python Anywhere à configuração de "ALLOWED_HOSTS", no arquivo, por exemplo:

```
ALLOWED_HOSTS = ['emaulaxyz.pythonanywhere.com']
```

14. É necessário reiniciar a app para que as configurações tenham efeito, então clique no botão verde "Reload USERNAME.pythonanywhere.com".

PRONTO! Agora você já pode visitar o seu site e ver o EmAula funcionando!

Guia original (em inglês):
https://help.pythonanywhere.com/pages/DeployExistingDjangoProject
