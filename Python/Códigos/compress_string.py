from itertools import groupby

S = input()

groups = groupby(S)

compressed_string = ' '.join(f"({len(list(group))}, {c})" for c, group in groups)

print(compressed_string)
