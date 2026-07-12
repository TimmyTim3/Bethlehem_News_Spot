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


/* ==========================
   ARTICLE REACTIONS
========================== */

const reactionButtons = document.querySelectorAll(".reaction-btn");

reactionButtons.forEach(button => {

    button.addEventListener("click", () => {

        const reaction = button.dataset.reaction;

        const articleId = window.location.pathname.split("/").pop();

        fetch(`/article/${articleId}/react`, {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                reaction: reaction
            })

        })

        .then(response => response.json())

        .then(data => {

            if(data.success){

                document.getElementById("like-count").textContent = data.likes;

                document.getElementById("love-count").textContent = data.loves;

                document.getElementById("wow-count").textContent = data.wows;

            }

        });

    });

});
