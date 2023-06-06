#fungsi bubble sort
def bubble_sort(arr):
    #panjang array
    n = len(arr)
    #perulangan untuk mengiterasi sebanyak n - 1 kali
    for i in range(n):
        # Flag untuk memeriksa apakah ada perubahan pada setiap iterasi, False berarti tidak ada perubahan
        swapped = False
        #perulangan untuk membandingkan pasangan elemen yang berdekatan
        for j in range(0, n - i - 1):
            # Membandingkan elemen ke j dengan elemen sebelahnya
            if arr[j] > arr[j + 1]:
                # Menukar elemen jika elemen ke j lebih besar
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                # Flag untuk memeriksa apakah ada perubahan pada setiap iterasi, Trua berarti ada perubahan
                swapped = True
        # Jika tidak ada pertukaran pada iterasi ini, array sudah terurut maka perulangan terhenti
        if not swapped:
            break
        # Menampilkan array pada setiap iterasi
        print(f"Iterasi {i + 1}: {arr}")
    return arr

# Contoh penggunaan
arr = [64, 34, 25, 12, 22, 11, 90]
print("Array sebelum diurutkan:", arr)
sorted_arr = bubble_sort(arr) #memanggil fungsi bubble sort yang telah didefinisikan
print("Array setelah diurutkan:", sorted_arr)