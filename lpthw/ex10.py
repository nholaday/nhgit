tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\tCat food
\tFishies
\tCatnip\n\tGrass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

r_cat = "%r"

print r_cat % tabby_cat
print r_cat % persian_cat
print r_cat % backslash_cat
print r_cat % fat_cat
