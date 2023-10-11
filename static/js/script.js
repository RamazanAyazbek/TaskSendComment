
    const form = document.querySelector('#formReview'); 
    form.addEventListener('submit', function(event) {
        event.preventDefault();
        fetch(form.action, {
            method: 'POST',
            body: new FormData(form)
        })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                alert(data.error);
            } else {
        
                window.location.href = data.redirect_url;
            }
        })
        .catch(error => {
        
            console.error('Error:', error);
        });
    });
