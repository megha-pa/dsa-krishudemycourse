# what is nginx?

Nginx is a robust and efficient web server that is widely used in modern web infrastructure. .

Nginx is versatile and can be configured to perform a variety of roles, including load balancing, HTTP caching, and acting as a reverse proxy. 


NGINX CAN ACT AS-
1.Loadbalancer-
2.Reverse Proxy
3.Encryption
4.caching


Advantages of Nginx
Nginx provides several key advantages that make it a preferred choice for many web projects:

Advantages of Nginx
Nginx provides several key advantages that make it a preferred choice for many web projects:

- High Concurrency: Capable of handling 10,000+ concurrent requests.
- HTTP Caching: Can cache HTTP requests, reducing server load and improving response times.
- Reverse Proxy: Acts as a reverse proxy, routing client requests to the appropriate server.
- Load Balancing: Distributes incoming requests across multiple servers to balance the load.
- API Gateway: Can act as an API gateway, managing and routing API requests.
- Static File Serving: Efficiently serves and caches static files like images and videos.
- SSL Termination: Handles SSL certificates, providing secure connections to users.

-High Requests Handling Architecture
    -Nginx utilizes an event-driven architecture and deals with the requests asynchronously. It was designed to use a non-blocking event-driven connection handling algorithm. Hence, its process can handle thousands of connections (requests) within 1 processing thread. Such connections process modules allow Nginx to work very fast and wide with limited resources. Also, you can use Nginx to handle more than 10,000 simultaneous connections with low (CPU & Memory) resources under heavy request loads.

-Nginx Reverse Proxy Overview
    -Nginx reverse proxy acts as an intermediate server that intercepts client requests and forwards them to the appropriate upstream backend server and subsequently forwarded a response from the server back to the client. The reverse proxy provides various benefits as an abstract layer above upstream servers.

-Important Benefits of Nginx as a Reverse Proxy
    -Load balancing: Nginx load balance the client request to multiple upstream servers evenly which improve performance and provide redundancy in case of server failure. This helps to keep the application up all the time to serve client requests and provide better SLA for application.

-Security: Nginx server provides security to backend servers that exist in the private network by hiding their identity. The backend servers are unknown to the client that are making requests. it also provides a single point of access to multiple backend servers regardless of the backend network topology.

-Caching: Nginx can serve static content like image, videos, etc directly and deliver better performance. It reduces the load on the backend server by serving static content directly instead of forwarding it to the backend server for processing.

-Logging: Nginx provides centralized logging for backed server request and response passing through it and provides a single place to audit and log for troubleshooting issues.

-TLS/SSL support: Nginx allows secure communication between client and server using TLS/SSL connection. User data remains secure & encrypted while transferring over the wire using an HTTPS connection.

-Protocol Support: Nginx supports HTTP, HTTPS, HTTP/1.1, HTTP/2, gRPC - Hypertext Transport Protocol along with both IP4 & IP6 internet protocol.

#### Proxy meaning


