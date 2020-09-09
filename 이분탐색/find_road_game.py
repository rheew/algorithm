import sys
sys.setrecursionlimit(10**6)
def preorder(node, answer):
    if not node : return
    rootinfo = node[0]

    left = []
    right = []
    answer.append(rootinfo[2])
    
    for i in node:
        if rootinfo[0] < i[0] :
            right.append(i)
        elif rootinfo[0] > i[0] :
            left.append(i)
    preorder(left, answer)
    preorder(right, answer)
    return

def postorder(node, answer):
    if not node : return
    
    rootinfo = node[0]
    left = []
    right = []

    for i in node:
        if rootinfo[0] < i[0] :
            right.append(i)
        elif rootinfo[0] > i[0] :
            left.append(i)
            
    postorder(left, answer)
    postorder(right, answer)
    
    answer.append(rootinfo[2])
    return

def solution(nodeinfo):
    answer = []
    node = []
    pre = []
    post = []
    for ind, i in enumerate(nodeinfo) :
        node.append(i+[ind + 1])
    
    node = sorted(node, key=lambda x : -x[1])
    preorder(node, pre)
    postorder(node, post)
    
    return [pre,post]