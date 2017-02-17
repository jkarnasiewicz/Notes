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

# This is more pleasant, but slower solution
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



# Lesson 7, Fish (100%)
def solution(A, B):
	alive = []
	for index, (a, b) in enumerate(zip(A, B)):
		if not alive:
			alive.append((a, b))
			continue
		if (alive[-1][1], b) == (1, 0):
			if alive[-1][0] > a:
				continue
			alive.pop()
			alive.append((a, b))
			try:
				while (alive[-2][1], alive[-1][1]) == (1, 0):
					if alive[-2][0] > alive[-1][0]:
						alive.pop()
						break
					else:
						alive.pop(-2)
			except IndexError:
				pass
		else:
			alive.append((a, b))

	return len(alive)



# Lesson 7, Nesting (100%)
def solution(S):
	lenght = len(S)
	if lenght == 0:
		return 1
	if lenght % 2 == 1:
		return 0

	brackets = []
	for index, item in enumerate(S):
		if not brackets:
			brackets.append(item)
			continue
		if (brackets[-1], item) == ('(', ')'):
			brackets.pop()
		else:
			brackets.append(item)

	return 0 if brackets else 1



# Lesson 8, Dominator (100%)
def solution(A):
	di = {}
	center = len(A)//2
	for index, item in enumerate(A):
		if item in di:
			di[item][0] += 1
		else:
			di[item] = [1, index]
		if di[item][0] > center:
			return di[item][1]
	return -1



# Lesson 8, EquiLeader (55%)
def solution(A):
	lenght = len(A)
	counter = 0
	l_leader = None
	r_leader = None

	left_leader = []
	left_counter = {}

	right_leader = []
	right_counter = {}

	for i in range(lenght):
		current_len = i + 1
		if A[i] in left_counter:
			left_counter[A[i]] += 1
		else:
			left_counter[A[i]] = 1
		if left_counter[A[i]] >= current_len//2 + 1:
			left_leader.append(A[i])
			l_leader = A[i]
		else:
			if left_counter[l_leader] >= current_len//2 + 1:
				left_leader.append(l_leader)
			else:
				left_leader.append('-')

		negative_index = -current_len
		if A[negative_index] in right_counter:
			right_counter[A[negative_index]] += 1
		else:
			right_counter[A[negative_index]] = 1
		if right_counter[A[negative_index]] >= current_len//2 + 1:
			right_leader.insert(0, A[negative_index])
			r_leader = A[negative_index]
		else:
			if right_counter[r_leader] >= current_len//2 + 1:
				right_leader.insert(0, r_leader)
			else:
				right_leader.insert(0, '-')

	if l_leader is None:
		return 0

	for i in range(lenght - 1):
		if left_leader[i] == right_leader[i + 1] == l_leader:
			counter += 1

	return counter



# Lesson 9, MaxDoubleSliceSum (100%)
def solution(A):
	length = len(A)
	max_ending_list_front = [0]*length
	max_ending_front = 0
	for index in range(1, length-1):
		max_ending_front = max(0, A[index] + max_ending_front)
		max_ending_list_front[index] = max_ending_front

	max_ending_list_back = [0]*length
	max_ending_back = 0
	for index in range(length-2, 0, -1):
		max_ending_back = max(0, A[index] + max_ending_back)
		max_ending_list_back[index] = max_ending_back

	max_slice = 0
	for i in range(len(max_ending_list_front)-2):
		max_slice = max(max_slice, max_ending_list_front[i] + max_ending_list_back[i+2])

	return max_slice



# Lesson 9, MaxProfit (100%)
def solution(A):
	if len(A) < 2:
		return 0
	max_item = 0
	min_item = A[0]
	best = 0
	for i in A:
		if i <= min_item:
			min_item = i
			max_item = 0
			continue
		if i >= max_item:
			max_item = i
			diff = max_item - min_item
			best = diff if diff > best else best
	return best



# Lesson 9, MaxSliceSum (84%)
def solution(A):
	l = len(A)
	if l == 0:
		return 0
	max_slice = A[0]
	for i in range(l):
		s = A[i]
		max_slice = max(max_slice, s)
		for j in range(i + 1, l):
			s = s + A[j]
			max_slice = max(max_slice, s)
	return max_slice



# Lesson 10, CountFactors (100%)
def solution(N):
	count = 0
	i = 1
	while i*i < N:
		if N%i == 0:
			count += 2
		i += 1
	if i*i == N:
		count += 1
	return count



# Lesson 10, MinPerimeterRectangle (100%)
def solution(N):
	min_perimeter = 2*1 + 2*N
	i = 2
	while i*i <= N:
		if N % i == 0 and 2*(i) + 2*(N//i) < min_perimeter:
			min_perimeter = 2*(i) + 2*(N//i)
		i += 1

	return min_perimeter



# Lesson 10, Peaks (72%)
def solution(A):
	length = len(A)
	peaks = []
	for index in range(1, length - 1):
		if A[index-1] < A[index] > A[index+1]:
			peaks.append(index)

	if not peaks:
		return 0

	i = 1
	factors = []
	len_peaks = len(peaks)
	while i*i <= length:
		if length % i == 0:
			if i <= len_peaks:
				factors.append(i)
			if length//i <= len_peaks:
				factors.append(length//i)
		i += 1

	factors = sorted(factors, reverse=True)


	for i in factors:
		ranges = length//i
		count = 0

		for j in range(1, i+1):
		 	for k in peaks:
		 		if k < j*ranges:
		 			count += 1
		 			break

		if i == count:
			return i



# Lesson 10, Flags (66%)
def solution(A):
	peaks = []
	for i in range(1, len(A)-1):
		if A[i-1] < A[i] > A[i+1]:
			peaks.append(i)

	flags = len(peaks)
	
	results = 0
	for f in range(1, flags+1):
		count_flags = 0
		start = None
		for p in peaks:
			if not start:
				start = p
				count_flags += 1
				continue
			if count_flags == f:
				break
			if p-start >= f:
				start = p
				count_flags += 1
			
		if count_flags > results:
			results = count_flags

	return results
