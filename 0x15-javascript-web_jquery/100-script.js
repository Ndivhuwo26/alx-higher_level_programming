// a JavaScript script that updates the text color of the <header> element to red (#FF0000):

document.addEventListener('DOMContentLoaded', () => {
  const header = document.querySelector('header');
  if (header) {
    header.style.color = '#FF0000';
  }
});

