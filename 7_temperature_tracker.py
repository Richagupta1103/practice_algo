'''
You decide to test if your oddly-mathematical heating company is fulfilling its All-Time Max, Min, Mean and Mode Temperature Guarantee.

Write a class TempTracker with these methods:


Optimize for space and time. Favor speeding up the getter functions (get_max(),
get_min(), get_mean(), and get_mode()) over speeding up the insert() function.

get_mean() should return a float, but the rest of the getter
functions can return integers. Temperatures will all be inserted as integers.
We will record our temperatures in Fahrenheit, so we can assume they'll all be in the range 0.110.

If there is more than one mode, return any of the modes.
'''


class TempTracker():

    def __init__(self):
        self.list_of_temp = [0]*111
        self.max_temp = 0
        self.min_temp = 0
        self.mean_temp = 0
        self.mode_temp = 0
        self.count = 0

    def insert(self,temp):
        self.list_of_temp[temp] += 1
        if not self.max_temp or self.max_temp < temp:
            self.max_temp = temp
        if not self.min_temp or self.min_temp > temp:
            self.min_temp = temp
        self.mean_temp += temp
        self.count += 1
        if not self.mode_temp or self.mode_temp < self.list_of_temp[temp]:
            self.mode_temp = temp

    def get_max(self):
        return self.max_temp

    def get_min(self):
        return self.min_temp

    def get_mean(self):
        return float(self.mean_temp)/self.count

    def get_mode(self):
        return self.mode_temp


obj = TempTracker()
obj.insert(12)
obj.insert(1)
obj.insert(100)
obj.insert(11)
obj.insert(12)
print obj.get_max()
print obj.get_min()
print obj.get_mean()
print obj.get_mode()

