from pydantic import BaseModel


class FibonacciNumber(BaseModel):
    result: int
