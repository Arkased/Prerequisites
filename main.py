import pickle
import sys
import networkx

if len(sys.argv) == 1:
    name = input("Name the graph.\n")
    graph = networkx.DiGraph()

elif len(sys.argv) == 2:
    name = sys.argv[1]
    with open(name, 'rb') as f:
        graph = pickle.load(f)

else:
    print('too many arguments')
    exit(1)


def add_tech(tech: str, prereqs=None):
    if prereqs is None:
        prereqs = []

    if graph.has_node(tech):
        print(f'DAG already has {tech}')
        return
    else:
        graph.add_node(tech, acquired=False)
        add_prereqs(tech, prereqs)
        print(f'added {tech} with prereqs {prereqs}')


def add_prereq(tech: str, prereq: str):
    if not graph.has_node(prereq):
        print(f'{prereq} is not listed in graph yet')
    elif graph.has_edge(prereq, tech):
        print(f'{prereq} is already a prerequisite of {tech}')
    else:
        graph.add_edge(prereq, tech)
        print(f'added {prereq} as a prerequisite of tech')


def add_prereqs(tech: str, prereqs: list):
    for prereq in prereqs:
        add_prereq(tech, prereq)


def acquire_tech(tech):
    if graph.nodes[tech]['acquired']:
        print(f'{tech} already acquired')
    else:
        graph.nodes[tech]['acquired'] = True
        print(f'acquired {tech}')


def remove_tech(tech):
    if not graph.nodes[tech]['acquired']:
        print(f'{tech} already not acquired')
    else:
        graph.nodes[tech]['acquired'] = False
        print(f'removed {tech}')


def show_graph():
    networkx.spring_layout(graph)
    networkx.draw_networkx(graph, with_labels=True)


def save_graph():
    with open(name, 'wb') as f:
        pickle.dump(graph, f)
