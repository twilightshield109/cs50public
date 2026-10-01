input1 = input("File name:")
input1 = input1.lower().strip()

if input1.endswith(".gif"):
    print("image/gif")
elif input1.endswith(".jpeg"):
    print("image/jpeg")
elif input1.endswith(".jpg"):
    print("image/jpeg")
elif input1.endswith(".png"):
    print("image/png")
elif input1.endswith(".pdf"):
    print("application/pdf")
elif input1.endswith(".zip"):
    print("application/zip")
elif input1.endswith((".txt")):
    print("text/plain")
else:
    print("application/octet-stream")
