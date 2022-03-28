class Solution5:
    # １文字場合と２文字の場合で中心を定めて2N-1回ループする
    # ループ内ループを含むとO(N^2)だがDP解よりも平均的に早い（LeetCodeのテストケースだと）
    def _longestPalindrome(self, s: str) -> str:
        longest = s[0]

        # Odd
        for i in range(0, len(s)):
            # 奇数なら中心は１文字
            left = i - 1
            right = i + 1

            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            if len(longest) < right - left - 1:
                longest = s[left + 1: right]

        # Even
        for i in range(0, len(s) - 1):
            # 偶数なら中心は２文字
            left = i
            right = i + 1

            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            if len(longest) < right - left - 1:
                longest = s[left + 1: right]

        return longest

    # DP解
    """
    input = cbabcとすると初期では以下のDP表ができる。
    `?`は走査して回文チェックをする箇所、`x`は走査する必要のない箇所。
    意味はi行目j列目 = 文字のj番目からi番目までの部分文字列。
    ## 0 1 2 3 4
    0  T x x x x --> 1ループ目
    1  ? T x x x --> 2ループ目
    2  ? ? T x x --> 3ループ目
    3  ? ? ? T x --> 4ループ目
    4  ? ? ? ? T --> 5ループ目

    ポイントは２点。
    1. 対角線上は当然Trueになり、その対角線の左下 or 右上 のみしか走査する必要がないこと
    2. とある端同士の文字が一致するとき、その間の文字列が回文かどうかをチェックすればいいこと
       （例えば、0,4番目の文字列が一致したとき、1,3番目の文字列までが回分であれば、0,4番目までの文字列も回文）
    """
    def longestPalindrome(self, s: str) -> str:
        dp = [[False] * len(s) for _ in range(len(s))]
        longest = s[0]
        for i in range(len(s)):
            dp[i][i] = True

        for i in range(len(s)):
            for j in range(i):
                # 端同士が一致するかつ（その間の文字列が回文 or 左端〜右端が２文字）
                if s[i] == s[j] and (dp[i-1][j+1] or i == j + 1):
                    dp[i][j] = True
                    if i - j + 1 > len(longest):
                        longest = s[j:i+1]

        return longest
