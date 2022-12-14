const toxic = document.querySelector('.toxic-input');
const severe_toxic = document.querySelector('.severe-input');
const obscene = document.querySelector('.obscene-input');
const threat = document.querySelector('.threat-input');
const insult = document.querySelector('.insult-input');
const identity_hate = document.querySelector('.identity-input');

const ctx = document.getElementById('mychart').getContext('2d');
let myChart = new Chart(ctx, {
    type: "doughnut",
    indexLabelPlacement: "outside",
    radius: "90%",
    innerRadius: "75%",
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