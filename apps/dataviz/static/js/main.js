$(document).ready(function(){

    var chart = AmCharts.makeChart(
        "chartdiv", {
            "type": "serial",
            "theme": "white",
            "fontFamily": "Helvetica Neue, Helvetica, Arial, sans-serif",
            "dataProvider": {
            },
            "valueAxes": [ {
                "gridColor": "#FFFFFF",
                "gridAlpha": 0.2,
                "dashLength": 0
            } ],
            "gridAboveGraphs": true,
            "startDuration": 1,
            "graphs": [ {
                "balloonText": "[[category]]: <b>[[value]]</b>",
                "fillAlphas": 1.0,
                "lineAlpha": 0.2,
                "type": "column",
                "valueField": "value"
            } ],
            "chartCursor": {
                "categoryBalloonEnabled": false,
                "cursorAlpha": 0,
                "zoomable": false
            },
            "categoryField": "name",
            "categoryAxis": {
                "gridPosition": "start",
                "gridAlpha": 0,
                "tickPosition": "start",
                "tickLength": 20,
                "labelRotation": 45
            },
            "export": {
                "enabled": false
            }
        }
    );

    function loadChart() {
        var form = $('form');
        data = form.serialize()

        $.ajax({
            url: '/api/v1/region/',
            method: 'POST',
            dataType: 'json',
            contentType: 'application/x-www-form-urlencoded',
            data: data,
            timeout: 1000,
            success: function(response){
                chart.dataProvider = response;
                chart.validateData();
                chart.animateAgain();
            },
            error: function(request, errorType, errorMessage){
                console.log(errorType, errorMessage)
            }
        });
    }

    loadChart()

    $('#region').on('change', function () {
        loadChart()
    });

});