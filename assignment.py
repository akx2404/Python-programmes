filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
newfilenames=[]
for i in filenames:
    k=len(i)-4
    if i[k:]==".hpp":
        f= i[:k] + ".h"
        newfilenames.append(f)
    else:
        newfilenames.append(i)

print(newfilenames)