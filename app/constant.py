PROBLEMS_DATA = {
    "sum_two_numbers": {
        "title": "Sum of Two Numbers",
        "description": "Write a program that adds two numbers",
        "test_cases": [
            {"input": "1 2", "output": "3"},
            {"input": "0 0", "output": "0"},
            {"input": "-1 5", "output": "4"}
        ],
        "sample_solution": """
        n1, n2 = map(int, input().split())
        print(n1 + n2)
        """
    },
    "fibonacci": {
        "title": "Fibonacci Number",
        "description": "Write a program that prints the nth Fibonacci number",
        "test_cases": [
            {"input": "0", "output": "0"},
            {"input": "1", "output": "1"},
            {"input": "5", "output": "5"},
            {"input": "7", "output": "13"}
        ],
        "sample_solution": """
        def fib(n):
            if n <= 1:
                return n
            return fib(n-1) + fib(n-2)

        n = int(input())
        print(fib(n))
        """
    }
}