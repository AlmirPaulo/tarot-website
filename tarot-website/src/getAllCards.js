window.addEventListener('load', () =>{
    const req = new XMLHttpRequest();
    req.open('GET', 'https://tarotapi.almirpaulo.repl.co/'
, false)
    req.send()
    const res = JSON.parse(req.response)
    console.log(res)
    //get images and place in page

});
