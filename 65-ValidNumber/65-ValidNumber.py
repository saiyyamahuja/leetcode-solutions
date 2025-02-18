class Solution:
    def isNumber(self, s: str) -> bool:
        allow_exp = True
        allow_sign = True
        allow_dot = True
        numerical = False

        for c in s:
            if c in ["+", "-"]:
                if not allow_sign:
                    return False

            elif c == ".":
                if not allow_dot:
                    return False

                allow_dot = False

            elif ord("0") <= ord(c) <= ord("9"):  # digit
                numerical = True

            elif c not in ["e", "E"]:  # regular character - not number
                return False

            allow_sign = False

            if c in ["e", "E"]:
                if not numerical or not allow_exp:
                    return False

                allow_exp = False
                allow_sign = True
                allow_dot = False
                numerical = False

        return numerical