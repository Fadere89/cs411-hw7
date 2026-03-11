

# We will implement Dijkstra's Algorithm
# First we'll need a min heap
import heapq as hq;

# the algorithm goes by filling the min heap with the nodes that are touching the starting node
# then we'll add all other nodes with infinite distance
# and checking the neighbors of the node in the top of the queue.




# so we'll start with our graph
graph = [[1, 2, 4], # (1)->(2) with weight 4
         [1, 3, 2],
         [2, 4, 2],
         [2, 3, 3],
         [2, 5, 3],
         [3, 2, 1],
         [3, 4, 4],
         [3, 5, 5],
         [5, 4, 1]
         ];
# https://www.youtube.com/watch?v=_lHSawdgXpI <- reference graph for test

def print_matrix(matrix):
    for row in matrix:
        print(row);

def left_child(index):
    return 2 * index + 1;

def right_child(index):
    return 2 * index + 2;

def adjacency_list(graph):
    # we'll want to create an adjacency list
    # even though this takes extra storage, it makes computation must smoother later

    # find the amount of nodes, O(|E|) by E = {edges}
    # we'll just search for the highest numbered node in our graph
    highest_indexed_node = 0;
    for edge in graph:
        canidate_1 = edge[0];
        canidate_2 = edge[1];
        if (canidate_1 > highest_indexed_node):
            highest_indexed_node = canidate_1;
        if (canidate_2 > highest_indexed_node):
            highest_indexed_node = canidate_2;

    # now that we have found the higest node, we'll create the adjacency list
    # O(|N|^2) by N = {nodes}
    adj_list = [];
    for i in range(highest_indexed_node + 1):
        row = [];
        for j in range(highest_indexed_node + 1):
            row.append(0);
        adj_list.append(row);

    # now we'll just populate the adjacency list
    for edge in graph:
        x = edge[0]; # we're going from x to y
        y = edge[1];
        weight = edge[2];
        adj_list[x][y] = weight;

    return adj_list;

def push_adj(heap, graph, adj_list, init_node, inf):
    # Now, we'll populate the heap with the adjacent notes to our starting node
    trans_node = 1; # the index of the node we're pointing to
    n = len(adj_list[init_node]); # how many nodes to check
    adj_row = adj_list[init_node];
    while trans_node < n:
        weight = adj_row[trans_node];
        if weight != 0: # if there's an edge
            if (inf != False):
                weight = inf;
            hq.heappush(heap, (weight, init_node, trans_node)); # it's important the weight goes first, so our heap functions properly
        trans_node += 1;

def dijkstra_search(graph, start_node, terminal_node):
    adj_list = adjacency_list(graph);
    h = [];
    push_adj(h, graph, adj_list, start_node, False); # make our inital adjacency list and heap
    inf = 0; # we'll also get an infinity value
    for edge in graph:
        inf += edge[2];
    
    terminal_path_exists = False; # assume this is false and only follow through with the algorithm
    # if the path exists
    for edge in h:
        trans_node = edge[2]
        push_adj(h, graph, adj_list, trans_node, inf) # push all neighbors neighbors
        if trans_node == terminal_node:
            terminal_path_exists = True;
            break; # stop as soon as we add the terminal node
    if not terminal_path_exists:
        return -1;
    
    # from here, we just need to do the actual searching.

    print(h);
    print_matrix(adj_list);

dijkstra_search(graph, 1, 3);