import re

str = "TGAAGTATGAGA"
print(str)

mo = re.search("TAT", str)
# print the match
print(mo.group())
# print the index
print(mo.span())

mo2 = re.search("TG.", str)
# print the match
print(mo2.group())
# print the index
print(mo2.span())

print(re.findall("TA.", str))
print(re.findall("TG.", str))

mos = re.finditer("TG.", str)
for x in mos:
    print(x.group())
    print(x.span())