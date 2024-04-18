# API para controle de veículos

## 
Desenvolvido por João Marcelo Gomes da Silva Batista, em Março/Abril de 2024, como requisito parcial para aprovação na sprint  **Desenvolvimento Full Stack Básico** da PUC Rio.

## Objetivo e Cenário:
O objetivo do projeto é apresentar um MVP que servirá como base para a solução do problema de controle de usuários autorizados a utilizar um estacionamento privado.

A ideia surgiu a partir de um problema que a minha empresa enfrenta para o controle de veículos autorizados, no entanto, a solução proposta tem aplicabilidade para condomínios, clubes, hospitais ou quaisquer outras instituições públicas ou privadas que possuam suas próprias áreas de estacionamento, tenham a necessidade de controlar o acesso às mesmas e ainda não possuam um sistema informatizado para tal.

Para o desenvolvimento, foi considerado o seguinte cenário:
1) Existe pelo menos um funcionário que realiza o controle de entrada dos veículos.
2) Atualmente o controle é realizado por intermédio de um cartão de estacionamento.
3) O funcionário realiza o controle de forma totalmente visual, simplesmente verificando se o condutor do veículo possui o cartão ou não. 
4) No estacionamento **não existe**, atualmente, nenhum sistema informatizado que possibilite o controle em tempo real por parte do funcionário.

Devido à grande quantidade de veículos, o cenário acima apresenta as seguintes fragilidades de segurança, que o sistema proposto objetiva mitigar:
1) Ingresso de terceiros, utilizando cartão de estacionamento emprestado por usuário autorizado.
2) Ingresso de terceiros, utilizando cartão de estacionamento roubado ou extraviado.
3) Ingresso de ex-funcionários que eventualmente detenham, mesmo que de forma irregular, seu cartão de estacionamento.

Dessa forma, a implementação da solução se dará da seguinte forma:
1) Haverá um funcionário na entrada do estacionamento com acesso ao Sistema de Controle de Veículos.
2) Assim que um veículo chegar, deverá parar na entrada do estacionamento e aguardar a verificação pelo funcionário.
3) O funcionário realizará a consulta no sistema a partir da placa e, caso o veículo esteja autorizado, será permitida a entrada no estacionamento.

Outras considerações:
- O sistema permitirá que o funcionário do estacionamento realize a consulta ao nome do condutor e ao seu setor de trabalho na empresa. Isto possibilitará entrar em contato com o condutor em caso de eventual necessidade, tais como esquecimento de luzes do veículo acesas, pneu vazio, necessidade de remoção do local estacionado, etc...


---
## Como instalar e executar:

É fortemente indicado o uso de ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

Para criar o ambiente virtual no Windows deve-se digitar no terminal, dentro da pasta do projeto no qual se deseja criar o ambiente virtual:
>python -m venv env

Em seguida, para ativar o ambiente virtual a partir do terminal:
>.\env\Scripts\Activate.ps1

Na sequência, irá aparecer (env) na esquerda do prompt, indicado que o usuário encontra-se no ambiente virtual.

Será necessário ter todas as libs python listadas no requirements.txt instaladas. Para instalar, de dentro do ambiente virtual:
>pip install -r requirements.txt

Para desativar o ambiente virtual: 
>deactivate 

Para deletar o ambiente virtual é só excluir a pasta env.

Para saber quais bibliotecas estão instaladas no env: 
>pip freeze

Para instalar as últimas versões das bibliotecas do requirements.txt, é só apagar a versão que está no arquivo (deixar as versões em branco)

Para executar a API basta executar, de dentro do ambiente virtual (env):
>flask run --host 0.0.0.0 --port 5000

Em modo de desenvolvimento é recomendado executar o comando acima utilizando o parâmetro reload, que reiniciará o servidor automaticamente após uma mudança no código fonte:
>flask run --host 0.0.0.0 --port 5000 --reload

Para verificar o status da API em execução, abrir no navegador:
>[http://localhost:5000/#/](http://localhost:5000/#/)
