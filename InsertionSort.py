def insertion_sort(arr):
    n = len(arr)
    
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        # Memindahkan elemen yang lebih besar dari key ke posisi setelahnya
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        # Menampilkan array pada setiap iterasi
        print(f"Iterasi {i}: {arr}")
    return arr

# Contoh penggunaan
arr = [64, 34, 25, 12, 22, 11, 90]
print("Array sebelum diurutkan:", arr)
sorted_arr = insertion_sort(arr)
print("Array setelah diurutkan:", sorted_arr)