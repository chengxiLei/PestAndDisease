function SetToPrimary(image) {
    location.href="/setPrimaryImage?FreshwaterId=" + guide.FreshwaterId + "&image=" + image
}


//get argue form template
guide = JSON.parse(document.getElementById("dataTrans").dataset.iteminfo.replaceAll("\'","\""))
console.log(guide)
//translate token into Quote
guide.CommonName = guide.CommonName.replaceAll("_tokeForSingleQuote_","'")
guide.CommonName = guide.CommonName.replaceAll("_tokeForDoubleQuote_",'"')

guide.ScientificName = guide.ScientificName.replaceAll("_tokeForSingleQuote_","'")
guide.ScientificName = guide.ScientificName.replaceAll("_tokeForDoubleQuote_",'"')

guide.KeyCharacteristics = guide.KeyCharacteristics.replaceAll("_tokeForSingleQuote_","'")
guide.KeyCharacteristics = guide.KeyCharacteristics.replaceAll("_tokeForDoubleQuote_",'"')

guide.BiologyDescription = guide.BiologyDescription.replaceAll("_tokeForSingleQuote_","'")
guide.BiologyDescription = guide.BiologyDescription.replaceAll("_tokeForDoubleQuote_",'"')

guide.Impacts = guide.Impacts.replaceAll("_tokeForSingleQuote_","'")
guide.Impacts = guide.Impacts.replaceAll("_tokeForDoubleQuote_",'"')

console.log(guide)


//fill in inital info
document.getElementById("type").value = guide.FreshwaterItemtType
document.getElementById("present").value = guide.PresentInNZ


document.getElementById("commonName").value = guide.CommonName
document.getElementById("scientificName").value = guide.ScientificName

document.getElementById("keyCharacteristics").value = guide.KeyCharacteristics
document.getElementById("biologyDescription").value = guide.BiologyDescription
document.getElementById("impacts").value = guide.Impacts




//get the editUser Failed Modal 
const editGuideFailedModalEle = document.getElementById('editGuideFailedModal')
const editGuideFailedModal = new bootstrap.Modal(editGuideFailedModalEle)

form = document.getElementById("editGuideForm")
//validate the form before submit 
function guideAddFormSubmit() {
    //check if the Common name is empty
    console.log(document.getElementById("commonName").value)
    if(!document.getElementById("commonName").value){
        //activate the modal
        activateModal("the common name must be filled")
        return 0
    }
    //submit
    form.submit()
    return 
}

function activateModal(text) {
    //cahnge the content of the modal
    editGuideFailedModalEle.addEventListener('show.bs.modal', function (event) {
        // Update the modal's content.
            var modalBodyInput = editGuideFailedModalEle.querySelector('.modal-body')
            modalBodyInput.innerHTML = text
            })
            editGuideFailedModal.show()
}



const deleteImageModalEle = document.getElementById('deleteImageModal')
const deleteImageModal = new bootstrap.Modal(deleteImageModalEle)
imageToDelete = ""

function activateDeleteImageModal(image) {
    imageToDelete = image
    deleteImageModal.show()
}
function deleteImage() {
    //check if image is primary, if yes, forbiden
    if(imageToDelete == guide.PrimaryImage){
        alert("You can not delete the Primary one, please try to set another one as primary, then delete this one.");
        return
    }
    //image is to remove from present arrays
    //deep copy
    deletedArray = guide.Images.slice(0)
    index = deletedArray.indexOf(imageToDelete)
    deletedArray.splice(index, 1)
    console.log(guide.Images)
    console.log(deletedArray)

    location.href = ("/deleteImage?FreshwaterId=" + guide.FreshwaterId + "&newImageArrayString=" + deletedArray.join(",") + "&imageTodelete=" + imageToDelete)
}