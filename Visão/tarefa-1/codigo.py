import os

caminho = "labels"
novo_caminho = "labels_new"

# Criar a pasta labels_new se ela não existir
if not os.path.exists(novo_caminho):
    os.makedirs(novo_caminho)

# Entrar na pasta
os.chdir(caminho)

# Percorrer labels
for arquivo in os.listdir():
    if arquivo.endswith('.txt'):
        with open(arquivo, "r") as label:
            linhas = label.readlines()

        # Trocar 0 por 1
        novo_nome = "new_" + arquivo  # Novo nome do arquivo
        with open(os.path.join("..", novo_caminho, novo_nome), "w") as novo_label:
            for i in linhas:
                if i.startswith('0'):
                    i = "1" + i[1:]
                novo_label.write(i)

os.chdir("..")
