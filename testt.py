# def  gridColouring( grid):
#     n = len(grid)
#     m = len(grid[0])
#     d1 = []
#     d2 = []
#     count = 0
#     for i in range(n):
#         row = grid[i]
#         row = row.upper()
#         for j in range(m):
#             if row[j] == 'G' or row[j] == 'R' and i not in d1:
#                 d1.append(i)
#             elif i in d1:
#                 if j>0 and grid[i][j-1] == 'B':
#                     count += 1
#             if row[j] == 'G' or row[j] == 'B' and j not in d2:
#                  d2.append(j)
#             elif j in d2:
#                 if i>0 and grid[i-1][j] == 'R':
#                     count += 1
#     horStrokes = len(d1)
#     verStrokes = len(d2)
#
#     minStrokes = horStrokes + verStrokes + count
#     return minStrokes
#
#
# # Complete the function below.
#
# def f(l):
#     a = []
#     for num in l:
#         print bin(num).count("1")
#
# l = [5,7,14,31]
# print f(l)
# def  swap_array( a):
#     d = dict()
#     for num in a:
#         m = num
#         count1 = 0
#         while m:
#             m &= (m-1)
#             count1 += 1
#         d[num] = count1
#     s_a = sorted(d.items(), key=lambda x: (-x[1],-x[0]))
#     for num in s_a:
#         print num[0]



# def  zombieCluster(zombies):
#     cluster = []
#     for i in range(len(zombies)):
#         for j in range(len(zombies)):
#             if i==j:
#                 continue
#             a = 'z'+str(i)
#             b = 'z'+str(j)
#             if zombies[i][j] == '1' and zombies[j][i] == '1' and [b,a] not in cluster:
#                 cluster.append([a,b])
#     i=0
#     while i < len(cluster)-1:
#         if list(set(cluster[i]) & set(cluster[i+1])):
#             cluster[i] = list(set(cluster[i]) | set(cluster[i+1]))
#             del cluster[i+1]
#         else:
#             i += 1
#     l = 0
#     for s in cluster:
#         l += len(s)
#     count = len(cluster) + len(zombies) - l
#     return count
#
#
#
#
# a = ['10000','01000','00100','00010','00001']
# print zombieCluster(a)


# def solveMissing(n, m):
#     n_cnt = [0] * 101
#     m_cnt = [0] * 101
#     offset = min(m)
#
#     for ele in m:
#         m_cnt[ele-offset] += 1
#
#     for ele in n:
#         n_cnt[ele-offset] += 1
#
#
#     for idx in xrange(101):
#         if m_cnt[idx] != n_cnt[idx]:
#             print idx + offset,
#
# a = [1,3,4,65,67,2]
# b = [1,3,4,65,67,2,6]
# solveMissing(a,b)


# from collections import Counter
#
# def isValid(S):
#     char_map = Counter(S)
#     char_occurence_map = Counter(char_map.values())
#     print char_occurence_map
#     if len(char_occurence_map) == 1:
#         return True
#
#     if len(char_occurence_map) == 2:
#         for v in char_occurence_map.values():
#             if v == 1:
#                 return True
#
#     return False
#
#
# S = raw_input()
# if isValid(S):
#     print "YES"
# else:
#     print "NO"


# def pairs(a,k):
#     answer = 0
#     for v in a:
#         if v+k in a:
#             answer += 1
#
#     return answer
# if __name__ == '__main__':
#     n, k = map(int, raw_input().split())
#     b = map(int, raw_input().split())
#     print pairs(b, k)


# def buildMap(s):
#     the_map = {}
#     for char in s:
#         if char not in the_map:
#             the_map[char] = 1
#         else:
#             the_map[char] +=1
#
#     return the_map
#
# def anagram(s1, s2):
#     map1 = buildMap(s1)
#     map2 = buildMap(s2)
#
#     diff_cnt = 0
#     for key in map2.keys():
#         if key not in map1:
#             diff_cnt += map2[key]
#         else:
#             diff_cnt += max(0, map2[key]-map1[key])
#
#     for key in map1.keys():
#         if key not in map2:
#             diff_cnt += map1[key]
#         else:
#             diff_cnt += max(0, map1[key]-map2[key])
#
#     return diff_cnt
#
# if __name__ == '__main__':
#     s1 = raw_input()
#     s2 = raw_input()
#     print anagram(s1, s2)


# def kSub(k, nums):
#     total = 0
#     cnt_mod = {}
#     cnt_mod[0] = 1
#     for num in nums:
#         total += num
#         total %= k
#         if total in cnt_mod:
#             cnt_mod[total] += 1
#         else:
#             cnt_mod[total] = 1
#     res = 0
#     for i in range(k):
#         res += cnt_mod[i]*(cnt_mod[i]-1)/2
#     return res
# print kSub(3,[1,2,3,4,1])


import re
import sys

pat = r'(/\*.*?\*/|//.*?$)'
txt = sys.stdin.read()
# re.sub() for Testcase #4: others will just work with comment
print "\n".join(re.sub('\n\s+', '\n', comment) for comment in re.findall(pat, txt, re.DOTALL|re.MULTILINE))



def max_difference(xs):
    max_idx, max_elem = max(enumerate(xs), key=operator.itemgetter(1))

    if max_idx == 0:
        return -1
    return max_elem - min(xs[:max_idx])