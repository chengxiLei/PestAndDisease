//get the editUser Failed Modal 
const addGuideFailedModalEle = document.getElementById('addGuideFailedModal')
const addGuideFailedModal = new bootstrap.Modal(addGuideFailedModalEle)

form = document.getElementById("addGuideForm")
//validate the form before submit 
function guideAddFormSubmit() {
    //check if the Common name is empty
    console.log(document.getElementById("commonName").value)
    if(!document.getElementById("commonName").value){
        //activate the modal
        activateModal("the common name must be filled")
        return 0
    }
    // check if the Primary Image is empty
    console.log(document.getElementById("addPrimary").value)
    if(!document.getElementById("addPrimary").value){
        //activate the modal
        activateModal("the primary image must be chose")
        return 0
    }
    //submit
    form.submit()
    return 
}

function activateModal(text) {
    //cahnge the content of the modal
    addGuideFailedModalEle.addEventListener('show.bs.modal', function (event) {
        // Update the modal's content.
            var modalBodyInput = addGuideFailedModalEle.querySelector('.modal-body')
            modalBodyInput.innerHTML = text
            })
            addGuideFailedModal.show()
}





