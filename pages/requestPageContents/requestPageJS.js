let isAuthenticated = {{ current_user.is_authenticated | lower }};

function openAnswerPopup() {
    if (!isAuthenticated) {
        window.location.href = '/loginPage.html';
        return;
    }
    document.getElementById('answer-popup').style.display = 'block';
}

function closeAnswerPopup() {
    document.getElementById('answer-popup').style.display = 'none';
}

function submitAnswer(questionId) {
    const answer = document.getElementById('answer-textarea').value;
    if (!answer) {
        alert("Answer cannot be empty!");
        return;
    }

    $.ajax({
        url: '/answer',
        method: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({
            question_id: questionId,
            answer: answer
        }),
        success: function(response) {
            const answerSection = document.getElementById('answers-container');
            const newAnswerDiv = document.createElement('div');
            newAnswerDiv.classList.add('answer');
            newAnswerDiv.innerHTML = `
                <div class="user-profile">
                    <img class="profile-img" src="${response.answer.user.profile_photo}" alt="Profile Picture">
                    <span class="user-name">${response.answer.user.username}</span>
                </div>
                <p>${response.answer.answer}</p>
            `;
            answerSection.prepend(newAnswerDiv);
            closeAnswerPopup();
        },
        error: function(error) {
            alert("Error submitting answer!");
            console.error(error);
        }
    });
}

function vote(type) {
    const voteCountElement = document.querySelector('.vote-count');
    if (type === 'up') {
        voteCount++;
    } else if (type === 'down') {
        voteCount--;
    }
    voteCountElement.textContent = voteCount;
}
