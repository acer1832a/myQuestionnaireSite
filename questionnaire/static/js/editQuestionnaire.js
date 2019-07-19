function deleteElement(buttonElement) {
    let divID = buttonElement.value;
    divID = divID.substring(0, divID.lastIndexOf('_'));
    console.log(divID);
    $('#'+divID).remove();
}