//Thank you modal
let modal = document.querySelector('.modal');
document.getElementById('modal-link').addEventListener('click', () => {
  modal.style.display = 'block';
});

document.querySelector('.close').addEventListener('click', () => {
  modal.style.display = 'none';
});

window.addEventListener('click', (e) => {
  if (e.target == modal) {
    modal.style.display = 'none';
  }
});

// Load the moon image responsively
const mobileWidth = 450;
var userScreenWidth = window.innerWidth;

const mobileImgSrc = './assets/images/moon-small.jpeg';
const desktopImgSrc = './assets/images/moon.jfif';

var img = document.querySelector('.responsive-img');

if (userScreenWidth < mobileWidth) {
  img.src = mobileImgSrc;
} else {
  img.src = desktopImgSrc;
}
