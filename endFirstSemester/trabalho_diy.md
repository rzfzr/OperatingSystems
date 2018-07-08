20 questoes 
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

Livros referenciais:
    Structured Computer Organization (6th edition) [1]
    Modern Operating Systems (4th edition) [2]


1. I/O function allows to exchange data directly between an

a. Process States
b. Registers
c. I/O module and the processor
d. I/O devices

Correta = c, como no primeiro paragrafo de 3.7 "Interfacing" na pagina 232 [1], I/O tem a funcao de fazer o computador se comunicar com o mundo externo
Errada = a, nao foi citado em 5.8.4 na pagina 424 [1] o uso de I/O para alterar estados de processos
Errada = b, como deduzido do primeiro paragrafo de 5.1.3 na pagina 349 [1], os registradores nao se relacionam com as funcoes de I/O
Errada = d, como descrito em todo o capitulo "Interfacing" iniciado na pagina 349 [1], formas de comunicacao somente entre dispositivos e computadores por meio do I/O, nao entre dispositivos distintos.

2. Cache memory is intended to provide memory access

a. Fastest
b. Slow
c. Very Slow
d. Fast

Correta = a, em 4.5.1 na pagina 304 [1] foi descrito a nescessidade que proporcionou o desenvolvimento da memoria cache, em que as memorias RAM continuam sendo melhoradas porem a um nivel muito abaixo das velocidades de processamentos das CPUs, assim atrapalhando o rendimento total, a solucao foi implementar uma memoria temporaria entre a RAM e os registradores, com baixa latency e velocidade extremamente alta, muitas vezes em paralelo para aumentar ainda mais os seus beneficios.
Incorretas = b,c,d, visto que o cache foi projetado para ser o mais rapido possivel

3. Interrupts are provided primarily as a way to

a. Improve processor utilization
b. Improve processor execution
c. Improve processor control
d. Improve processor speed

Correta = a, como descrito em 5.6.5 na pagina 414 [1], as interrupcoes alteram o fluxo de controle quando por exemplo um processo eh finalizado, a CPU entao acha um novo processo por via do vector de interrupcao, diminuindo assim os ciclos onde o processador esta idle, aumentando a utilizacao.
Incorretas = b,c e d, Interrupcao nao afeta essas outras variaveis

4. Program counter contains the address of the

a. Next programs to be fetched
b. Previous programs to be fetched
c. Previous information to be fetched
d. Next information to be fetched

Correta = d, como descrito no passo 6 de "Hardware Actions" na pagina 415 [1], o program counter aponta para a proxima informacao.
Incorreta = a, como descrito no mesmo passo, o program counter nao apontara nescessariamente para uma aplicacao, no exemplo dado ele apontaria para uma rotina de servicos provenientes do dispositivo causando a interrupcao.
Incorretas = b e c, nao achei mencao em [1] de backtracking/backlogging nescessario para retonar em processos anteriores.

5. Cache size issue can have significant impact on

a. input
b. output
c. Information
d. Performance

Correta = d, dito no quarto paragrafo da pagina 84 [1], performance esta positivamente relacionada ao tamanho do cache
Incorretas = a e b, como descrito no mesmo paragrafo, quanto maior o cache, cria-se o problema de maior o custo de acesso
Incorreta = c, tamanho do cache nao afeta a informacao nele contida

6. Data and instructions that are being used frequently are stored in

a. Cache
b. Block
c. hard disk
d. main memory

Correta = b, como descrito no terceiro paragrafo da pagina 84, as memorias sao subdevididas em blocos, no caso de cache
Incorreta = a, como descrito na pagina 83 [1], eh usado para manter dados de rapido acesso
Incorreta = c, como dito na pagina 86, esse tipo de memoria eh extremamente lenta (porem de maior capacidade), comparada com as de nivel acima, nao seria usado para data e instrucoes de acesso frequente
Incorreta = d, abstracao que inclui outros tipos de memoria como visto no capitulo 2

7. In implementation of Semaphores, for a single processor system, it is possible to inhibited

a. Deadlock
b. Interrupts
c. Lock Step
d. None

Correta = b, no segundo capitulo da pagina 480 [1] o autor cita o "truque" que funciona somente para sistemas com um unico processador, ao desabilitar os interrupts, assim o processador deve terminar um processo antes de comecar o outro

8. Time sharing technique handles

a. Single Interactive Job
b. Multiple Interactive Job
c. Recent Interactive Job
d. Old Interactive Job

Correta = b, como mencionado em "Introduction to Scheduling" na pagina 150 [2] timesharing eh uma das tecnicas utilizadas para gerenciar multiplos programas

9.  With the use of multiprogramming batch processing work can be

a. Efficient
b. Rigid
c. Expensive
d. Flexible

Correta = a, Descrito em "introduction to Scheduling" na pagina 150 [2] a multiprogramacao lida com o fato de escalonador dever tratar requsicoes de multiplos usuarios.


11. With Microkernel architecture it is possible to handle hardware interrupts as

a. Application
b. Information
c. Data
d. Message

Correta = d, em "Microkernels" quarto paragrafo da pagina 66, foi citado a possivel comunicacao entre processos utilizando interrupts

11. The owner of an address space can grant a number of its

a. Modules
b. Pages
c. Devices
d. Computers

Correta = b, em "Memory-Mapped I/O" na pagina 342 [2] o autor explica que com memoria mapeada nao ha nescessidade de mecanismos de protecao externos para impedir que usuarios performem I/O, cada usuario tem acesso a sua tabela de paginas.

12. A common synchronization mechanism used in multiprocessor operating system is

a. Complex
b. Locks
c. Lockstep
d. None

Correta = b, em "Multiprocessor Synchronization" pagina 535 [2] o autor cita o uso da syscronizacao por bloqueio

13. I/O interrupt-driven is more efficient than

a. I/O Modules
b. I/O Devices
c. Programmed I/O
d. CPU

Correta = c, em 5.2.2 "Programmed  I/O" na pagina 252 [2] o autor cita que que entrada e saida programada eh a forma mais simples de I/O, onde a CPU faz todo o trabalho

14. I/O modules performs the requested action on

a. Programmed I/O
b. Direct Memory Access (DMA)
c. Interrupt driven I/O
d. I/O devices

Correta = a, em "Modules in Linux" na pagina 755 [2] o autor cita o funcionamento do Programmed I/O ao checar periodicamente ate o fim da operacao

15. Secure system concerned with protecting the system against

a. User
b. Security
c. Interruption
d. Damage

Correta = c, em 9.4 "Formal Models of Secures Systems" na pagina 611 [2] o autor explica como eh usada a matrix de protecao para gerencial qual o proximo passo de um processo no dominio determinado

16. The concept of process for the structure of operating system is

a. Fundamental
b. Effective
c. Old
d. Modern

Correta = a, (e b) em 1.5.1 "Processes" na pagina 39 [2], o autor define processos como um "conceito chave", fundamentalmente nescessario para conter toda informacao nescessaria para execucao de um programa. 

17. Thread is a dispatch able unit of

a. Program
b. Work
c. Time
d. Process

Correta = a, em 2.2.1 "Thread Usage" na pagina 97 [2] o autor explica a razao para a multiplicidade das threads e como sao facilmente destruidas pelos seus processos pais

18. In processes, access control implements a

a. Security Policy
b. Access Policy
c. Control Policy
d. Check Policy

Correta = a, em 9.3.2 na pagina 605 e 606 eh ilustrada a lista de controle de acesso, supostamente com as funcoes das outras alternativas inclusas

19. Cache manager improves the performance of

a. Programmed I/O
b. File base I/O
c. I/O device
d. I/O Modules

Correta = b, em 11.6 "Caching in Windows" na pagina 942 [2] o autor confirma que o cache melhora a performance dos sistemas de arquivos, mantendo os arquivos de uso recente e frequente em memoria, em especifico em NTFS como ele armazena todos os dados como arquivos, incluindo a metadata do file system

20. Process is a collection of

a. Threads
b. Files
c. Registers
d. Buffers

Correta = a, em 2.2 "Threads" na pagina 97 [2], o autor cita que em sistemas operacionais tradicionais cada processo tem somente uma thread, porem em muitas situacoes ter multiplos threads eh algo favoravel
Incorreta = b, como descrito nas paginas 41 e 42 [2] arquivos sao tratados pelo file system
Incorreta = c, descrito em 3.3.3 "Registers" na pagina 174 [1] registradores sao items de memoria