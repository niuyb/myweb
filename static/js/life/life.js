var MaterialModals = function() {

    var modalTriggers = document.querySelectorAll('.modal__wrapper-deactive')

    var triggerModal = function(e) {

        var modal = e.currentTarget
        // var bounds = modal.getBoundingClientRect()
        var modalNavigation = document.querySelector('.modal__navigation')
        var img = modal.querySelector('.life_infos_img')
        // var img = modal.getElementsByClassName('life_infos_img')

        // makeFillerDiv(modal, bounds)
        // setStarting(modal, bounds)

        modal.classList.remove('modal__wrapper-deactive')
        img.style.height = "auto"
        modal.style.position = 'fixed'


        setTimeout(function() {

            modal.classList.add('modal__wrapper-active')
            modalNavigation.classList.add('modal__navigation-active')

        }, 100)


    }

    var closeModal = function() {

        var modal = document.querySelector('.modal__wrapper-active')
        var fillerDiv = document.querySelector('.modal__wrapper-filler')
        // var bounds = fillerDiv.getBoundingClientRect()
        var modalNavigation = document.querySelector('.modal__navigation-active')
        var img = modal.querySelector('.life_infos_img')

        // setStarting(modal, bounds)

        modal.style.transition = 'all .3s'
        modal.classList.remove('modal__wrapper-active')
        modal.classList.add('modal__wrapper-deactive')
        img.style.height = "400px"

        // resetModal(modal, fillerDiv)

        modalNavigation.classList.remove('modal__navigation-active')

    }

    var resetModal = function(modal, fillerDiv) {

        var parent = document.getElementById('modals_wrapper')

        setTimeout(function() {

            modal.style = ''
            parent.removeChild(fillerDiv)

        }, 500)

    }

    // var makeFillerDiv = function(modal, bounds) {

        // var fillerDiv = document.createElement('div')
        // var parent = document.getElementById('modals_wrapper')

        // fillerDiv.style.width = bounds.width + 'px'
        // fillerDiv.style.height = bounds.height + 'px'

        // fillerDiv.className = 'modal__wrapper modal__wrapper-filler'
        // parent.insertBefore(fillerDiv, modal);

    // }

    var setStarting = function(modal, bounds) {

        modal.style.top = bounds.top + 'px'
        modal.style.left = bounds.left + 'px'
        modal.style.width = bounds.width + 'px'
        modal.style.height = bounds.height + 'px'
        modal.style.position = 'fixed'
        modal.style.margin = 0

    }

    var init = function() {

        for (var i = 0; i < modalTriggers.length; i++) {

            modalTriggers[i].addEventListener('click', triggerModal)

        }

        document.getElementById('modal__back').addEventListener('click', closeModal)

    }

    init()

}()