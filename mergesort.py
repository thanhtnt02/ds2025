import matplotlib.pyplot as plt


def assign_value(destination, dest_index, source, source_index):
    """Assigns a value from source to destination."""
    destination[dest_index] = source[source_index]


def merge_sort(lst):
    """Sorts a list in-place using the merge sort algorithm."""
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


# Ursprüngliche Liste
my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]

# Plot vor dem Sortieren
plt.figure(figsize=(8, 4))
plt.bar(range(len(my_list)), my_list, color='steelblue')
plt.title("Vor dem Sortieren (MergeSort)")
plt.xlabel("Index")
plt.ylabel("Wert")
plt.grid(True, axis='y', linestyle='--', linewidth=0.5)
plt.tight_layout()
plt.show()

# Sortieren
merge_sort(my_list)

# Plot nach dem Sortieren
plt.figure(figsize=(8, 4))
plt.bar(range(len(my_list)), my_list, color='seagreen')
plt.title("Nach dem Sortieren (MergeSort)")
plt.xlabel("Index")
plt.ylabel("Wert")
plt.grid(True, axis='y', linestyle='--', linewidth=0.5)
plt.tight_layout()
plt.show()

