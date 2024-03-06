IdNumberToDelete = -1;

const DeleteModal = new bootstrap.Modal(document.getElementById('deleteUserModal'))


function GotoUserEdit(IdNumber,fromPersonalInfo) {
    location.href="/editUser?IdNumber=" + IdNumber + "&fromPersonalInfo=" + fromPersonalInfo
}

function deleteUser() {
    location.href="/deleteUser?IdNumber=" + IdNumberToDelete
}

function AddMoreUser(fromDashBoard) {
    location.href="/addUser?fromDashBoard=" + fromDashBoard
}

function callDeleteModal(IdNumber) {
    
    DeleteModal.show()
    IdNumberToDelete = IdNumber

}