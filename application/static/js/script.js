// application/static/js/script.js


const date = new Date();

(function() {
    date.toLocaleString('en-US', { 
        hour12: false, 
        year: 'numeric', 
        month: 'long', 
        day: 'numeric', 
        weekday: 'long', 
        timeZone: 'UTC', 
        minute: '2-digit', 
        second: '2-digit', 
        second: '2-digit', 
        hour: '2-digit' 
    });
    document.querySelector('.date-and-time').textContent = date;
})();
