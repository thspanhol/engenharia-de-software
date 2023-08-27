'''
-- Requisitos funcionais

É a definição do que o sistema deve e não deve fazer. 
Servem para que o desenvolvedor implemente essas 
funcionalidades. Descrevem as ações que o produto deve 
realizar para ser útil. Praticamente qualquer ação pode 
representar um requisito funcional (calcular, inspecionar, 
publicar, etc). Dos requisitos funcionais, espera-se 
completeza (todos os serviços requeridos pelo usuário 
devem ser definidos) e consistência (as definições não 
devem ser contraditórias ou ambíguas).
Por exemplo, para efetivar o empréstimo de um livro, o 
sistema de uma biblioteca deverá:

• permitir a inclusão, alteração e exclusão dos livros 
do acervo;

• ter um identificador único para cada obra;

• verificar se a obra está:
 o cadastrada;
 o ativa;
 o disponível (não reservada).

• garantir que o usuário não esteja com cinco livros 
emprestados, considerando que esse seja o número 
máximo de empréstimos simultâneos permitido;

• gerar um recibo de empréstimo.

-- Requisitos não funcionais

São restrições aos serviços e funções oferecidos pelo 
sistema. Muitas vezes se aplicam a todo o sistema. Eles 
vão definir restrições a nível de propriedade ou qualidade. 
Caso não seja bem especificado ou programado, um 
requisito não funcional pode afetar um requisito funcional. 
Além disso, um requisito não funcional pode gerar novos 
requisitos funcionais, ou eles podem se relacionar.
Há requisitos não funcionais de usabilidade, 
confiabilidade, desempenho e portabilidade (qual banco 
de dados será utilizado, em qual linguagem o software
será desenvolvido, quanto tempo o aplicativo vai demorar 
para abrir).
Exemplos:

• O sistema deve suportar 2 mil usuários.

• O sistema deve impedir que qualquer dado pessoal 
ou confidencial seja imprimível.

• O produto deve utilizar a ortografia do inglês 
britânico.

• A resposta do sistema deve ocorrer em até três 
segundos após uma solicitação.
Dos requisitos não funcionais, espera-se que sejam 
verificáveis. Para isso, é preciso que tenham uma métrica 
associada a eles. Quanto à velocidade, por exemplo, 
é possível ter um número de transações por segundo; 
quanto à facilidade de uso, um número de erros na 
utilização.

Os requisitos não funcionais categorizam-se em:

1. Organizacionais: referem-se a políticas e 
procedimentos nas organizações do cliente e do 
desenvolvedor. Por exemplo: políticas de entrega, de 
implementação, padrões de processo.

2. Externos: referem-se a fatores externos ao sistema 
e ao seu processo de desenvolvimento. Por exemplo: 
fatores de interoperabilidade (interação do sistema com 
outros), éticos, legais (privacidade e segurança).

3. De produto: especificam o comportamento do 
produto. Por exemplo: comportamentos em relação à 
eficiência (desempenho, espaço, rapidez, memória), 
confiabilidade, portabilidade.

-- Stakeholders

São as partes interessadas no projeto, todos que estão 
envolvidos nele – pessoas ou organizações – e que podem 
influenciá-lo de modo positivo ou negativo. Dentre essas 
partes, destacam-se o patrocinador, os fornecedores, os 
clientes, entre outras, conforme infográfico exibido pela 
professora. Stakeholders podem contemplar áreas e um 
indivíduo específico.

-- User stories

No começo dessa parte da aula, a professora explica 
que a user story é uma descrição curta de determinada 
funcionalidade solicitada pelo cliente. Elas são muito 
utilizadas atualmente, principalmente no framework Scrum, 
por conta das metodologias ágeis, mas se originam do XP 
na década de 80. Seu principal objetivo era representar o 
desejo do usuário por alguma funcionalidade, e deveriam 
ser de fácil priorização.

Temas: grupo de stories.

Épicos: são stories grandes sem especificações - ou 
features, funcionalidades muito grandes - que ainda não 
foram “quebrados” em stories menores.
As user stories devem obedecer a uma estrutura: Eu como
<tipo do usuário>, gostaria/quero/devo <objetivo>, com o/
para que <propósito>. 

Essas estórias geralmente são escritas em um cartão ou 
ficha, do ponto de vista de quem vai utilizar esse sistema 
(funcionário, caixa, professor, aluno, cliente, etc), e trazem 
a necessidade desse usuário, os requisitos. Também é 
preciso justificar essa solicitação, apontar quais benefícios 
o usuário terá depois de a funcionalidade ser desenvolvida. 
Já no verso do cartão vão os critérios de aceitação, ou 
como a funcionalidade deve se comportar. É possível, ainda, 
acrescentar em nota informações adicionais relevantes para 
o desenvolvimento do produto.
'''