def shell_sort(arr, h_sequence):
    comparisons = 0
    n = len(arr)

    for h in h_sequence:
        for i in range(h, n):
            temp = arr[i]
            j = i
            comparisons += 1

            while j >= h and arr[j - h] > temp:
                arr[j] = arr[j - h]
                j -= h
                comparisons += 1

            arr[j] = temp

    return comparisons


def generate_h_sequence(log_base, n):
    h_sequence = []
    h = 1

    while h < n:
        h_sequence.append(h)
        h = log_base * h + 1

    return h_sequence


def main():
    with open('input.txt', 'r') as f:
        arr = list(map(int, f.readline().split()))

    n = len(arr)

    log_base_2 = int(n.bit_length())  # ⌊log2 N⌋
    h_sequence_1 = generate_h_sequence(2, log_base_2)

    log_base_3 = int((2 * n + 1).bit_length() - 1)  # ⌊log3 (2N + 1)⌋ − 1
    h_sequence_2 = generate_h_sequence(3, log_base_3)

    sorted_arr_1 = arr.copy()
    comparisons_1 = shell_sort(sorted_arr_1, h_sequence_1)

    sorted_arr_2 = arr.copy()
    comparisons_2 = shell_sort(sorted_arr_2, h_sequence_2)

    with open('output.txt', 'w') as f:
        f.write(' '.join(map(str, sorted_arr_1)) + '\n')
        f.write(f'{comparisons_1}\n')
        f.write(' '.join(map(str, sorted_arr_2)) + '\n')
        f.write(f'{comparisons_2}\n')


if __name__ == "__main__":
    main()
