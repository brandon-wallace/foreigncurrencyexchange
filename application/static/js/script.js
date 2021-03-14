// application/static/js/script.js


const date = new Date();

(function() {
    date.toLocaleString({ 
    document.querySelector('.date_time').textContent = date;
})();
