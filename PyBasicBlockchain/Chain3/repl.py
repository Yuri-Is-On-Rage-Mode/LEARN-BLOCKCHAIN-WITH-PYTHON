import os

while True:
    try:
        other = input(">> ")
        if other.strip().lower() == "exit":
            break  # Exit the loop and terminate the script
        if other.strip().lower() == "clear" or other.strip().lower() == "cls":
            os.system("cls")
        elif other.strip().lower() == "":
            continue  # Exit the loop and terminate the script
        os.system(f"python nSqlServerUtil.py {other}")
    except KeyboardInterrupt:
        print("<return::KeyboardInterrupt>")
    except Exception as e:
        print(f"<return::Error::{e}>")
