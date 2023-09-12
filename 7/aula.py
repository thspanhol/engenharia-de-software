'''
-- Arquitetura de software
A arquitetura de software envolve o conjunto de
decisões que definem a organização do sistema
objetivando: definir os elementos estruturais e suas
interfaces de modo a estabelecer a composição do
sistema, estabelecer o comportamento pela colaboração
entre estes elementos e compor estes elementos
estruturais e comportamentais em subsistemas.
- Concorrência
Quando eu tenho vários usuários tentando fazer acesso
ao mesmo tipo de funcionalidade.
- Interface
A interface do usuário – user interface (UI) – é o espaço
onde os usuários interagem com um site, programa,
aplicativo etc. Isso pode incluir telas de exibição, um
mouse, teclados e a aparência de uma área de trabalho.

- Requisitos e arquitetura de software
Apesar de os requisitos funcionais definirem as
principais características do funcionamento do
software, os requisitos não-funcionais têm forte
influência na definição da arquitetura do software,
são eles: disponibilidade, usabilidade, desempenho,
confiabilidade, segurança e manutenibilidade. Ana
Paula apresenta os aspectos chave em arquitetura
de software: concorrência, controle e tratamento
de eventos, distribuição de componentes e
tratamento de exceções e tolerância a falhas. Além
disso, conferimos os aspectos de um software
bem arquitetado: performance, escalabilidade e
flexibilidade. A professora sugere que seja feito um
balanço entre as prioridades do cliente, relacionando,
por exemplo, fatores como desempenho e segurança.
Ela afirma que as decisões do engenheiro de software
serão tomadas com base nos interesses do cliente em
questão.

- Padrões de arquitetura
No padrão de segurança centralizada, revemos o conceito
de manutenibilidade e sua relação com a performance.
A professora apresenta problemas a serem solucionados
considerando segurança e usabilidade, falando sobre
o padrão de segurança em níveis e, na relação entre
disponibilidade e time-to-market, conferimos os
componentes redundantes. 
-Segurança centralizada
Simplifica o acesso à informação pois todo o conteúdo,
em termos de dados, fica centralizado num único local.
Ao mesmo passo que a informação centralizada gera
facilidade de se projetar e construir, há que se atentar
para o fato de que, uma vez que as informações estejam
todas no mesmo ambiente, em caso de quebra de
segurança, todos os dados podem ser perdidos.
-Componentes redundantes
Um sistema pode ser redundante em diversos dos seus
componentes. Para isso, basta que ele tenha pelo menos
dois recursos diferentes integrados e capazes de se
substituírem.

- Organização dos componentes
Neste capítulo, analisamos os elementos essenciais
sem preocupação com os detalhes. O foco deve
ser nos componentes de larga escala. A professora
apresenta o modelo de camadas, geralmente utilizado
para demonstrar a organização dos componentes.
Cada camada é uma área de responsabilidades
a ser considerada de forma independente das
demais, os componentes são independentes, não
sobrepõem funcionalidades e as interfaces entre as
camadas não devem mudar com frequência. Vemos
questões transversais na arquitetura de camadas
relacionando os aspectos de segurança, performance
e disponibilidade.
-Arquitetura em camadas
Estilo arquitetural que dentre vários objetivos, destacase o de organizar as responsabilidades de partes de um
software, normalmente criando um isolamento e dando
um propósito bem definido a cada camada de forma que
ela possa ser reutilizável por um nível mais alto ou até
substituível.

- Arquiteturas distribuídas
Tem como objetivo definir servidores do sistema
e a alocação dos componentes nestes serviços.
Neste tipo de arquitetura a interface com o usuário
é executada no próprio computador ou dispositivo
móvel do usuário. O padrão de arquitetura MVC divide
um sistema interativo em: model, views e controllers.
A professora explica cada um deles e relaciona com o
padrão MVC com o Cliente Servidor.
-Cliente Servidor
Uma arquitetura de aplicação distribuída, ou seja, na
rede existem os fornecedores de recursos ou serviços
a rede, que são chamados de servidores, e existem os
requerentes dos recursos ou serviços, denominados
clientes.

- Detalhamento de projeto
Vemos o conceito de UML e os modelos de diagramas
de atividades, de classes, de sequência, de componente
e de implantação. Ana Paula afirma que todas as classes
mapeadas dentro de um diagrama precisam mostrar as
propriedades ou atributos e apresentar comportamentos
comuns, também chamados de métodos. A professora
reforça que os diagramas ajudam a equipe de
desenvolvimento a visualizar, através desses esquemas
ilustrativos, as melhores formas de desenvolver o software.
-UML
Linguagem Unificada de Modelagem é, como o nome
indica, uma linguagem de notação utilizada para modelar
e documentar as diversas fases do desenvolvimento de
sistemas orientados a objetos.

- Utilizamos diagramas para:
• Softwares de maior complexidade que envolvam
integração de serviços diversos;
• Entender melhor a solução de software e como a
comunicação entre as suas partes se estabelecem;
• Regras de negócios mais complexas que precisam
de um melhor entendimento por parte do time de
desenvolvedores;
• Documentar a forma como a implantação
acontecerá quando entregue ao cliente;
• Modelar a estrutura de dados que será persistida
em um banco de dados,
• Fazer reuso de partes do projeto.

- Padrões de projeto
De acordo com o livro “Padrões de Projeto: soluções
reutilizáveis de software orientado a objetos”, os padrões
“GoF” são divididos em 24 tipos e classificados de acordo
com as suas finalidades. São 3 as classificações/famílias:
padrões de criação, estruturais e comportamentais.
Ana Paula explica a composição do padrão de projeto
expressado entre contexto, problema e solução,
considerando escopo de classe e de objeto. 
-Padrão Singleton 
Tem como definição garantir que uma classe tenha
apenas uma instância de si mesma e que forneça um
ponto global de acesso a ela. Ou seja, uma classe
gerencia a própria instância dela, além de evitar que
qualquer outra classe crie uma instância dela. 
-Padrão Strategy 
Sugere que se produza uma família de classes para cada
variação do algoritmo e que se forneça para a classe
hospedeira uma instância de Strategy para a qual ela
delegará em tempo de execução.

- Arquitetura Limpa
Propõe estrutura em elipse das mais internas para as mais
externas na seguinte ordem: regras de negócio, regras da
aplicação, adaptadores de interface e frameworks e drivers.
A professora explica cada um dos níveis da elipse e sugere
algumas plataformas de aplicação de arquitetura limpa.
-Regras do negócio
Encapsula as abstrações com a qual a empresa trabalha
ou a área em questão e dificilmente sofre alteração em
função de solicitações relativas à aplicação, só mudam
quando os objetivos da empresa ou da área mudam.
-Regras da aplicação
Contêm regras de negócio específicas da aplicação
(sistema sendo desenvolvido), encapsulam e
implementam todos os casos de uso / user stories da
aplicação.
-Nível de adaptadores de interface
O software deste nível é composto por um conjunto de
adaptadores que converte os dados entre o formato
mais conveniente para os casos de uso e entidades, e os
formatos mais convenientes para os níveis externos tais
como persistência e GUI.
-Nível de Frameworks e Drivers 
Quaisquer serviços dependentes de uma tecnologia
específica (API externa, protocolo de comunicação etc.)
se encontram neste nível.

Existem vários tipos de arquitetura de software, cada um projetado para atender a diferentes necessidades e requisitos de aplicativos. Abaixo, listo alguns dos tipos mais comuns de arquitetura de software:

Arquitetura Monolítica: Neste modelo, toda a aplicação é desenvolvida como um único código-fonte e implantada como uma única unidade. É mais simples de desenvolver, implantar e testar, mas pode ser difícil de escalar e manter em projetos complexos.

Arquitetura em Camadas: Divide a aplicação em camadas distintas, como a camada de apresentação, lógica de negócios e acesso a dados. Isso promove a separação de preocupações e facilita a manutenção.

Arquitetura Cliente-Servidor: Divide a aplicação em duas partes principais: um cliente que interage com o usuário e um servidor que processa as solicitações do cliente e fornece recursos ou dados. Pode ser implementada em várias configurações, como cliente-servidor de duas camadas ou cliente-servidor de três camadas.

Arquitetura Orientada a Serviços (SOA): Baseia-se na ideia de criar serviços independentes que podem ser acessados e combinados para atender às necessidades de negócios. Esses serviços são geralmente expostos através de interfaces de serviço e podem ser reutilizados em várias partes da aplicação.

Microservices: Similar à arquitetura SOA, mas com foco em serviços menores e autônomos que podem ser implantados e escalados de forma independente. Cada microserviço é responsável por uma parte específica da funcionalidade da aplicação.

Arquitetura Baseada em Eventos: Neste modelo, os componentes da aplicação se comunicam por meio de eventos assíncronos. Os eventos são gerados e consumidos para realizar ações e atualizações de estado.

Arquitetura em Nuvem: Projetada para implantação em ambientes de computação em nuvem, essa arquitetura aproveita os recursos escaláveis e elásticos da nuvem para dimensionar aplicativos conforme necessário.

Arquitetura de Microsserviços sem Servidor (Serverless): Neste modelo, os desenvolvedores se concentram na criação de funções independentes que são executadas em resposta a eventos, sem se preocupar com a infraestrutura subjacente.

Arquitetura Orientada a Componentes: Divide a aplicação em componentes reutilizáveis que podem ser usados para construir aplicativos maiores. Isso promove a modularidade e a reutilização de código.

Arquitetura Distribuída: Projetada para aplicativos que são distribuídos geograficamente ou que envolvem várias instâncias em locais diferentes. Essa arquitetura lida com os desafios de comunicação e coordenação entre os componentes distribuídos.

Arquitetura em Malha (Service Mesh): Introduz uma camada de infraestrutura para gerenciar a comunicação entre serviços em um ambiente de microsserviços. Isso ajuda a lidar com problemas como descoberta de serviço, balanceamento de carga e segurança.

Arquitetura Baseada em Componentes de Interface de Usuário (UI): Neste modelo, a UI é dividida em componentes reutilizáveis que podem ser combinados para criar interfaces de usuário mais complexas.
'''