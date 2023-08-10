list_vowels = "ауоыиэяюёе" 
list_input = input("Введите стих:").lower().split()
list_count = [] 
for el in list_input:    
    list_count.append(sum(el.count(i) for i in list_vowels))

for i in range(1, len(list_count)):
    if list_count[0] != list_count[i]:
        print("Пам парам")
        break
else:
    print("Парам пам-пам")
