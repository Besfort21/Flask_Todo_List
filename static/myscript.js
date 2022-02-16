window.onload = function () {
    var moveUp = document.querySelectorAll(".up");

    for (var i = 0; i < moveUp.length; i++) {
        moveUp[i].addEventListener('click', function () {
            var wrapper = this.parentElement;

            if (wrapper.previousElementSibling)
                wrapper.parentNode.insertBefore(wrapper, wrapper.previousElementSibling);
        });
    }

    var moveDown = document.querySelectorAll(".down");

    for (var i = 0; i < moveDown.length; i++) {
        moveDown[i].addEventListener('click', function () {
            var wrapper = this.parentElement;

            if (wrapper.nextElementSibling)
                wrapper.parentNode.insertBefore(wrapper.nextElementSibling, wrapper);
        });
    }
}