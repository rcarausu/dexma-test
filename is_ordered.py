def check_order(n):
    s = str(n)
    if len(s) == 0 or len(s) == 1:
        return True
    if s[0] <= s[1]:
        return check_order(int(s[1:]))
    return False

print(check_order(142345))
