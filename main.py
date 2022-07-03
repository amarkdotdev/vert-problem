import random

NUM_OF_BOXES_AND_PRISONERS = 10
NUM_OF_BOXES_AND_PRISONERS += 1

set_of_good_boxes = []


def find_number(prisoner, set_of_boxes, number_of_tries):
    counter = number_of_tries
    index = prisoner

    while counter != 0:
        counter -= 1

        if prisoner == set_of_boxes[index]:
            return True
        else:
            index = set_of_boxes[index]
    return False


def get_boxes():
    dict_of_boxes = {i: 0 for i in range(1, NUM_OF_BOXES_AND_PRISONERS)}
    list_of_all_numbers = [i for i in range(1, NUM_OF_BOXES_AND_PRISONERS)]

    key = 1
    while list_of_all_numbers:
        value = random.choice(list_of_all_numbers)
        list_of_all_numbers.remove(value)
        dict_of_boxes[key] = value
        key += 1

    return dict_of_boxes


def do_a_test():
    prisoner_list = [i for i in range(1, NUM_OF_BOXES_AND_PRISONERS)]
    counter_of_goods = 1

    boxes = get_boxes()

    for prisoner in prisoner_list:
        if find_number(prisoner, boxes, int(len(boxes) / 2)):
            counter_of_goods += 1
        else:
            return False

    if counter_of_goods == NUM_OF_BOXES_AND_PRISONERS:
        set_of_good_boxes.append(boxes)
        return True


def main():
    global NUM_OF_BOXES_AND_PRISONERS
    NUM_OF_BOXES_AND_PRISONERS = int(input("How many prisoners and boxes? (Press 0 to leave at 100) "))
    NUM_OF_BOXES_AND_PRISONERS = 100 if NUM_OF_BOXES_AND_PRISONERS == 0 else 1 + 1  # 1+1 does nothing
    NUM_OF_BOXES_AND_PRISONERS += 1

    # sample_size = 1000
    sample_size = int(input("Enter the amount of times you would like to do this test (sample size): "))

    counter = 0
    for i in range(sample_size):
        if do_a_test():
            counter += 1

    print(f"At the and, out of {sample_size} tests, we got {counter} successes. That's {counter}/{sample_size}:")
    print(counter / sample_size)

    print(f'VERY CLOSE TO 1/3!')

    # OPTIONAL: IF YOU WANT TO SEE THE GOOD SETS, UNCOMMENT THE LINES BELOW!
    # print(f'The good boxes or sets are:')
    # for box in set_of_good_boxes:
    #     print(box)


main()
