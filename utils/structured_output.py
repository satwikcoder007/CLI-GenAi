from pydantic import BaseModel, Field, root_validator
from typing import List, Optional

class FunctionAnalysis(BaseModel):
    function_name: str = Field(description="Name of the function or method(Only one function or method).")
    code: Optional[str] = Field(default=None, description="Corrected function code, required for fix tasks ")
    description: Optional[str] = Field(default=None, description="Explanation of the function, required for description tasks not required in fixing type of task.")

class StructuredResponse(BaseModel):
    functions: List[FunctionAnalysis] = Field(
        description="List of function analyses — either corrected code or descriptions."
    )
