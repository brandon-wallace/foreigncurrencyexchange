// application/static/js/script.js


const form = document.querySelector('form');
const table = document.querySelector('table');


const displayTable = () => {
    document.getElementById('hide').style.display = 'block';
}


form.addEventListener('submit', setTimeout(displayTable, 500), false);
