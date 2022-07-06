# PA0_ReverseSocket
Internet Tech Project 0 

Partners: Isaac Brukhman and Alex Dziemianowski
RUIDs: ivb8 and ajd318

Issues:
- only works on localhost bc the connection is continuously refused when we try to connect.
- Another slight issue was getting the file to close completely. This was due to an extra while true statement that we disregarded

Collaborations:
- We collaborated with eachother when we could not get the server to work
- Google is our best friend when it comes to socket work but we couldn't figure out why connection kept refusing 
- Sought out python basics to undestand how to attack the problem 

Problems:
We had issues with getting the server to connect properly with any DNS ip that we gave. 
The example, "vi.cs.rutgers.edu" that was given kept giving a connection refusal and
we could only get the localhost to work
- This is the main issue and want to figure at what point is causing this
- As the port is recongnized and the listen and binding functions work properly however, won't claim the host

Lessons:
- The basics of how to work sockets interms of sending, recieving, connecting, and closing
- Revisting the basics of Python since it's been a while
- Learned how to decode and encode while having client use strip 
- Understand how to send/receive data using sockets
- Look for office hours
