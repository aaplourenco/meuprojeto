document.addEventListener('DOMContentLoaded', () => {
    const tutorialDivs = document.querySelectorAll('.tutoriais');

    tutorialDivs.forEach(div => {
        div.addEventListener('click', () => {
            const link = div.getAttribute('data-link');
            window.location.href = link;
        });
    });
});
