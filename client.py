import xmlrpc.client

def main():
    client = xmlrpc.client.ServerProxy("http://localhost:8000/")
    num = int(input("Enter an integer: "))
    result = client.factorial(num)
    print(f"The factorial of {num} is: {result}")

if __name__ == "__main__":
    main()
