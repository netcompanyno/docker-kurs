const express = require('express');
const app = express();

app.use(express.static('public'));

app.get('/', (req, res) => res.sendFile(__dirname + '/index.html'));
app.get('/clicks.js', (req, res) => res.sendFile(__dirname + '/clicks.js'));

app.listen(3000);
