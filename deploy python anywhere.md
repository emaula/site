# Implantação no Python Anywhere

## Criar uma conta no Python Anywhere

1. Plano básico no [Python Anywhere](https://www.pythonanywhere.com/) é gratuito, e mantém app rodando por três meses para testar. Crie uma conta lá, em "Pricing & signup" / "Create a Beginner account".

2. Validar seu e-mail.

## Abrir novo console e instalar o EmAula

1. Em "Consoles", "Start a new console" com Bash.

2. Clone o projeto do GitHub, conforme o "Guia para desenvolvimento".

3. Crie um ambiente virtual com o seguinte comando:

```
$ mkvirtualenv --python=/usr/bin/python3.6 myvenv
```

4. Entre na pasta do projeto.
```
(myvenv)$ cd site
```

5. Instale as dependências.

```
(myvenv)$ pip install -r requirements.txt
```

6. Entre na pasta do manage.py

```
$ cd emaula
```

7. Compile os arquivos estáticos (imagens, folhas de estilo, etc):

```
$ python manage.py collectstatic --settings=website.settings.base
```

8. Configure o banco de dados:

```
python manage.py migrate --settings=website.settings.base
```

9. Crie um superusuário que administrará o site:

```
python manage.py createsuperuser --settings=website.settings.base
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
path = '/home/emaulaxyz/site/emaula/website'

if path not in sys.path:
    sys.path.insert(0, path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'website.settings.base'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

13. Adicione o seu endereço no Python Anywhere à configuração de "ALLOWED_HOSTS", no arquivo "site/emaula/website/settings/base.py", por exemplo:

```
ALLOWED_HOSTS = ['emaulaxyz.pythonanywhere.com']
```

14. É necessário reiniciar a app para que as configurações tenham efeito, então clique no botão verde "Reload USERNAME.pythonanywhere.com".

PRONTO! Agora você já pode visitar o seu site e ver o EmAula funcionando!

Guia original (em inglês):
https://help.pythonanywhere.com/pages/DeployExistingDjangoProject
