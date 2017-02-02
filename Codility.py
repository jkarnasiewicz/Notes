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



# Lesson 5, GenomicRangeQuery (100%)
def solution(S, P, Q):
	imp_factor = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
	item = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
	results = []
	mod_S = []

	for letter in S:
		item[letter] += 1
		mod_S.append(item.copy())

	for i, j in zip(P, Q):
		if (i == j):
			results.append(imp_factor[S[i]])
			continue

		res = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
		for l in ['A', 'C', 'G', 'T']:
			res[l] = mod_S[j][l] - mod_S[i-1][l] if i != 0 else mod_S[j][l]
			if res[l] > 0:
				results.append(imp_factor[l])
				break
		
	return results

# This is better, but slow
# def solution(S, P, Q):
#   results = []
#   imp_factor = (('A', 1), ('C', 2), ('G', 3), ('T', 4))
#   for i, j in zip(P, Q):
#       unique_letters = set(S[i:j+1])
#       for letter, factor in imp_factor:
#           if letter in unique_letters:
#               results.append(factor)
#               break
#   return results



# Lesson 6, Distinct (100%)
def solution(A):
	return len(set(A))

# def solution(A):
#     count = 0
#     s = set()
#     for i in A:
#         if i in s:
#             continue
#         else:
#             s.add(i)
#             count += 1

#     return count



# Lesson 6, MaxProductOfThree (100%)
def solution(A):
	A = sorted(A)
	pos = A[-1] * A[-2] * A[-3]
	if A[-1] <= 0 or A[0] > 0:
		return pos
	else:
		neg = A[0] * A[1] * A[-1]
		return pos if pos > neg else neg



# Lesson 6, Triangle (100%)
def solution(A):
	A = sorted(A)
	for index, i in enumerate(A):
		try:
			if i + A[index+1] > A[index+2] and i + A[index+2] > A[index+1] and A[index+1] + A[index+2] > i:
				return 1
		except IndexError:
			return 0
			
	return 0



# Lesson 6, NumberOfDiscIntersections (56%)
def solution(A):
	count = 0
	sorted_list = sorted([(i-j, i+j) for i,j in enumerate(A)])
	for index, item in enumerate(sorted_list):
		for i in sorted_list[index+1:]:
			if item[1] < i[0]:
				break
			if((item[0] <= i[0] <= item[1]) or (item[0] <= i[1] <= item[1])):
				count += 1
				if count > 10**7:
					return -1
	return count

# ?
# def solution_u(A):
	
#     upper = sorted([i + val for i, val in enumerate(A)])
#     lower = sorted([i - val for i, val in enumerate(A)])
	
#     counter = 0
#     j = 0
#     for i, uval in enumerate(upper):
#         while j < len(upper) and uval >= lower[j]:
#             counter += j-i
#             j += 1
#         if counter > 10**7: return -1
				
#     return counter



# Lesson 7, Brackets (100%)
def solution(S):
	lenght = len(S)
	op = ['(', '[', '{']
	en = [')', ']', '}'] 
	if lenght == 0:
		return 1
	if lenght % 2 == 1:
		return 0
	results = []
	for i in S:
		if i in op:
			results.append(i)
		else:
			try:
				if en.index(i) == op.index(results[-1]):
					del results[-1]
				else:
					return 0
			except IndexError:
				return 0
	
	return 1 if len(results) == 0 else 0



# Lesson 7, StoneWall (92%)
def solution(H):
	counter = 0
	unique_heights = {}
	last_height = None
	for index, h in enumerate(H):
		if h in unique_heights:
			if min(H[unique_heights[h]:index]) >= h:
				counter += 1

		unique_heights[h] = index

	return len(H) - counter
