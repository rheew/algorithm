#시계방향으로 한바퀴
arr = [[1,2,3], [4,5,6], [7,8,9]]

print(arr)

arr.reverse()
rotateArr = [list(i) for i in zip(*arr)]

print(rotateArr)
