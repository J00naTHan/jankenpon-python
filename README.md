# Python Terminal JanKenPon with Python

---
## Language: En

### Introduction
This project consists of a simplified *jankenpon* game, using the **object-driven paradigm** in **python**. The game has a **single gamemode**, which is **player X AI**, using a pretty simple AI to simulate an opponent in matches.

### Details
Each **run** consists of a **single match** in the **best of three** format or until there's a winner, creating new rounds while the game is **tied**. The player starts inputting his **name**, and then choosing between the **three options** of a *jankenpon* game (rock, paper and scissor), the AI chooses an option too, and lastly the winner is decided.

### Implementation
The player and the AI are defined as **subclasses** of an superclass that implements almost all the **attributes** and **methods**.
The game itself is made using **iterative** code blocks, starting with the initialization of the AI, followed by an `while` loop **validating** the `input` for the **player's name**. Then there's other `while` loop, this loop **creates new turns** based on a **counter** for turns played. Each turn takes care of the **terminal UI** and the general process of each turn, defining the **player's choice** and calling the following methods:
- **Duel** (`duel`): receives the player and AI data and validates both to define which one is winning. This method is used to define the winner.
- **Scoreboard** (`scoreboard`): takes the data of the player, the AI and the actual state of the match (if it's the last turn or not) and renderizes in the terminal a scoreboard template.

---
## Language: Pt-Br

### Introdução
Este projeto consiste de um jogo de *jankenpon* simplificado, utlilizando **paradigma** de **orientação a objetos** na linguagem *python*. O jogo possui um **único modo de jogo**, que é **jogador X IA**, usando uma IA extremamente simples para simular um adversário para a partida.

### Funcionamento
W.I.P

### Implementação
W.I.P