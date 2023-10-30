import time
import random
start11 = time.time()
start = time.time()



################################################################################################

N = 10000

start = time.time()
def gen():
    a = []
    for i in range (N):
        a.append(random.randint(1,10000))
    return a

def bubble_sort(nums):  
    
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                
                swapped = True


random_list_of_nums = gen()  
bubble_sort(random_list_of_nums)  


end = time.time()
c1 = end - start
print(f'1 код {c1}')


#############################################################################################


start = time.time()

def selection_sort(nums):  
    
    for i in range(len(nums)):
        
        lowest_value_index = i
        
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j
        
        nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]

random_list_of_nums = gen()  
selection_sort(random_list_of_nums)  

end = time.time()
c2 = end - start
print(f'2 код {c2}')


################################################################################################


start = time.time()

def insertion_sort(nums):  
    
    for i in range(1, len(nums)):
        item_to_insert = nums[i]
        
        j = i - 1
        
        while j >= 0 and nums[j] > item_to_insert:
            nums[j + 1] = nums[j]
            j -= 1
        
        nums[j + 1] = item_to_insert

random_list_of_nums = gen()  
insertion_sort(random_list_of_nums)  

end = time.time()
c3 = end - start
print(f'3 код {c3}')


################################################################################################


start = time.time()

def heapify(nums, heap_size, root_index):  
    
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    
    if left_child < heap_size and nums[left_child] > nums[largest]:
        largest = left_child

    
    if right_child < heap_size and nums[right_child] > nums[largest]:
        largest = right_child

    
    if largest != root_index:
        nums[root_index], nums[largest] = nums[largest], nums[root_index]
        
        heapify(nums, heap_size, largest)

def heap_sort(nums):  
    n = len(nums)

    
    for i in range(n, -1, -1):
        heapify(nums, n, i)

    
    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)


random_list_of_nums = gen() 
heap_sort(random_list_of_nums)  


end = time.time()
c4 = end - start
print(f'4 код {c4}')


################################################################################################


start = time.time()

def merge(left_list, right_list):  
    sorted_list = []
    left_list_index = right_list_index = 0

    
    left_list_length, right_list_length = len(left_list), len(right_list)

    for _ in range(left_list_length + right_list_length):
        if left_list_index < left_list_length and right_list_index < right_list_length:
            
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            
            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1

        
        elif left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1
        
        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1

    return sorted_list

def merge_sort(nums):  
    
    if len(nums) <= 1:
        return nums

    
    mid = len(nums) // 2

    
    left_list = merge_sort(nums[:mid])
    right_list = merge_sort(nums[mid:])

    
    return merge(left_list, right_list)


random_list_of_nums = gen()  
random_list_of_nums = merge_sort(random_list_of_nums)  


end = time.time()
c5 = end - start
print(f'5 код {c5}')


################################################################################################


start = time.time()

def partition(nums, low, high):  
    
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1

        j -= 1
        while nums[j] > pivot:
            j -= 1

        if i >= j:
            return j

        
        nums[i], nums[j] = nums[j], nums[i]

def quick_sort(nums):  
    
    def _quick_sort(items, low, high):
        if low < high:
            # This is the index after the pivot, where our lists are split
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(nums, 0, len(nums) - 1)


random_list_of_nums = gen() 
quick_sort(random_list_of_nums)  


end = time.time()
c6 = end - start
print(f'6 код {c6}')

end11 = time.time()
c11 = end11 - start11
print(f'общее время 6 кодов {c11}')

ma = max(c1, c2, c3, c4, c5, c6)

mi = min(c1, c2, c3, c4, c5, c6)

print("самое долгое:", ma)
print("самое быстрое:", mi)