q1>def minimumDeleteSum(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n+1) for _ in range(m+1)]

    for i in range(m):
        for j in range(n):
            if s1[i] == s2[j]:
                dp[i+1][j+1] = dp[i][j] + ord(s1[i])
            else:
                dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])

    sum_of_ASCII = sum(ord(ch) for ch in s1 + s2)
    lcs_length = dp[m][n]
    lowest_ascii_sum = sum_of_ASCII - 2 * lcs_length

    return lowest_ascii_sum
q2>def checkValidString(s):
    stack = []

    for ch in s:
        if ch in '(*':
            stack.append(ch)
        elif ch == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(ch)

    count = 0

    for ch in reversed(stack):
        if ch == '(':
            if count == 0:
                return False
            count -= 1
        else:
            count += 1

    return True
q3>def minDistance(word1, word2):
    m, n = len(word1), len(word2)
    dp = [[0] * (n+1) for _ in range(m+1)]

    for i in range(m):
        for j in range(n):
            if word1[i] == word2[j]:
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])

    lcs_length = dp[m][n]
    min_steps = m + n - 2 * lcs_length

    return min_steps

q4>class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def str2tree(s):
    stack = []
    i = 0

    while i < len(s):
        if s[i].isdigit() or s[i] == '-':
            j = i
            while j < len(s) and (s[j].isdigit() or s[j] == '-'):
                j += 1
            value = int(s[i:j])
            node = TreeNode(value)
            stack.append(node)
            i = j - 1
        elif s[i] == '(':
            i += 1
        elif s[i] == ')':
            if len(stack) > 1:
                node = stack.pop()
                parent = stack[-1]
                if not parent.left:
                    parent.left = node
                else:
                    parent.right = node
            i += 1
        i += 1

    return stack[-1]

q5>def compress(chars):
    write = 0
    count = 1

    for read in range(1, len(chars) + 1):
        if read < len(chars) and chars[read] == chars[read - 1]:
            count += 1
        else:
            chars[write] = chars[read - 1]
            write += 1

            if count > 1:
                count_str = str(count)
                for digit in count_str:
                    chars[write] = digit
                    write += 1

            count = 1

    return write

q6>from collections import defaultdict

def findAnagrams(s, p):
    p_freq = [0] * 26
    s_freq = [0] * 26

    for ch in p:
        p_freq[ord(ch) - ord('a')] += 1

    left = 0
    right = 0
    count = len(p)
    result = []

    while right < len(s):
        s_freq[ord(s[right]) - ord('a')] -= 1

        if s_freq[ord(s[right]) - ord('a')] >= p_freq[ord(s[right]) - ord('a')]:
            count -= 1

        if right - left + 1 == len(p):
            if count == 0:
                result.append(left)

            s_freq[ord(s[left]) - ord('a')] += 1

            if s_freq[ord(s[left]) - ord('a')] > p_freq[ord(s[left]) - ord('a')]:
                count += 1

            left += 1

        right += 1

    return result

q7>def decodeString(s):
    stack = []

    for ch in s:
        if ch.isdigit():
            stack.append(int(ch))
        elif ch == '[':
            stack.append(ch)
        elif ch == ']':
            substr = ''

            while stack and stack[-1] != '[':
                substr = stack.pop() + substr

            stack.pop()  # Pop the '[' character

            count = stack.pop()  # Get the repetition count

            stack.append(substr * count)  # Repeat the substring and push it back onto the stack
        else:
            stack.append(ch)

    return ''.join(stack)

q8>def buddyStrings(s, goal):
    if len(s) != len(goal):
        return False

    diff_count = 0
    diff_positions = []

    for i, ch in enumerate(s):
        if ch != goal[i]:
            diff_count += 1
            diff_positions.append(i)

        if diff_count > 2:
            return False

    if diff_count != 2:
        return False

    return s[diff_positions[0]] == goal[diff_positions[1]] and s[diff_positions[1]] == goal[diff_positions[0]]


