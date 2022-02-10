dic = {}


def func(list_):
    for i in list_:
        if type(i) in [int]:
            dic['int'] = i
        elif type(i) in [bool]:
            dic['bool'] = i
        elif type(i) in [float]:
            dic['float'] = i
        elif type(i) in [str]:
            dic['str'] = i
        elif type(i) is not None:
            dic['none'] = None


func([1, 4.7, 'hi', False, None])
print(dic)
