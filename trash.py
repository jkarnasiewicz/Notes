# REGULAR EXPRESSIONS
import re

# compile - compile regexp pattern
re.compile(r'pattern')
# re.compile(r'(\d{3})-(\d{3})-(\d{4})-(\d+)')

# findall - return all matches of pattern
re.findall(pattern, string)
# re.findall("[a-zA-Z]+|[0-9]+", string)            # every word, and every number
# re.findall('http[^"]*', string)                   # every string that start with http and end with "
# re.findall('href="(.+?)"', string)                # everything between href=" and "
# re.findall(' s.*? s', string)                     # regular expression looks for a space,
#                                                   # an s, and then the shortest possible
#                                                   # series of any character(.*?),
#                                                   # then a space, then another s

# sub - replace occurances of pattern
re.sub(pattern, replacement, string, count=0, flags=0)
# re.sub("D:[^\ ]Filmy[^\ ]", "", string)                  # D:\Filmy\ => ""

# split - split string by occurrences of pattern
re.split(pattern, string)
# re.split(r'[;,\s]+', 'asdf fjdk; afed, fjek,asdf, foo')

# search - search for pattern in string
re.search(pattern, string, flags=0)
# re.search(pattern, string, re.VERBOSE)  # verbose regular expressions

# match - checks if string starts with pattern
re.match(pattern, string)
# re.match("c", "abcdef")                 			# no match
# re.search("c", "abcdef")                			# match

# group - returns one or more subgroups of the match
search_object.group()								# group(1)/groups()



# .					matches any character except a newline
# *                 match 0 or more repetitions of the preceding RE
# +                 match 1 or more repetitions of the preceding RE
# ?					match 0 or 1 repetitions of the preceding RE

# greedy - they match as much text as possible
# <.*> is matched against '<a> b <c>', it will match the entire string, and not just <a>

# non-greedy or minimal fashion - they match as few characters as possible
# <.*?> is matched against '<a> b <c>', will match only <a>



# ^					matches the start of a string
# $					matches the end of the string or just before the newline at the end of the string

# {m}				specifies that exactly m copies of the previous RE should be matched
# {m, n}			(greedy)causes the resulting RE to match from m to n repetitions of the preceding RE, attempting to match as many repetitions as possible
# {m, n}?			(non-greedy)causes the resulting RE to match from m to n repetitions of the preceding RE, attempting to match as few repetitions as possible

# [] 				indicate a set of characters, e.g. [amk] will match 'a', 'm', or 'k', special characters lose their special meaning inside sets e.g. [(+*)] will match any of the literal characters '(', '+', '*', or ')'
# [^/]+             which will match everything up to the first /

# (...)             matches whatever regular expression is inside the parentheses, and indicates the start and end of a group
# (A|B|C)           match exactly one of A, B, or C
# (?P<name>...)     similar to regular parentheses, but the substring matched by the group is accessible via the symbolic group name name

# \d                digit (0–9)
# \D                non digits

# \b                empty string boundary
# \B 				empty string non boundary

# \w 				alphanumeric
# \W 				non-alphanumeric

# \s 				whitespace
# \S 				non whitespace

# \A 				start of the string
# \Z 				end of the string
