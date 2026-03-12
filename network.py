

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
         [4, 4, 4],
         [5, 4, 1],
         #[5, 7, 9]
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

def push_adj(heap, graph, adj_list, init_node, inf, visited):
    # Now, we'll populate the heap with the adjacent notes to our starting node
    trans_node = 1; # the index of the node we're pointing to
    n = len(adj_list[init_node]); # how many nodes to check
    adj_row = adj_list[init_node];
    while trans_node < n:
        weight = adj_row[trans_node];
        if weight != 0: # if there's an edge
            if (inf != False):
                weight = inf;
            hq.heappush(heap, (weight, trans_node)); # it's important the weight goes first, so our heap functions properly
            visited[trans_node] = True;
        trans_node += 1;

def update_weight(heap, node, new_weight):
    # this function just replaces the weight of the transition in our heap as specified
    i = 0;
    n = len(heap);
    while i < n:
        edge = heap[i];
        if edge[1] == node:
            heap[i] = (new_weight, node);
            return True;
        i += 1;
    return False;


def push_transitive(heap, graph, adj_list, init_node, inf, visited, adj_row_width):
    next_node = 1;
    while next_node < adj_row_width:
        if (visited[next_node]):
            next_node += 1;
            continue;
        if adj_list[init_node][next_node] != False:
            hq.heappush(heap, (inf, next_node));
            visited[next_node] = True;
            push_transitive(heap, graph, adj_list, next_node, inf, visited, adj_row_width)
        next_node += 1;
    return;     

def heap_weight(heap, node):
    i = 0;
    while i < len(heap):
        if heap[i][1] == node:
            return heap[i][0];
        i += 1;
    return;



def dijkstra_search(graph, start_node, terminal_node):
    visited = []; # list of nodes we've visited #O(|V|) space
    max_numbered_node = 0;
    for edge in graph:
        if edge[0] > max_numbered_node:
            max_numbered_node = edge[0];
        if edge[1] > max_numbered_node:
            max_numbered_node = edge[1];
    for i in range(max_numbered_node+1):
        visited.append(False);
    
    adj_list = adjacency_list(graph);
    adj_row_width = len(adj_list[0]);
    h = [];
    
    push_adj(h, graph, adj_list, start_node, False, visited); # make our inital adjacency list and heap
    inf = 0; # we'll also get an infinity value
    for edge in graph:
        inf += edge[2];
    
    init_neighbors = len(h);
    terminal_path_exists = False;
    i = 0;
    # we'll add all the achieveable nodes from this one to the queue, with infinite weight
    while i < init_neighbors:
        push_transitive(h, graph, adj_list, h[i][1], inf, visited, adj_row_width);
        i += 1;
    for edge in h:
        if edge[1] == terminal_node:
            terminal_path_exists = True;
    if not terminal_path_exists:
        return -1;

    
    # from here, we just need to do the actual searching.
    k = 0;
    n = len(h);
    while k < n: # now just go through our queue, checking all values
        # check the edge with the lowest weight
        edge = h[k];
        cur_weight = edge[0];
        cur_node = edge[1];

        # then update the weight of the next nodes that it points to
        adj_row = adj_list[cur_node];
        j = 1;
        while j < adj_row_width:
            weight2 = adj_row[j];
            if (weight2 != 0): # if there is not a path to this node then just move on
                new_weight = cur_weight + weight2; # weight of the node in the heap
                if (new_weight < heap_weight(h, j)):
                    update_weight(h, j, new_weight);
            j += 1;

        k += 1;
    
    # once our search is done, return the minimum value found for the paths that end with our terminal node
    min_weight = inf;
    for path in h:
        weight = path[0];
        cur_node = path[1];
        if cur_node == terminal_node and weight < min_weight:
            min_weight = weight;

    return min_weight;

print(graph);
print(dijkstra_search(graph, 1, 5));