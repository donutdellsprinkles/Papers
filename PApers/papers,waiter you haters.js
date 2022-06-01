var button = document.querySelector('button');
button.onclick = ()=> {var quotes = new Array();
    quotes[0] = "Action is the real measure of intelligence.";
    quotes[1] = "Baseball has the great advantage over cricket of being sooner ended.";
    quotes[2] = "Every goal, every action, every thought, every feeling one experiences, whether it be consciously or unconsciously known, is an attempt to increase one's level of peace of mind.";
    quotes[3] = "A good head and a good heart are always a formidable combination.";
    quotes[4] = "Having a fatty does not mean you baddie.";
    quotes[5] = "are you happy for me?";
    quotes[6] = "really are you happy for me?";
    var rand = Math.floor(Math.random()*quotes.length);
document.getElementById('quotedisplay').innerHTML = quotes[rand];
}
    writeRandomQuote();