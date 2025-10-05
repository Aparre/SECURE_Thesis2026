const express = require('express');
const fs = require('fs');
const path = require('path');

const app = express();
const PORT = 3000;

app.use(express.json());
app.use(express.static(__dirname));

// Endpoint to append content to 1.txt
app.post('/append-file', (req, res) => {
  const content = req.body.content || '';
  const filePath = path.join(__dirname, '1.txt');
  fs.appendFile(filePath, content + '\n', (err) => {
    if (err) {
      return res.status(500).json({ message: 'Error writing to file.' });
    }
    res.json({ message: 'Content added to 1.txt successfully.' });
  });
});

app.listen(PORT, () => {
  console.log(`Server running at http://localhost:${PORT}`);
});