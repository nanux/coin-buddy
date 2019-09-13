$(document).ready(function () {
    $.getJSON("assets/cards/falling-sky.json", function (data) {
        renderPage(data);
    });
})

let supportedGames = [
    { file: 'falling-sky', name: 'Falling Sky' },
    { file: 'fire-in-the-lake', name: 'Fire in the Lake' },
    { file: 'gandhi', name: 'Gandhi' }
]

function renderPage(cards) {
    let app = new Vue({
        el: '#content',
        data: {
            game: 'Falling Sky',
            cardTitle: '',
            cardFlavor: '',
            cardText2: '',
            cardFlavor2: '',
            cardFactions: '',
            cardText: '',
            cardTip: '',
            cardBackground: '',
            cardNumber: '',
            secondVersion: false,
            cards: cards
        },
        methods: {
            updateCard: function (event) {
                event.preventDefault();

                const cardNumber = $("#cardNumberInput").val();
                if (cardNumber == "") {
                    return;
                }

                const results = app.cards.filter(card => card.number == cardNumber);

                let result;
                if (results.length > 0) {
                    result = results[0]
                    $("#result").show();
                } else {
                    return;
                }


                const factions = [{
                    faction: result.first_faction,
                    avatar: getAvatar(result.first_faction)
                }, {
                    faction: result.second_faction,
                    avatar: getAvatar(result.second_faction)
                }, {
                    faction: result.third_faction,
                    avatar: getAvatar(result.third_faction)
                }, {
                    faction: result.fourth_faction,
                    avatar: getAvatar(result.fourth_faction)
                }]

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
                let game = event.target.name;

                var sg = supportedGames.filter((g) => g.file === game);

                if (sg.length != 1) {
                    console.error("This is an unsupported game");
                    return;
                }
                $("#result").hide();
                $("#cardNumberInput").val("");
                this.game = sg[0].name;
                // TODO potentially insecure
                $.getJSON("assets/cards/" + game + ".json").then((response) => {
                    this.cards = response;
                });

            }
        }
    })
}

let getAvatar = function (faction) {
    let avatar = ""

    if (faction.startsWith("Ro")) {
        avatar = "romans"
    } else if (faction.startsWith("Ae")) {
        avatar = "aedui"
    } else if (faction.startsWith("Ar")) {
        avatar = "arverni"
    } else if (faction.startsWith("Be")) {
        avatar = "belgae"
    }


    return "assets/img/avatar_" + avatar + ".png"
}