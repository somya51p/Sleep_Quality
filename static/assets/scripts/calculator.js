const calculator = document.querySelector('#calculator');
const questionFile = '../data/calculator-questions.json';
const answerFile = '../data/calculator-answers.json';
var questions;
var answers;

console.log("Hello World");
// Initiate score and question tracking
let sleepScore = 0;
let questionNumber = 0;
let prevQuestionScores = [];

// Create the basic calculator structure with a header, question, form, and buttons
let sectionStructure = document.createDocumentFragment();

let header = document.createElement('h3');
sectionStructure.appendChild(header);

let firstPara = document.createElement('p');
sectionStructure.appendChild(firstPara);

let secondPara = document.createElement('p');
secondPara.classList.add('calculator-spacing');
secondPara.textContent = `Not sure if you answered correctly? Reset the calculator and try again!`;
secondPara.style.display = 'none';

sectionStructure.appendChild(secondPara);

const form = document.createElement('form');
sectionStructure.appendChild(form);

const buttonContainer = document.createElement('div');
buttonContainer.id = 'button-container';

const backButton = document.createElement('button');
backButton.textContent = 'Back';
backButton.classList.add('calculator-button');

backButton.addEventListener('click', (event) => {
  event.preventDefault();
  updateSleepScore('return');
  changeQuestion(-1);
});

buttonContainer.appendChild(backButton);

const submit = document.createElement('input');
submit.setAttribute('type', 'submit');
submit.setAttribute('disabled', 'disabled');
submit.textContent = 'Submit';
submit.classList.add('calculator-button');

submit.addEventListener('click', (event) => {
  event.preventDefault();
  updateSleepScore('submit');
  if (questionNumber < questions.length) {
    changeQuestion(1);
    submit.setAttribute('disabled', 'disabled');
  } else {
    postScore();
  }
});

buttonContainer.appendChild(submit);

const reset = document.createElement('button');
reset.textContent = 'Reset';
reset.classList.add('calculator-button');
reset.style.display = 'none';

reset.addEventListener('click', (event) => {
  event.preventDefault();
  resetCalculator();
});

buttonContainer.appendChild(reset);

function changeQuestion(direction) {
  questionNumber += direction;
  statusMessage = `Question ${questionNumber} out of 8`;
  header.textContent = statusMessage;

  updateCalculator();
}

function updateSleepScore(action) {
  if (action === 'submit') {
    let value = parseInt(
      document.querySelector('input[name="answer-group"]:checked').value
    );
    sleepScore += value;
    prevQuestionScores.push(value);
  } else {
    sleepScore -= prevQuestionScores.pop();
  }
}

function postScore() {
  removeLastQuestion();

  let finalText = `Want to improve your score? Read on to learn practical tips for getting better sleep!`;

  // Hide all elements we'd want to reload on a reset
  submit.style.display = 'none';
  backButton.style.display = 'none';

  reset.style.display = 'inline-block';
  secondPara.style.display = 'inline-block';

  buttonContainer.style.justifyContent = 'center';

  let score = calculateScore();

  header.textContent = `Your sleep score is: ${score}`;
  firstPara.textContent = finalText;
}

function calculateScore() {
  let scorePercentage = (sleepScore / 32) * 100;
  if (scorePercentage % 1 < 0.5) {
    scorePercentage = Math.floor(scorePercentage);
  } else {
    scorePercentage = Math.ceil(scorePercentage);
  }
  return `${scorePercentage}%`;
}

function updateCalculator() {
  if (questionNumber == 2) {
    backButton.removeAttribute('disabled');
  } else if (questionNumber == 1) {
    backButton.setAttribute('disabled', 'disabled');
  }

  removeLastQuestion();
  let currentQuestion = questions[questionNumber - 1].question;
  firstPara.textContent = currentQuestion;

  let answerList = answers[questions[questionNumber - 1].answerType];
  setAnswers(answerList);

  let buttons = document.querySelector('#button-container');
  if (buttons != null) {
    form.appendChild(buttons);
  }
}

function removeLastQuestion() {
  let answerDivs = document.querySelectorAll('.answer-container');

  if (answerDivs != null) {
    let postedAnswers = document.querySelectorAll('.answer');
    postedAnswers.forEach((answer) => {
      answer.remove();
    });
    answerDivs.forEach((div) => div.remove());
  }
}

function setAnswers(answerList) {
  let answerValue = 4;
  answerList.forEach((answer) => {
    let radioContainer = document.createElement('div');
    radioContainer.classList.add('answer-container');

    let radioInput = document.createElement('input');
    radioInput.setAttribute('type', 'radio');
    radioInput.setAttribute('name', 'answer-group');
    radioInput.setAttribute('value', answerValue);
    radioInput.id = answer;
    radioInput.classList.add('answer');

    radioInput.addEventListener('input', () =>
      submit.removeAttribute('disabled')
    );

    radioContainer.appendChild(radioInput);

    let label = document.createElement('label');
    label.textContent = answer;
    label.htmlFor = answer;
    label.classList.add('answer');

    radioContainer.appendChild(label);
    form.appendChild(radioContainer);

    answerValue -= 1;
  });
}

function resetCalculator() {
  prevQuestionScores = [];
  questionNumber = 0;
  sleepScore = 0;

  submit.style.display = 'inline-block';
  backButton.style.display = 'inline-block';
  reset.style.display = 'none';
  secondPara.style.display = 'none';

  buttonContainer.style.justifyContent = 'space-between';

  changeQuestion(1);
}

async function buildCalculator() {
  questions = await fetchData(questionFile);
  answers = await fetchData(answerFile);

  changeQuestion(1);

  form.appendChild(buttonContainer);
  calculator.appendChild(sectionStructure);
}

async function fetchData(fileName) {
  console.log("response1");
  return fetch(fileName).then((response) => {
    console.log("response2");
    return response.json();
  });
}

