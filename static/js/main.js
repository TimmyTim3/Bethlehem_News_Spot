const menuButton=document.getElementById("menu-toggle");

const nav=document.getElementById("main-nav");

if(menuButton){

menuButton.addEventListener("click",()=>{

nav.classList.toggle("show");

});

}

function copyArticleLink() {

    navigator.clipboard.writeText(window.location.href);

    alert("Article link copied!");

}
