    /**
     * Mobile menu
     */
    var $navToggler = $('.navbar-toggler');
    $navToggler.on('click', function () {
    $(this).toggleClass('actived');
    })
    $navToggler.on('click', function () {
    $('.navbar-collapse').toggleClass('menu-opened');
    })

    /**
     * Tooltip
     */
    $(function() {
        $('[data-toggle="tooltip"]').tooltip()
    })
