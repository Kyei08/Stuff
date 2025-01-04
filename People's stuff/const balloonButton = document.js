const balloonButton = document.querySelector('.balloon-button');
const balloonsContainer = document.querySelector('.balloons-container');

balloonButton.addEventListener('click', () => {
    const balloon = document.createElement('div');
    balloon.classList.add('balloon');

    const randomX = Math.random() * window.innerWidth;
    const randomY = Math.random() * window.innerHeight;

    balloon.style.left = `${randomX}px`;
    balloon.style.top = `${randomY}px`;

    balloonsContainer.appendChild(balloon);

    setTimeout(() => {
        balloon.remove();
    }, 5000); // Adjust the duration as needed
});