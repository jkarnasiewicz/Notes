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



# Lesson 2, CyclicRotation (100%)
def lsolution(A, K):
    if A:
        for i in range(K):
            A.insert(0, (A.pop()))
    return A



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



# Lesson 4, PermCheck (100%)
def solution(A):
    l = len(A)
    table = [0]*l
    for i in A:
        try:
            table[i-1] += 1
        except IndexError:
            return 0
    return 0 if 0 in table else 1



# Lesson 4, FrogRiverOne (100%)
def solution(X, A):
	final_set = set()
	for index, i in enumerate(A):
		if i <= X:
			final_set.add(i)
			if len(final_set) == X:
				return index
	return -1



# Lesson 4, MissingInteger (100%)
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


# Lesson 4, MaxCounters (88%)
def solution(N, A):
    result = [0]*N
    highest_value = 0
    last_operation = 'max_counter'
    for i in A:
        if i == N+1:
            if last_operation == 'increase':
                result = [highest_value]*N
                last_operation = 'max_counter'
            continue
        result[i-1] += 1
        if result[i-1] > highest_value:
            highest_value = result[i-1]
            last_operation = 'increase'
    return result



# Lesson 5, PassingCars (100%)
def solution(A):
    results = [0, 0]
    for i in A:
        if i == 0:
            results[0] += 1
        else:
            results[1] += results[0]
        if results[1] > 1000000000:
            return -1
    return results[1]



# Lesson 5, CountDiv (100%)
def solution(A, B, K):
    edge = 0
    if A == 0 and B == 0:
        return 1
    if A == B:
        if A%K == 0:
            return 1
        return 0
    if K == 1:
        return B - A + 1
    if A%K == 0:
        edge += 1
    if K >= A:
        return B//K + edge
    else:
        return B//K - A//K + edge
