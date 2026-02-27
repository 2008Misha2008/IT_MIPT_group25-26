import heapq
def my_code(n, m, s, t, edges):
    graph = [[] for x in range(n)]
    for u, v, dist in edges:
        graph[u].append((v, dist))
    dist = [float('inf')] * n
    dist[s] = 0
    parent = [None] * n
    pq = [(0, s)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, weight in graph[u]:
            new_dist = dist[u] + weight
            if new_dist < dist[v]:
                dist[v] = new_dist
                parent[v] = u
                heapq.heappush(pq, (new_dist, v))
    if dist[t] == float('inf'):
        return "Ne mogu naiti marshrut! :'("
    path = []
    c = t
    while c is not None:
        path.append(c)
        if c == s:
            break
        c = parent[c]
    path.reverse()
    return f"{dist[t]}\n{' '.join(map(str, path))}"

def test_gps_cases():
    tests = [
        # Тест 1:
        {
            "n": 8, "m": 8, "s": 0, "t": 7,
            "edges": [(0,1,600),(0,2,1200),(1,3,800),(2,3,400),(2,4,700),(3,5,500),(4,5,300),(5,7,900)],
            "answer": "2800\n0 1 3 5 7"
        },
        # Тест 2:
        {
            "n": 4, "m": 3, "s": 0, "t": 3,
            "edges": [(0,1,1),(1,2,1),(0,2,10)],
            "answer": "Ne mogu naiti marshrut! :'("
        },
        # Тест 3:
        {
            "n": 4, "m": 4, "s": 0, "t": 3,
            "edges": [(0,1,4),(0,3,12),(1,2,3),(2,3,5)],
            "answer": "12\n0 3"
        },
        # Тест 4:
        {
            "n": 1, "m": 0, "s": 0, "t": 0,
            "edges": [],
            "answer": "0\n0"
        },
        # Тест 5:
        {
            "n": 3, "m": 3, "s": 0, "t": 2,
            "edges": [(0,1,5),(0,2,12),(1,2,3)],
            "answer": "8\n0 1 2"
        }
    ]

    for i, test in enumerate(tests, 1):
        print(f"Тест {i}:")
        result = my_code(test["n"], test["m"], test["s"], test["t"], test["edges"])
        print(f"Ожидаемый: {test['answer']}")
        print(f"Получено:  {result}")
        print("-" * 50)

test_gps_cases()