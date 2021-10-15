def solution(enroll, referral, seller, amount):
    answer = []
    entry = {name: [recommand, 0] for name, recommand in list(zip(enroll, referral))}
    for seller, amount in list(zip(seller, amount)):
        commission(entry, seller, amount * 100)

    answer = [int(value) for name, value in entry.values()]

    return answer


def commission(entry, seller, benefit):
    if seller == '-':
        return

    remain = benefit * 10 // 100

    if remain < 1:
        entry[seller][1] += benefit
        return

    entry[seller][1] += benefit - remain
    seller = entry[seller][0]
    commission(entry, seller, remain)