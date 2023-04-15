const humburgerBtn = document.getElementById('hamburger');
const folders = document.getElementById('folders');
const files = document.getElementById('files');
const main = document.getElementById('main');

humburgerBtn.addEventListener('click', () =>{
    folders.classList.toggle('hide');
    files.classList.toggle('hide');
    main.classList.toggle('hide');
})