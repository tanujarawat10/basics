#combining or concenating the strings
from email import message


first_name='tanuja'
last_name='rawat'
full_name=first_name+' '+last_name
# message="Hello, "+full_name.title()+"!"
message=f"hello, {first_name} {last_name}!" #this is the f-strings
print(full_name)
print(message)