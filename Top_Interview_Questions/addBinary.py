class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) < len(b):
            a, b = b, a

        result = list(a)

        carry = 0
        a_i, b_i = len(a) - 1, len(b) - 1
        while a_i >= 0: # cus a is longer
            cur_add = carry + int(a[a_i])
            if b_i >= 0:
                cur_add += int(b[b_i])

            result[a_i] = "0"
            carry = 0
            if cur_add == 1:
                result[a_i] = "1"
            elif cur_add == 2:
                carry = 1
            elif cur_add == 3:
                result[a_i] = "1"
                carry = 1
        
            a_i -= 1
            b_i -= 1

        if carry == 1:
            return "1" + "".join(result)
        return "".join(result)