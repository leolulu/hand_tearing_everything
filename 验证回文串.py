import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r"[^0-9a-z]", '', s.lower())
        pb, pe = 0, len(s) - 1
        while pe > pb:
            if s[pe] != s[pb]:
                return False
            pb += 1
            pe -= 1
        return True


if __name__ == "__main__":
    s = Solution()
    print(
        s.isPalindrome("A man, a plan, a canal: Panama")
    )
