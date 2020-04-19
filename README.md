# Game Invasão Alienígena

Jogo de plataforma tem como objetivo não deixar as espaçonaves chegarem ao inferior da tela ou colidir com a nave principal. Conforme o jogador vai destruindo todas as espaçonaves alienígenas, a mudança de level ocorre, aumentando assim a velocidade do jogo a cada level. O Jogo possui por padrão 3 vidas, que são indicadas no canto superior esquerdo. No canto superior direito, tem as indicações de pontuação e level que o jogador está no momento, e no centro da tela é sua melhor pontuação.

![](jogo.gif)

## Instalação

Considerando que você ja tenha Python e o gerenciador de pacotes Python __pip__ intalados, seguimos com as instruções para a instalação do jogo.

Para o funcionamento do jogo, é necessário a instalação da biblioteca PyGame, que é usada para construção de jogos em Python.

Esta biblioteca pode ser instalada com o comando a seguir:

### Linux:

```$ sudo apt-get install python-pygame```

No linux, o pygame depende de algumas bibliotecas para o jogo funcionar corretamente:

```$ sudo apt-get install python-dev mercurial```
```$ sudo apt-get install libsdl-image1.2-dev libsdl2-dev libsdl-ttf2.0-dev```

Agora instale o pygame usando o seguinte comando:

```$ pip install --user hg+http://bitbucket.org/pygame/pygame```

### Windows:

```python -m pip install --user pygame-1.9.2a0-cp35-none-win32.whl```

Para testar a instalação, execute uma sessão de terminal Python e experimente importar o PyGame.

    $ python
    >>> import pygame
    >>>

Se isso funcionar, a biblioteca foi instalada com sucesso.

Logo após ter instalado a biblioteca devemos clonar este repositório:

```$git clone https://github.com/lucasmcast/invasao_alienigena.git```

Para jogar, basta direcionar para a pasta do repositório clonado e executar o módulo alien_invasion.py:

    $ cd invasão_alienigena
    $ python alien_invasion.py




