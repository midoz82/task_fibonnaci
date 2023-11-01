from fastapi import APIRouter, HTTPException, Path

from app.schemas.fibonacci import FibonacciNumber
from app.utils.fibonacci import calculate_fibonacci

router = APIRouter()


@router.get("/{n}", response_model=FibonacciNumber)
async def calculate_fibonacci_value(
        n: int = Path(..., title="The number", description="The number to calculate the Fibonacci sequence", ge=1)):
    try:
        fib_number = calculate_fibonacci(n)
        return {"result": fib_number}
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
