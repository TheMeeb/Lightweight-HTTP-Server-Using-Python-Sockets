# Import everything from the socket module (so we can create a server)
from socket import *

def createServer():
    # Setting up a server socket using IPv4 (AF_INET) and TCP (SOCK_STREAM)
    serversocket = socket(AF_INET, SOCK_STREAM)
    try:
        # Binding the server to 'localhost' on port 9000
        serversocket.bind(('localhost', 9000))
        # Start listening for incoming connections (up to 5 clients in the queue)
        serversocket.listen(5)
        
        print("Server is running on http://localhost:9000")

        while True:  # Keep the server running indefinitely
            # Accept an incoming connection from a client
            clientsocket, address = serversocket.accept()
            print(f"Connection received from {address}")

            # Receive the client's request (up to 5000 bytes), then decode it
            request_data = clientsocket.recv(5000).decode()
            request_lines = request_data.split("\n")  # Split request into lines

            # Print the first line of the request (usually something like 'GET / HTTP/1.1')
            if len(request_lines) > 0: 
                print(f"Client Request: {request_lines[0]}")

            # Creating a simple HTTP response
            response = "HTTP/1.1 200 OK\r\n"  # Status line (200 OK means success)
            response += "Content-Type: text/html; charset=utf-8\r\n"  # Specify content type
            response += "\r\n"  # Blank line to separate headers from body
            response += "<html><body><h1>Hello, World!</h1></body></html>\r\n\r\n"  # The actual page content

            # Send the response back to the client
            clientsocket.sendall(response.encode())
            # Tell the client we're done sending data
            clientsocket.shutdown(SHUT_WR)

    except KeyboardInterrupt:
        # If the user stops the server with Ctrl+C, print a friendly message
        print("\nServer is shutting down...")

    except Exception as e:
        # If something unexpected happens, print the error
        print("Oops! Something went wrong:")
        print(e)

    # Close the server socket before exiting
    serversocket.close()

# Let the user know where to access the server
print("Starting the server... Access it at http://localhost:9000")

# Run the server function
createServer()
