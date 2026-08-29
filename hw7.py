
CAMERA = 1
MICROPHONE = 2
STORAGE = 4 
LOCATION = 8
approvedapps = [
    "coding app",
    "math app",
    "reading app",
    "science app"
]
studentname = input("Enter your name: ")
requestedapp = input("Enter the app you want to access: ").lower()
print("\n--- Identity Operator Check ---")
if type(studentname) is str:
    print("The student name is stored as text.")
if type(requestedapp) is not int:
    print("The requested app is not stored as a number.")
print("\n--- Membership Operator Check ---")
if requestedapp in approvedapps:
    print(requestedapp, "is an approved student app.")
else:
    print(requestedapp, "is not an approved student app.")
restrictedapps = [
    "gaming app",
    "shopping app",
    "social media app"
]
if requestedapp not in restrictedapps:
    print("The app is not in the restricted list.")
else:
    print("Access denied because the app is restricted.")
print("\n--- App Permission Settings ---")
studentpermissions = CAMERA | MICROPHONE | STORAGE
print("Permission value:", studentpermissions)
print("Permission bits:", bin(studentpermissions))
if studentpermissions & CAMERA:
    print("Camera permission: Enabled")
if studentpermissions & MICROPHONE:
    print("Microphone permission: Enabled")
if studentpermissions & STORAGE:
    print("Storage permission: Enabled")
if studentpermissions & LOCATION:
    print("Location permission: Enabled")
else:
    print("Location permission: Disabled")
print("\n--- Bit Shift Demonstration ---")
nextpermission = CAMERA << 1
print("Camera bit:", bin(CAMERA))
print("After left shift:", bin(nextpermission))
previouspermission = STORAGE >> 1
print("Storage bit:", bin(STORAGE))
print("After right shift:", bin(previouspermission))
print("\n--- Final Access Result ---")
if requestedapp in approvedapps and requestedapp not in restrictedapps:
    print("Access granted to", requestedapp)
else:
    print("Access denied to", requestedapp)
