email = input("Enter Your Email: ").strip()
username = email[:email.index("@")]
domain_name = email[email.index("@")+1:]
print(f"Your user name is '{username}'and your domain is '{domain_name}'")







