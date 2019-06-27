from vertex import Vertex
import csv

# Made by Otavio Bertucini / 2019

def make_graph():

    vertices = []

    # create new vertices
    with open("grafo02.csv", "rb") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=",", quotechar="|")

        for row in spamreader:
            new_vertex = Vertex(int(row[0]))
            vertices.append(new_vertex)

    # join the graphs
    with open("grafo02.csv", "rb") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=",", quotechar="|")

        for row in spamreader:
            vertex = vertices[int(row[0])-1]
            new_edges = []
            for i in range(1, len(row)):
                to_add = vertices[int(row[i]) - 1]
                new_edges.append(to_add)
            vertex.edges = new_edges

    return vertices

# returns the index of the vertex with the highest degree
def get_max_degree(vertices):

    max_degree = -1
    max_index = 0
    index = 0

    for vertex in vertices:
        if vertex.get_degree() > max_degree:
            max_index = index
            max_degree = vertex.get_degree()
        index += 1

    return max_index

# returns the index of the vertex with the highest saturation degree
def get_max_sat_degree(vertices):

    max_degree = -1
    max_index = 0
    index = 0

    for vertex in vertices:
        if vertex.get_sat_degree() > max_degree and vertex.color is None:
            max_index = index
            max_degree = vertex.get_sat_degree()
        index += 1

    return max_index

def color_vertex(vertex, colors):

    used_colors = []

    # check the used colors by the adjacent vertices
    for edge in vertex.edges:
        if edge.color is not None and edge.color not in used_colors:
            used_colors.append(edge.color)

    # if no color were used, create new one and then assign it to the vertex
    if len(used_colors) == 0 and len(colors) == 0:
        colors.append(1)
        vertex.color = 1
        change_sat_degre(vertex)
        return vertex

    for color in colors:

        if color in used_colors:
            continue

        vertex.color = color
        change_sat_degre(vertex)
        return vertex

    new_color = colors[len(colors) - 1] + 1
    vertex.color = new_color
    colors.append(new_color)
    change_sat_degre(vertex)
    return vertex

# add one to the saturation degree of all adjacent vertices of vertex
def change_sat_degre(vertex):

    for edge in vertex.edges:
        edge.sat_degree += 1

def main():

    colors = []
    colored = 0

    # create the graph
    vertices = make_graph()

    # choose the vertex with the highest degree and color it
    max_index = get_max_degree(vertices)
    vertices[max_index] = color_vertex(vertices[max_index], colors)
    colored += 1

    # continue until all vertices are colored
    while colored < len(vertices):
        max_sat_degre = vertices[get_max_sat_degree(vertices)].sat_degree
        equal_degrees = []
        for vertex in vertices:
            if vertex.sat_degree == max_sat_degre:
                equal_degrees.append(vertex)
        print(equal_degrees)
        vertex = vertices[get_max_degree(equal_degrees)]
        vertex = color_vertex(vertex, colors)

        colored += 1


    for vertex in vertices:

        print(vertex.color)


main()
