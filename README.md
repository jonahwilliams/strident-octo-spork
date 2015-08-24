# strident-octo-spork
An automagic statistician.


<h1>Concept</h1>
An automatic statistician that uses either GPs or gradient descent on hyperparameters to find a good model for arbitrary data.

<h3>Node Server</h3>
The Node server is responsible for connecting the client and python processes, listening for input, and streaming results back to the client.  I'm currently using socket.io to open a websocket on connection and child-process to spawn a python process with command-line args.





