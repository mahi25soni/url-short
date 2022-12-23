let some = document.getElementById('user-name')
if(some.innerHTML == 'AnonymousUser'){
    some.innerHTML = 'Login'
}
else{
    some.pathname = '/logout/'
}

function copyit() {
    
    var copyText = document.getElementById("mymessage")
    copyText.innerHTML
    navigator.clipboard.writeText(copyText.innerHTML);
    setTimeout(() => {
        document.location.reload();
      }, 000);
}