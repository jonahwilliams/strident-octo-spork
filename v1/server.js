var express = require('express');
var app = express();
var cp = require('child_process');
var http = require('http').Server(app);
var io = require('socket.io')(http);


app.get('/', function (req, res) {
    res.sendFile(__dirname + '/index.html');
});


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

http.listen(8080);
