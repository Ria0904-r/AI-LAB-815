import re
solved = False
def solve(letters, values, visited, words):
global solved
if len(set) == len(values):
map = {}
for letter, val in zip(letters,values):
map[letter] = val
if map[words[0][0]] == 0 or map[words[1][0]] == 0 or
map[words[2][0]] == 0:
return
word1, word2, res = &quot;&quot;, &quot;&quot;, &quot;&quot;
for c in words[0]:

word1 += str(map[c])
for c in words[1]:
word2 += str(map[c])
for c in words[2]:
res += str(map[c])
if int(word1) + int(word2) == int(res):
print(&quot;{} + {} = {}\t{}&quot;.format(word1, word2, res, map))
solved = True
return
for i in range(10):
if not visited[i]:
visited[i] = True
values.append(i)
solve(letters, values, visited, words)
values.pop()
visited[i] = False

print(&quot;\nCRYPTARITHMETIC PUZZLE SOLVER&quot;)
print(&quot;WORD1 + WORD2 = RESULT&quot;)
word1 = input(&quot;Enter WORD1: &quot;).upper()
word2 = input(&quot;Enter WORD2: &quot;).upper()
result = input(&quot;Enter RESULT: &quot;).upper()
if (not re.match(&quot;^[A-Z]*$&quot;, word1)) or (not re.match(&quot;^[A-Z]*$&quot;,
word2)) or (not re.match(&quot;^[A-Z]*$&quot;, result)):
print(&quot;\nOnly Letters allowed.&quot;)
elif len(result) &gt; (max(len(word1), len(word2)) + 1):
print(&quot;\n0 Solutions!&quot;)
else:
set = []
for c in word1:

if c not in set:
set.append(c)
for c in word2:
if c not in set:
set.append(c)
for c in result:
if c not in set:
set.append(c)
if len(set) &gt; 10:
print(&quot;\nNo solutions!&quot;)
exit()
print(&quot;Solutions:&quot;)
solve(set, [], [False for _ in range(10)], [word1, word2, result])
if not solved:
print(&quot;\n0 solutions!&quot;)
