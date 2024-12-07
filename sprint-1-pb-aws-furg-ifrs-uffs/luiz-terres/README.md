# Funcionalidadde

Código fonte para verificação de PIN (Personal Identification Number) usando JavaScript.

***

## Funcionamento Básico

O usuário busca acertar o número PIN gerado [pseudo-randomicamente](https://en.wikipedia.org/wiki/Pseudorandomness) pela biblioteca [Math](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/random). O usuário é parabenizado ao acertar o PIN, caso contrário, recebe um retorno seguindo a tabela:

| Última entrada |  "Sua próxima entrada deve ser ... que a anterior!"   |
|----------------|-------------------------------------------------------|
|Entrada > PIN   | Menor                                                 |
|Entrada < PIN   | Maior                                                 |
|Entrada/2 >= PIN| Muito Menor                                           |
|Entrada*2 <= PIN| Muito Maior                                           |

O método [prompt()](https://developer.mozilla.org/en-US/docs/Web/API/Window/prompt) é usado para input de dados do usuário.

***

# Execute esse código na sua máquina

Clone esta branch do repositório:
```bash
git clone -b luiz-terres --single-branch https://github.com/Compass-pb-aws-2023-FURG-IFRS-UFFS/sprint-1-pb-aws-furg-ifrs-uffs && cd sprint-1-pb-aws-furg-ifrs-uffs
```

No **Linux**:
```bash
firefox index.html  
```
ou
```bash
chromium index.html 
```
No **Windows** (cmd/powershell/git bash):
```
explorer
```
E duplo clique no arquivo "index.html"

## Notas de desenvolvimento
O sistema foi desenvolvido buscando simplicidade de código e lógica, sendo eficaz no que se propõe a fazer.
Não foram encontradas grandes dificuldades durante o desenvolvimento.

Desenvoledor: Luiz Paulo Grafetti Terres.
