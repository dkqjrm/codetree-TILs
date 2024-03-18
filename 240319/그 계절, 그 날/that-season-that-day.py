Y, M, D = map(int, input().split())

def check_yoon(Y):
    if Y % 4 == 0:
        if Y % 100 == 0:
            if Y % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def check_season(M):
    if 3 <= M <= 5:
        return 'Spring'
    elif 6 <= M <= 8:
        return 'Summer'
    elif 9 <= M <= 11:
        return 'Fall'
    elif M == 12 or M <= 2:
        return 'Winter'

def check_day(Y, M, D):
    yoon = check_yoon(Y)

    if M in [1, 3, 5, 7, 8, 10, 12]:
        if D < 1 or D > 31:
            return -1
        else:
            return check_season(M)
    elif M == 2:
        if yoon:
            if D < 1 or D > 29:
                return -1
            else:
                return check_season(M)
        else:
            if D < 1 or D > 28:
                return -1
            else:
                return check_season(M)
    elif M in [4, 6, 9, 11]:
        if D < 1 or D > 30:
            return -1
        else:
            return check_season(M)

print(check_day(Y, M, D))