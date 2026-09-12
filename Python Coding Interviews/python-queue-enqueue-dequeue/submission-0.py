from typing import List, Deque
from collections import deque


def rotate_list(arr: List[int], k: int) -> Deque[int]:
    queue = deque(arr)

    for i in range(k):
        temp = queue.popleft()
        queue.append(temp)
        #or 
        #queue.append(queue.popleft())
    return queue

    #or

    # while len(queue) > 0 and k > 0:
    #     temp = queue.popleft()
    #     queue.append(temp)
    #     k -= 1
    # return queue



# do not modify below this line
print(rotate_list([1, 2, 3, 4, 5], 0))
print(rotate_list([1, 2, 3, 4, 5], 1))
print(rotate_list([1, 2, 3, 4, 5], 2))
print(rotate_list([1, 2, 3, 4, 5], 3))
print(rotate_list([1, 2, 3, 4, 5], 4))
print(rotate_list([1, 2, 3, 4, 5], 5))
