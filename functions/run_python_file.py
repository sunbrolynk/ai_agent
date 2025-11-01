import os
import subprocess
import sys

def run_python_file(working_directory, file_path, args=[]):
    full_path = os.path.join(working_directory, file_path)
    #print(full_path)
    abs_working = os.path.abspath(working_directory)
    #print(abs_working)
    abs_target = os.path.abspath(full_path)
    #print(abs_target)
    
    if not abs_target.startswith(abs_working):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.exists(abs_target):
        return f'Error: File "{file_path}" not found.'
    
    if not abs_target.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    
    try:
        result = subprocess.run([sys.executable, file_path, *args],
                  capture_output=True,
                  shell=False,
                  cwd=abs_working,
                  timeout=30,
                  check=False,
                  encoding=None,
                  errors=None,
                  text=True,
                  env=None,
                  universal_newlines=None
            )
        return f'STDOUT: {result.stdout}, STDERR: {result.stderr}'
        
        
        if result.returncode != 0:
            return f'Process exited with code {result.returncode}'
        elif not result:
            return "No output produced."
            
        
    except Exception as e:
        return f'Error: {e}'