from queue import LifoQueue


class Solution:
    def isValid(self, s: str) -> bool:
        correspondings = {')': '(', ']': '[', '}': '{'}
        left = ['(', '[', '{']
        right = [')', ']', '}']

        q = LifoQueue()

        for idx, i in enumerate(s):
            if i in left:
                q.put_nowait(i)
            elif i in right:
                if q.qsize() == 0 or correspondings[i] != q.get_nowait():
                    return False
        if q.queue == []:
            return True
        else:
            return False


if __name__ == "__main__":
    s = Solution()
    print(
        s.isValid('}')
    )
