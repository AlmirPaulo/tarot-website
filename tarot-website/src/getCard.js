window.addEventListener('load', () =>{
    //make request to get API data
    const req = new XMLHttpRequest();
    req.open('GET', 'https://tarotapi.almirpaulo.repl.co/'
, false)
    req.send()
    const res = JSON.parse(req.response)
    console.log(res)

    //get a random number to get a random card
   const pick = parseInt(Math.random() * 21)
    
//DOM elements variables
    const cardImg = document.getElementById('card-img');
    const cardTitle = document.getElementById('title');
    const questions = document.getElementById('questions');

    //Set new values
    cardTitle.innerText = res.cards[pick].title

    const card = document.createElement('IMG');
    const cardSrc = card.src
    cardSrc = res.cards[pick].picture
    const cardAlt = card.getAttribute('alt');
    cardAlt = 'card'
    card.id = 'card'


    

});
