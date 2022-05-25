document.getElementById("firstBtn").onclick = function () { checkInstitutions() };
function checkInstitutions() {
    const array = []
    var checkboxes = document.querySelectorAll('input[type=checkbox]:checked')

    for (var i = 0; i < checkboxes.length; i++) {
        array.push(checkboxes[i].value)
    }
    return array
}

document.getElementById("firstBtn").onclick = function () { setInstitutions() };
function setInstitutions() {


    var institutions = document.getElementsByClassName("organizations");

    for (var i = 0; i < institutions.length; i++) {
        institutions_values = institutions[i].getAttribute('data-categories')

        const arr = checkInstitutions()
        const contains = arr.some(element => {
            if (institutions_values.includes(element)) {
                return true;
            }

            return false;
        });

        if (contains == false) {
            institutions[i].style.display = "none";
        }
        else {
            institutions[i].style.display = "block";
        }

    }
}