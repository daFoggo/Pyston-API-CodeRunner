from pyston import PystonClient, File
from .schemas import CodeRequest, CodeResponse, TestResult
from .constant import PROBLEMS_DATA
import time
from fastapi import HTTPException
from typing import Optional, Tuple

class CodeExecutor:
    def __init__(self):
        self.client = PystonClient()
    
    # Execute code with a single test case
    async def execute_test_case(self, code: str, language: str, test_case_input: str) -> Tuple[Optional[str], Optional[str]]:
        try:
            code_file = File(code)
            result = await self.client.execute(
                language=language,
                files=[code_file],
                stdin=test_case_input
            )
                
            actual_output = ""
            
            # Check if the result object has a raw_output attribute == Success
            if hasattr(result, 'raw_output'):
                actual_output = result.raw_output
            else:
                print("Result object:", result.__dict__)
                actual_output = str(result)
            
            return actual_output.strip() if actual_output else "", None
                
            
        except Exception as e:
            print(f"Error executing code: {str(e)}")
            return None, str(e)

    # Execute code with all test cases
    async def execute_with_test_cases(self, request: CodeRequest) -> CodeResponse:
        if request.problem_id not in PROBLEMS_DATA:
            raise HTTPException(status_code=404, detail="Problem not found")

        # REPLACE W DATABASE
        problem_data = PROBLEMS_DATA[request.problem_id]
        test_cases = problem_data["test_cases"]
        
        results = []
        total_time = 0
        passed_tests = 0

        for test_case in test_cases:
            start_time = time.time()
            output, error = await self.execute_test_case(
                request.code,
                request.language,
                test_case["input"]
            )
            end_time = time.time()
            total_time += (end_time - start_time)

            # Compare results
            passed = False
            if error is None and output is not None:
                passed = output.strip() == test_case["output"].strip()
                if passed:
                    passed_tests += 1

            results.append(TestResult(
                input=test_case["input"],
                expected_output=test_case["output"],
                actual_output=output if output is not None else "",
                passed=passed,
                error=error
            ))

        return CodeResponse(
            results=results,
            total_tests=len(test_cases),
            passed_tests=passed_tests,
            execution_time=total_time
        )