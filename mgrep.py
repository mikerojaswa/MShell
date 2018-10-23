def m_grep(text, sub):
	myDict = {k: v for v, k in enumerate(sub)}
	if len(sub) > len(text): return -1
	i = len(sub) - 1
	while i < len(text):
		skip_distance = bad_character_rule(myDict, text, sub, i) 
		if skip_distance > 0:
			i += skip_distance
		else: 
			i += 1
	

def bad_character_rule(d, text, sub, idx):
	for i in range(len(sub)):
		current = text[idx] 
		if sub[len(sub) - i - 1] != current:
			if current in d:
				return len(sub) - i - d[current] - 1
			else: return len(sub)
		idx -= 1
	return -1

m_grep("CCAABBBGTDDFHIK", "AGDDDT")
			
"""			
0 1 2 3 4 5 6 7 8			
C C A A B B B G T D D F H I K
                  A G D D D T
6 - 1 - 1
i = 7 - 1 => 6

6 - 1 = 5
"""