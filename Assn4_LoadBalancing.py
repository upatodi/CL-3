class LoadBalancer:
    def __init__(self, servers):
        """
        Initialize the LoadBalancer with a list of servers.
        """
        self.servers = servers
        self.current_server_index = 0

    def distribute_request(self):
        """
        Distribute incoming requests among servers using a round-robin algorithm.
        """
        server = self.servers[self.current_server_index]
        self.current_server_index = (self.current_server_index + 1) % len(self.servers)
        return server

class Server:
    def __init__(self, name):
        """
        Initialize the Server with a name.
        """
        self.name = name

    def process_request(self, request):
        """
        Process a request received by the server.
        """
        print(f"Processing request '{request}' on server '{self.name}'")

# Creating servers
server1 = Server("Server 1")
server2 = Server("Server 2")
server3 = Server("Server 3")

# Creating a load balancer with the servers
load_balancer = LoadBalancer([server1, server2, server3])

# Simulating incoming requests
requests = ["Request 1", "Request 2", "Request 3", "Request 4", "Request 5"]

for request in requests:
    # Distribute the request among servers using the load balancer
    server = load_balancer.distribute_request()
    # Process the request on the selected server
    server.process_request(request)
