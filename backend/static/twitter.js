const toxic = document.querySelector('.toxic-input');
const severe_toxic = document.querySelector('.severe-input');
const obscene = document.querySelector('.obscene-input');
const threat = document.querySelector('.threat-input');
const insult = document.querySelector('.insult-input');
const identity_hate = document.querySelector('.identity-input');

const data1 = { 'labels': ['toxic', 'severe_toxic', 'obscene', 'threat', 'insult', 'identity_hate'], 'data': [3.3537470735609523, 0.22055037552490703, 0.934887211769819, 0.457239768002181, 0.417689303867518, 0.17944169230759102] }

const ctx = document.getElementById('mychart').getContext('2d');
let myChart = new Chart(ctx, {
    type: "doughnut",
    data: {

        labels: data1.labels,
        datasets: [
            {
                label: '# of votes',
                data: data1.data,
                backgroundColor: ['#2adece', '#dd3b79', 'red', 'black', 'yellow', 'green'],
                borderWidth: 1,
                cutout: "90%"
            }
        ]
    },
});



/* const updateChartValue = (input, dataOrder) => {
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
updateChartValue(identity_hate, 5); */