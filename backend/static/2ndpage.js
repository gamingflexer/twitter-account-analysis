const bad = document.querySelector('.bad-input');
const good = document.querySelector('.good-input');
const toxic = document.querySelector('.toxic-input');

const ctx = document.getElementById('mychart').getContext('2d');
let myChart = new Chart(ctx, {
    type: 'doughnut',
    data: {

        labels: ['Bad', 'Good', 'Toxic'],
        datasets: [
            {
                label: '# of votes',
                data: [0, 0, 0],
                backgroundColor: ['#2adece', '#dd3b79', 'red'],
                borderWidth: 1
            }
        ]
    }
});

const updateChartValue = (input, dataOrder) => {
    input.addEventListener('change', e => {
        myChart.data.datasets[0].data[dataOrder] = e.target.value;
        myChart.update();
    });
};

updateChartValue(bad, 0);
updateChartValue(good, 1);
updateChartValue(toxic, 2);