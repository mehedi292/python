import re
pattern = r"colour"
if re.match(pattern,"colour is a colour, I love red colour"):
    print("Match")
else:
    print("Not Matched")



# example more search 

import re
pattern  = r"colour"
text = "My favourite colour is Red."
match = re.search(pattern,text)
if match:
    print(match.start())
    print(match.end())
    print(match.span())