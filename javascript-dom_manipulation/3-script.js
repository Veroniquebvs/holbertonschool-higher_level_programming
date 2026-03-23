const btn = document.getElementById('toggle_header');
const header = document.querySelector('header');
btn.addEventListener('click', () => {
  if (header.classList.contains('red')) {
    header.classList.remove('red');
    header.classList.add('green');
  } else {
    header.classList.remove('green');
    header.classList.add('red');
  }
});
