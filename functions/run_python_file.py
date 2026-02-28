import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=None):
  
  try:
    working_directory_abs = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(working_directory_abs, file_path))
    valid_target_dir = os.path.commonpath([working_directory_abs, target_dir]) == working_directory_abs
    
    if not valid_target_dir:
      return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(target_dir):
      return f'Error: "{file_path}" does not exist or is not a regular file"'
    
    if not target_dir.endswith(".py"):
      return f'Error: "{file_path}" is not a Python file'
    
    command = ["python", target_dir]
    
    if args:
      command.extend(args)
      
    completed_process = subprocess.run(command, cwd=working_directory_abs, capture_output=True, text=True, timeout=30)
    
    return_code = completed_process.returncode
    
    output_str = ""
    
    if return_code != 0:
      output_str = f"Process exited with code {return_code}"
      
    if not completed_process.stdout and not completed_process.stderr:
      output_str += "No output produced"
    
    if completed_process.stdout: 
      output_str += f"STDOUT: {completed_process.stdout}"
      
    if completed_process.stderr:
      output_str += f"STDERR: {completed_process.stderr}"
      
    return output_str
    
  except Exception as e:
    return f'Error: executing Python file: {e}'
  
schema_run_python_file = types.FunctionDeclaration(
  name="run_python_file",
  description="Execute Python files with optional arguments",
  parameters=types.Schema(
    type=types.Type.OBJECT,
    properties={
      "file_path": types.Schema(
        type=types.Type.STRING,
        description="File path relative to the file we want to execute"
      ),
      "args": types.Schema(
        type=types.Type.ARRAY,
        items=types.Schema(
          type=types.Type.STRING
        ),
        description="Optional arguments to be used while executing Python files"
      ),
    },
    required=["file_path"]
  ),
)