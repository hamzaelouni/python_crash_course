import requests

# Manage multiple files using context manager
with open("file1.csv", "rb") as file1, open("file2.csv", "rb") as file2:
    # Create a list of files
    files = [
        ("files", ("file1.csv", file1, "text/csv")),
        ("files", ("file2.csv", file2, "text/csv")),
    ]

    response = requests.post(
        "http://127.0.0.1:8000/upload-files",
        files=files, # use files keyword argument to send files
    )


print(response.json())



# # Without context manager

# # Open the files
# file1 = open("file1.csv", "rb")
# file2 = open("file2.csv", "rb")

# # Create a list of files
# files = [
#     ("files", ("file1.csv", file1, "text/csv")),
#     ("files", ("file2.csv", file2, "text/csv")),
# ]

# # Upload a single file
# # files = {"file": open("file1.csv", "rb")}  # For single file upload

# response = requests.post(
#     "http://127.0.0.1:8000/upload-files",
#     files=files, # use files keyword argument to send files
# )

# # Close the files
# file1.close()
# file2.close()

# print(response.json())
