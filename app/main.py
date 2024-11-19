from fastapi import FastAPI, HTTPException
from .schemas import CodeRequest, CodeResponse
from .executor import CodeExecutor
from .constant import PROBLEMS_DATA

app = FastAPI(title="PISTON CODE RUNNER")
executor = CodeExecutor()


@app.post("/api/execute", response_model=CodeResponse)
async def execute_code(request: CodeRequest):
    try:
        return await executor.execute_with_test_cases(request)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Get all problems
@app.get("/api/problems")
async def get_problems():
    return {
        "problems": [
            {
                "id": problem_id,
                "title": data["title"],
                "description": data["description"]
            }
            for problem_id, data in PROBLEMS_DATA.items()
        ]
    }

# Get problem w ID
@app.get("/api/problems/{problem_id}")
async def get_problem(problem_id: str):
    if problem_id not in PROBLEMS_DATA:
        raise HTTPException(status_code=404, detail="Problem not found")
    
    problem = PROBLEMS_DATA[problem_id]
    return {
        "id": problem_id,
        "title": problem["title"],
        "description": problem["description"],
        "sample_solution": problem["sample_solution"]
    }