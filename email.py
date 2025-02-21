def email_slicer(email):
    try:
        username, domain = email.split("@")
        return f"username: {username}\nDomain: {domain}"
    except ValueError:
        return " please enter a valid email:"
    
email = input("enter your email: ")
print(email_slicer(email))