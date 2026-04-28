class ListAnalyzer:
    def __init__(self, lst):
        self.lst = lst

    def highest_repeating_value(self):
        counts = {}
        for num in self.lst:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1

        max_count = 0
        max_num = 0
        for num, count in counts.items():
            if count > max_count:
                max_count = count
                max_num = num
        return max_num


list1 = [1, 2, 3, 4, 5, 6, 7, 8, 1, 1, 1, 3, 5, 2, 4]
analyzer = ListAnalyzer(list1)
print(analyzer.highest_repeating_value())
