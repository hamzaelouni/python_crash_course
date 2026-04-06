# Variable annotation
name: str = "Alice"
age: int = 30

# Function with parameter and return type hints
def greet(name: str, age: int) -> str:
    return f"Hello {name}, you are {age} years old"

    # Common types
from typing import List, Dict, Optional, Tuple, Union

def process(items: List[int]) -> Dict[str, int]:
    return {"count": len(items)}

    # Optional (can be None)
def find() -> Optional[str]:
    return None

# Union (multiple types)
def parse(value: Union[str, int]) -> str:
    return str(value)

# Modern Python 3.10+ syntax
def greet(name: str | None = None) -> str:
    return f"Hello {name or 'World'}"