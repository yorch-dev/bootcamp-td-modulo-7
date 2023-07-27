setTimeout(function() {
    var messages = document.getElementsByClassName('alert');
    for (var i = 0; i < messages.length; i++) {
        messages[i].remove('show');
    }
}, 3000);