import os
from config import MAX_CHARS
from google.genai import types

def get_file_content(working_directory, file_path):
  
  try:
    working_directory_abs = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(working_directory_abs, file_path))
    valid_target_dir = os.path.commonpath([working_directory_abs, target_dir]) == working_directory_abs
    
    if not valid_target_dir:
      return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(target_dir):
      return f'Error: File not found or is not a regular file: "{file_path}"'   
    
    with open(target_dir, "r") as f:
      file_content_string = f.read(MAX_CHARS)
    
      if f.read(1):
        file_content_string += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
      
    return file_content_string
    
    
  except Exception as e:
    return f"Error: {e}"

schema_get_file_content = types.FunctionDeclaration(
  name="get_file_content",
  description="Read the contents of the specified file",
  parameters=types.Schema(
    type=types.Type.OBJECT,
    properties={
      "file_path": types.Schema(
        type=types.Type.STRING,
        description="File path relative to the file which content we want to read"
      ),
    },
    required=["file_path"]
  ),
)