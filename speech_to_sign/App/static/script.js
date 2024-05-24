document.addEventListener('DOMContentLoaded', function() {
    const iframeContainer = document.getElementById('iframeContainer');
  
    // Assume 'data' is the response object
    const data = {
      "iframeSrc": "https://www.youtube.com/embed/AZP9YCS8Rrk",
      "status": "Success"
    };
  
    if (data.status === 'Success' && data.iframeSrc) {
      const iframe = document.createElement('iframe');
      iframe.src = data.iframeSrc;
      iframe.style.width = '100%';
      iframe.style.height = '400px'; // Adjust height as needed
      iframeContainer.appendChild(iframe);
    } else {
      console.error('Invalid response from server.');
    }
  });
  