import re

def check_password_strength(password):
    # Check the length of the password
    if len(password) < 8:
        return "Weak", "Password must be at least 8 characters long."
    
    # Check for lowercase letters
    if not re.search("[a-z]", password):
        return "Weak", "Password must include at least one lowercase letter."
    
    # Check for uppercase letters
    if not re.search("[A-Z]", password):
        return "Weak", "Password must include at least one uppercase letter."
    
    # Check for digits
    if not re.search("[0-9]", password):
        return "Weak", "Password must include at least one digit."
    
    # Check for special characters
    if not re.search("[!@#$%^&+=!]", password):
        return "Weak", "Password must include at least one special character."
    
    return "Strong", "Your password is strong!"

# Example usage
password = input("Enter your password: ")
strength, message = check_password_strength(password)
print(f"Password Strength: {strength} - {message}")
