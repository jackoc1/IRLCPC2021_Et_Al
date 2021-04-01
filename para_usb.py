# READ INPUT
floors = int(input())
no_usb = int(input())

if no_usb == 1:
    print(floors)

def test_throw(floor, maxsafefloor):
    if floor > maxsafefloor:
        return False
    else:
        return True

def no_test_throws(no_usbs, min_floor, max_floor, maxsafefloor, num_tests):

    if (max_floor - min_floor) <2:
        return num_tests

    if no_usbs == 1:
        return num_tests + max_floor - min_floor

    max_test = test_throw(max_floor, maxsafefloor)
    min_test = test_throw(min_floor, maxsafefloor)

    if not min_test:
        return num_tests

    if not max_test:
        #print("Between the range")
        return no_test_throws(no_usbs-1, min_floor, (min_floor + max_floor)//2, maxsafefloor, num_tests + 1)

    elif max_test:
        #print("Safe floor above the range")
        old_max_floor = (max_floor*2)-min_floor
        return no_test_throws(no_usbs, max_floor, old_max_floor, maxsafefloor, num_tests + 1)

max = 0

for i in range(floors):
    test_throws = no_test_throws(no_usb, 1, floors, i+1, 1)
    if test_throws > max:
        max = test_throws

print(max)

