# Import necessary modules from FastAPI
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from app.operations.addition import Addition
from app.operations.subtraction import Subtraction
from app.operations.multiplication import Multiplication
from app.operations.division import Division
from pathlib import Path

# Create FastAPI instance
app = FastAPI()

# Serve static files (like CSS)
# Updated the directory path to reference the correct static folder at the root level
app.mount("/static", StaticFiles(directory=Path(__file__).parent.parent / "static"), name="static")

# Define the input data schema for validation using Pydantic
class CalculationRequest(BaseModel):
    operand1: float
    operand2: float
    operation: str

# Route to serve the index page
@app.get("/", response_class=HTMLResponse)
async def index():
    # Updated the path to the templates folder
    template_path = Path(__file__).parent.parent / "templates" / "index.html"
    with open(template_path) as f:
        return HTMLResponse(content=f.read(), status_code=200)

# Route to handle the calculation (POST request)
@app.post("/", response_model=dict)
async def calculate(request: CalculationRequest):
    operand1 = request.operand1
    operand2 = request.operand2
    operation = request.operation

    # Perform the appropriate operation
    try:
        if operation == "Add":
            result = Addition().calculate(operand1, operand2)
        elif operation == "Subtract":
            result = Subtraction().calculate(operand1, operand2)
        elif operation == "Multiply":
            result = Multiplication().calculate(operand1, operand2)
        elif operation == "Divide":
            if operand2 == 0:
                raise HTTPException(status_code=400, detail="Cannot divide by zero")
            result = Division().calculate(operand1, operand2)
        else:
            raise HTTPException(status_code=400, detail="Invalid operation")

        return {"result": result}

    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid input")
