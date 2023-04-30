$(document).ready(function () {
    jQuery('.flexslider').flexslider({
        animation: "slide",
        controlNav: true,
        directionNav: true,
        pausePlay: true,
        slideshowSpeed: 6000,
        touch: true,
        start: function (slider) {
            jQuery('body').removeClass('loading');
        }
        //animationSpeed: 500,
    });
});