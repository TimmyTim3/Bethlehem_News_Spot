const menuButton=document.getElementById("menu-toggle");

const nav=document.getElementById("main-nav");

if(menuButton){

menuButton.addEventListener("click",()=>{

nav.classList.toggle("show");

});

}
