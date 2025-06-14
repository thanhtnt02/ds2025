import matplotlib.pyplot as plt


def assign_value(destination, dest_index, source, source_index):
    # Assigns a value from source to destination
    destination[dest_index] = source[source_index]


def merge_sort(lst):
   # Sorts a list in-place using the merge sort algorithm
    if len(lst) <= 1:
        return

    mid = len(lst) // 2
    left_half = lst[:mid]
    right_half = lst[mid:]

    merge_sort(left_half)
    merge_sort(right_half)

    left_index = 0
    right_index = 0
    merged_index = 0

    while left_index < len(left_half) and right_index < len(right_half):
        if left_half[left_index] <= right_half[right_index]:
            assign_value(lst, merged_index, left_half, left_index)
            left_index += 1
        else:
            assign_value(lst, merged_index, right_half, right_index)
            right_index += 1
        merged_index += 1

    while left_index < len(left_half):
        lst[merged_index] = left_half[left_index]
        left_index += 1
        merged_index += 1

    while right_index < len(right_half):
        lst[merged_index] = right_half[right_index]
        right_index += 1
        merged_index += 1


def plot_list(data, title):
    #Plots a list of numbers.
    plt.plot(range(len(data)), data)
    plt.title(title)
    plt.show()


if __name__ == "__main__":
    data = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    plot_list(data, "Vor dem Sortieren")
    merge_sort(data)
    plot_list(data, "Nach dem Sortieren")

