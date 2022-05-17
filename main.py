# TP01 - AEDS 3
# Vitor Marques dos Santos - 20.2.8175
# Diogo Leite Lucas - 20.2.8072

# Linha para importação e utilização da classe grafos
import grafos

#Declaração de um objeto do tipo 'Grafo'
g1=grafos.Grafo()

print("**** Arquivos **** \n")
print("toy.txt")
print("rg300_4730.txt")
print("rome99c.txt")
print("facebook_combined.txt")
print("USA-road-dt.DC.txt")
print("USA-road-dt.NY.txt")
print("web-Google.txt")

# Linha para pegar as vaiáveis utilizadas durante a execução

nome=input("\nInforme o nome do arquivo:")

origem=int(input("Informe o vertice de origem:"))

destino=int(input("Informe o vertice de destino:"))

g1.menu(nome,origem,destino) # Chamada de função com passagem dos parâmetros



