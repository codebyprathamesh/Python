def email(address):
  dot=address.find(".")
  at=address.find("@")
  while True:
    if (dot==-1):
      print("Invalid Email Address")
      break
    elif (at==-1):
      print("Invalid Email Address")
      break
    else:
      print("This is a valid email address")
      break
email("abc@gmailcom")