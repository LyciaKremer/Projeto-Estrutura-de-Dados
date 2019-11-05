# Projeto de Estrutura de Dados
Projeto avaliativo da disciplina de Estrutura de Dados.



## Projeto Banco de Questões
*Descrição:
Este documento refere-se à descrição do sistema Banco de Questões. Como o próprio
nome já diz, o sistema consiste em armazenar e administrar banco de questões para serem
utilizados em provas, simulados, testes e demais tipos de avaliações realizadas aos alunos da
instituição.*

*O sistema deverá ser acessado por dois tipos de usuários:*
- Professor
- Coordenador

*O professor precisa acessar um menu similar ao seguinte:*
- Cadastrar Questão.
- Minhas Questões.
- Gerar exercício ou prova.
- Acessar provas anteriores e gabaritos.
- Avaliar questões de outros professores.

*Neste mesmo sentido, o coordenador precisa ter acesso a um menu equivalente a este:*
- Listar Questões
- Cadastrar disciplinas
- Cadastrar professor à disciplina

*Poderá existir outros menus de interação, dependerá da estrutura do projeto.*
- O coordenador pode ser um professor. 
- O coordenador do curso deve alocar outros dois professores para avaliar as questões de cada disciplina utilizando os valores de 1 a 3:
    - 1 - Questão reprovada - muito fácil ou incorreta; 
    - 2 - Questão incompleta; 
    - 3 - Questão aprovada;
- Se ao menos um professor marcar 1, a questão não será disponibilizada para o uso. 
- Caso os dois professores marquem 2, ou um 2 e outro 3, a questão precisa ser refeita. 
- Se os 2 marcarem 3, pode ser usada pelo sistema.
- Cada disciplina deve ter seus assuntos cadastrados no sistema. 
- Cada questão deve indicar se é:
    - Aberta (questão subjetiva).
    - Fechada (questão objetiva), ter um texto do enunciado, as alternativas. Se for fechada, o nível de dificuldade, de 1 a 3, e estar associada a um conteúdo da disciplina. 
- Cada professor pode cadastrar questões para as suas disciplinas, que está associada a um curso.

*Funcionalidade extra:*
- O ideal é que uma lista de questões pudessem ser importadas e salvas a partir de um arquivo texto gerado pelo professor (.xml, .doc,     .txt, etc.).
*Funcionalidade extra em Estrutura de Dados:*
- Interface gráfica (sugestão: biblioteca tkinter).

## Authors

* **Lycia Kremer** - *Trabalho inicial* - [LyciaKremer](https://github.com/LyciaKremer)
* **Karolline Carvalho** - *Trabalho inicial*
* **Rodrigo Cézar** - *Trabalho inicial*
* **Igor Marques** - *Continuidade do projeto* - [igorpms](https://github.com/igorpms)
