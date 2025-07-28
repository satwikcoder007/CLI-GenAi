from langchain_core.prompts import PromptTemplate

User_Prompt = PromptTemplate(
    template="""
You are a highly skilled software engineer and technical writer.

Your task is to follow the instruction below and perform it on the given {file_extension} code:
Instruction: {task_instruction}
Code: {file_content}
Return your answer clearly and concisely.
""",


input_variables=["file_extension", "file_content", "task_instruction"],
)