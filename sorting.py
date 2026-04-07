# selection sort                 
nums = [3,4,5,2,1,6,0,7]


def selection_sort(nums):
    length = len(nums)
    for i in range(0, length):
        minimum_index = i
        for j in range(i + 1, length):
            if nums[j] < nums[minimum_index]:
                minimum_index = j

        nums[i], nums[minimum_index] = nums[minimum_index], nums[i]

    return nums


# print(selection_sort(nums))

# bubble sort

def bubble_sort(nums):
    length = len(nums)
    is_swap = False
    for i in range(length - 2, -1, -1):
        for j in range(0, i + 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                is_swap = True
            else:
                pass
        if not is_swap:
             return nums

    return nums

# print(bubble_sort(nums))

#insertion sort






