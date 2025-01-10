#Context Manager
with open("Cool_Features/Files/example.txt", "r") as file:
    content = file.read()
print(content)


# #With Custom Context Manager
# class FileManager:
#     def __init__(self, file_name, mode):
#         """
#         Initialize the file manager with the file name and mode.
        
#         Args:
#             file_name (str): The name of the file to open.
#             mode (str): The mode to open the file in (e.g., 'r', 'w').
#         """
#         self.file_name = file_name
#         self.mode = mode
#         self.file = None

#     def __enter__(self):
#         """
#         Open the file and return the file object.
#         """
#         print(f"Opening file: {self.file_name}")
#         self.file = open(self.file_name, self.mode)
#         return self.file

#     def __exit__(self, exc_type, exc_value, traceback):
#         """
#         Close the file when exiting the context.
        
#         Args:
#             exc_type (type): The exception type, if any.
#             exc_value (Exception): The exception value, if any.
#             traceback (Traceback): The traceback object, if any.
        
#         Returns:
#             bool: True to suppress exceptions, False otherwise.
#         """
#         if self.file:
#             self.file.close()
#             print(f"Closing file: {self.file_name}")
#         if exc_type:
#             print(f"Exception occurred: {exc_type.__name__}: {exc_value}")
#         return False  # Do not suppress exceptions


# with FileManager("Cool_Features/Files/example.txt", "w") as f:
#     f.write("Hello, this is written using a custom context manager.")


# #With Context Manager Decorator
# from contextlib import contextmanager

# @contextmanager
# def file_manager(file_name, mode):
#     """
#     A context manager to handle file operations.
    
#     Args:
#         file_name (str): The name of the file to be opened.
#         mode (str): The mode in which the file is to be opened (e.g., 'r', 'w').
#     """
#     file = None
#     try:
#         print(f"Opening file {file_name}")
#         file = open(file_name, mode)
#         yield file
#     finally:
#         if file:
#             file.close()
#             print(f"Closing file {file_name}")


# with file_manager("Cool_Features/Files/example.txt", "w") as f:
#     f.write("Hello, this is written using a context manager created with decorator.")
