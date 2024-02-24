let namsteBtn = document.querySelector('button');
namsteBtn.addEventListener('click',inputMsg);

function inputMsg(){
    let name = prompt('Enter Name of the Student');
    namsteBtn.textContent = 'now roll no. 1 is ' + name;

    //alert('Namaste World!'); // shows a pop-up alert from top 
}


function myFunction(){
    document.getElementById('dateTime').innerHTML = Date();
}

function paraFn(){
    document.getElementById('para').innerHTML = "Paragraph has been changed."
}