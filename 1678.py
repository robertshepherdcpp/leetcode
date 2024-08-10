class Solution:
    def interpret(self, command: str) -> str:
        skip = False
        final = ""
        for i in command:
            if not skip:
                if i == "(":
                    skip = True
                elif i == "a":
                    skip = True
                elif i == "G":
                    final += "G"
            else:
                if i == ")":
                    final += "o"
                if i == "l":
                    final += "al"
                if i != "a":
                    skip = False
        return final
