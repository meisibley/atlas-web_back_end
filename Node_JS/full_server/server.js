//a small Express server(port 1245), use the routes defined in full_server/routes/index.js
const express = require('express');
const routeControl = require('./routes');

const app = express();
app.use('/', routeControl);
app.listen(1245, () => {
  console.log('...');
});

module.exports = app;
