# Avaliação da Sprint 2 - Equipe 1 - XKCD GIFter

## Integrantes da Equipe
- Luiz Paulo Grafetti Terres
- João Victor Winderfeld Bussolotto
- Luiz Augusto Scarsi
- Angemydelson Saint-Bert

## Descrição
Esta é uma aplicação web simples que permite o usuário visualizar uma tirinha do XKCD e também exibe três gifs relacionados ao título da tirinha.

## APIs Utilizadas [any-api.com]
- API [xkcd](https://any-api.com/xkcd_com/xkcd_com/docs/API_Description): Webcomic of romance, sarcasm, math, and language.
- API [giphy](https://any-api.com/giphy_com/giphy_com/docs/API_Description): GIPHY, the first and largest GIF search engine

## Tecnologias
```
├── HTML 5
├── Bootstrap
├── Javascript
└── Node.js
    ├── Axios
    ├── Express
    │   └── + Handlebars
    └── Path
```

## Arquitetura
```
.
├── models
│   ├── Comic.js
│   ├── Gif.js
│   └── MediaItem.js
├── views
│   ├── layouts
│   │   └── main.handlebars
│   └── index.handlebars
├── controllers
│   ├── giphyController.js
│   └── xkcdController.js
├── routes
│   └── xkcdPlusGiphy.js
├── index.js
├── config.js
├── package-lock.json
├── package.json
└── README.md

```
OBS: Em função da limitação de transações diária da chave giphy disponibilizada para ambiente de desenvolvimento, a chave não está publicamente junto ao código. Para obter acesso ao conteúdo do giphy e a uma experiência completa da aplicação, o arquivo ``` config.js ``` deve ser requisitado à equipe de desenvolvimento, ou uma nova chave deve ser adquirida pelo usuário. 

Estrutura do arquivo ```config.js```:
```
const giphyApiKey = 'api-key';

module.exports = {
  giphyApiKey
};
```
Para mais informações: https://developers.giphy.com/docs/sdk/#web.

## Como testar esta aplicação na sua máquina:
### Pré-requisitos
- Navegador web atualizado.
- Conexão com a internet.
- [Git](https://git-scm.com/downloads): ferramenta para gerenciamento de configuração.
- [Npm](https://www.npmjs.com/): gerenciador de pacotes.


Clone esta branch do repositório:
```bash
git clone -b equipe-1 --single-branch https://github.com/Compass-pb-aws-2023-FURG-IFRS-UFFS/sprint-2-pb-aws-furg-ifrs-uffs && cd sprint-2-pb-aws-furg-ifrs-uffs
```
Instale as dependências da aplicação: 
```
npm install
```
Execute o script para rodar a aplicação com [Nodemon](https://www.npmjs.com/package/nodemon)
```
npm run dev
```
Agora basta acessar a porta ```3000``` do seu localhost no navegador:
```
localhost:3000
```

## Dificuldades encontradas
- Distribuição das atividades de forma equivalente e dinâmica
- Manter o código limpo e organizado durante o trabalho em equipe
- Organizar e utilizar branches eficientemente
