import sys
import heapq
from collections import deque

entrada = sys.stdin.read().split()

idx = 0
while idx < len(entrada):
    n = int(entrada[idx])
    idx += 1
    
    is_stack = True
    is_queue = True
    is_pq = True
    
    stack = []
    queue = deque()
    pq = []
    
    for _ in range(n):
        op = int(entrada[idx])
        val = int(entrada[idx+1])
        idx += 2
        
        if op == 1:
            if is_stack: 
                stack.append(val)
            if is_queue: 
                queue.append(val)
            if is_pq: 
                heapq.heappush(pq, -val)
                
        elif op == 2:
            if is_stack:
                if len(stack) == 0 or stack.pop() != val:
                    is_stack = False
                    
            if is_queue:
                if len(queue) == 0 or queue.popleft() != val:
                    is_queue = False
                    
            if is_pq:
                if len(pq) == 0 or -heapq.heappop(pq) != val:
                    is_pq = False
 
    matches = is_stack + is_queue + is_pq
    
    if matches == 0:
        print("impossible")
    elif matches > 1:
        print("not sure")
    elif is_stack:
        print("stack")
    elif is_queue:
        print("queue")
    elif is_pq:
        print("priority queue")