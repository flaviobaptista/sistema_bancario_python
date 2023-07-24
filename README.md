<h1 style="color: #b298dc;">Gerenciamento de Conta Bancária</h1>

<img style="margin-right: 50px;" align="left" alt="Developer Art" width="250px" src="./img/1026870_OJZ2IH1.png">
<br>
<br>
<br>
<br>
<p align="justify">
Este projeto consiste em um sistema simples de gerenciamento de conta bancária, desenvolvido em Python. O programa permite ao usuário realizar operações de depósito, saque, verificar extrato e limite de saque.
<br>
Uma das principais características do sistema é a utilização de um menu interativo, no qual o usuário pode escolher as opções desejadas através de um número correspondente. O menu foi projetado para proporcionar uma experiência intuitiva ao usuário, tornando a interação com o sistema mais fácil e acessível.
<br>
Além disso, o sistema foi aprimorado com a implementação de funções modulares, proporcionando uma organização mais clara e eficiente do código. Isso possibilita a manutenção e extensão do projeto de forma mais prática e compreensível.
<br>
Em suma, o sistema de gerenciamento de conta bancária oferece uma solução prática e funcional para controlar as movimentações financeiras, possibilitando que o usuário realize operações bancárias de forma eficiente e segura.
<p>

<h2 style="color: #b9faf8;">Funcionalidades</h2>

- Depósito: O usuário pode realizar depósitos em sua conta informando o valor desejado.

- Saque: O usuário pode fazer saques de sua conta, desde que o valor solicitado não exceda o saldo disponível e o limite de saques.

- Extrato: O usuário pode verificar o extrato de movimentações realizadas em sua conta, exibindo os depósitos e saques efetuados.

- Limite de Saque: O programa possui um limite máximo de saques diários, que é configurado para 3 saques por padrão. O usuário será informado caso tente realizar um saque após exceder esse limite.

<h2 style="color: #b9faf8;">Requisitos</h2>

- Python 3.x
<br>

<h1 style="color: #b298dc;">Como Utilizar</h1>

1. Clone o repositório para o seu computador:

2. Navegue até o diretório do projeto:

3. Execute o script Python:

4. Siga as instruções apresentadas no menu para realizar as operações bancárias.


<h3 style="color: white;"><span style="color: #ff7096;">Exemplo 1:</span> Realizar um depósito de R$ 100,00</h3> 

<details>
<summary style="color: #a5ffd6;">Exemplo</summary> 

- Selecionar a opção: 1 ***<<< DIGITE O NÚMERO E APERTE ENTER NO TECLADO PARA DEPOSITAR***
- Informe o valor do depósito: 100 ***<<< DIGITE O VALOR DO DEPÓSITO E APERTE ENTER NO TECLADO***
<pre>
============== Menu ==============
Olá, seja bem-vindo...

Escolha uma das opções a seguir.
_________________________________

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair
_________________________________

==================================
Selecionar a opção: 1
Informe o valor do depósito: 100

Depósito realizado com sucesso!

</pre>

</details>

<h3 style="color: white;"><span style="color: #ff7096;">Exemplo 2:</span> Tentar sacar R$ 200,00 (excedendo o saldo disponível)</h3> 

<details>
<summary style="color: #a5ffd6;">Exemplo</summary> 

- Selecionar a opção: 2 ***<<< DIGITE O NUMERO 2 E APERTE ENTER NO TECLADO PARA SACAR***
- Informe o valor do SAQUE: 200 ***<<< DIGITE O VALOR DO SAQUE E APERTE ENTER NO TECLADO***

<pre>
============== Menu ==============
Olá, seja bem-vindo...

Escolha uma das opções a seguir.
_________________________________

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair
_________________________________

==================================
Selecionar a opção: 2
Informe o valor do saque: 200

Operação falhou! Você não tem saldo suficiente.

</pre>

</details>

<h3 style="color: white;"><span style="color: #ff7096;">Exemplo 3:</span> Realizar três saques de R$ 50,00 cada (excedendo o limite de saques)</h3> 

<details>
<summary style="color: #a5ffd6;">Exemplo</summary> 

- Selecionar a opção: 2 ***<<< DIGITE O NUMERO 2 E APERTE ENTER NO TECLADO PARA REALIZAR O SAQUE***
- Informe o valor do SAQUE: 50 ***<<< DIGITE O VALOR DO SAQUE E APERTE ENTER NO TECLADO***

===================== <span style="color: #c7f9cc;">REPITA O PROCESSO 3 VEZES</span> =====================


<pre>
============== Menu ==============
Olá, seja bem-vindo...

Escolha uma das opções a seguir.
_________________________________

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair
_________________________________

==================================
Selecionar a opção: 2
Informe o valor do saque: 50

Saque realizado com sucesso!

============== Menu ==============
Olá, seja bem-vindo...

Escolha uma das opções a seguir.
_________________________________

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair
_________________________________

==================================
Selecionar a opção: 2
Informe o valor do saque: 50

Saque realizado com sucesso!

============== Menu ==============
Olá, seja bem-vindo...

Escolha uma das opções a seguir.
_________________________________

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair
_________________________________

==================================
Selecionar a opção: 2
Informe o valor do saque: 50

Operação falhou! Número máximo de saques excedido.


</pre>

</details>

<h3 style="color: white;"><span style="color: #ff7096;">Exemplo 4:</span> Exibindo extrato</h3> 

<details>
<summary style="color: #a5ffd6;">Exemplo</summary> 

- Selecionar a opção: 3 ***<<< DIGITE O NUMERO 3 E APERTE ENTER NO TECLADO PARA VER O SALDO NO EXTRATO***

<pre>
============== Menu ==============
Olá, seja bem-vindo...

Escolha uma das opções a seguir.
_________________________________

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair
_________________________________

==================================
Selecionar a opção: 3

================ EXTRATO ================
Depósito: R$ 100.00
Saldo: R$ 100.00
=========================================

</pre>

</details>

<h3 style="color: white;"><span style="color: #ff7096;">Exemplo 5:</span> Saindo do sistema</h3> 

<details>
<summary style="color: #a5ffd6;">Exemplo</summary> 

- Selecionar a opção: 4 ***<<< DIGITE O NUMERO 4 E APERTE ENTER NO TECLADO PARA SAIR***

<pre>
============== Menu ==============
Olá, seja bem-vindo...

Escolha uma das opções a seguir.
_________________________________

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair
_________________________________

==================================
Selecionar a opção: 4

- FIM DA OPERAÇÂO -

</pre>

</details>

<br>
<br>
<br>
<br>
<br>

<h1 style="color: #efebce;">Referências e Atribuioções</h1>

<details align="left">
  <summary>Clique para visualizar</summary> 

  - GitHub Stats by <a href="https://github.com/anuraghazra/github-readme-stats">anuraghazra</a>
 <a href="https://br.freepik.com/vetores-gratis/projeto-do-fundo-do-banco_1026870.htm#query=bank&position=10&from_view=search&track=sph#position=10&query=bank">Imagem de GraphiqaStock</a> no Freepik
  <br>
  <br>
  <br>

 
  <div align="center">Created by <a href="https://github.com/flaviobaptista">Flávio P. Baptista</a>.</div>
    <br>

</details>

