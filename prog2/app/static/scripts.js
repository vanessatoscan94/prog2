/* exported myFunction */

function myFunction() {
    document.getElementById("dropdown_exercises").classList.toggle("show");
}

window.onclick = function(event) {
    if (!event.target.matches('.dropdown_button')) {
        var dropdowns = document.getElementsByClassName("drop_exer_content");
        var i;
        for (i = 0; i < dropdowns.length; i++) {
            var openDropdown = dropdowns[i];
            if (openDropdown.classList.contains('show')) {
                openDropdown.classList.remove('show');
            }
        }
    }
}