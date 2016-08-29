 # Lesson 1, BinaryGap (100%)
 def solution(N):
    bin_value = bin(N).split('1')[1:-1]
    length_value = [len(i) for i in bin_value]
    return max(length_value) if length_value else 0



# Lesson 2, OddOccurrencesInArray (100%)
def solution(A):
	di = dict()
	for i in A:
		if i in di:
			del di[i]
		else:
			di[i] = 0
	return di.popitem()[0]



# Lesson 3, FrogJmp (100%)
def solution(X, Y, D):
    floor_div, remainder = divmod(Y - X, D)
    return floor_div if remainder == 0 else floor_div + 1



# Lesson 3, PermMissingElem (100%)
def solution(A):
	len_A = len(A) + 2
	set_A = set(A)
	set_B = set(range(1, len_A))
	return (set_B - set_A).pop()



# Lesson 3, TapeEquilibrium (100%)
def solution(A):
    sum_A, sum_B = sum(A[:1]), sum(A[1:])
    result = abs(sum_A - sum_B)
    for i in range(1, len(A)-1):
        sum_A = sum_A + A[i]
        sum_B = sum_B - A[i]
        diff = abs(sum_A - sum_B)
        result = diff if diff < result else result
    return result



# Lesson 4, FrogRiverOne (100%)
def solution(X, A):
	final_set = set()
	for index, i in enumerate(A):
		if i <= X:
			final_set.add(i)
			if len(final_set) == X:
				return index
	return -1



# Lesson 4, MissingInteger
def solution(A):
    ori_set = {i for i in A if i > 0}
    if not ori_set:
        return 1
    if len(ori_set) == 1:
        number = ori_set.pop()
        return  1 if number != 1 else 2
    max_set = max(ori_set)
    for i in xrange(1, max_set + 2):
        if i not in ori_set:
            return i
