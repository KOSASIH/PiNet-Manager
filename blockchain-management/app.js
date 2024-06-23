const express = require('express');
const bodyParser = require('body-parser');
const api = require('./routes/api');

const app = express();
app.use(bodyParser.json());
app.use('/api', api);

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server listening on port ${PORT}`);
});
