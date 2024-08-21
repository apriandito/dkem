for i in range(10):
    if i == 5:
        break  # Hentikan loop ketika i adalah 5
    if i % 2 == 0:
        continue  # Lompat ke iterasi berikutnya jika i genap
    print(i)
