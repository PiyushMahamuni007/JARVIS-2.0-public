$(document).ready(function () {
    //display speaking text
    eel.expose(DisplayMessage);
    function DisplayMessage(message) {
        $('.siri-msg li:first').text(message);
        $('.siri-msg').textillate('start');
    }

  // Display hood
    eel.expose(DisplayHood);
    function DisplayHood() {
    $("#Oval").attr("hidden", false);
    $("#SiriWave").attr("hidden", true);}



    // to display sender and receiver text in chat box

  eel.expose(senderText)
    function senderText(message) {
        var chatBox = document.getElementById("chat-canvas-body");
        if (message.trim() !== "") {
            chatBox.innerHTML += `<div class="row justify-content-end mb-4">
            <div class = "width-size">
            <div class="sender_message">${message}</div>
        </div>`; 
    
            // Scroll to the bottom of the chat box
            chatBox.scrollTop = chatBox.scrollHeight;
        }
    }

    eel.expose(receiverText)
    function receiverText(message) {

        var chatBox = document.getElementById("chat-canvas-body");
        if (message.trim() !== "") {
            chatBox.innerHTML += `<div class="row justify-content-start mb-4">
            <div class = "width-size">
            <div class="receiver_message">${message}</div>
            </div>
        </div>`; 
    
            // Scroll to the bottom of the chat box
            chatBox.scrollTop = chatBox.scrollHeight;
        }
        
    }




});