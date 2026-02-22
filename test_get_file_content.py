from functions.get_file_content import get_file_content
from config import MAX_CHARS

def test_get_file_content(working_directory, file_path):
  file_content = get_file_content(working_directory, file_path)
  content_size = len(file_content)
  print(content_size)
  if content_size > MAX_CHARS:    
    print(file_content[MAX_CHARS:])
  else:
    print(file_content)
  return "\n"

print("Result for lorem.txt:")
print(test_get_file_content("calculator", "lorem.txt"))

print("Result for main.py:")
print(test_get_file_content("calculator", "main.py"))

print("Result for pkg/calculator.py:")
print(test_get_file_content("calculator", "pkg/calculator.py"))

print("Result for /bin/cat:")
print(test_get_file_content("calculator", "/bin/cat"))

print("Result for pkg/does_not_exist.py:")
print(test_get_file_content("calculator", "pkg/does_not_exist.py"))
