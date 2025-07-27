# split()method can be used in string sepation
# if we split the string its tranfer into single words and into a list


program=" the quick brown fox jumps over the lazy dog"

#if we write our sting in different formate this will give the same output
# program= """the quick brown 
# fox jumps \tover 
# the lazy dog"""

words= program.split()
print(words)