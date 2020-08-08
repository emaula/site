### Para commitar as mudanças que você fez:

Forke esse repositório para o seu Github e faça as alterações.

Crie um novo branch para a funcionalidade desenvolvida:
```
$ git checkout -b NOME_DO_NOVO_BRANCH
```

Adicione os arquivos alterados. Por exemplo:
```
$ git add --all .
```

Faça o commit descrevendo na mensagem o que foi alterado:
```
$ git commit -m "altera tal e tal coisa"

```

Envie para o repositório de origem, criando branch nova lá:
```
$ git push --set-upstream origin NOME_DO_NOVO_BRANCH
```

Abra um Pull-Request para esse repositório.
