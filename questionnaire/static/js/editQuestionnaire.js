function deleteElement(buttonElement) {
    const DELETETAG = 'delete_';
    if (buttonElement.value.startsWith('choice')) {
        buttonElement.parentNode.style.display = 'none';
        let choiceElement = buttonElement.previousSibling;
        choiceElement.name = DELETETAG+choiceElement.name;
    } else {
        let questionDiv = buttonElement.parentNode.parentNode;
        questionDiv.style.display = 'none';
        let inputElements = questionDiv.querySelectorAll("input");
        for (const key in inputElements) {
            inputElements[key].name = DELETETAG+inputElements[key].name;
        }
    }
}