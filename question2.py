from interval import Interval
#############THE QUESTION IS###########
# input a list of intervals
# expected output: how many intersections are there for the list of intervals
#######################################gs

# intuition 1:  first sort the list by starting point, if we don't, it would be a mess to check interval
# intuition 2: if the given intervals are sorted, we just need to check on by one from first to last.
# intuition 3: draw on paper more, don't waste the time thinking only
# in this process, if 2 intervals are intersected

itlist = []
for i in range(5):
    it = Interval.generateRandomIntervalPairWithInRange(1, 100);
    itlist.append(it)

print("...before sorting...")
for item in itlist:
    item.printInterval()

# do real stuff
# this is a sorted list of the current group of right end(group means the sections in the group are connected by way of intersection)

union_end=[]

final_result = []

# sort interval by start
itlist.sort(key=lambda x: x.start, reverse=False)
print("...after sorting...")
for item in itlist:
    item.printInterval()

for item in itlist:
    if(len(union_end)<1):
        union_end.append(item.end)
    else:
        # if no intersection at all
        if(item.start>union_end[-1]):
            union_end = []
        else:
            # do truncate and union to update the list
            # truncate the union_end list so that the items smaller than start of interval is dropped
            while(True):
                if(union_end[0]<item.start):
                    del union_end[0]
                else:
                    break
            # the the intersections and append to final result
            # add the current right end to the union
            pos = -1
            flag=False
            hasFollow = False
            for i in range(len(union_end)):
                if(union_end[i]==item.end):
                    flag=True
                    pos=i
                    hasFollow=True
                    break
                if (union_end[i] > item.end):
                    union_end.insert(i, item.end)
                    pos = i
                    flag = True
                    hasFollow=True
                    break
            if(flag==False):
                union_end.append(item.end)
                pos = len(union_end)-1

            if(hasFollow):
                for i in range(pos+1):
                    final_result.append(Interval(item.start, union_end[i]))
            else:
                for e in union_end[0:-1]:
                    final_result.append(Interval(item.start, e))

print("intersections:=====")
for item in final_result:
    item.printInterval()

print("===number of intersections:=====")
print(len(final_result))


#print("=========sequence after sorting======")

# ============ method 2:
# class SortableData(object):
#     def __init__(self, val, type, index):
#         self.val = val
#         self.type=type
#         self.index=index
#
#     def printPretty(self):
#         print(str(self.val)+","+self.type+str(self.index))
#
# sortableList = []
# for i in range(len(itlist)):
#     el = itlist[i]
#     sortableList.append(SortableData(el.start, 's', i))
#     sortableList.append(SortableData(el.end, 'e', i))
#
#
# sortableList.sort(key=lambda x: x.val, reverse=False)
#
# cnt = 0;
# maxCount = 1
# for item in sortableList:
#     if(item.type=='s'):
#         cnt+=1
#     else:
#         cnt-=1
#     if(cnt>maxCount):
#         maxCount = cnt
#     item.printPretty()
#
#
# print("=========")
# print(maxCount)
