# Import necessary modules from FastAPI
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware  # Import CORSMiddleware
from app.operations.addition import Addition
from app.operations.subtraction import Subtraction
from app.operations.multiplication import Multiplication
from app.operations.division import Division
from pathlib import Path

# Create FastAPI instance
app = FastAPI()

# Allow CORS for all origins or configure it as needed
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict this to specific domains if needed
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, OPTIONS, etc.)
    allow_headers=["*"],  # Allows all headers
)

# Serve static files (like CSS)
# Updated the directory path to correctly reference the static folder inside the app folder
app.mount("/static", StaticFiles(directory=Path(__file__).parent / "static"), name="static")

# Define the input data schema for validation using Pydantic
class CalculationRequest(BaseModel):
    operand1: float
    operand2: float
    operation: str

# Route to serve the index page
@app.get("/", response_class=HTMLResponse)
async def index():
    # Updated the path to the templates folder inside the app folder
    template_path = Path(__file__).parent / "templates" / "index.html"
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
