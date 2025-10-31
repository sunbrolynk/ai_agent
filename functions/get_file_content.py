
import os
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    full_path = os.path.join(working_directory, file_path)
    #print(full_path)
    abs_working = os.path.abspath(working_directory)
    #print(abs_working)
    abs_target = os.path.abspath(full_path)
    #print(abs_target)
    
    if not abs_target.startswith(abs_working):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(abs_target):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    try:

        with open(abs_target, "r") as f:
            file_content_string = f.read()
            
        if len(file_content_string) > MAX_CHARS:
            trunc_text = file_content_string[:MAX_CHARS]
            return f'{trunc_text}[...File "{file_path}" truncated at {MAX_CHARS} characters]'
        else:
            return file_content_string
        
        
    except Exception as e:
        return f'Error: {e}' 