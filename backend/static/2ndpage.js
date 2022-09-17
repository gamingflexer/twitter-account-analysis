const toxic = document.querySelector('.toxic-input');
const severe_toxic = document.querySelector('.severe-input');
const obscene = document.querySelector('.obscene-input');
const threat = document.querySelector('.threat-input');
const insult = document.querySelector('.insult-input');
const identity_hate = document.querySelector('.identity-input');


const ctx = document.getElementById('mychart').getContext('2d');
let myChart = new Chart(ctx, {
    type: "doughnut",
    data: {

        labels: ['toxic', 'severe_toxic', 'obscene', 'threat', 'insult', 'identity_hate'],
        datasets: [
            {
                label: '# of votes',
                data: [0, 0, 0, 0, 0, 0],
                backgroundColor: ['#2adece', '#dd3b79', 'red', 'black', 'yellow', 'green'],
                borderWidth: 1,
                cutout: "75%"
            }
        ]
    },
});

const updateChartValue = (input, dataOrder) => {
    input.addEventListener('change', e => {
        myChart.data.datasets[0].data[dataOrder] = e.target.value;
        myChart.update();
    });
};

updateChartValue(toxic, 0);
updateChartValue(severe_toxic, 1);
updateChartValue(obscene, 2);
updateChartValue(threat, 3);
updateChartValue(insult, 4);
updateChartValue(identity_hate, 5);