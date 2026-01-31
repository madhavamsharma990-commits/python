class pair_elements:
    def twosum(self, number, target):
        lookup = {}
        for i, num in enumerate(number):
            if target - num in lookup:
                return (lookup[target - num], i)
            lookup[num] = i
value = int(input("Enter sum for which you want to make this serch: "))
print( pair_elements().twosum((10, 20, 30, 40, 50, 60, 70), value))