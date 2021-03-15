// application/static/js/script.js


let date = new Date();

(function() {
    date = date.toISOString();
    document.querySelector('.date_time').textContent = date;
})();
