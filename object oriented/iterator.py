# Iterator
nums = [4,3,5,6]
# print(nums[1])
# for i in nums:
#     print(i)

# iterator
# it = iter(nums)
# print(it.__next__())
# print(it.__next__())
#
# print(next(it))
#
# for i in nums:
#     print(i)


# Mahni iterator kan lo siam anga
# Mahni a iterator kan siam dawn chuan pawimawh deuh pahnih a awm a. chung te chu:
# iter() method leh next() method a ni.
class Topten:
    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= 10:
            val = self.num
            self.num += 1

            return val
        else:
            raise StopIteration


values = Topten()
print(next(values))  # hei hi a print nawn tawh lovang a hnuai a mi hian.
for i in values:
    print(i)