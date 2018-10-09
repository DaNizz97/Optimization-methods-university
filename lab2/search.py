from lab2.const import (
    graph,
    start,
    end,
)


shortest_way = {}
node_stack = []

node = start
while True:

    for curr_node in graph[node]:
        node_stack.append(curr_node)

        if curr_node in node_stack:
            pass
        else:
            shortest_way[curr_node] = []