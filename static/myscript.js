/**
 * Returns all elements that match up or down.
 * Then loops through the elements.
 * Saves the parent element of the specified element in wrapper.
 * If there is a previous element or an element immediately following the specified element, in the same tree level.
 * inserts the element before the previous element when selector is up.
 * inserts the nextElementSibling before the element when selector is down. ---> the opposite way because there is no insert after method. 
 */
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