function enableFirstStep() {
    var checkboxes = document.querySelectorAll('input[type=checkbox]:checked')
    if(checkboxes.length > 0){
        document.getElementById('firstBtn').disabled = false;
    }
    else{
        document.getElementById('firstBtn').disabled = true;
    }
  }
function enableSecondStep() {
    bags = document.querySelector('input[name=bags]').value
    if(bags > 0){
        document.getElementById('secondBtn').disabled = false;
    }
    else{
        document.getElementById('secondBtn').disabled = true;
    }
  }
function enableThirdStep() {
    institutions = document.querySelector('input[type=radio][name=organization]:checked');
    if(institutions){
        document.getElementById('thirdBtn').disabled = false;
    }
    else{
        document.getElementById('thirdBtn').disabled = true;
    }
  }
function enableFourthStep() {
    var street = document.getElementsByName('address')[0].value
    var city = document.getElementsByName('city')[0].value
    var postcode = document.getElementsByName('postcode')[0].value
    var phone = document.getElementsByName('phone')[0].value
    var date = document.getElementsByName('data')[0].value
    var time = document.getElementsByName('time')[0].value
    var more_info = document.getElementsByName('more_info')[0].value
    var postcode_pattern = /[0-9]{2}-[0-9]{3}$/;
    var phone_pattern = /^(?:\(?\?)?(?:[-\.\(\)\s]*(\d)){9}\)?$/
    postcode_validation = postcode_pattern.test(postcode)
    phone_validation = phone_pattern.test(phone)
    function checkDate(date){
        const today = new Date()
        today.setHours(0, 0, 0, 0);
        const tomorrow = new Date(today)
        tomorrow.setDate(tomorrow.getDate() + 1)
        if(new Date(date) > tomorrow){
            return true
        }
        else{
            return false
        }

    }

    
    if(street && city && more_info && time && postcode_validation && phone_validation && checkDate(date)){
        document.getElementById('fourthBtn').disabled = false;
    }
    else{
        document.getElementById('fourthBtn').disabled = true;
    }
  }

document.getElementById('firstBtn').addEventListener('click', function(){
    checkInstitutions();
    institutionNames();
});

function checkInstitutions() {
    categoriesID = []
    var checkboxes = document.querySelectorAll('input[type=checkbox]:checked')

    for (var i = 0; i < checkboxes.length; i++) {
        categoriesID.push(checkboxes[i].value)

    }
    return categoriesID
}

function institutionNames() {
    var checkboxes = document.querySelectorAll('input[type=checkbox]:checked')
    categoriesNames =""
    for (var i = 0; i < checkboxes.length; i++) {
        var parentLabel = checkboxes[i].parentElement
        var institutionName = parentLabel.querySelector('.description').innerHTML;
        categoriesNames += institutionName + ", "
    }
    return categoriesNames
}


document.getElementById("firstBtn").onclick = function () { setInstitutions() };
function setInstitutions() {


    var institutions = document.getElementsByClassName("organizations");

    for (var i = 0; i < institutions.length; i++) {
        institutions_values = institutions[i].getAttribute('data-categories')
        
        const checkedInstitutions = checkInstitutions()
        const contains = checkedInstitutions.every(element => {
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

document.getElementById("secondBtn").onclick = function () { getBags() };
function getBags() {
    bags = document.querySelector('input[name=bags]').value
    return bags
}

document.getElementById("thirdBtn").onclick = function () { getInstitutions() };
function getInstitutions() {
    var institutions = document.querySelector('input[type=radio][name=organization]:checked');
    var parentLabel = institutions.parentElement
    var description = parentLabel.querySelector('.description');
    title = description.querySelector('.title').innerHTML;
    return title
}

document.getElementById('fourthBtn').addEventListener('click', function(){
    getAddress();
    fillSummary();
});


function getAddress() {
    var street = document.getElementsByName('address')[0].value
    var city = document.getElementsByName('city')[0].value
    var postcode = document.getElementsByName('postcode')[0].value
    var phone = document.getElementsByName('phone')[0].value
    var date = document.getElementsByName('data')[0].value
    var time = document.getElementsByName('time')[0].value
    var more_info = document.getElementsByName('more_info')[0].value
    addressDictionary = { "street": street, "city": city, 
                "postcode": postcode, "phone": phone, 
                "date": date, "time": time, 
                "more_info": more_info}
    return addressDictionary
}


function fillSummary() {
    document.getElementById("donatedBags").innerHTML= bags + " worków " +  categoriesNames ;
    document.getElementById("donatedFoundations").innerHTML= "Dla fundacji: " + title ;
    document.getElementById("donatedStreet").innerHTML = addressDictionary["street"] ;
    document.getElementById("donatedCity").innerHTML = addressDictionary["city"] ;
    document.getElementById("donatedPostal").innerHTML = addressDictionary["postcode"] ;
    document.getElementById("donatedPhone").innerHTML = addressDictionary["phone"] ;
    document.getElementById("donatedDate").innerHTML = addressDictionary["date"] ;
    document.getElementById("donatedHour").innerHTML = addressDictionary["time"] ;
    document.getElementById("donatedComments").innerHTML = addressDictionary["more_info"] ;
}
