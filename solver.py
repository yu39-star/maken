#get numbers
nums = input("type nums and ans: ").rstrip().split(" ")
first = float(nums[0])
second = float(nums[1])
third = float(nums[2])
forth = float(nums[3])
ans = float(nums[4])
numbers = [first, second, third, forth]
kotaetati = []
atta = False
print("I'm trying to make "+str(int(ans))+" with "+str(int(first))+", "+str(int(second))+", "+str(int(third))+", "+str(int(forth))+".")

print("Answers:")
nans = False
#solve make n
for i in range(1, 25, 1):
#
    if i > 18:
        iti = numbers[3]
        next = i - 18

        if next > 4:
            ni = numbers[2]
            if next % 2 == 1:
                san = numbers[0]
                yon = numbers[1]
            else:
                san = numbers[1]
                yon = numbers[0]

        elif next > 2:
            ni = numbers[1]
            if next % 2 == 1:
                san = numbers[0]
                yon = numbers[2]
            else:
                san = numbers[2]
                yon = numbers[0]

        elif next > 0:
            ni = numbers[0]
            if next % 2 == 1:
                san = numbers[1]
                yon = numbers[2]
            else:
                san = numbers[2]
                yon = numbers[1]
#
    elif i > 12:
        iti = numbers[2]
        next = i - 12

        if next > 4:
            ni = numbers[3]
            if next % 2 == 1:
                san = numbers[0]
                yon = numbers[1]
            else:
                san = numbers[1]
                yon = numbers[0]

        elif next > 2:
            ni = numbers[1]
            if next % 2 == 1:
                san = numbers[0]
                yon = numbers[3]
            else:
                san = numbers[3]
                yon = numbers[0]

        elif next > 0:
            ni = numbers[0]
            if next % 2 == 1:
                san = numbers[1]
                yon = numbers[3]
            else:
                san = numbers[3]
                yon = numbers[1]
#
    elif i > 6:
        iti = numbers[1]
        next = i - 6

        if next > 4:
            ni = numbers[3]
            if next % 2 == 1:
                san = numbers[0]
                yon = numbers[2]
            else:
                san = numbers[2]
                yon = numbers[0]

        elif next > 2:
            ni = numbers[2]
            if next % 2 == 1:
                san = numbers[0]
                yon = numbers[3]
            else:
                san = numbers[3]
                yon = numbers[0]

        elif next > 0:
            ni = numbers[0]
            if next % 2 == 1:
                san = numbers[2]
                yon = numbers[3]
            else:
                san = numbers[3]
                yon = numbers[2]
#
    elif i > 0:
        iti = numbers[0]
        next = i

        if next > 4:
            ni = numbers[3]
            if next % 2 == 1:
                san = numbers[1]
                yon = numbers[2]
            else:
                san = numbers[2]
                yon = numbers[1]

        elif next > 2:
            ni = numbers[2]
            if next % 2 == 1:
                san = numbers[1]
                yon = numbers[3]
            else:
                san = numbers[3]
                yon = numbers[1]

        elif next > 0:
            ni = numbers[1]
            if next % 2 == 1:
                san = numbers[2]
                yon = numbers[3]
            else:
                san = numbers[3]
                yon = numbers[2]
    #print(f"{iti} {ni} {san} {yon}")
    #set symbol
    for j in range(1, 65, 1):
        if j > 48:
            ikko = "/"
            next = j - 48

        elif j > 32:
            ikko = "*"
            next = j - 32

        elif j > 16:
            ikko = "-"
            next = j - 16

        elif j > 0:
            ikko = "+"
            next = j

        if next > 12:
            niko = "/"
            next = next - 12
        elif next > 8:
            niko = "*"
            next = next - 8
        elif next > 4:
            niko = "-"
            next = next - 4
        elif next > 0:
            niko = "+"
            next = next

        if next == 4:
            sanko = "/"
        elif next == 3:
            sanko = "*"
        elif next == 2:
            sanko = "-"
        elif next == 1:
            sanko = "+"
        
        try:
            value = eval(f"( ( {iti} {ikko} {ni} ) {niko} {san} ) {sanko} {yon}")
        except ZeroDivisionError:
            continue
        if abs(value - ans) < 1e-6:
            kotae = f"( ( {int(iti)} {ikko} {int(ni)} ) {niko} {int(san)} ) {sanko} {int(yon)}"
            for x in range(len(kotaetati)):
                if kotaetati[x] == kotae:
                    atta = True
                    break
            if not atta:
                kotaetati.append(kotae)
                print(kotae)
                nans = True
                atta = False

        try:
            left = eval(f"{iti}{ikko}{ni}")
            right = eval(f"{san}{sanko}{yon}")
            value = eval(f"{left}{niko}{right}")
        except ZeroDivisionError:
            continue
        if abs(value - ans) < 1e-6:
            kotae = f"( {int(iti)} {ikko} {int(ni)} ) {niko} ( {int(san)}  {sanko} {int(yon)} )"
            for x in range(len(kotaetati)):
                if kotaetati[x] == kotae:
                    atta = True
                    break
            if not atta:
                kotaetati.append(kotae)
                print(kotae)
                nans = True
                atta = False

if not nans:
    print("Nothing")

#        if int(eval(math)) == int(ans):
#            print(int(iti),ikko,int(ni),niko,int(san),sanko,int(yon))
"""        # solver
        if ikko == "+":
            cache =  iti + ni
        if ikko == "-":
            cache = iti - ni
        if ikko == "*":
            cache = iti * ni
        if ikko == "/":
            cache = iti / ni

        if niko == "+":
            cache =  cache + san
        if niko == "-":
            cache = cache - san
        if niko == "*":
            cache = cache * san
        if niko == "/":
            cache = cache / san

        if sanko == "+":
            cache =  cache + yon
        if sanko == "-":
            cache = cache - yon
        if sanko == "*":
            cache = cache * yon
        if sanko == "/":
            cache = cache / yon
if cache == ans:
    print(int(iti),ikko,int(ni),niko,int(san),sanko,int(yon))
"""