list=[1,'a',2,'b',3]
y=0
for x in list:
    try:
        y+=int(x)
    except ValueError:
        print("a valueerror occurred")
print(f"The sum is: {y}")