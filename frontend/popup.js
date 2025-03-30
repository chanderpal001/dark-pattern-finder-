document.getElementById('switch').addEventListener('change', function () {
  chrome.tabs.query({currentWindow: true, active: true}, function(tabs){
    const url=tabs[0].url;
    
    sendUrlToServer(url);
});
  });
  
  function sendUrlToServer(url) {
    alert(url);
    fetch('http://localhost:4000/receive-url', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ url: url }),
    })
      .then(response => response.json())
      .then(data => {
        console.log(data);
      })
      .catch(error => {
        console.error('Error:', error);
      });
  }