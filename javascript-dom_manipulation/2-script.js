const btn = document.getElementById('red_header');
const header = document.querySelector('header');
btn.addEventListener('click', () => {
  header.classList.add('red');
});
