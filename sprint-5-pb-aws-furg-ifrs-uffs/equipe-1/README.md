
<h1  align="center"> Hotel Reservations Price Prediction </h1>

 O objetivo deste projeto: criar uma API com uma rota para realizar inferências usando um modelo treinado no Amazon SageMaker.
 
 O seguinte [dataset](https://www.kaggle.com/datasets/ahsan81/hotel-reservations-classification-dataset) foi utilizado para fazer o treino do modelo no SageMaker.

Para fazer consultas,usa-se uma requisição POST no seguinte link:

http://hotel-reservations-price-ml-model-prediction.us-east-1.elasticbeanstalk.com/api/v1/predict

Ao entrar a lista de valores obrigatório de entrada, contendo informações sobre uma reserva de quarto de hotel, a API retorna a previsão contendo a classificação (faixa de preço) da reserva.
| Classe |  Faixa de preço! |
|:--------:|:-----------:|
| 1 | preço <= 85 | 
| 2 | 85 < preço < 115 |
| 3 | preço >= 115 |

***

<h2  align="center"> Tecnologias Utilizadas </h2>

***

<p  align="center">


<img  height="45"  src="https://github.com/devicons/devicon/blob/master/icons/python/python-original.svg" alt='Python'>

<img  height="45"  src="https://github.com/devicons/devicon/blob/master/icons/fastapi/fastapi-original-wordmark.svg" alt='FastApi'>

<img  height="45"  src="https://github.com/devicons/devicon/blob/master/icons/amazonwebservices/amazonwebservices-plain-wordmark.svg" alt='AWS'>

<img  height="45"  src="https://github.com/devicons/devicon/blob/master/icons/docker/docker-original.svg" alt='Docker'>

<img  height="45"  src="https://github.com/devicons/devicon/blob/master/icons/github/github-original.svg" alt='GitHub'>

<img  height="45"  src="https://github.com/devicons/devicon/blob/master/icons/trello/trello-plain-wordmark.svg" alt='Trello'>

</p>

  
* Python - Para o desenvolvimento da API.

* FastApi - Para expor o endpoint para inferência.

* AWS - Para o treinamento no modelo no SageMaker, e armazenamento com S3 e Elastic BeansTalk.

* Docker - Para a criação do ambiente no AWS Elastic Beanstalk.

* GitHub - Para auxiliar no controle de versão e envio do projeto.

* Trello - Para divisão e acompanhamento das tarefas.
  

***

<h2  align="center"> Funcionamento </h2>
  
***

### Rota → Get /

1. Nesta rota será efetuado um get na raiz do projeto.

2. O retorno desta API deverá ter um texto simples.

3. Status code para sucesso da requisição será `200`

<p><img  width= 100%  height=auto  src="https://i.imgur.com/thrUHar.png"></p>

  

***

### Rota → POST /api/v1/predict

1. Nesta rota será efetuado um POST, sendo necessário passar as informações no body da requisição. Um exemplo de entrada é: 
```json
{
    "no_of_adults": 2,
    "no_of_children": 0,
    "no_of_weekend_nights": 1,
    "no_of_week_nights": 2,
    "required_car_parking_space": 0,
    "lead_time": 224,
    "arrival_year": 2017,
    "arrival_month": 10,
    "arrival_date": 2,
    "repeated_guest": 0,
    "no_of_special_requests": 0,
    "no_of_previous_cancellations": 0,
    "no_of_previous_bookings_not_canceled": 0,
    "type_of_meal_plan": "Meal Plan 1",
    "room_type_reserved": "Room_Type 1",
    "market_segment_type": "Offline"
}
```
2. O retorno da API  deverá  ser no seguinte formato:

```json

{
"result":  1
}
```

***

### Rota → Get /docs

1. Essa rota mostra a documentação da API utilizando Swagger

<p><img  width= 100%  height=auto  src="https://i.imgur.com/NgMGUxY.png"></p>

***

<h2  align="center"> Estrutura de pastas </h2>

***

*  ```api```
	*  ```api/v1```
		*  ```endpoints```
			* ```predict.py```
		* ```api.py```
	*  ```core```
		* ```config.py```
	*  ```schemas```
		* ```Booking.py```
		* ```Prediction.py```
	*  ```services```
		* ```prediction_service.py```
		* ```booking_formatter.py```
	* ```.env```
	* ```Dockerfile```
	* ```Dockerrun.aws-example.json```
	* ```main.py``` 
	* ```requirements.txt```
*  ```notebook```
	*  ```datasets```
		* ```xgboost```
			* ```hotelrooms_test_xgboost.csv```
			* ```hotelrooms_train_xgboost.csv```
		* ```Hotel Reservations.csv```
	* ```xgboost-model.ipynb``` 



  

***

<h2  align="center"> AWS </h2>

  

***

  

### Arquitetura na AWS

  
![sprint-5-draw-io](https://github.com/Compass-pb-aws-2023-FURG-IFRS-UFFS/sprint-5-pb-aws-furg-ifrs-uffs/assets/57230577/4a4d94c9-4cdd-4bae-883a-7422e70eb448)

***

<h2  align="center"> Testando localmente a aplicação </h2>

***

  

### Pré-requisitos


* Ter o [Python](https://www.python.org/) instalado

* Ter o [Postman](https://www.postman.com/) instalado

* Conexão com a internet

* Ter o [Git](https://git-scm.com/downloads) instalado

1. Clone este repositório para o seu ambiente local:

```bash

git clone -b equipe-1 --single-branch https://github.com/Compass-pb-aws-2023-FURG-IFRS-UFFS/sprint-5-pb-aws-furg-ifrs-uffs.git && cd  sprint-5-pb-aws-furg-ifrs-uffs
```

2. Inicie e ative um ambiente virtual com python3
```
python -m venv ./../env
```
```
source ./../env/bin/activate
```

3. Instale todas as dependências do projeto com o PIP
```bash
pip install -r api/requirements.txt 
```
  

4. Execute o arquivo ``main.py``:
```bash
python ./api/main.py
```

Com o comando executado, o servidor será iniciado:
<p><img  width= 100%  height=auto  src="https://i.imgur.com/YcmHvAc.png"></p>

5. Com o Postman aberto, troque a requisição HTTP para **POST**, e insira o seguinte link:

```bash
http://localhost:8000/api/v1/predict
```
ou
```bash

http://127.0.0.1:8000/api/v1/predict

```

5. Em *Headers*, adicione em **Key** o **``Content-Type``** , e em **Value** insira **``application/json``**:

 

<p><img  width= 100%  height=auto  src="https://i.imgur.com/k5XDRpC.png"></p>

6. Em *Body* insira as informações necessárias para fazer a requisição, como no exemplo a seguir: 
```json
{
"no_of_adults":  3,
"no_of_children":  3,
"type_of_meal_plan":  "example",
"no_of_weekend_nights":  1,
"no_of_week_nights":  0,
"required_car_parking_space":  1,
"room_type_reserved":  "Room_Type 1",
"lead_time":  5,
"arrival_year":  2022,
"arrival_month":  7,
"arrival_date":  6,
"market_segment_type":  "Online",
"repeated_guest":  1,
"no_of_special_requests":  0,
"booking_status":  "Not_Canceled"
}
```
7.  Com tudo devidamente configurado, envie a requisição, a resposta esperada deverá ser similar a seguinte:
<p><img  width= 100%  height=auto  src="https://i.imgur.com/Soh8fg6.png"></p>
  
***
<h2  align="center"> Como alterar e atualizar Aplicação na AWS </h2>

***

**Pra fazer alterações:**

- Buildar nova imagem no ECR 
```bash
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin SEU_ACCOUNT_ID.dkr.ecr.us-east-1.amazonaws.com
docker build -t sprint5-api .
docker tag sprint5-api:latest URI-DO-REPOSITORIO-ECR
docker push URI-DO-REPOSITORIO-ECR:latest
```
- Criar nova versão da aplicação 
```bash
aws elasticbeanstalk create-application-version \

  --application-name NOME_DA_APLICACAO \

  --version-label VERSAO \

  --source-bundle S3Bucket=NOME_DA_BUCKET,S3Key=Dockerrun.aws.json

```
- Atualizar o ambiente
```bash
aws elasticbeanstalk update-environment \

  --environment-name PNOME_DA_ENV \

  --version-label VERSAO
```
- Pronto!

***
<h2  align="center"> Dificuldades Encontradas </h2>
***

Primeiramente ficamos com dificuldade em como separar as atividades, e sobre como deveriamos fazer o trabalho. A solução foi criar uma IAM para fornecer o acesso ao mesmo estúdio do SageMaker para os integrantes do grupo.
Outro problema que ocorreu foi o pequeno incidente com o AutoPilot da AWS, que acabou gerando uma grande cobrança na AWS da noite para o dia,  e fez com que a equipe se preocupasse com o ocorrido.
  
***
<h2  align="center"> Equipe </h2>

<center>

[João Victor Winderfeld](https://github.com/joaowinderfeldbussolotto) - [Luiz Paulo Grafetti Terres](https://github.com/luizpgt) - [Paulo Sergio Nunes](https://github.com/Paulocc) - [Felipe Marzani](https://github.com/FeMarzani)

</center>