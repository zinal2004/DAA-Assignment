def sum(n):
    n_str = str(n)
    total=0
    for i in n_str:
        total += int(i)
    return total
def main():
    num = int(input("Number: "))
    digit_sum = sum(num)
    print(f"The sum of digits of {num} is {digit_sum}.")
if __name__ =="__main__":
    main()
