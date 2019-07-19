function addChoice(buttonElement){
    $buttonElement = $(buttonElement);
    let buttonValue = $buttonElement.val();
    let choiceName = buttonValue.substring(0,buttonValue.lastIndexOf('_'));
    let choiceCount = parseInt(buttonValue.substring(buttonValue.lastIndexOf('_')+1));
    let newChoiceName = choiceName + '_' + (choiceCount+1);
    let formGroupID = 'group_' + choiceName + '_' + choiceCount;
    $formGroup = $('#'+formGroupID);
    $inputDivElement = $('<div class="col-sm-10"></div>');
    $buttonDivElement = $('<div class="col-sm-offset-2 col-sm-10"></div>');
    $buttonElement.val(choiceName + '_' + (choiceCount+1));
    $label = $('<label class="control-label col-sm-2"></label>');
    $label.attr('for', 'id_'+newChoiceName);
    $label.text('選項' + (choiceCount+1));
    $input = $('<input type="text" required class="form-control"></input>');
    $input.attr('id', 'id_'+newChoiceName);
    $input.attr('name', newChoiceName);
    $newElement = $('<div class="form-group" id="group_' + choiceName + '_' + (choiceCount+1)+'"></div>');
    $label.appendTo($newElement);
    $inputDivElement.append($input).appendTo($newElement);
    $buttonDivElement.append($buttonElement).appendTo($newElement);
    $formGroup.after($newElement);
}

function addQuestion(buttonElement){
    let $buttonElement = $(buttonElement);
    let buttonValue = $buttonElement.val();
    let questionIndex = parseInt(buttonValue.substring(buttonValue.lastIndexOf('_')+1))+1;
    let questionName = buttonValue.substring(0,buttonValue.lastIndexOf('_'))+'_'+questionIndex;
    const questionElementHTML = '<div class="form-group" id="' + questionName + '">\
                            <div class="col-sm-offset-2 col-sm-10">\
                            <div class="panel panel-default">\
                            <div class="panel-heading">問題' + questionIndex + '</div>\
                            <div class="panel-body">\
                                <div class="form-group">\
                                    <label for="id_' + questionName + '_text" class="control-label col-sm-2">問題內容</label>\
                                    <div class="col-sm-8">\
                                        <input type="text" required name="' + questionName + '_text" id="id_' + questionName + '_text" class="form-control">\
                                    </div>\
                                    <div class="checkbox col-sm-2">\
                                        <label for="id_' + questionName + '_allowed_mutiple_answers"><input type="checkbox" name="' + questionName + '_allowed_mutiple_answers" id="id_' + questionName + '_allowed_mutiple_answers">是否允許多選</label>\
                                    </div>\
                                </div>\
                                <div class="form-group" id="group_' + questionName + '_choice_text_1">\
                                    <label for="id_' + questionName + '_choice_text_1" class="control-label col-sm-2">選項1</label>\
                                    <div class="col-sm-10">\
                                        <input type="text" required name="' + questionName + '_choice_text_1" id="id_' + questionName + '_choice_text_1" class="form-control">\
                                    </div>\
                                    <div class="col-sm-offset-2 col-sm-10">\
                                        <button type="button" onclick="addChoice(this)" value="' + questionName + '_choice_text_1"  class="btn btn-success">新增選項</button>\
                                    </div>\
                                </div>\
                            </div>\
                        </div>\
                    </div>\
                </div>';
    $buttonElement.parent().parent().before($(questionElementHTML));
    $buttonElement.val(questionName);
}