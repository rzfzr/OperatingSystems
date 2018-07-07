20 questoes concurso publico
    Introducao a SO
    Estrutura SO
    Processos e Threads

multipla escolha, justificado com referencia

Analise de qual assunto eh comum para concurso publico
    artigo 4 paginas padrao acm/ieee coluna dupla

entrega 4/7

Questoes de multipla escolha retiradas do seguinte livro: https://www.amazon.com/Operating-Systems-MCQs-Multiple-Questions-ebook/dp/B01G3WZMLK
Site do livro: http://www.mcqslearn.com/cs/operating-systems/operating-systems-topics.php

Nao usado, segunda opcao: http://www.siteforinfotech.com/2017/01/mcq-questions-threads-smp-microkernels.html

<!-- Feitas 25 por tem 4 alternativas ao envez de 5 -->


1. I/O function allows to exchange data directly between an

a. Process States
b. Registers
c. I/O module and the processor
d. I/O devices

Correta = c, como no primeiro paragrafo de 3.7 "Interfacing" na pagina 232, I/O tem a funcao de fazer o computador se comunicar com o mundo externo
Errada = a, nao foi citado em 5.8.4 na pagina 424 o uso de I/O para alterar estados de processos
Errada = b, como deduzido do primeiro paragrafo de 5.1.3 na pagina 349, os registradores nao se relacionam com as funcoes de I/O
Errada = d, como descrito em todo o capitulo "Interfacing" iniciado na pagina 349, formas de comunicacao somente entre dispositivos e computadores por meio do I/O, nao entre dispositivos distintos.

2. Cache memory is intended to provide memory access

a. Fastest
b. Slow
c. Very Slow
d. Fast

Correta = a, em 4.5.1 na pagina 304 foi descrito a nescessidade que proporcionou o desenvolvimento da memoria cache, em que as memorias RAM continuam sendo melhoradas porem a um nivel muito abaixo das velocidades de processamentos das CPUs, assim atrapalhando o rendimento total, a solucao foi implementar uma memoria temporaria entre a RAM e os registradores, com baixa latency e velocidade extremamente alta, muitas vezes em paralelo para aumentar ainda mais os seus beneficios.
Incorretas = b,c,d, visto que o cache foi projetado para ser o mais rapido possivel
3. Interrupts are provided primarily as a way to

a. Improve processor utilization
b. Improve processor execution
c. Improve processor control
d. Improve processor speed

Correta = a, como descrito em 5.6.5 na pagina 414, as interrupcoes alteram o fluxo de controle quando por exemplo um processo eh finalizado, a CPU entao acha um novo processo por via do vector de interrupcao, diminuindo assim os ciclos onde o processador esta idle, aumentando a utilizacao.
Incorretas = b,c e d, Interrupcao nao afeta essas outras variaveis

4. Program counter contains the address of the

a. Next programs to be fetched
b. Previous programs to be fetched
c. Previous information to be fetched
d. Next information to be fetched

Correta = d, como descrito no passo 6 de "Hardware Actions" na pagina 415, o program counter aponta para a proxima informacao.
Incorreta = a, como descrito no mesmo passo, o program counter nao apontara nescessariamente para uma aplicacao, no exemplo dado ele apontaria para uma rotina de servicos provenientes do dispositivo causando a interrupcao.
Incorretas = b e c, nao achei mencao de backtracking/backlogging nescessario para retonar em processos anteriores.


5. Cache size issue can have significant impact on

a. input
b. output
c. Information
d. Performance

Correta = d, dito no quarto paragrafo da pagina 84, performance esta positivamente relacionada ao tamanho do cache
Incorretas = a e b, como descrito no mesmo paragrafo, quanto maior o cache, cria-se o problema de maior o custo de acesso
Incorreta = c, tamanho do cache nao afeta a informacao nele contida

6. Data and instructions that are being used frequently are stored in

a. Cache
b. Block
c. hard disk
d. main memory

Correta = b, como descrito no terceiro paragrafo da pagina 84, as memorias sao subdevididas em blocos, no caso de cache
Incorreta = a, como descrito na pagina 83, eh usado para manter dados de rapido acesso
Incorreta = c, como dito na pagina 86, esse tipo de memoria eh extremamente lenta (porem de maior capacidade), comparada com as de nivel acima, nao seria usado para data e instrucoes de acesso frequente
Incorreta = d, abstracao que inclui outros tipos de memoria como visto no capitulo 2

7. In implementation of Semaphores, for a single processor system, it is possible to inhibited

a. Deadlock
b. Interrupts
c. Lock Step
d. None

Correta = b, no segundo capitulo da pagina 480 o autor cita o "truque" que funciona somente para sistemas com um unico processador, ao desabilitar os interrupts, assim o processador deve terminar um processo antes de comecar o outro

