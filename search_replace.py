import re
pattern = r"colour"
text = "My favourite colour is red. I love blue colour as well which is most beautiful"
text1 = re.sub(pattern,"color",text)
print(text1)



# match character class

import re 
pattern = r"[A-Z][a-z][0-9]"
if re.match(pattern,"Aggafdfbdf072mj"):
    print("Matched")
else:
    print("Not matched")