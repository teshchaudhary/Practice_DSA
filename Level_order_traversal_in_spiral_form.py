from collections import deque

def findSpiral(root):
	res = []

	q = deque()
	q.append(root)
	reverse = True

	while q:
		n = len(q)

		if not reverse:
			while n > 0:
				n -= 1
				node = q.popleft()
				if (node.left):
					q.append(node.left)

				if (node.right):
					q.append(node.right)

				res.append(node.data)
				
			reverse = not reverse
			
		else:
			while n > 0:
				n -= 1
				node = q.pop()
		
				if (node.right):
					q.appendleft(node.right)

				if (node.left):
					q.appendleft(node.left)

				res.append(node.data)

			reverse = not reverse
	
	return res
