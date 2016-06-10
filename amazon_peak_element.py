def find_peak_elem(elem, start, end , l):
    mid = (start+end)/2
    if (mid == 0 or elem[mid] >= elem[mid-1]) and (mid == l-1 or elem[mid] >= elem[mid+1]):
        print elem[mid]
        return True
    if mid > 0 and elem[mid] < elem[mid-1]:
        find_peak_elem(elem, start, mid-1,l)
    else:
        find_peak_elem(elem, mid+1, end, l)

elem = [1, 2, 3, 4, 5]
start = 0
end = len(elem)-1
find_peak_elem(elem, start, end, end+1)



# class Celsius:
#     def __init__(self, temperature = 0):
#         self._temperature = temperature
#
#     def to_fahrenheit(self):
#         return (self.temperature * 1.8) + 32
#
#     @property
#     def temperature(self):
#         print("Getting value")
#         return self._temperature
#
#     @temperature.setter
#     def temperature(self, value):
#         if value < -273:
#             raise ValueError("Temperature below -273 is not possible")
#         print("Setting value")
#         self._temperature = value
#
# c = Celsius()
# c.temperature = 300
# print c.temperature



