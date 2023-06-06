google.charts.load('current', { 'packages': ['corechart'] });

$(function(){
    google.charts.setOnLoadCallback(graficar);
    $.ajaxSetup({
        headers:{
            'X-CSRFToken':getCookie('csrftoken')
        }
    })
})

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function graficar() {

    $.ajax({
        url: '/graficaGoogle1/',
        dataType: 'json',
        type: 'post',
        cahce: false,
        async: false,
        success: function(resultado){
            console.log(resultado);
            var data = google.visualization.arrayToDataTable(resultado.datos);
            var options = {
                    title: 'Ventas por Producto',
                    legend: 'none'
                };

            var grafica = document.getElementById('grafica');
            
            var chart = new google.visualization.AreaChart(grafica);
            
            chart.draw(data, options);
        }
    })

    // var data = google.visualization.arrayToDataTable([
    //     ['Task', 'Hours per Day'],
    //     ['Estudiar', 11],
    //     ['Comer', 2],
    //     ['Entrenar', 2],
    //     ['Ver TV', 2],
    //     ['Dormir', 7],
    //     ['Leer', 2],
    // ]);

    // var options = {
    //     title: 'Mis Actividades Diarias',
    //     pieHole: 0.4,
    // };

    // var chart = new google.visualization.BarChart(grafica);

    // chart.draw(data, options);
}