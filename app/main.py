from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from pathlib import Path

from app.operations.addition import Addition
from app.operations.subtraction import Subtraction
from app.operations.multiplication import Multiplication
from app.operations.division import Division
from app.models.calculation_history import CalculationHistory
from database import SessionLocal, engine, Base

# Create tables in the database
Base.metadata.create_all(bind=engine)

# Create FastAPI instance
app = FastAPI()

# Health check endpoint
@app.get("/health")
async def health():
    return {"status": "OK"}

# Allow CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve static files
app.mount("/static", StaticFiles(directory=Path(__file__).parent / "static"), name="static")

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Pydantic schema for input
class CalculationRequest(BaseModel):
    operand1: float
    operand2: float
    operation: str

# Pydantic schema for returning history
class CalculationHistoryResponse(BaseModel):
    id: int
    operation: str
    operand1: float
    operand2: float
    result: float

# Serve the index page
@app.get("/", response_class=HTMLResponse)
async def index():
    template_path = Path(__file__).parent / "templates" / "index.html"
    with open(template_path) as f:
        return HTMLResponse(content=f.read(), status_code=200)

# Perform and store the calculation
@app.post("/", response_model=dict)
async def calculate(request: CalculationRequest, db: Session = Depends(get_db)):
    operand1 = request.operand1
    operand2 = request.operand2
    operation = request.operation

    operations = {
        "Add": Addition(),
        "Subtract": Subtraction(),
        "Multiply": Multiplication(),
        "Divide": Division(),
    }

    if operation not in operations:
        raise HTTPException(status_code=400, detail="Invalid operation")

    if operation == "Divide" and operand2 == 0:
        raise HTTPException(status_code=400, detail="Cannot divide by zero")
    
    result = operations[operation].calculate(operand1, operand2)

    calculation = CalculationHistory(
        operation=operation,
        operand1=operand1,
        operand2=operand2,
        result=result
    )
    db.add(calculation)
    db.commit()
    db.refresh(calculation)

    return {"result": result}

# Retrieve the calculation history
@app.get("/history", response_model=list[CalculationHistoryResponse])
async def get_history(db: Session = Depends(get_db)):
    return db.query(CalculationHistory).all()

# Clear calculation history
@app.delete("/history")
async def clear_history(db: Session = Depends(get_db)):
    db.query(CalculationHistory).delete()
    db.commit()
    return {"message": "Calculation history cleared."}

# Undo the last calculation
@app.delete("/history/undo")
async def undo_last_calculation(db: Session = Depends(get_db)):
    last_calculation = db.query(CalculationHistory).order_by(CalculationHistory.id.desc()).first()
    if not last_calculation:
        raise HTTPException(status_code=404, detail="No calculations to undo.")
    db.delete(last_calculation)
    db.commit()
    return {"message": "Last calculation undone."}
