let backgroundColor = [
    'rgba(255, 99, 132, 0.2)',
    'rgba(54, 162, 235, 0.2)',
    'rgba(255, 206, 86, 0.2)',
    'rgba(75, 192, 192, 0.2)',
    'rgba(153, 102, 255, 0.2)',
    'rgba(255, 159, 64, 0.2)'
];
let borderColor = [
    'rgba(255, 99, 132, 1)',
    'rgba(54, 162, 235, 1)',
    'rgba(255, 206, 86, 1)',
    'rgba(75, 192, 192, 1)',
    'rgba(153, 102, 255, 1)',
    'rgba(255, 159, 64, 1)'
];
let chartType = 'bar';
let questionnaireID = document.querySelector('div.questionnaire').id;
let canvasList = document.querySelectorAll('canvas.question');
for (let index=0; index<canvasList.length; index++) {
    let element = canvasList[index];
    let apiURL = window.location.origin + '/statistics/api/question/' + element.id.split('-')[1] + "/";
    //使用Ajax获取json数据
    let jsonData = $.ajax({
        url: apiURL,
        dataType: 'json',
    }).done(function (results) {
        // 将获取到的json数据分别存放到两个数组中
        let labels = [], data=[];
        let choice_set = results['choice_set'];
        for (let key in choice_set) {
            let choice = choice_set[key];
            labels.push(choice['choice_text']);
            data.push(choice['counts']);
        }
        var myChart = new Chart(element, {
            type: chartType,
            data: {
                labels: labels,
                datasets: [{
                    label: '# 選項票數',
                    data: data,
                    backgroundColor: backgroundColor,
                    borderColor: borderColor,
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    yAxes: [{
                        ticks: {
                            beginAtZero: true
                        }
                    }]
                }
            }
        });
    });
}

//取依性別區分統計
$.ajax({
    url: window.location.origin+'/statistics/api/questionnaire/'+questionnaireID+'/get-gender-count/',
    dataType: 'json'
}).done(function (results) {
    let canvas = document.querySelector('.questionnaire-gender');
    let labels = [], data = [];
    for (let i=0; i<results.length; i++) {
        labels.push(results[i]['gender']);
        data.push(results[i]['total']);
    }
    let myChart = new Chart(canvas, {
        type: chartType,
        data: {
            labels: labels,
            datasets: [{
                label: '# 人數',
                data: data,
                backgroundColor: backgroundColor,
                borderColor: borderColor,
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            }
        }
    });
});
//取依學歷區分統計
$.ajax({
    url: window.location.origin+'/statistics/api/questionnaire/'+questionnaireID+'/get-education-count/',
    dataType: 'json'
}).done(function (results) {
    let canvas = document.querySelector('.questionnaire-education');
    let labels = [], data = [];
    for (let i=0; i<results.length; i++) {
        labels.push(results[i]['education']);
        data.push(results[i]['total']);
    }
    let myChart = new Chart(canvas, {
        type: chartType,
        data: {
            labels: labels,
            datasets: [{
                label: '# 人數',
                data: data,
                backgroundColor: backgroundColor,
                borderColor: borderColor,
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            }
        }
    });
});
//取依年收入區分統計
$.ajax({
    url: window.location.origin+'/statistics/api/questionnaire/'+questionnaireID+'/get-annual-income-count/',
    dataType: 'json'
}).done(function (results) {
    let canvas = document.querySelector('.questionnaire-annual-income');
    let labels = [], data = [];
    for (let i=0; i<results.length; i++) {
        labels.push(results[i]['annual_income']);
        data.push(results[i]['total']);
    }
    let myChart = new Chart(canvas, {
        type: chartType,
        data: {
            labels: labels,
            datasets: [{
                label: '# 人數',
                data: data,
                backgroundColor: backgroundColor,
                borderColor: borderColor,
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            }
        }
    });
});