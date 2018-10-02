import src.tsp as tsp
import src.directedgraph as d_graph
import time


def run_rsp_solution():
    rsp = tsp.RSP()
    while True:
        entry = rsp.get_next_key()
        success = rsp.is_success(entry)
        if success is None:
            rsp.update_memory(entry)
            continue
        break
    print("[Output] The shortest solution for this TSP problem is : " + str(success.cost))
    print("[Output] The path for the solution is: ")
    print("[Output] ", end="")
    for state in success.path:
        print("->", end="")
        print(state, end="")


def run_directed_graph_solution():
    input_graph = d_graph.DirectedGraph.generate_graph()
    graph = d_graph.DirectedGraph(input_graph)
    path = graph.find_path()
    print("[Output] The shortest path for the two link is: ")
    print("[Output] ", end="")
    for p in path:
        print("->", end="")
        print(p, end="")
    print()


if __name__ == "__main__":
    start_time = time.time()
    # run_rsp_solution()
    run_directed_graph_solution()
    elapsed = (time.time() - start_time) * 1000
    print("[Output] The process time: " + str(elapsed) + "ms")
