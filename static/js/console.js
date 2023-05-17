window.addEventListener("DOMContentLoaded", (event) => {

    const consoleBackendLog = document.getElementById('a-console-log');
    var consoleBackendLogSetInterval;
    consoleBackendLog.addEventListener('click', (event) => {
        const buttonShowVoicesSwitch = document.getElementById('button-show-voice-window');
        const buttonShownAnimationsSwitch = document.getElementById('button-show-animation-window');

        document.getElementById('table_speech_result').style.display = 'none';
        document.getElementById('table_body_deepfake_result').style.display = 'none';

        // Create the console log element
        var consoleLogElement = document.createElement('code');
        consoleLogElement.style.padding = '15pt';
        consoleLogElement.style.fontSize = '10pt';
        consoleLogElement.style.width = '280pt';
        consoleLogElement.style.display = 'flex';
        consoleLogElement.style.overflowWrap = 'break-word';
        consoleLogElement.id = 'console-log';

        // Append the console log element to the existing HTML structure
        var synthesizedResultTable = document.getElementById('synthesized_result_table');
        synthesizedResultTable.appendChild(consoleLogElement);

        buttonShowVoicesSwitch.addEventListener('click', function() {
            // Check if the element exists
            if (consoleLogElement) {
              // Remove the element from the DOM
              consoleLogElement.remove();
              // Later, when you want to stop the interval:
                clearInterval(consoleBackendLogSetInterval);
            }
        });

        buttonShownAnimationsSwitch.addEventListener('click', function() {
            // Check if the element exists
            if (consoleLogElement) {
              // Remove the element from the DOM
              consoleLogElement.remove();
              // Later, when you want to stop the interval:
              clearInterval(consoleBackendLogSetInterval);
            }
        });

        function updateConsoleLog() {
          fetch('/console_log', {
            method: 'GET',
            headers: {
              'Content-Type': 'application/json'
            }
          })
            .then(response => response.text())
            .then(data => {
              // Update the element with id="console-log" with the logs
              document.getElementById('console-log').innerText = data;
            })
            .catch(error => {
              console.error('Log field deleted, message from setInterval:', error);
            });
        }

        // Update console log initially
        updateConsoleLog();

        // Update console log every 5 seconds
        consoleBackendLogSetInterval = setInterval(updateConsoleLog, 5000);
    });
});