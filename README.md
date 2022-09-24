# PA0_ReverseSocket
Internet Tech Project 0 

Partners: Isaac Brukhman and Alex Dziemianowski
RUIDs: ivb8 and ajd318

Issues:
- Hopefully none

Collaborations::
- We collaborated with eachother when we could not get the server to work
- Google is our best friend when it comes to socket work but we couldn't figure out why connection kept refusing 
- Sought out python basics to undestand how to attack the problem 

Problems:
We had issues with getting the server to connect properly with any DNS ip that we gave. 
The example, "vi.cs.rutgers.edu" that was given kept giving a connection refusal and
we could only get the localhost to work
- This is the main issue and want to figure at what point is causing this
- As the port is recongnized and the listen and binding functions work properly however, won't claim the host
- Fix: added an arg to retrieve the port # and using socket.gethostname() to get the current computers iLab address

Getting the file to close completely. This was due to an extra while true statement that we disregarded. 
- Fix: got rid of the extra loop in Server


Lessons:
- The basics of how to work sockets interms of sending, recieving, connecting, and closing
- Revisting the basics of Python since it's been a while
- Learned how to decode and encode while having client use strip// this is due to the client only sending a single line
- Understand how to send/receive data using sockets
- Look for office hours
