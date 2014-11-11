D= {}
def tree_action(L):
	def wrapper(func):
		M=L #nonlocal
		if type(M)==str:
			M= M.split()
		for x in M:
			tree_action.D[x]= func
	return wrapper
tree_action.D= D

@tree_action('gh')
def f(x):
	return x**2

@tree_action('ab')
def f(x):
	return x-1
