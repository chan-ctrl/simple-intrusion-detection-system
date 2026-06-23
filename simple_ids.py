failed_attempts =0

with open("security_log.txt", "r") as file:
    for line in file:
        if "LOGIN FAILED" in line:
            failed_attempts += 1

print("Failed Login Attempts:", failed_attempts)

if failed_attempts >= 3:
    print("Alert: Possible Intrusion Detected!")
else:
    print("System Appears Normal")