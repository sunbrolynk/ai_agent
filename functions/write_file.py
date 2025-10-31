import os



def write_file(working_directory, file_path, content):
    full_path = os.path.join(working_directory, file_path)
    #print(full_path)
    abs_working = os.path.abspath(working_directory)
    #print(abs_working)
    abs_target = os.path.abspath(full_path)
    #print(abs_target)
    
    if not abs_target.startswith(abs_working):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.exists(abs_target):
        directory_name = os.path.dirname(abs_target)
        try:
            if directory_name:
                os.makedirs(directory_name, exist_ok=True)
        except Exception as e:
            return f'Error: {e}'
    
    try:
        with open(abs_target, "w") as f:
            f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
            
    except Exception as e:
        return f'Error: {e}'
        