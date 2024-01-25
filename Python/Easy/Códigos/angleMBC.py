import math

AB, BC = int(input()), int(input())

AC = math.sqrt(AB**2 + BC**2)
ang_ACB = round(math.degrees(math.acos(BC/AC)))
ang_MBC = ang_ACB

result = f"{ang_MBC}\u00b0"
print(result)
