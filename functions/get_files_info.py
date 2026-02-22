import os

def get_files_info(working_directory, directory="."):
  
  try:  
    working_directory_abs = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(working_directory_abs, directory))
    valid_target_dir = os.path.commonpath([working_directory_abs, target_dir]) == working_directory_abs
    
    if not valid_target_dir:
      return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    if not os.path.isdir(target_dir):
      return f'Error: "{directory}" is not a directory'
    
    files = []
      
    for content in os.listdir(target_dir):    
      file_name = content
      full_path = os.path.join(target_dir, content)
      file_size = os.path.getsize(full_path)
      is_dir = os.path.isdir(full_path)
      files.append(f"- {file_name}: file_size={file_size} bytes, is_dir={is_dir}")
    
    return "\n".join(files)
  
  except Exception as e:
    return f"Error {e}"