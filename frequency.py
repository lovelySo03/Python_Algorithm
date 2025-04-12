# 빈드수가 높은 순서대로 출력
# DAT (Direct Address Table)

class Solution:
    def frequencySort(self, s: str) -> str:
        lst = list(s)
        bucket = [0]*200
        for i in range(len(s)):
            temp = ord(lst[i])
            bucket[temp] += 1

        temp = []
        for j in range(len(bucket)):
            if bucket[j] > 0:
                temp.append([bucket[j], chr(j)])

        # 빈도수를 기준으로 내림차순 정렬
        temp.sort(reverse=True)

        ans = []
        for freq, char in temp:
            ans.extend([char] * freq)

        ans2 = "".join(ans)
        print(ans2)
        return ans2


# 하드코딩된 입력
s = "tree"
solution = Solution()
solution.frequencySort(s)
