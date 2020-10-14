import sys
sys.setrecursionlimit(10001)
input = sys.stdin.readline

n = 1
node = []
while n :
    n = input().rstrip()
    if not n : break
    node.append(int(n))

def postOrder(node) :
    if not node : return

    root = node[0]

    leftNode = []
    rightNode = []
    for i in node :
        if i > root :
            rightNode.append(i)
        elif i < root:
            leftNode.append(i)

    postOrder(leftNode)
    postOrder(rightNode)
    print(root)

postOrder(node)


