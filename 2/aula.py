'''
--Processo em Engenharia de Software

A professora Ana Paula relembra que processo em
Engenharia de Software significa um conjunto de atividades
cuja meta é o desenvolvimento ou evolução de software. A
partir disso, reflete com os alunos sobre a necessidade
desses processos, explicando que os modelos de processo
de desenvolvimento são classificados de duas formas:

• Modelos Prescritivos: possuem em sua estrutura uma
ordem formal de elementos do processo; são modelos
com foco na previsibilidade e planejamento antecipado;
considerados Modelos Tradicionais. Ex: Cascata, Orientado à
Reúso.

• Modelos Adaptativos: não são processos rígidos, mas são
focados no produto, nas pessoas que o desenvolvem e são
abertos a mudanças; têm foco no planejamento incremental
e flexível.  Ex: Scrum, XP, Crystal, FDD e  DSDM.


-Modelo Cascata

Neste momento, Ana Paula explica mais detalhadamente
sobre os modelos prescritivos, que são métodos mais
tradicionais, alertando que podemos usar esses modelos
ainda hoje, mas é necessário saber em que situação aplicalos e identificar se eles são adequados em determinada
situação e tipos dos problemas.

Na sequência, a professora apresenta as fases do Modelo
Cascata, que são:

• Levantamento de Requisitos;
• Desenvolvimento do Projeto;
• Implementação do Projeto;
• Testes para Verificação da Implementação;
• Implantação e Manutenção do software.

Vantagens
• Cada fase é bem definida e deixa claro o que precisa ser
feito para passar por ela;
• Existe uma razão pela qual as etapas acontecem na
ordem determinada; o projeto se torna algo realmente
estruturado.

Desvantagens
• Exige que todos os requisitos sejam definidos no início do
projeto, já na primeira fase;
• Particionamento inflexível do projeto em estágios distintos,
dificulta a resposta aos requisitos de mudança do cliente;
• Poucos sistemas de negócio têm requisitos estáveis.
• Dificuldade de acomodação das mudanças depois que o
processo está em andamento;
• Só é possível visualizar algo quando as fases já estão bem
avançadas;
• Uma fase tem de estar completa antes de passar para a
próxima.

Quando utilizar do Modelo Cascata?

O Modelo Cascata é apropriado somente quando os
requisitos são bem compreendidos e quando as mudanças
forem bastante limitadas durante o desenvolvimento do
sistema. Uma forma de utilizar o modelo cascata é quando
precisamos fazer adaptações ou aperfeiçoamentos em um
sistema já existente.

-Modelo de Prototipação

Ana explica que o Modelo de Prototipação é um exemplo
de modelo de desenvolvimento evolucionário, que significa
o desenvolvimento de uma implementação inicial, expondo
o resultado aos comentários do usuário e refinando esses
comentários por meio de várias versões até que seja
desenvolvido um sistema adequado.
O modelo de prototipação apresenta o objetivo de entender
os requisitos do usuário para obter uma melhor definição dos
requisitos do sistema.
Fases do Modelo:
• Obter Requisitos;
• Elaborar Projeto Rápido;
• Construir Protótipo;
• Avaliar o protótipo;
• Refinar o protótipo.

Vantagens

• Possibilita que o desenvolvedor crie um modelo
(protótipo) do software que deve ser construído;
• Uso apropriado quando o cliente não definiu
detalhadamente os requisitos

Desvantagens

• Cliente não sabe que o software que ele vê não
considerou, durante o desenvolvimento, a qualidade
global e a manutenibilidade a longo prazo.
• Desenvolvedor frequentemente faz uma implementação
comprometida (utilizando o que está disponível) com o
objetivo de produzir rapidamente um protótipo.

-Iteração de processo

Ana Paula explica sobre a iteração de processos, mostrando que
requisitos de sistema sempre evoluem no curso de um projeto
e, sendo assim, a iteração de processo, onde estágios iniciais
são retrabalhados, é sempre parte do processo dos sistemas
de grande porte. Nesse sentido, a iteração pode ser aplicada a
qualquer um dos modelos genéricos do processo.
Na sequência, são mostrados modelos preditivos e iterativos
e suas características, como: Desenvolvimento incremental,
Modelo Espiral e RUP (Rational Unified Process).

Desenvolvimento Incremental
• O sistema é entregue ao cliente em incrementos;
• Os requisitos são priorizados;
• Uma vez que o desenvolvimento de um incremento é
iniciado, os requisitos são congelados.

Modelo Espiral

• Engloba as melhores características do Modelo Cascata
e da Prototipação, adicionando um novo elemento: a
Análise de Riscos;
• O que é um risco? algo que pode dar errado;
• Segue a abordagem de passos sistemáticos do Modelo
Cascata, incorporando-os numa estrutura iterativa;
• É dividido em uma série de regiões, tipicamente de 3 a
6, que delimitam atividades.

Rational Unified Process (RUP)
• Processo Unificado (PU);
• Um framework genérico;
• Uma abordagem para a construção, implantação e manutenção
de software;
• Um processo iterativo para o desenvolvimento de software
visando a construção de sistemas orientados à objetos.

-Processo Unificado: funcionamento
• Para cada iteração, os desenvolvedores identificam os
casos de uso relevantes, analisando-os segundo a arquitetura
selecionada;
• O produto da iteração são componentes (modelos ou
módulos executáveis); iteração, casos de uso e arquitetura;
• Verifica-se então se os componentes satisfazem os casos
de uso e a arquitetura;
• Se a implementação atinge os objetivos, o desenvolvimento
passa para a próxima iteração;
• Caso contrário, os desenvolvedores devem revisar as
decisões anteriores e tentar uma nova abordagem.

-Desenvolvimento Orientado a Serviços
Um serviço é a funcionalidade a ser oferecida por um
sistema, a qual pode ser reutilizada. Assim, o objetivo do
desenvolvimento orientado a serviços é desenvolver software
como uma composição de serviços e promover o reuso dos
mesmos. Na sequência, são mostrados os tipos de serviços
característicos:

Serviços de Utilidades
Funcionalidades Gerais que podem ser utilizadas por
diferentes sistemas.

Serviços de Negócios
Função específica de negócio.

Serviços de Coordenação
Serviços que viabilizam a comunicação entre os serviços de
negócios.
'''