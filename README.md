# 1. Create .venv and active
python -m venv .venv

.venv\Scripts\Activate.ps1

# 2. Install requirements
pip install -r requirements.txt

# 3. Test api
- For Execute API :
```
{
    "problem_id": "sum_two_numbers",
    "code": "n1, n2 = map(int, input().split())\nprint(n1 + n2)",
    "language": "python"
}
```

- For others, just use GET