import React, { useState } from 'react';
import './App.css';

function App() {
  const [inputText, setInputText] = useState('');
  const [outputText, setOutputText] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState('');

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    if (!inputText.trim()) {
      setError('Please enter some text');
      return;
    }

    setIsLoading(true);
    setError('');

    try {
      const response = await fetch('http://localhost:8000/api/process', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text: inputText }),
      });

      if (!response.ok) {
        throw new Error(`Server responded with ${response.status}`);
      }

      const data = await response.json();
      setOutputText(data.processed_text);
    } catch (err) {
      setError(`Error: ${err instanceof Error ? err.message : String(err)}`);
      setOutputText('');
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Diakriticar</h1>
        <p>Add Croatian diacritics to your text</p>
      </header>

      <main>
        <form onSubmit={handleSubmit}>
          <div className="input-group">
            <label htmlFor="input-text">Enter text without diacritics:</label>
            <textarea
              id="input-text"
              value={inputText}
              onChange={(e) => setInputText(e.target.value)}
              rows={5}
              placeholder="Enter Croatian text without diacritics..."
            />
          </div>

          <button type="submit" disabled={isLoading}>
            {isLoading ? 'Processing...' : 'Add Diacritics'}
          </button>

          {error && <div className="error">{error}</div>}

          {outputText && (
            <div className="output-group">
              <h2>Text with diacritics:</h2>
              <div className="output-text">{outputText}</div>
            </div>
          )}
        </form>
      </main>
    </div>
  );
}

export default App;
