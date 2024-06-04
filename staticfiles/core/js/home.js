
$(document).ready(function(){
    const typewriter = document.querySelector("#typewriter");
    tinyTypewriter(typewriter, {
        items: ['project topics.', "research materials."]
    });

	$(window).on("scroll",function(){
        var scroll = $(window).scrollTop();
        
        if (scroll > 50) {
            $('nav').removeClass('navbar-transparent shadow-none');
            $('.navbar-brand').removeClass('text-white')
            $('nav').addClass('navbar-light bg-white shadow-lg');
            $('.navbar-brand').addClass('text-dark')

        } else{
            $('nav').removeClass('navbar-light bg-white shadow-lg');
            $('.navbar-brand').removeClass('text-dark')
            $('nav').addClass('navbar-transparent shadow-none');
            $('.navbar-brand').addClass('text-white')
        }
    });
});
