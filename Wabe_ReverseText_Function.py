def reverse_text():
 while True:
   text = input("Enter a text: ")
   if text.isalpha():  # Check if input contains only letters
     reversed_text = text[::-1]
     print("The reversed text is:", reversed_text)
     break  # Exit the loop if valid text is entered
   else:
     print("Error Reported! Enter text only.")

reverse_text()
