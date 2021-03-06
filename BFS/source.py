from queue import Queue

MAX = 100
V = None
E = None
visited = [False for i in range(MAX)]
path = [0 for i in range(MAX)]
graph = [[] for i in range(MAX)]


def BFS(s):
    for i in range(V):
        visited[i] = False
        path[i] = -1

    q = Queue()
    visited[s] = True
    q.put(s)

    while not q.empty():
        u = q.get()
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                path[v] = u
                q.put(v)


def printPath(s, f):
    b = []
    if f == s:
        print(s)
        return
    if path[f] == -1:
        print("No path")
        return

    while True:
        b.append(f)
        f = path[f]
        if f == s:
            b.append(s)
            break

    for i in range(len(b) - 1, -1, -1):
        print(b[i], end=" ")


def printPathRecursion(s, f):
    if f == s:
        print(f, end=" ")
    else:
        if path[f] == -1:
            print("No path")
        elif:
            printPathRecursion(s, path[f])
            print(f, end=" ")


if __name__ == "__main__":
