def prefix_sum_array(nums: list) -> list:
    prefix_sum = [nums[0]]
    for index in range(1, len(nums)):
        prefix_sum.append(prefix_sum[index - 1] + nums[index])
    return prefix_sum


def get_even_array(num_array: list) -> list:
    arr_even = [0 if num_array[0] % 2 == 1 else 1]
    for index in range(1, len(num_array)):
        if num_array[index] % 2 == 0:
            arr_even.append(arr_even[index - 1] + 1)
        else:
            arr_even.append(arr_even[index - 1])
    return arr_even


def get_count_of_even_nums(nums_array: list, queries_list: list[list[int]]) -> list:
    prefix_sum_num_array: list = prefix_sum_array(nums_array)
    even_array: list = get_even_array(nums_array)
    even_num_count: list = []
    index = 0
    while len(queries_list) > index:
        if queries_list[index][0] == 0:
            even_num_count.append(even_array[queries_list[index][1]])
        else:
            even_num_count.append(
                even_array[queries_list[index][1]] - (even_array[queries_list[index][0] - 1]))
        index += 1

    return even_num_count


try:
    print("Enter integer elements of an array separated by space : ")
    numbers_array = list(map(int, input().split()))
    queries = int(input("Enter Number of queries : "))
    queries_list: list[list[int]] = []
    for query in range(queries):
        print(f"Enter Range values for query {query + 1} separated by space : ")
        query_list = list(map(int, input().split()))
        queries_list.append(list(query_list))
    print("Even Numbers count : ", get_count_of_even_nums(numbers_array, queries_list))
except ValueError:
    print("Invalid input. Please Enter only Integers separated by space")
