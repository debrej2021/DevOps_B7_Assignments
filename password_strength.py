import re

def check_password_strength(password):
    # Minimum length
    if len(password) < 8:
        return False
    
    # Contains both uppercase and lowercase letters
    if not re.search("[a-z]", password) or not re.search("[A-Z]", password):
        return False
    
    # Contains at least one digit
    if not re.search("[0-9]", password):
        return False
    
    # Contains at least one special character
    if not re.search("[!@#$%^&*(),.?\":{}|<>]", password):
        return False
    
    return True

def main():
    password = input("Enter your password: ")
    
    if check_password_strength(password):
        print("Your password is strong.")
    else:
        print("Your password is weak. Please ensure it is at least 8 characters long, contains both uppercase and lowercase letters, at least one digit, and at least one special character.")

if __name__ == "__main__":
    main()
