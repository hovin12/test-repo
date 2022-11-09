
def mean(lst):
	return sum(lst)/len(lst)

def var(lst):
	return (sum([(i-mean(lst))**2 for i in lst]))/(len(lst)-1)

print(mean(list(range(1,11)))

print('hello world')
