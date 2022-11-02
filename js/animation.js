(function () {
    const checkVisibility = function (docElement) {
        const docHeight = window.innerHeight;
        const scrollHeight = document.body.scrollTop;
        return (
            docElement.offsetTop < scrollHeight + docHeight &&
            docElement.offsetTop + docElement.clientHeight > scrollHeight
        );
    };
    const triggerAnimation = function () {
        const victims = document.querySelectorAll(".unanimated-fade-in");
        for (const element of victims) {
            if (checkVisibility(element)) {
                element.classList.remove("unanimated-fade-in");
                element.classList.add("animated-fade-in");
            }
        }
    };
    triggerAnimation();
    window.onscroll = triggerAnimation;
})();//apply a fade-in effect on all tags with the class "unanimated-fade-in"
