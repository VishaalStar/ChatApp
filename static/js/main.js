document.addEventListener('DOMContentLoaded', function() {
    const toggleBtn = document.getElementById('toggleMenu');
    const leftMenu = document.getElementById('leftMenu');

    toggleBtn.addEventListener('click', function() {
        leftMenu.classList.toggle('collapsed');
    });

    function adjustScale() {
        const width = window.innerWidth;
        let scale = 1;

        if (width >= 992 && width <= 1600) {
            scale = 0.9;
        } else if (width >= 700 && width <= 767) {
            scale = 0.8;
        } else if (width >= 600 && width < 700) {
            scale = 0.75;
        } else if (width <= 600) {
            scale = 0.5;
        }

        document.body.style.transform = `scale(${scale})`;
    }

    window.addEventListener('resize', adjustScale);
    adjustScale();
});

