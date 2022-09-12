import sys

class CircularArrayAdvance:
  def steps(self):

    def createList(n):
        l = []
        for i in range(n):
            l.append(i + 1)
        return(l)

    def advance(i, m):
        new_i = (i + m - 1) % n
        return (new_i, nums[i])

    n = 5
    m = 4

    nums = createList(n)

    is_first_iteration = True
    i = None
    s = ""

    while i != 0:
        if is_first_iteration:
            enumerated_val = advance(0, m)
            is_first_iteration = False
        else:
            enumerated_val = advance(i, m)
        i = enumerated_val[0]
        s += str(enumerated_val[1])
    return s

print(CircularArrayAdvance().steps())