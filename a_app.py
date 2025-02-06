# ---- Session on Clean Coding, Data types, Functions, TDD ----
hr = "-" * 40

# Refactor the following

# Assigning Lists
#              0  1  2   3      4  5
list_sample = [1, 2, 3, "Four", 5, 6]

# Access Lists
print("     Item 1:", list_sample[0])
print("     Item 4:", list_sample[3])
print("  Item Last:", list_sample[-1])
print("Slice items:", list_sample[2:len(list_sample)], f" array length: {len(list_sample)}")
# Loop through Lists
print(" ---- Listing Items in List ----")
for item in list_sample:
  print(item)
print(" ---- Listing Items using range() ----")
# for using range(start,stop,step) / range(stop)
for index in range(len(list_sample)):
  print(index, ":", list_sample[index])
print(hr)

email = "j@em2.com"

# Dictionary : { key_1: value_1, key_2: value_2, ..... key_n: value_n }
dictionary_sample = {
  "id" : 123,
  "name": "John",
  "email" : [
      "j@em.com",
      email
  ]
}

# Access dictionaries individually
print("   ---- Access Dictionaries ----")
print("     Id:")
print("   Name:")
print(" Emails:")
print("Email 1:")
print("Email 2:")
print(hr)
# Loop through dictionaries print key : value - element type
# for
print("-"*20)

