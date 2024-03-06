FreshwaterIdToDelete = -1;

const DeleteModal = new bootstrap.Modal(document.getElementById('deleteGuideModal'))

//transform token of quotes to quotes and display them
guides = JSON.parse(document.getElementById("dataTrans").dataset.guidearray.replaceAll("\'", "\""))
console.log(guides)
index = 0
guides.forEach(guide => {
    guide.CommonName = guide.CommonName.replaceAll("_tokeForSingleQuote_", "'")
    guide.CommonName = guide.CommonName.replaceAll("_tokeForDoubleQuote_", '"')
    document.getElementById("titleForCommonName"+"'"+index+"'").innerHTML = guide.CommonName
    index++
});


function GotoDetail(FreshwaterId) {
    location.href = "/detail?FreshwaterId=" + FreshwaterId
}

function GotoEdit(FreshwaterId) {
    location.href = "/editguide?FreshwaterId=" + FreshwaterId
}

function AddMoreGuide() {
    location.href = "/addGuide"
}

function deleteGuide() {
    location.href = "/deleteGuide?FreshwaterId=" + FreshwaterIdToDelete
}


function callDeleteModal(FreshwaterId) {

    DeleteModal.show()
    FreshwaterIdToDelete = FreshwaterId

}