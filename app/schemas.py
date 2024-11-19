from pydantic import BaseModel
from typing import Optional, List

class TestCase(BaseModel):
    input: str

class ProblemTestCase(BaseModel):
    input: str
    output: str

class CodeRequest(BaseModel):
    code: str
    problem_id: str
    language: str = "python"

class TestResult(BaseModel):
    input: str 
    expected_output: str
    actual_output: str
    passed: bool
    error: Optional[str] = None

class CodeResponse(BaseModel):
    results: List[TestResult]
    total_tests: int
    passed_tests: int
    execution_time: float
