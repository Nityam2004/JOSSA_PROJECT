// script.js

document.addEventListener('DOMContentLoaded', () => {
    const faqItems = document.querySelectorAll('.faq-item');

    faqItems.forEach(item => {
        item.addEventListener('click', () => {
            const answer = item.querySelector('.answer');
            answer.classList.toggle('visible');

            const icon = item.querySelector('.faq-question .icon');
            if (answer.classList.contains('visible')) {
                icon.textContent = '-';
            } else {
                icon.textContent = '+';
            }
        });
    });
});
