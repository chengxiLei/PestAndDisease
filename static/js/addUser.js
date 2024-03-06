//get the editUser Failed Modal 
const editUserFailedModalEle = document.getElementById('editUserFailedModal')
const editUserFailedModal = new bootstrap.Modal(editUserFailedModalEle)

//need to fix
function userEditFormSubmit() {
    //check if any input contain quotes
    if (checkIfFormValueContainQuote()) {
        activateModal("quote is included in some field, please remove these quotes")
        return 0
    }
    //check if the new Username is duplicated with the existed ones
    form = document.getElementById("userAddForm")
    console.log(form)
    newUsername = document.getElementById("Username").value
    Passwd = document.getElementById("Passwd").value
    console.log(!newUsername)
    //if new Username is empty
    if (!newUsername) {
        activateModal("The Username is empty, please change the Username.")
        return 0
    }
    if (!Passwd) {
        activateModal("The Password is empty, please change the Password.")
        return 0
    }
    //check email format
    email = document.getElementById("Email").value
    if (!email.includes("@") && email) {
        activateModal("email format is incorrect")
        return 0
    }

    //if the form change Username, check if it is duplicated with existed ones (other than the original Username of itself)
    url = 'http://' + window.location.host + '/checkUsernameDuplication'
    const Http = new XMLHttpRequest();
    Http.open("GET", url);
    Http.send();
    //feedback function to respond
    Http.onload = (e) => {
        UsernameArray = JSON.parse(Http.responseText)
        //remove the original Username of itself among all Usernames
        if (!UsernameArray.includes(newUsername)) {
            //validation is finished
            form.submit()
        } else {
            //Username duplicated
            activateModal("The Username is duplicated with an existed one, please change the Username.")
        }
    }

}

function activateModal(text) {
    //cahnge the content of the modal
    editUserFailedModalEle.addEventListener('show.bs.modal', function (event) {
        // Update the modal's content.
        var modalBodyInput = editUserFailedModalEle.querySelector('.modal-body')
        modalBodyInput.innerHTML = text
    })
    editUserFailedModal.show()
}


//check if form contains quotes

var idsOfFormInputShouldBeChecked = ["LastName", "FirstName", "Address", "Email", "PhoneNumber", "Username","Passwd"]

function checkIfFormValueContainQuote() {
    var containQuote = false
    idsOfFormInputShouldBeChecked.forEach(function (id) {
        if (stringContainQuotes(document.getElementById(id).value)) { containQuote = true }
    })
    return containQuote;
}
function stringContainQuotes(str) {
    return str.includes("'") || str.includes('"')
}


