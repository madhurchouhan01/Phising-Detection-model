document.addEventListener('DOMContentLoaded', function() {
  chrome.storage.local.get("selectedText", function(data) {
    const selectedText = data.selectedText;
    console.log("Selected Text: ", selectedText); // Log selected text for debugging

    if (selectedText) {
      fetch('http://127.0.0.1:5000/predict', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ text: selectedText })
      })
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok ' + response.statusText);
        }
        return response.json();
      })
      .then(data => {
        console.log("Server response: ", data); // Log server response for debugging

        if (data && data.label !== undefined) {
          document.getElementById('result').innerText = `Result: ${data.label}`;
        } else {
          document.getElementById('result').innerText = 'Error: Invalid response from server';
        }
      })
      .catch(error => {
        console.error('There was a problem with the fetch operation:', error);
        document.getElementById('result').innerText = 'Error: ' + error.message;
      });
    } else {
      document.getElementById('result').innerText = 'No text selected.';
    }
  });
});
