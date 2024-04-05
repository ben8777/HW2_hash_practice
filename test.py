char_count = {}
with open('data.txt', 'r') as file:
    for line in file:
          char = line.strip()
          if char not in char_count:
              char_count[char] = 1
          else:
              char_count[char] += 1

total_unique_chars = len(char_count)

print(f"總共有 {total_unique_chars} 個不重複的英文字：")
for char, count in char_count.items():
    print(f"{char}: {count} 次")