# strident-octo-spork
An automagic statistician.


<h1>Concept</h1>
An automatic statistician that uses either GPs or gradient descent on hyperparameters to find a good model for arbitrary data.

<h3>Node Server</h3>
The Node server is responsible for connecting the client and python processes, listening for input, and streaming results back to the client.  I'm currently using socket.io to open a websocket on connection and child-process to spawn a python process with command-line args.

![server](https://github.com/jonahwilliams/strident-octo-spork/images/websocketServer.png)

<h3>Python Process</h3>
The python process takes a command-line argument for the location of the data,
iteratively performs compuations and prints the intermediate results to standard out.
The node server listens for these and pushes them to the client. Currently the python process just counts to a number.

![python](https://github.com/jonahwilliams/strident-octo-spork/images/pythonProcess.png)

<h3>Client & UI</h3>
I plan to replace these with nicer visuals soon.  The code to open a websocket with the server is fairly simple, and displaying results is just a bit of javascript.

![UI](https://github.com/jonahwilliams/strident-octo-spork/images/clientUI.png)

![JS](https://github.com/jonahwilliams/strident-octo-spork/images/clientProcess.png)
