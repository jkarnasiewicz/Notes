# -*- coding: utf-8 -*-
# design pattern
# facade
# iterators
# decoartors



# def split(string, delimiter=' '):
# 	index = 0
# 	dl = len(delimiter)
# 	sl = len(string)
# 	result = []
# 	s = ''
# 	while True:
# 		if string[index:index+dl] != delimiter:
# 			s += string[index]
# 			index = index + 1
# 		else:
# 			index = index + dl
# 			result.append(s)
# 			s = ''

# 		if index >= sl:
# 			break

# 	result.append(s)

# 	return result


# import unittest


# def split(string, pattern=' '):
# 	if type(string) != str or type(pattern) != str:
# 		raise TypeError
# 	string_len = len(string)
# 	pattern_len = len(pattern)
# 	result = []
# 	temp = ''
# 	index = 0

# 	while True:
# 		if string[index:index+pattern_len] == pattern:
# 			result.append(temp)
# 			temp = ''
# 			index = index+pattern_len
# 		else:
# 			temp += string[index]
# 			index += 1

# 		if index >= string_len:
# 			break


# 	result.append(temp)


# 	return result


# class SplitTest(unittest.TestCase):
	
# 	def test_split_return_type(self):
# 		self.assertEqual(type(split('random string', 'r')), list)

# 	def test_arguments_type(self):
# 		for case in [('random string', 1), (1, 'r')]:
# 			with self.subTest(case=case):
# 				with self.assertRaises(TypeError):
# 					split(case[0], case[1])

# 	def test_split_short_pattern(self):
# 		self.assertEqual(split('random string', 'r'), ['', 'andom st', 'ing'])

# 	def test_split_long_pattern(self):
# 		self.assertEqual(split('random and string', 'and'), ['r', 'om ', ' string'])

# 	def test_default_pattern_value(self):
# 		self.assertEqual(split('random string'), ['random', 'string'])

# 	def test_no_match(self):
# 		self.assertEqual(split('random string', 'x'), ['random string'])

# 	def test_special_character(self):
# 		self.assertEqual(split('ran\\dom str\\ing', '\\'), ['ran', 'dom str', 'ing'])



# if __name__ == '__main__':
# 	unittest.main(verbosity=2)





# from re import finditer

# def split(string, delimiter=' '):
# 	result = []
# 	index = 0
# 	for item in finditer(delimiter, string):
# 		result.append(string[index:item.start()])
# 		index = item.end()

# 	result.append(string[index:])
# 	print(result)



# split('asd efef fefe', 'ef')
# print('asd efef fefe'.split('ef'))

# split('  aa a  aa   aaa', '  ')
# print('  aa a  aa   aaa'.split('  '))

# split('asd asd asd asd', 's')
# print('asd asd asd asd'.split('s'))

# Testing
# + test return type check



# monitor the code flow of a program in python

# import sys
 
# def trace_calls(frame, event, arg):
#     # The 'call' event occurs before a function gets executed.
#     if event != 'call':
#         return
#     # Next, inspect the frame data and print information.
#     print('Function name={}, line num={}'.format(frame.f_code.co_name, frame.f_lineno))
#     return
 
# def demo2():
#     print('in demo2()')
 
# def demo1():
#     print('in demo1()')
#     demo2()
 
# sys.settrace(trace_calls)
# demo1()





# sign declaration of confidence

# What Can You Contribute to This Company?
# I like to learn and constantly develop myself in different fields and technologies -
# i still adding new technologies to my cv :)

# Currently im learning about machine learning/data science and i would like to add
# that to my python developer skills/skill set. So if your firm has interest in machine learning
# and you use python I think i would be a good asset, because i really want to develop
# in that direction

# Im pretty eager to work, im trying to do a little bit more that i have to -
# in my previous job i was developing 4 projects at once, that was a lot in compare to others

# I think as a person Im pretty openminded and likeable, i meet really nice people in my
# previous jobs and I still have contact with them, and we like to spend time together.

# # And Im pretty honest about my opinions





# # Last 6 months
# Currently i just started looking for a job. I couldnt work for last 6 month,
# unfortunately my mother had terrible accident and she was completely disable(physically)
# for couple of months. She broke her leg in 3 different placeces and have - i belive
# 11 bolts/screws - so its very seriuos injury, and in addition to tha i needed to take
# minor operation on my right shoulder(that was in may) so now i was disable for
# couple of weeks. two weeks ago i was staring to recover a i was starting to use my right arm,
# so i decide that it is good time to finally searching for a job.
# My mother still goes to rehabilitation clinic, and she still didnt recover fully 





# # Last job responibilities
# before acident i was working i small firm. I was hired as full-stack developer but
# most of the time i work as backend developer, so python and django
# (and other technologies), and in addition to that i was responsible for creating
# and maintaining our beta servers. I terms of frond end, i have just couple of minor
# bootstrap, css and js tasks and that was it. I was also in touch with our clients
# durning the mettings and through the e-mail conversations





# Hobbies



# Make the capturing pattern optional, and remember to deal with a trailing slash appropriately.
# Id find a noncapturing group around the capturing group the safest way to do that:

# url(r'^(?:(?P<book_id>\w+)/)?$', 'pro.views.book', name='book'),



# from django.contrib.auth.decorators import user_passes_test
# @user_passes_test(lambda user: user.is_anonymous)

# and meantaining all the code in github reposiotry

# zarabiac adekwatnie do osób ktore maja podobne umiejetnosci, widze i doswiadczenie

# najpierw bardzo prosty i modyfikowalny kod
# nie pisac wyspecjalizowanego kodu od razu - poczekać na akceptacje klienta i dopiero pozniej tworzyc optymilizacje kodu - nauczka z poprzednich projektow gdzie aplikacja miala mic taka funkcjonalnosc a pozniej sie okazalo ze bedzie miec inna

# but I prefer different approach to the problems with 'good practice' not Design Patterns with depends on language and are to general

# interview algorithm questions and answers
# python interview questions



# from collections import defaultdict

# class Graph:

# 	def __init__(self):
# 		self.graph = defaultdict(list)
 
# 	def addEdge(self, u, v):
# 		self.graph[u].append(v)

# 	def BFS(self, s):
# 		visited = [False] * len(self.graph)
# 		queue = []
# 		result = []
		
# 		visited[s] = True
# 		result.append(s)

# 		queue.extend(self.graph.get(s))

# 		while queue:
# 			actual_node = queue.pop(0)

# 			if visited[actual_node]:
# 				continue

# 			visited[actual_node] = True
# 			result.append(actual_node)

# 			for item in self.graph.get(actual_node):
# 				if visited[item]:
# 					continue
				
# 				queue.append(item)

# 		return result


# g = Graph()
# g.addEdge(0, 1)
# g.addEdge(0, 2)
# g.addEdge(1, 2)
# g.addEdge(2, 0)
# g.addEdge(2, 3)
# g.addEdge(3, 3)

# print(g.BFS(2))


# from collections import defaultdict

# class Graph:

# 	def __init__(self):
# 		self.graph = defaultdict(list)
 
# 	def addEdge(self, u, v):
# 		self.graph[u].append(v)

# 	def BFS(self, s):
# 		visited = [False] * len(self.graph)
# 		stack = []
# 		result = []
		
# 		visited[s] = True
# 		result.append(s)

# 		stack.append(s)

# 		while stack:
# 			actual_node = stack[-1]

# 			for item in self.graph.get(actual_node):
# 				if not visited[item]:
# 					stack.append(item)
# 					visited[item] = True
# 					result.append(item)
# 					break
# 			else:
# 				stack.pop()

# 		return result


# g = Graph()
# g.addEdge(0, 1)
# g.addEdge(0, 2)
# g.addEdge(1, 2)
# g.addEdge(2, 0)
# g.addEdge(2, 3)
# g.addEdge(3, 3)

# print(g.BFS(2))

# 2 0 1 3


# Python program to insert in sorted list
# class Node:

# 	def __init__(self, data):
# 		self.data = data

# 	def __repr__(self):
# 		return '{}'.format(self.data)

# 	def __le__(self, rhs):
# 		return self.data <= rhs.data

 
# class LinkedList:
 
# 	def __init__(self):
# 		self.list = []
 
# 	def sortedInsert(self, new_node):
# 		# print(self.list)
# 		if self.list:
# 			for index, node in enumerate(self.list, start=1):
# 				if new_node <= node:
# 					self.list.insert(index-1, new_node)
# 					return

# 		self.list.append(new_node)

# 	def printList(self):
# 		print(self.list)



# # Driver program
# llist = LinkedList()
# new_node = Node(5)
# llist.sortedInsert(new_node)
# new_node = Node(10)
# llist.sortedInsert(new_node)
# new_node = Node(7)
# llist.sortedInsert(new_node)
# new_node = Node(3)
# llist.sortedInsert(new_node)
# new_node = Node(1)
# llist.sortedInsert(new_node)
# new_node = Node(9)
# llist.sortedInsert(new_node)
# print("Create Linked List")
# llist.printList()

# # Created Linked List
# # 1 3 5 7 9 10 



# class Node:
 
#     # Constructor to create a new node
#     def __init__(self, key):
#         self.c = key ; 
#         self.next = None
 
# def compare(list1, list2):
     
#     # Traverse both lists. Stop when either end of linked 
#     # list is reached or current characters don't watch
#     while(list1 and list2 and list1.c == list2.c):
#         list1 = list1.next
#         list2 = list2.next
 
#     # If both lists are not empty, compare mismatching
#     # characters 
#     if(list1 and list2):
#         return 1 if list1.c > list2.c else -1
 
#     # If either of the two lists has reached end
#     if (list1 and not list2):
#         return 1
 
#     if (list2 and not list1):
#         return -1
#     return 0
 
# # Driver program
 
# list1 = Node('g')
# list1.next = Node('e')
# list1.next.next = Node('e')
# list1.next.next.next = Node('k')
# list1.next.next.next.next = Node('s')
# list1.next.next.next.next.next = Node('b')
 
# list2 = Node('g')
# list2.next = Node('e')
# list2.next.next = Node('e')
# list2.next.next.next = Node('k')
# list2.next.next.next.next = Node('s')
# list2.next.next.next.next.next = Node('a')
 
# print(compare(list1, list2))


# question_template = {
#     "title": "default title",
#     "question": "default question",
#     "answer": "default answer",
#     "hints": []
# }


# def make_new_question(title, question, answer, hints=None):
#     new_q = question_template.copy()

#     # always require title, question, answer
#     new_q["title"] = title
#     new_q["question"] = question
#     new_q["answer"] = answer

#     # sometimes there aren't hints, that's fine. Otherwise, add them:
#     if hints is not None:
#         new_q["hints"] = hints

#     return new_q


# question_1 = make_new_question("title1", "question1", "answer1", ["q1 hint1", "q1 hint2"])
# question_2 = make_new_question("title2", "question2", "answer2")
# question_3 = make_new_question("title3", "question3", "answer3", ["q3 hint1"])

# print(question_1, question_2, question_3, question_template, sep='\n')



# "^.{8,255}|[ABCDEFGHIJKLMNOPQRSTUVWXYZ]|[abcdefghijklmnopqrstuvwxyz]|[0-9]|[!@#\$%\^&\*]"
import re

count = 0
with open('top_1M.txt', mode='rt') as f:
	for line in f:
		match_1 = re.search('(?=.*[A-Z]+)(?=.*[a-z]+)(?=.*\d+)(?=.*[.,!@#\$%^&*/]+)(?!.*wsx)(?!.*WSX)(?!.*qaz)(?!.*QAZ)(?!.*zxc)(?!.*ZXC)(?!.*asd)(?!.*ASD)(?!.*qwe)(?!.*QWE)(?!.*123)', line)
		# match = re.search('(?=.*[A-Z]+)(?=.*[a-z]+)(?=.*\d+)(?=.*[.,!@#\$%^&*/]+)(?!.*[w|Ws|Sx|X]{3})(?!.*[q|Qa|Az|Z]{3})(?!.*[z|Zx|Xc|C]{3})(?!.*[a|A|s|S|d|D]{3})(?!.*[123]{3})', line)

		match_2 = re.search('password', line.lower().replace('@', 'a').replace('0', 'o').replace('$', 's'))
		# match = re.search('(wsx)|(qaz)|(zxc)|(asd)|(123)|', line, flags=re.IGNORECASE)
		if match_1 and not match_2:
			count += 1
			print(match_1)
			print(line)

print('Count: ', count)

# '(?=.*[A-Z]+)(?=.*[a-z]+)(?=.*\d+)(?=.*[!@#\$%\^&\*]+){8,255}'


