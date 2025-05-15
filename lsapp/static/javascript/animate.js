function fadeEffect() {
    let text = document.getElementById('messagefade');
    if (!text) return;

    // Fade in
    text.classList.add('visible');

    // After 3 seconds, fade out
    setTimeout(() => {
        text.classList.remove('visible');
    }, 5000); // adjust delay if needed
}

window.addEventListener('DOMContentLoaded', fadeEffect);