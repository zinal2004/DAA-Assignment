def gen_fibonacci(n):
    if n <=0:
        return "give a positive integer"
    if n == 2:
        return [0,1]
    else:
        fibonacci_series = [0,1]
        while len(fibonacci_series) < n:
            next_term = fibonacci_series[-1] + fibonacci_series[-2]
            fibonacci_series.append(next_term)
        return fibonacci_series
def main():
    num = int(input("number of terms: "))
    fibonacci_series = gen_fibonacci(num)
    print(f"fibonacci series upto number {num} is {fibonacci_series}")

if __name__=="__main__":
    main()
