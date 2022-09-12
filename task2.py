import sys

class MinStepsToOneNumber:
    def steps(self):
        def read_from_file():
            filepath = sys.argv[1]
            l = []
            with open(filepath, 'r', encoding='utf-8') as f:
                    l = [int(number) for number in f.readline().split(' ')]
                    return l

        nums = read_from_file()
        least = min(nums)
        total_dif = 0
        for n in nums:
            total_dif += n - least
            
        return total_dif

print(MinStepsToOneNumber().steps())