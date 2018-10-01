import tsp
import time

if __name__ == "__main__":
    start_time = time.time()
    rsp = tsp.RSP()
    memory = rsp.memory
    while True:
        entry = rsp.get_next_key()
        success = rsp.is_success(entry)
        if success is None:
            rsp.update_memory(entry)
            continue
        break
    elapsed = (time.time() - start_time) * 1000
    print("[Output] The process time: " + str(elapsed) + "ms")
    print("[Output] The shortest solution for this TSP problem is : " + str(success.cost))
    print("[Output] The path for the solution is: ")
    print("[Output] ", end="")
    for state in success.path:
        print("->", end="")
        print(state, end="")
