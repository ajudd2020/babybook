
var scroll=window.requestAnimationFrame ||
    function(callback) {
        window.setTimeout(callback, 1000/60)
    };

// Helper function from: http://stackoverflow.com/a/7557433/274826
function isElementInViewport(el) {
    var rect = el.getBoundingClientRect();
    return (
      (rect.top <= 0
        && rect.bottom >= 0)
      ||
      (rect.bottom >= (window.innerHeight || document.documentElement.clientHeight) &&
        rect.top <= (window.innerHeight || document.documentElement.clientHeight))
      ||
      (rect.top >= 0 &&
        rect.bottom <= (window.innerHeight || document.documentElement.clientHeight))
    );
  }

  var elementsToShow = document.querySelectorAll('.scroll-appear');

function loop() {
    elementsToShow.forEach(function(element) {
        if (isElementInViewport(element)) {
            element.classList.add('visible');
        } else {
            element.classList.remove('visible');
        }
    });

    scroll(loop)
}

loop();
