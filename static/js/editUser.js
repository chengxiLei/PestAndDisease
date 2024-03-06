//get argue form template
user = JSON.parse(document.getElementById("dataTrans").dataset.iteminfoforuser.replaceAll("\'", "\""))
console.log(user)
//from personal info page or user page
requstfrompersonalinfo = (document.getElementById("dataTransrequstfrompersonalinfo").dataset.requstfrompersonalinfo.replaceAll("\'", "\""))
console.log(requstfrompersonalinfo == "True")

//fill in inital info
document.getElementById("Status").value = user.Status
document.getElementById("Authority").value = user.Authority

//get the editUser Failed Modal 
const editUserFailedModalEle = document.getElementById('editUserFailedModal')
const editUserFailedModal = new bootstrap.Modal(editUserFailedModalEle)


function userEditFormSubmit() {
    //check if any input contain quotes
    if (checkIfFormValueContainQuote()) {
        activateModal("quote is included in some field, please remove these quotes")
        return 0
    }
    //check if the new Username is duplicated with the existed ones
    form = document.getElementById("userEditForm")
    console.log(form)
    newUsername = document.getElementById("Username").value
    oldUsername = user.Username
    console.log(!newUsername)
    //if new Username is empty
    if (!newUsername) {
        activateModal("The Username is empty, please change the Username.")
        return 0
    }
    //only from personal page can we change password
    if (requstfrompersonalinfo == "True") {
        Passwd = document.getElementById("Passwd")
        if (Passwd.value == "") {
            Passwd.disabled = true
            form.submit()
            return 0
        }
    }
    //check email format
    email = document.getElementById("Email").value
    if (!email.includes("@") && email) {
        activateModal("email format is incorrect")
        return 0
    }
    //if the form did not change Username fine
    if (oldUsername == newUsername && !!newUsername) {
        form.submit()
    } else {
        //if the form change Username, check if it is duplicated with existed ones (other than the original Username of itself)
        url = 'http://' + window.location.host + '/checkUsernameDuplication'
        const Http = new XMLHttpRequest();
        Http.open("GET", url);
        Http.send();
        //feedback function to respond
        Http.onload = (e) => {
            UsernameArray = JSON.parse(Http.responseText)
            //remove the original Username of itself among all Usernames
            indexofOldUsername = UsernameArray.indexOf(oldUsername)
            UsernameArray.splice(indexofOldUsername, 1)
            if (!UsernameArray.includes(newUsername)) {
                //validation is finished
                form.submit()
            } else {
                //Username duplicated
                activateModal("The Username is duplicated with an existed one, please change the Username.")
            }
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



var idsOfFormInputShouldBeChecked = ["LastName", "FirstName", "Address", "Email", "PhoneNumber", "Username"]

//only from personal page can we change password
if (requstfrompersonalinfo == "True") {
    idsOfFormInputShouldBeChecked.push("Passwd")
}

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






