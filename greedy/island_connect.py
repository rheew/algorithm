def union(a, b, node):
    parents_a = find(a, node)
    parents_b = find(b, node)

    if parents_a == parents_b:
        return False

    node[parents_b] = parents_a

    return True


def find(a, node):
    if a != node[a]:
        node[a] = find(node[a], node)
    return node[a]


def solution(n, costs):
    answer = 0
    costs = sorted(costs, key=lambda x: x[2])
    node = [i for i in range(n)]

    for x, y, cost in costs:

        if union(x, y, node):
            answer += cost
    return answer