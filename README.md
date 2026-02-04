# 🛡️ Simulação Educacional de Ransomware (Projeto: Isca Free Robux)

> ⚠️ **AVISO LEGAL: PROJETO ESTRITAMENTE EDUCACIONAL**
>
> Este software foi desenvolvido para fins acadêmicos no curso de **Engenharia de Computação**. O objetivo é demonstrar na prática os conceitos de Criptografia Simétrica e Engenharia Social.
>
> **NÃO** execute este código em máquinas de terceiros sem autorização. A autora não se responsabiliza pelo uso indevido desta ferramenta.

## 📖 Sobre o Projeto

Este projeto simula um ataque de **Ransomware** disfarçado de gerador de moedas para jogos (Robux). Ele ilustra as duas etapas principais de uma infecção por Trojan:

1.  **A Isca (Frontend):** Uma interface de linha de comando (CLI) atrativa, criada com a biblioteca `rich`, que promete benefícios falsos para enganar o usuário.
2.  **O Payload (Backend):** Um script oculto que utiliza criptografia **AES (Fernet)** para bloquear arquivos em uma pasta alvo específica.

## 📚 Referências e Inspiração

Este projeto foi baseado em estudos de Segurança Ofensiva e Referências Técnicas:

* **[Vídeo] FIZ UM MALWARE** - Canal *DEPRE*: [Assistir no YouTube](https://youtu.be/4pobgFPm19c?list=PLAaIJOs2LYLil4yLjwO5ITnZ0MH_GpGa9)
    > *Fonte primária para a lógica de criptografia e estruturação do script.*

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3.12+
* **Interface Visual:** [Rich](https://github.com/Textualize/rich) (Cores, Tabelas, Layouts).
* **Segurança:** [Cryptography](https://pypi.org/project/cryptography/) (Algoritmo Fernet/AES).
* **Automação:** Scripts Batch (`.bat`) para execução facilitada.

## ⚙️ Estrutura dos Arquivos

| Arquivo | Descrição |
| :--- | :--- |
| `GanheAqui.bat` | **Início da Simulação.** Executável que lança a isca para o usuário. |
| `free.py` | Script da interface gráfica (Engenharia Social) que distrai a vítima. |
| `cript.py` | O Malware. Localiza a pasta alvo e criptografa os arquivos. |
| `descript.bat` | **A Solução.** Executável para recuperar os arquivos. |
| `descript.py` | Script que lê a `chave.key` e descriptografa os dados. |
| `chave.key` | Arquivo gerado automaticamente contendo a chave de criptografia. |

## 🚀 Como Executar (Ambiente de Teste)

1.  **Instale as dependências:**
    ```bash
    pip install rich cryptography
    ```

2.  **Prepare o Ambiente:**
    * Certifique-se de que existe uma pasta de teste configurada no script (para não criptografar seus arquivos pessoais por engano).

3.  **Para "Atacar":**
    * Execute o arquivo `GanheAqui.bat`.
    * Siga as instruções na tela e aguarde a mensagem final.

4.  **Para Recuperar:**
    * Execute o arquivo `descript.bat`.

---
**Desenvolvido por [Alwenny] - Engenharia de Computação**
