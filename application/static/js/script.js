// application/static/js/script.js


const form = document.querySelector('form');
const table = document.querySelector('table');


const displayTable = () => {
    document.getElementById('hide').style.display = 'block';
}


form.addEventListener('submit', displayTable, false);
