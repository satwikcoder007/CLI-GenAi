import re
def extract_code_blocks(text):
    
    pattern = r"```(?:[a-zA-Z0-9]+)?\n(.*?)```"
    matches = re.findall(pattern, text, re.DOTALL)
    return [match.strip() for match in matches]