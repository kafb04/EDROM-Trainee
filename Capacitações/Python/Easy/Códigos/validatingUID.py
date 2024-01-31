import re

def is_valid_uid(uid):
    condition1 = len(re.findall(r"[A-Z]", uid)) >= 2
    condition2 = len(re.findall(r"\d", uid)) >= 3
    condition3 = len(re.findall(r"[^\w\d]", uid)) == 0
    condition4 = len(set(uid)) == len(uid)
    condition5 = len(uid) == 10
    return all([condition1, condition2, condition3, condition4, condition5])

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        uid = input()
        result = 'Valid' if is_valid_uid(uid) else 'Invalid'
        print(result)
