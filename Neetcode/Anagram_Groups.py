"""
Anagram Groups
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: strs = ["act","pots","tops","cat","stop","hat"]

Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
Example 2:

Input: strs = ["x"]

Output: [["x"]]
Example 3:

Input: strs = [""]

Output: [[""]]
"""

"""
1. 리스트 정렬 
2. 첫번쨰 원소와 같은 애들 있는지 정렬해서 확인
3. 1,2 과정 반복
"""
# strs = ["act","pots","tops","cat","stop","hat"]

# sorted_lst = sorted(strs)

# first_ele = sorted(strs[0])
# li = [] 

# for idx in range(0+1, len(sorted_lst)):
#     if first_ele == sorted(sorted_lst[idx]):
#         print(sorted_lst[idx])

# 조금 더 파야함
# class Solution:

#     def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

#         def remove_element(origin_strs:list[str], new_strs:list[str]) -> None:
#             for remove_ele in new_strs:
#                 origin_strs.remove(remove_ele)

#         total_lst = []

#         # if len(set(strs)) != len(strs):

#         if len(strs) > 1:
            
#             sorted_lst = sorted(strs)
#             # print(sorted_lst)

#             # for idx in range(len(sorted_lst)):
#             while len(sorted_lst) > 0:
#                 # print(total_lst)
#                 print(sorted_lst)
#                 # first_ele = sorted(sorted_lst[idx])
#                 first_ele = sorted(sorted_lst[0])
#                 li = []
#                 # li.append(sorted_lst[idx])
#                 li.append(sorted_lst[0])

#                 # for idx_2 in range(idx+1, len(sorted_lst)):
#                 for idx_2 in range(1, len(sorted_lst)):

#                     if first_ele == sorted(sorted_lst[idx_2]):
#                         li.append(sorted_lst[idx_2])
            
#                 total_lst.append(li)
                
#                 if len(sorted_lst) == 1:
#                     total_lst.append([sorted_lst[0]])
#                     break
                
#                 # 지우는 부분이 뭔 문제가 있는 것 같은데...
#                 if len(li) != 0:
#                     remove_element(origin_strs = sorted_lst, new_strs = li)

#         elif len(strs) == 1:
#             total_lst.append([strs[0]])
#         else:
#             total_lst.append([""])
        
#         # else:
#         #     total_lst.append([""])
            
#         return total_lst

"""
리스트에 들어가 있는 문자를 모두 정렬 후 같은 것들 있는지 확인
있다면 그건 다른 리스트에 넣고 없다면 넣지 않음
최종적으로 그 리스트에 개수가 1 이상이라면 [""] 넣고 아니라면 그대로 return
"""
class Solution:


    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        from collections import defaultdict

        def find_duplicates_with_indices(lst : list) -> dict:
            # 문자별로 인덱스를 저장할 딕셔너리 생성
            index_map = defaultdict(list)

            # 리스트를 순회하면서 각 문자의 인덱스를 기록
            for index, item in enumerate(lst):
                index_map[item].append(index)

            # 인덱스 리스트가 2개 이상인 항목만 필터링하여 반환
            duplicates = {item: indices for item, indices in index_map.items()}

            return duplicates

        new_sorted_strs = []
        for idx in range(len(strs)):
            
            # 문자열 정렬
            new_sorted_strs.append("".join(sorted(strs[idx])))

        # 동일 문자열 index 정보 추출
        find_d = find_duplicates_with_indices(new_sorted_strs)

        total_lst = []
        for d, v in find_d.items():
            li = []
            for num in v:
                li.append(strs[num])
            total_lst.append(li)


        return total_lst

# print(total_lst)
strs = ["act","pots","tops","cat","stop","hat"]
strs = ["",""]
strs = ['', 'b'] 
q = Solution()

print(q.groupAnagrams(strs))