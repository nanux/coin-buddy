$(document).ready(function () {
    var game = "falling_sky";
    if (game === "falling_sky") {
        $.getScript("./assets/cards/falling-sky.js", renderPage);
    } else {
        $.getScript("./assets/cards/gandhi.js", renderPage);
    }
})

function renderPage() {
    let app = new Vue({
        el: '#content',
        data: {
            cardTitle: '',
            cardFlavor: '',
            cardText2: '',
            cardFlavor2: '',
            cardFactions: '',
            cardText: '',
            cardTip: '',
            cardBackground: '',
            cardNumber: '',
            secondVersion: false
        },
        methods: {
            updateCard: function (event) {
                event.preventDefault();

                const cardNumber = $("#cardNumberInput").val();
                if (cardNumber == "") {
                    return;
                }

                const results = cards.filter(card => card.number == cardNumber);

                let result;
                if (results.length > 0) {
                    result = results[0]
                    $("#result").show();
                } else {
                    return;
                }

                const factions = result.first_faction + " | " + result.second_faction + " | " + result.third_faction + " | " + result.fourth_faction;
                app.cardTitle = result.title;
                app.cardFactions = factions;
                app.cardText = result.text;
                app.cardTip = result.tips;
                app.cardBackground = result.background;
                app.cardFlavor = result.flavor;
                app.cardNumber = cardNumber;

                if (result.text_2 != undefined) {
                    app.secondVersion = true;
                    app.cardText2 = result.text_2;
                    app.cardFlavor2 = result.flavor_2;
                } else {
                    app.secondVersion = false;
                    app.cardText2 = '';
                    app.cardFlavor2 = '';
                }
            },
            changeGame: function (event) {
                var game = event.target.name;
                console.log(game);
            }
        }
    })
}