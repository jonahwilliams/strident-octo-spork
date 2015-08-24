# strident-octo-spork
An automagic statistician.


<h1>Concept</h1>
An automatic statistician that uses either GPs or gradient descent on hyperparameters to find a good model for arbitrary data.

<h3>Node Server</h3>
The Node server is responsible for connecting the client and python processes, listening for input, and streaming results back to the client.  I'm currently using socket.io to open a websocket on connection and child-process to spawn a python process with command-line args.

```javascript
io.on('connection', function (socket) {

    // Init python process where the math happens
    // get argument from client
    io.emit('chat message', 'Websocket Open');

    socket.on('chat message', function (msg) {
        var python = cp.spawn('python', ['python.py', msg]);

        python.stdout.on('data', function (buffer) {
            var data = buffer.toString();
            io.emit('data', data);
        });

        python.on('close', function () {
            io.emit('chat message', 'Process Completed');
        });

        python.on('error', function (err) {
            console.error(err);
        });
    });
});
```

<h3>Python Process</h3>
The python process takes a command-line argument for the location of the data,
iteratively performs compuations and prints the intermediate results to standard out.
The node server listens for these and pushes them to the client. Currently the python process just counts to a number.

```python
import sys
import time
import json
if __name__=='__main__':
    target = sys.argv[1]
    for i in xrange(int(target)):
        time.sleep(0.001)
        sys.stdout.write(json.dumps({'data': i}))
        sys.stdout.flush()
```


<h3>Client & UI</h3>
I plan to replace these with nicer visuals soon.  The code to open a websocket with the server is fairly simple, and displaying results is just a bit of javascript.

```javascript
var socket = io();
    socket.on('chat message', function (msg) {
        $('#messages').append($('<li>').text(msg));
    });

    socket.on('data', function (d) {
        t = JSON.parse(d)
        $('#nums').append($('<li>').text(t.data));
    });

    $('form').submit(function(){
        socket.emit('chat message', $('#m').val());
        $('#m').val('');
        return false;
    });
```

