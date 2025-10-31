import os

def get_files_info(working_directory, directory="."):  
    full_path = os.path.join(working_directory, directory)
    #print(full_path)
    abs_working = os.path.abspath(working_directory)
    #print(abs_working)
    abs_target = os.path.abspath(full_path)
    #print(abs_target)
     
    if not abs_target.startswith(abs_working):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    if not os.path.isdir(abs_target):
        return f'Error: "{directory}" is not a directory'
    
    try:
        dir_list = os.listdir(abs_target)
        
        #print(dir_list)
    
        lines_list = []
        
        for item in dir_list:
            size = os.path.getsize(os.path.join(abs_target, item))
            is_dir = os.path.isdir(os.path.join(abs_target, item))
        
            lines_list.append(f" - {item}: file_size={size}, is_dir={is_dir}")
        
        return "\n".join(lines_list)
    except Exception as e:
        return f"Error: {e}"