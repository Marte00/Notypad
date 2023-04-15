function auto_height(elem) {  /* javascript */
    elem.style.height = "1px";
    elem.style.height = (elem.scrollHeight)+"px";
}

let optionsButtons = document.querySelectorAll(".option-button");
let advanceOptionButton = document.querySelectorAll(".adv-option-button");
let fontName = document.getElementById("fontName");
let fontSizeRef = document.getElementById("fontSize");
let writingArea = document.getElementById("text-input");
let linkButton = document.getElementById("createLink");
let alignButtons = document.querySelectorAll(".align");
let spacingButtons = document.querySelectorAll(".spacing");
let formatButtons = document.querySelectorAll(".format");
let scriptButtons = document.querySelectorAll(".script");

// liste de font
let fontList = ["Montserrat", "Arial","Verdana","Times New Roman","Garamond","Georgia","Courier New","cursive"]

// initialise les paramètres
const initilizer = () => {
    highlighter(alignButtons,true);
    highlighter(spacingButtons,true);
    highlighter(formatButtons,false);
    highlighter(scriptButtons,true);

    fontList.map((value) => {
        let option = document.createElement("option");
        option.value = value;
        option.innerHTML = value;
        fontName.appendChild(option);
    });
    
    for(let i =1 ; i <= 7 ; i++){
        let option = document.createElement("option");
        option.value = i;
        option.innerHTML = i;
        fontSizeRef.appendChild(option);
    }

    // valeur par defaut
    fontSizeRef.value = 3;
};

const modifyText = (command,defaultUi, value) =>{
    document.execCommand(command,defaultUi,value);
};

// italic et gras
optionsButtons.forEach((button) => {
    button.addEventListener("click", () => {
        modifyText(button.id,false,null);
    });
});

// couleur et fonts
advanceOptionButton.forEach((button) => {
    button.addEventListener("change", () => {
        modifyText(button.id, false , button.value);
    });
});

// liens
linkButton.addEventListener("click", () =>{
    let userLink = prompt("Entrer un lien");
    if(/http/i.test(userLink)){
        modifyText(linkButton.id,false,userLink);
    }
    else{
        userLink = "http://" + userLink;
        modifyText(linkButton.id,false,userLink);
    }
});



const highlighter = (className,needRemoval) =>{
    className.forEach( (button) => {
        button.addEventListener("click",() => {
            if(needRemoval){
                let alreadyActive = false;
                
                if(button.classList.contains("active")){
                    alreadyActive = true;
                }

                highlighterRemover(className);
                if(!alreadyActive){
                    button.classList.add("active");
                }
            }
            else{
                button.classList.toggle("active");
            }
        });
    });
}

const highlighterRemover = (className) => {
    className.forEach( (button) => {
        button.classList.remove("active");
    });
};

const editableDiv = document.getElementById('text-input');
const hiddenInput = document.getElementById('content-input');
const noteForm = document.getElementById('note-form');
hiddenInput.value = editableDiv.innerHTML;

editableDiv.addEventListener('input', (event) => {
    let content = event.target.innerHTML;
    hiddenInput.value = content;
    event.target.scrollTop = event.target.scrollHeight;
});

window.onload = initilizer();


