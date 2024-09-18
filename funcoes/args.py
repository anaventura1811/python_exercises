# PEP 8

def soma(*nums):
    # print(type(nums))
    total = 0
    for n in nums:
        total += n
    return total


def resultado_final(**kwargs):  # key word args
    print(type(kwargs))


# key word args
def resultado_final2(**kwargs):
    print(kwargs['nome'])
    # print(kwargs['nota'])
