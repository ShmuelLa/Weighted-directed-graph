from src.GraphAlgo import GraphAlgo
import networkx as nx
import datetime
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


def test_time1():
    node_a = 5
    node_b = 2
    graph = GraphAlgo()
    file = "../data/Graphs_on_circle/G_10_80_1.json"
    graph.load_from_json(file)
    g_nx = nx.Graph()
    for i in graph.get_graph().get_all_v().keys():
        g_nx.add_node(i)
    for k, v in graph.get_graph().get_all_v().items():
        for node_id, w in graph.get_graph().all_out_edges_of_node(k).items():
            g_nx.add_edge(k, node_id, weight=w)
    print("[-] Test for G_10_80_1.json \n")
    nx_start = datetime.datetime.now()
    nx.shortest_path(g_nx, node_a, node_b)
    nx.shortest_path(g_nx, node_b, node_a)
    nx_end = datetime.datetime.now()
    nx_time = (nx_end - nx_start)
    print("[-] Networkx time in shortest path is: ", nx_time)
    nx_start = datetime.datetime.now()
    nx.connected_components(g_nx)
    nx_end = datetime.datetime.now()
    nx_time = (nx_end - nx_start)
    print("[-] Networkx time in get components is: ", nx_time)
    my_start = datetime.datetime.now()
    graph.shortest_path(node_a, node_b)
    graph.shortest_path(node_b, node_a)
    my_send = datetime.datetime.now()
    my_time = (my_send - my_start)
    print("[-] Our time in shortest path is: ", my_time)
    my_start = datetime.datetime.now()
    graph.connected_components()
    my_send = datetime.datetime.now()
    my_time = (my_send - my_start)
    print("[-] Our time in get components is: ", my_time)
    print("[-] G_10_80 has finished! \n")


def test_time2():
    node_a = 98
    node_b = 36
    graph = GraphAlgo()
    file = "../data/Graphs_on_circle/G_100_800_1.json"
    graph.load_from_json(file)
    g_nx = nx.Graph()
    for i in graph.get_graph().get_all_v().keys():
        g_nx.add_node(i)
    for k, v in graph.get_graph().get_all_v().items():
        for node_id, w in graph.get_graph().all_out_edges_of_node(k).items():
            g_nx.add_edge(k, node_id, weight=w)
    print("[-] Test for G_100_800_1.json")
    nx_start = datetime.datetime.now()
    nx.shortest_path(g_nx, node_a, node_b)
    nx.shortest_path(g_nx, node_b, node_a)
    nx_end = datetime.datetime.now()
    nx_time = (nx_end - nx_start)
    print("[-] Networkx time in shortest path is: ", nx_time)
    nx_start = datetime.datetime.now()
    nx.connected_components(g_nx)
    nx_end = datetime.datetime.now()
    nx_time = (nx_end - nx_start)
    print("[-] Networkx time in get components is: ", nx_time)
    my_start = datetime.datetime.now()
    graph.shortest_path(node_a, node_b)
    graph.shortest_path(node_b, node_a)
    my_send = datetime.datetime.now()
    my_time = (my_send - my_start)
    print("[-] Our time in shortest path is: ", my_time)
    my_start = datetime.datetime.now()
    graph.connected_components()
    my_send = datetime.datetime.now()
    my_time = (my_send - my_start)
    print("[-] Our time in get components is: ", my_time)
    print("[-] G_100_800 has finished! \n")


def test_time3():
    node_a = 152
    node_b = 93
    graph = GraphAlgo()
    file = "../data/Graphs_on_circle/G_1000_8000_1.json"
    graph.load_from_json(file)
    g_nx = nx.Graph()
    for i in graph.get_graph().get_all_v().keys():
        g_nx.add_node(i)
    for k, v in graph.get_graph().get_all_v().items():
        for node_id, w in graph.get_graph().all_out_edges_of_node(k).items():
            g_nx.add_edge(k, node_id, weight=w)
    print("[-] Test for G_1000_8000_1.json")
    nx_start = datetime.datetime.now()
    nx.shortest_path(g_nx, node_a, node_b)
    nx.shortest_path(g_nx, node_b, node_a)
    nx_end = datetime.datetime.now()
    nx_time = (nx_end - nx_start)
    print("[-] Networkx time in shortest path is: ", nx_time)
    nx_start = datetime.datetime.now()
    nx.connected_components(g_nx)
    nx_end = datetime.datetime.now()
    nx_time = (nx_end - nx_start)
    print("[-] Networkx time in get components is: ", nx_time)
    my_start = datetime.datetime.now()
    graph.shortest_path(node_a, node_b)
    graph.shortest_path(node_b, node_a)
    my_send = datetime.datetime.now()
    my_time = (my_send - my_start)
    print("[-] Our time in shortest path is: ", my_time)
    my_start = datetime.datetime.now()
    graph.connected_components()
    my_send = datetime.datetime.now()
    my_time = (my_send - my_start)
    print("[-] Our time in get components is: ", my_time)
    print("[-] G_1000_8000 has finished! \n")


def test_time4():
    node_a = 2841
    node_b = 9977
    graph = GraphAlgo()
    file = "../data/Graphs_on_circle/G_10000_80000_1.json"
    graph.load_from_json(file)
    g_nx = nx.Graph()
    for i in graph.get_graph().get_all_v().keys():
        g_nx.add_node(i)
    for k, v in graph.get_graph().get_all_v().items():
        for node_id, w in graph.get_graph().all_out_edges_of_node(k).items():
            g_nx.add_edge(k, node_id, weight=w)
    print("[-] Test for G_10000_80000_1.json")
    nx_start = datetime.datetime.now()
    nx.shortest_path(g_nx, node_a, node_b)
    nx.shortest_path(g_nx, node_b, node_a)
    nx_end = datetime.datetime.now()
    nx_time = (nx_end - nx_start)
    print("[-] Networkx time in shortest path is: ", nx_time)
    nx_start = datetime.datetime.now()
    nx.connected_components(g_nx)
    nx_end = datetime.datetime.now()
    nx_time = (nx_end - nx_start)
    print("[-] Networkx time in get components is: ", nx_time)
    my_start = datetime.datetime.now()
    graph.shortest_path(node_a, node_b)
    graph.shortest_path(node_b, node_a)
    my_send = datetime.datetime.now()
    my_time = (my_send - my_start)
    print("[-] Our time in shortest path is: ", my_time)
    my_start = datetime.datetime.now()
    graph.connected_components()
    my_send = datetime.datetime.now()
    my_time = (my_send - my_start)
    print("[-] Our time in get components is: ", my_time)
    print("[-] G_10000_80000 has finished! \n")


def test_time5():
    node_a = 17533
    node_b = 4974
    graph = GraphAlgo()
    file = "../data/Graphs_on_circle/G_20000_160000_1.json"
    graph.load_from_json(file)
    g_nx = nx.Graph()
    for i in graph.get_graph().get_all_v().keys():
        g_nx.add_node(i)
    for k, v in graph.get_graph().get_all_v().items():
        for node_id, w in graph.get_graph().all_out_edges_of_node(k).items():
            g_nx.add_edge(k, node_id, weight=w)
    print("[-] Test for G_20000_160000_1.json")
    nx_start = datetime.datetime.now()
    nx.shortest_path(g_nx, node_a, node_b)
    nx.shortest_path(g_nx, node_b, node_a)
    nx_end = datetime.datetime.now()
    nx_time = (nx_end - nx_start)
    print("[-] Networkx time in shortest path is: ", nx_time)
    nx_start = datetime.datetime.now()
    nx.connected_components(g_nx)
    nx_end = datetime.datetime.now()
    nx_time = (nx_end - nx_start)
    print("[-] Networkx time in get components is: ", nx_time)
    my_start = datetime.datetime.now()
    graph.shortest_path(node_a, node_b)
    graph.shortest_path(node_b, node_a)
    my_send = datetime.datetime.now()
    my_time = (my_send - my_start)
    print("[-] Our time in shortest path is: ", my_time)
    my_start = datetime.datetime.now()
    graph.connected_components()
    my_send = datetime.datetime.now()
    my_time = (my_send - my_start)
    print("[-] Our time in get components is: ", my_time)
    print("[-] G_20000_160000 has finished! \n")


def test_time6():
    node_a = 4975
    node_b = 29567
    graph = GraphAlgo()
    file = "../data/Graphs_on_circle/G_30000_240000_1.json"
    graph.load_from_json(file)
    g_nx = nx.Graph()
    for i in graph.get_graph().get_all_v().keys():
        g_nx.add_node(i)
    for k, v in graph.get_graph().get_all_v().items():
        for node_id, w in graph.get_graph().all_out_edges_of_node(k).items():
            g_nx.add_edge(k, node_id, weight=w)
    print("[-] Test for G_3000_240000_1.json")
    nx_start = datetime.datetime.now()
    nx.shortest_path(g_nx, node_a, node_b)
    nx.shortest_path(g_nx, node_b, node_a)
    nx_end = datetime.datetime.now()
    nx_time = (nx_end - nx_start)
    print("[-] Networkx time in shortest path is: ", nx_time)
    nx_start = datetime.datetime.now()
    nx.connected_components(g_nx)
    nx_end = datetime.datetime.now()
    nx_time = (nx_end - nx_start)
    print("[-] Networkx time in get components is: ", nx_time)
    my_start = datetime.datetime.now()
    graph.shortest_path(node_a, node_b)
    graph.shortest_path(node_b, node_a)
    my_send = datetime.datetime.now()
    my_time = (my_send - my_start)
    print("[-] Our time in shortest path is: ", my_time)
    my_start = datetime.datetime.now()
    graph.connected_components()
    my_send = datetime.datetime.now()
    my_time = (my_send - my_start)
    print("[-] Our time in get components is: ", my_time)
    print("[-] G_30000_240000 has finished! \n")


def plot_results():
    labels = ['Shortest Path', 'Connected Components']
    java = [1.983, 1.819]
    python = [2.276, 1.980]
    networkx = [0, 0.941]
    x = np.arange(len(labels))
    width = 0.2
    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width / 2, java, width, label='Java')
    rects2 = ax.bar(x + width / 2, python, width, label='Python')
    rects3 = ax.bar(x + 3*width / 2, networkx, width, label='Networkx')
    ax.set_ylabel('Runtime in seconds')
    ax.set_xlabel('Graphs by size ->')
    ax.set_title('Runtime by library')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    def autolabel(rects):
        """Attach a text label above each bar in *rects*, displaying its height."""
        for rect in rects:
            height = rect.get_height()
            ax.annotate('{}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height), xytext=(0, 3),
                        textcoords="offset points", ha='center', va='bottom')

    autolabel(rects1)
    autolabel(rects2)
    autolabel(rects3)
    fig.tight_layout()
    plt.show()


if __name__ == '__main__':
    test_time1()
    test_time2()
    test_time3()
    test_time4()
    test_time5()
    test_time6()
    plot_results()
