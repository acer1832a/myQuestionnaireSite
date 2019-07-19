$('button[type="submit"]').on('click', function() {
    let isValid = true;
    //remove alert
    $('li.alert').remove();
    $('.alert').parent().remove();
    
    if ($('#id_birthday').val() == '') {
        $('#id_birthday').parent().after($('<div class="col-sm-9"><div class="alert alert-warning alert-dismissible" role="alert">\
        <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button>\
        <strong>Warning!</strong> 請選擇生日。\
        </div></div>'));
        
        isValid = false;
    }
    if ($('#gender').val() == '請選擇') {
        $('#gender').parent().after($('<div class="col-sm-9"><div class="alert alert-warning alert-dismissible" role="alert">\
        <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button>\
        <strong>Warning!</strong> 請選擇性別。\
        </div></div>'));
        
        isValid = false;
    }
    if ($('#education').val() == '請選擇') {
        $('#education').parent().after($('<div class="col-sm-9"><div class="alert alert-warning alert-dismissible" role="alert">\
        <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button>\
        <strong>Warning!</strong> 請選擇最高學歷。\
        </div></div>'));
        isValid = false;
    }
    if ($('#annual_income').val() == '請選擇') {
        $('#annual_income').parent().after($('<div class="col-sm-9"><div class="alert alert-warning alert-dismissible" role="alert">\
        <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button>\
        <strong>Warning!</strong> 請選擇年收入。\
        </div></div>'));
        isValid = false;
    }

    $('.list-group').each(function () {
        let $listGroup = $(this);
        let inputs = $listGroup.find('input');
        for (var i=0; i<inputs.length;i++) {
            if ($(inputs[i]).prop('checked')) {
                return;
            }
        }

        $listGroup.find('.list-group-item').first().after($('<li class="list-group-item alert alert-warning alert-dismissible" role="alert">\
        <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button>\
        <strong>Warning!</strong> 請選擇答案。\
        </li>'));
    });
    
    return isValid;
});

$( function() {
    $( "#id_birthday" ).datepicker({
        dateFormat: "yy-mm-dd"
      });
  } );