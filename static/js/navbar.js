document.addEventListener('DOMContentLoaded', function() {
    console.log("test")
    var elems = document.querySelectorAll('.sidenav');
    var instances = M.Sidenav.init(elems);
  });