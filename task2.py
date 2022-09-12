class MinStepsToOneNumber:
    def steps(self):
        def read_from_file():
            l = []
            path = r'f1.txt'
            with open(path, 'r', encoding='utf-8') as f:
                    l = [int(number) for number in f.readline().split(' ')]
                    print(l)
                    return l

        nums = read_from_file()
        least = min(nums)
        total_dif = 0
        for n in nums:
            total_dif += n - least
            
        return total_dif

print(MinStepsToOneNumber().steps())