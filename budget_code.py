arr_2d = [
    [3, 3, 3, 3, 3, 3, 5, 6],
    [2.5, 2.5, 2.5, 2.5, 2.5, 4, 4],
    [4, 4, 4, 4, 4, 4, 10],
    [1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5],
    [2, 2, 2, 2, 2, 4, 4]
]


keys = ["TOI", "Hindu", "ET", "BM", "HT"]


dicti= {}


for i, row in enumerate(arr_2d):
    key = keys[i] 
    # Finding Sum of each row representing the price of newspaper.
    row_sum = sum(row)  
    # Maping the newspaper name to the sum.    
    dicti[key] = row_sum  


# Taking budget as input:
budget = float(input())

found_pairs = []
for i in range(len(keys)):
    for j in range(i+1, len(keys)):
        if dicti[keys[i]] + dicti[keys[j]] < budget:
            found_pairs.append((keys[i], keys[j]))


out = ", ".join([f"{{{pair[0]}, {pair[1]}}}" for pair in found_pairs])


if out:
    
    print(out)
else:
    print("Budget too low")