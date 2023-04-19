import networkx as nx
import matplotlib.pyplot as plt
import pickle

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        with open("nos.pkl", "rb") as f:
            nos = pickle.load(f)
        self.nos = nos
        with open("grafo.pkl", "rb") as f:
            grafo = pickle.load(f)
        self.grafo = grafo

    def adicionar_aresta(self, inicio, fim, peso):
        self.grafo.append([inicio, fim, peso])

    def mostrar_estacoes(self, distancia, origem):
        distancias = ""
        for chave, valor in distancia.items():
            if valor != float("Inf") and valor != 0:
                distancias += f"{origem} ---> {chave}: {valor:.2f} Km\n"
        return distancias

    def bellman_ford(self, inicio, fim):
        # Inicializa as distâncias e predecessores de todos os nós
        distancias = {no: float('inf') for no in self.nos}
        predecessores = {no: None for no in self.nos}
        distancias[inicio] = 0

        # Relaxa as arestas repetidamente
        for i in range(len(self.nos) - 1):
            for u, v, peso in self.grafo:
                try:
                    if distancias[u] + peso < distancias[v]:
                        distancias[v] = distancias[u] + peso
                        predecessores[v] = u
                except:
                    pass

        # Verifica se há ciclos negativos
        for u, v, peso in self.grafo:
            try:
                if distancias[u] + peso < distancias[v]:
                    raise ValueError("O grafo contém um ciclo negativo")
            except:
                pass

        # Constrói o trajeto a partir dos predecessores
        trajeto = [fim]
        no_atual = fim
        while predecessores[no_atual] is not None:
            trajeto.insert(0, predecessores[no_atual])
            no_atual = predecessores[no_atual]

        # Retorna a distância mais curta e o trajeto
        return f'{inicio} ---> {fim} : {distancias[fim]:.2f}', trajeto

    def plotar_subgrafo(self, mDistancia, mPercurso, mOption):
        if mOption == 1:
            # Executa o algoritmo Bellman-Ford
            distancia, trajeto = mDistancia, mPercurso

            # Cria um subgrafo que contém apenas os nós e as arestas no trajeto
            subgrafo = nx.DiGraph()
            for no in trajeto:
                subgrafo.add_node(no)
            for u, v, peso in self.grafo:
                if u in trajeto and v in trajeto:
                    subgrafo.add_edge(u, v, weight=peso)

            # Define o layout do grafo
            pos = nx.spring_layout(subgrafo)

            # Desenha o subgrafo com as arestas e os pesos
            nx.draw(subgrafo, pos, with_labels=True, node_color='lightblue', node_size=800, font_size=12)
            labels = nx.get_edge_attributes(subgrafo, 'weight')
            nx.draw_networkx_edge_labels(subgrafo, pos, edge_labels=labels, font_size=10)

            # Adiciona um título com a distância mais curta
            #plt.title('Distância mais curta: {:.2f}'.format(distancia))
            plt.title('Distância mais curta')

            # Mostra o gráfico
            plt.show()
        else:
            pass

        print(44 * '*')
        print("     Obrigado por usar nossos serviços!")
        print(44 * '*')
grafo = Graph(214)

def toquioMetro():
    pontoInicio = input('Digite a primeira estação: ')
    pontoFim = input('Digite a segunda estação: ')

    distancia, percurso = grafo.bellman_ford(pontoInicio, pontoFim)

    print(42*'=')
    print('Seu percurso será: ')
    for i in percurso:
        print(i)
    print(distancia)
    print(42*'=')

    menu2 = int(input('''
    VOCÊ QUER EXIBIR O SEU CAMINHO?
    [SIM(1)] [NÃO(2)]: '''))
    grafo.plotar_subgrafo(distancia, percurso, menu2)

menu = f'''
{42*'='}
       BEM VINDO AO METRO DE TÓQUIO
    FAREMOS O MELHOR TRAJETO PARA VOCÊ
{42*'='}
    '''
print(menu)

toquioMetro()
