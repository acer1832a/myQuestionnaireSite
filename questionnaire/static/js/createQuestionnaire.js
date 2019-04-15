function addChoice(buttonElement){
    $buttonElement = $(buttonElement);
    let buttonValue = $buttonElement.val();
    let choiceName = buttonValue.substring(0,buttonValue.lastIndexOf('_'));
    let choiceCount = parseInt(buttonValue.substring(buttonValue.lastIndexOf('_')+1));
    let newChoiceName = choiceName + '_' + (choiceCount+1);
    $buttonElement.val(choiceName + '_' + (choiceCount+1));
    $label = $('<label></label>');
    $label.attr('for', 'id_'+newChoiceName);
    $label.text('選項' + (choiceCount+1));
    $input = $('<input type="text" required></input>');
    $input.attr('id', 'id_'+newChoiceName);
    $input.attr('name', newChoiceName);
    $newElement = $('<li></li>');
    $label.appendTo($newElement);
    $input.appendTo($newElement);
    $buttonElement.before($newElement);
}

function addQuestion(buttonElement){
    let $buttonElement = $(buttonElement);
    let buttonValue = $buttonElement.val();
    let questionIndex = parseInt(buttonValue.substring(buttonValue.lastIndexOf('_')+1))+1;
    let questionName = buttonValue.substring(0,buttonValue.lastIndexOf('_'))+'_'+questionIndex;
    const questionElementHTML = '<div>\n'
        +'<label for="id_' + questionName + '_text">問題' + questionIndex + '：</label><input type="text" name="' + questionName + '_text" id="id_' + questionName + '_text" required></input>\n'
        +'<label for="id_' + questionName + '_allowed_mutiple_answers">是否允許多選：</label><input type="checkbox" name="' + questionName + '_allowed_mutiple_answers" id="id_' + questionName + '_allowed_mutiple_answers">\n'
        +'<ul>\n'
            +'<li><label for="id_' + questionName + '_choice_text_1">選項1</label><input type="text" required name="' + questionName + '_choice_text_1" id="id_' + questionName + '_choice_text_1"></li>\n'
            +'<button type="button" onclick="addChoice(this)" value="' + questionName + '_choice_text_1">新增選項</button>\n'
        +'</ul>\n'
    +'</div>';
    $buttonElement.before($(questionElementHTML));
    $buttonElement.val(questionName);
}