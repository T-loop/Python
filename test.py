

text = "diesisteinextremlangertextohnesinnaber" \
+ "mitviiielenbuchstabenzumzaehlen"
n = len(text)
BT = {}
for i in range(n):
 x = text[i]
 if x in BT.keys():
  BT[x].append(i)
 else:
  BT[x] = [i]
H = []

print(BT)