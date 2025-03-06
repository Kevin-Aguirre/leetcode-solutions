# Problem 13
# Large Sum
# Difficulty rating: 5%
# 03-06-2025

def main():
    with open('nums.txt', 'r') as ifile:
        nums = [int(line.strip()) for line in ifile.readlines()] 
    total_sum = sum(nums) 
    first_10_digits = str(total_sum)[:10]  
    print(first_10_digits)  

main()