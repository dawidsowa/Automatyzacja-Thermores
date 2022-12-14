var scripts = document.getElementsByTagName('script');
currentScript = scripts[scripts.length - 1];
m = currentScript.parentElement.parentElement.parentElement;
$(m).replaceWith("<h3>"+ $(m).children('button')[0].innerText +"</h3>");