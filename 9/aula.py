'''
-- Dilemas
Em decorrência da implementação e de todos os 
artefatos que serão gerados, desde a especificação de 
requisitos até o momento no qual conseguimos trabalhar 
a implementação e o software, do ponto de vista de 
gerenciamento dos artefatos, chegamos a alguns dilemas. 
Eles dizem respeito a:
• Mudança de ideia por parte do cliente;
• Mudança de requisitos;
• Mudança de código;
• Mudança no ambiente;
• Como saber o que foi modificado no código?;
• Como saber quem mexeu no arquivo?;
• Como saber quando ocorreram essas modificações?;
• Depois das mudanças, o sistema continua funcionando 
bem?
• Como saber se não foi inserido algum tipo de erro?
Nesse sentido, algumas ações necessárias são: controlar 
e acompanhar estas mudanças; registrar a evolução do 
projeto; garantir a integridade do sistema.

- Operações do Git
Algumas operações que são feitas no Git são:
Git pull: busca as alterações remotas no clone local e as 
mescla nos arquivos de trabalho atuais.
Git checkout: substitui os arquivos de trabalho atuais por 
arquivos de uma ramificação;
Git checkout --track: cria uma ramificação local a partir de 
uma ramificação remota, vincula-as, e substitui os arquivos 
de trabalho atuais por arquivos desta ramificação; 
Git fetch: baixa as alterações de um repositório remoto para 
o clone local;
Git reset: faz com que a ramificação atual aponte para 
alguma revisão ou ramificação específica;
Git reset --hard: faz com que a ramificação atual aponte 
para alguma revisão ou ramificação específica e substitui 
os arquivos de trabalho atuais pelos arquivos dessa 
ramificação;
Git merge: mescla os arquivos da branch com os arquivos 
da ramificação atual; 
Git push: carrega as alterações das ramificações locais para 
os respectivos repositórios remotos;
Git add: coloca os arquivos de trabalho atuais na staging 
(versão em desenvolvimento); 
Git commit: confirma alterações em etapas para uma 
ramificação local;
Git commit -a: confirma todos os arquivos modificados 
para uma ramificação local (abreviação para “git add” e “git 
commit”).

- Fluxo de trabalho entre Git e GitHub
Faça “fork” do projeto -> Crie um branch” para alterações 
no master -> Faça alguns “commits” para aprimorar o 
projeto -> Abra um “Pull Request” no GitHub -> Discuta e 
opcionalmente continue “commitando” -> O proprietário do 
projeto faz merge ou fecha o “Pull Request”.

Boas práticas no Git
São boas práticas elaborar boas mensagens de commit, 
que realmente deem a entender o que está sendo 
alterado dentro da nova versão do item de configuração. 
Existem mensagens que representam um fix, que é uma 
correção de bug que não deixava clientes terminarem a 
inscrição no site; outras que dizem respeito a um update 
dentro daquele conteúdo, mas que não tenha sido gerado 
devido a algum erro; e ainda o “clone”, que trata de um 
update das dependências do npm para a última versão. 
Existem ainda mensagens não tão boas mensagens de 
commit, como informalismos que não mostram o que de 
fato gerou a necessidade de uma nova versão do produto.
'''