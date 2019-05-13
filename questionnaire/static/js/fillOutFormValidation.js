$('button[type="submit"]').on('click', function() {
    let isValid = true;
    let fieldSets = document.querySelectorAll('form fieldset');
    for (let index = 0; index < fieldSets.length; index++) {
        const fieldSet = fieldSets[index];
        let h1Node = fieldSet.querySelector('h1');
        if (h1Node) {
            fieldSet.removeChild(h1Node);
        }
        
        if (fieldSet.querySelectorAll('input:checked').length === 0) {
            isValid = false;
            let h = document.createElement("H1");
            let t = document.createTextNode("尚未勾選任何項目!");
            h.appendChild(t);
            fieldSet.insertBefore(h, fieldSet.firstChild);
        }
    }
    
    return isValid;
});

$( function() {
    $( "#id_birthday" ).datepicker({
        dateFormat: "yy-mm-dd"
      });
  } );