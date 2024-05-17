
// Code for asking a question
var down = document.getElementById("ask_DOWN");
function ask() {

    // Create a form dynamically
    var form = document.createElement("form");
    form.setAttribute("method", "post");
    form.setAttribute("action", "submit_question.php"); // Change the action to your PHP script handling question submission

    // Create an input element for the question
    var questionInput = document.createElement("input");
    questionInput.setAttribute("type", "text");
    questionInput.setAttribute("name", "question");
    questionInput.setAttribute("placeholder", "Type your question here...");
    questionInput.style.width = "400px";
    questionInput.style.height = "200px";

    // Create a submit button
    var submitButton = document.createElement("input");
    submitButton.setAttribute("type", "submit");
    submitButton.setAttribute("value", "Submit");

    // Append the question input to the form
    form.appendChild(questionInput);

    // Append the submit button to the form
    form.appendChild(submitButton);

    // Append the form to the body
    document.body.appendChild(form);
}


// Code for reply button
var down = document.getElementById("reply_DOWN");
function reply() {
   
    // Create a form dynamically
    var form = document.createElement("form");
    form.setAttribute("method", "post");
    form.setAttribute("action", "submit.php");

    // Create an input element for replyID
    var ID = document.createElement("input");
    ID.setAttribute("type", "text");
    ID.setAttribute("name", "replyID");
    ID.setAttribute("placeholder", "Type answer here...");
    ID.style.width = "400px";
    ID.style.height = "200px";

    // Create a submit button
    var s = document.createElement("input");
    s.setAttribute("type", "submit");
    s.setAttribute("value", "Submit");

    // Append the reply_ID input to the form
    form.append(ID); 
   
    // Append the button to the form
    form.append(s); 

    document.getElementsByTagName("body")[0]
   .appendChild(form);
}


