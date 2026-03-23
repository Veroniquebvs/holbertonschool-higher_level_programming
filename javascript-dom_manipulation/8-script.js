document.addEventListener('DOMContentLoaded', () => {
  const hello = document.getElementById('hello');

  fetch('https://hellosalut.stefanbohacek.com/?lang=fr')
    .then(res => res.json())
    .then(data => {
      hello.textContent = data.hello;
    });
});
