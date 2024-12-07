# <p align="center"><text>[Compass PB Assistente](http://equipe2-sprint6.s3-website-us-east-1.amazonaws.com/)</text></p>
### <p align="center"><text> API de Conversão de Texto para Áudio </text></p>

<p align="center">
<!-- Create <img> tags using shield for amazon poly, s3, dynamoDB, lambda, api gateway python and terraform with their own icons-->

<img src="https://img.shields.io/badge/-AWS%20API%20Gateway-000?&logo=amazonapigateway" height="25">
<img src="https://img.shields.io/badge/-AWS%20DynamoDB-000?&logo=amazondynamodb&logoColor=4053D6" height="25">
<img src="https://img.shields.io/badge/-AWS%20Lambda-000?&logo=awslambda" height="25">
<img src="https://img.shields.io/badge/-AWS%20Polly-000?&logo=amazon-aws" height="25">
<img src="https://img.shields.io/badge/-AWS%20S3-000?&logo=amazons3" height="25">
<img src="https://img.shields.io/badge/-Python-000?&logo=python" height="25">
<img src="https://img.shields.io/badge/-Serverless-000?&logo=serverless" height="25">
<img src="https://img.shields.io/badge/-Terraform-000?&logo=terraform&logoColor=7B42BC" height="25">
</p>

## Descrição
Uma página html que captura uma frase qualquer inserida pelo usuário e transforma essa frase em um audio em mp3 via polly.

## Utilização

Ao acessar a [aplicação](http://equipe2-sprint6.s3-website-us-east-1.amazonaws.com/) você deve digitar uma frase para que nosso assistente possa gerar um aúdio dessa frase

![tela_inicial](https://github.com/JohnMarcelSilveira/consulta-api-github-v2/assets/29494433/23b4b32a-a27b-4f40-b6bc-8d7617ddb286)

Com a frase digitada você tem 3 botões:

V1: que aponta para a rota `https://bamhh6pajl.execute-api.us-east-1.amazonaws.com/v1/tts` que receberá um post no formato abaixo:

```json
  {
    "phrase": "converta esse texto para áudio"
  }
```

- Essa frase recebida é transformada em áudio via AWS Polly
- É armazenada em um S3 
- A resposta da chamada da API contém o endereço do audio gerado no S3

Resposta:

```json
  {
    "received_phrase": "converta esse texto para áudio",
    "url_to_audio": "https://meu-buckect/audio-xyz.mp3",
    "created_audio": "02-02-2023 17:00:00"
  }
```

V2: rota `https://bamhh6pajl.execute-api.us-east-1.amazonaws.com/v2/tts` que receberá um post no formato abaixo:

```json
  {
    "phrase": "converta esse texto para áudio e salve uma referencia no dynamoDB"
  }
```

- A frase recebida tem um id unico (um hash).
- Com essa frase recebida é transformada em áudio via AWS Polly
- É armazenada em um S3 
- É salva uma referencia no dynamoBD com as seguintes informações: id, frase e url do s3
- A resposta da chamada da API contém o endereço do audio gerado no S3

Resposta:

```json
  {
    "received_phrase": "converta esse texto para áudio",
    "url_to_audio": "https://meu-buckect/audio-xyz.mp3",
    "created_audio": "02-02-2023 17:00:00",
    "unique_id": "123456"
    
  }
```

V3: a rota `https://bamhh6pajl.execute-api.us-east-1.amazonaws.com/v3/tts` que receberá um post no formato abaixo:

```json
  {
    "phrase": "converta esse texto para áudio e salve uma referencia no dynamoDB. Caso a referencia já exista me devolva a URL com audio já gerado"
  }
```

- Com o hash verifica se a frase já foi gerada anteriormente.
- Caso o hash já exista no dynamo entregue o retorno conforme abaixo.
- Caso não exista faça a geração do audio, grava no s3 e grave as referencias no dynamo conforme Parte V2

Resposta:

```json
  {
    "received_phrase": "converta esse texto para áudio",
    "url_to_audio": "https://meu-buckect/audio-xyz.mp3",
    "created_audio": "02-02-2023 17:00:00",
    "unique_id": "123456"
  }
```


## Rodando o projeto localmente 

Passo a passo para iniciar o projeto:

1. Efetue o clone dessa Branch
```bash
git clone -b equipe-2 --single-branch https://github.com/Compass-pb-aws-2023-FURG-IFRS-UFFS/sprint-6-pb-aws-furg-ifrs-uffs.git && cd sprint-6-pb-aws-furg-ifrs-uffs
```

2. Instale o framework [serverless](https://www.serverless.com/framework/docs/getting-started) em seu computador e o [plugin para environment variables](https://github.com/neverendingqs/serverless-dotenv-example)
```bash
npm install -g serverless && npm i -D serverless-dotenv-plugin
```

3. Gere suas credenciais (AWS Acess Key e AWS Secret) na console AWS pelo IAM. Mais informações [aqui](https://www.serverless.com/framework/docs/providers/aws/guide/credentials/)

4. Gere os recursos de armazenamento utilizados por meio do terraform disponibilizado. Mais informações para [instalar o terraform](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli)

  * Dentro da pasta terraform mude as variáveis de ambiente no arquivo `terraform.tfvars` para os valores da sua conta AWS.

  * Execute os seguintes commandos em sequência:
```bash
terraform init
```
```bash
terraform plan -out=plan.out
```
```bash
terraform apply
```
```bash
terraform output -json env_variables_json | jq -r . > ../api-tts/.env
```

**Nota:** É importante que você formate o arquivo `.evn`, já que o output do terraform é em formato json. [Mais informações](https://www.freecodecamp.org/learn/back-end-development-and-apis/basic-node-and-express/use-the--env-file).
**Nota:** O serviço da Polly não está contido no terraform.

5. Em seguida insira as credenciais e execute o comando conforme exemplo:

```bash
serverless config credentials \
  --provider aws \
  --key AKIAIOSFODNN7EXAMPLE \
  --secret wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
```

Também é possivel configurar via [aws-cli](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) executando o comando:

```bash
$ aws configure
AWS Access Key ID [None]: AKIAIOSFODNN7EXAMPLE
AWS Secret Access Key [None]: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
Default region name [None]: us-east-1
Default output format [None]: ENTER
```

6. Para executar localmente uma função:

Rotas GET: 
```bash
serverless invoke local \
   --function functionName \
```

Rotas POST: 
```bash
serverless invoke local \
   --function functionName \
   --data '{"phrase": "{string}"}'
```

**Nota:** para fins de simplicidade, para que a experiência de teste local seja viável, é importante nos arquivos `tts.py` da rota que pretende testar e `awsutils.py` inverter a posição a linha com comentário "enable on local env", pela linha acima do comentário, alterando assim o valor da variavel `data`. 

## Deploy do projeto na AWS

1. Certificar-se de que estão criados os bancos de armazenamento conforme o passo 4 das instruções para execução local do projeto. 

2. Usar o comando deploy do serverless dentro da pasta que contém o arquivo `serverless.yml`
```bash
sls deploy
```

**Nota:** É importante configurar CORS no APIGateway caso seja de interesse. Mais informações: [Medium: Simple steps to enable CORS in API Gateway](https://medium.com/geekculture/simple-steps-to-enable-cors-in-api-gateway-through-console-cloud-formation-c09d9df31c07)

### Rota 1 → Get /

1. Esta rota já está presente no projeto
2. O retorno rota é:

```json
  {
    "message": "Go Serverless v3.0! Your function executed successfully!",
    "input": { 
        ...(event)
      }
  }
```

3. Status code para sucesso da requisição será `200`

### Rota 2 → Get /v1

1. Esta rota já está presente no projeto
2. O retorno rota é:

```json
  {
    "message": "TTS api version 1."
  }
 
```

3. Status code para sucesso da requisição será `200`

### Rota 3 → Get /v2

1. Esta rota já está presente no projeto
2. O retorno rota é:

```json
  {
    "message": "TTS api version 2."
  }
 
```

***

Após conseguir rodar o projeto base o objetivo final será divida em duas partes:

## Observações retorno

- status code para sucesso da requisição `200`
- status code para erros  `500`

***
## Estrutura do Projeto
```
|—— api-tts
|    |—— .env
|    |—— handler.py
|    |—— requirements.txt
|    |—— routes
|        |—— v1
|            |—— tts.py
|        |—— v2
|            |—— tts.py
|        |—— v3
|            |—— tts.py
|    |—— serverless.yml
|    |—— utils
|        |—— awsutils.py
|        |—— dynamodb.py
|        |—— polly.py
|        |—— s3.py
|        |—— utils.py
|—— public
|    |—— css
|        |—— styles.css
|    |—— img
|        |—— faviconV2.png
|        |—— magicwand.png
|    |—— index.html
|    |—— js
|        |—— index.js
|—— README.md
|—— terraform
|    |—— aws-bucket
|        |—— bucket.tf
|        |—— outputs.tf
|    |—— aws-lambda
|        |—— aws-lambda.tf
|        |—— main.tf
|        |—— tags.tf
|    |—— bucket.tf
|    |—— main.tf
|    |—— outputs.tf
|    |—— tags.tf
```


## Arquitetura AWS

<h1><p align="center"><img src="./public/img/arquitetura.svg"> </p></h1>

## Dificuldades Encontradas

Até o momento não houve dificuldades para realizar essa atividade

## Equipe

| [<img src="https://avatars.githubusercontent.com/u/54964022?v=4" width=85><br><sub>Fabiano Mendonça</sub>](https://github.com/FabianoMendonca) | [<img src="https://avatars.githubusercontent.com/u/29494433?v=4" width=85><br><sub>John Marcel Silveira</sub>](https://github.com/JohnMarcelSilveira) | [<img src="https://avatars.githubusercontent.com/u/57230577?v=4" width=85><br><sub>Luiz Paulo Grafetti</sub>](https://github.com/luizpgt) | [<img src="https://avatars.githubusercontent.com/u/12057302?v=4" width=85><br><sub>Matheus Henrique</sub>](https://github.com/matth3wss) |
| :--------------------------------------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------------------------------------: | ---------------------------------------------------------------------------------------------------------------------------------- |