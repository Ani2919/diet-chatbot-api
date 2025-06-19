const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');
const app = express();
const port = process.env.PORT || 8080;

app.use(cors());
app.use(bodyParser.json());

// If using Ollama locally, install and run it before using this endpoint
// Requires "ollama" Node.js wrapper or call Ollama using fetch if needed
const fetch = require('node-fetch');

app.post('/api/generate', async (req, res) => {
  try {
    const { message } = req.body;

    const ollamaResponse = await fetch('http://localhost:11434/api/generate', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        model: 'health',
        prompt: `SYSTEM: Answer the following query in clean HTML only.\nUSER: ${message}`,
        stream: false
      })
    });

    const data = await ollamaResponse.json();
    res.json({ response: data.response });

  } catch (err) {
    console.error('Error in backend /api/generate:', err);
    res.status(500).json({ error: 'Failed to generate response' });
  }
});

app.listen(port, () => {
  console.log(`🚀 API Server running on http://localhost:${port}`);
});
