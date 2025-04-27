// Get DOM elements
const triesLeftElement = document.getElementById('tries-left');
const feedbackMessageElement = document.getElementById('feedback-message');
const guessSlider = document.getElementById('guessSlider');
const currentGuessValueElement = document.getElementById('current-guess-value');
const submitGuessBtn = document.getElementById('submit-guess-btn');
const restartGameBtn = document.getElementById('restart-game-btn');

// Game state variables
let targetNumber;
let triesLeft;
let gameOver; // Flag to prevent multiple guesses after game ends

// --- Game Functions ---

// Function to start or reset the game
function initGame() {
    // 1. Generate a new random number between 0 and 10
    targetNumber = Math.floor(Math.random() * 11); // 0 to 10 inclusive
    triesLeft = 3;
    gameOver = false;

    // For debugging: console.log("Target Number:", targetNumber);

    // 2. Update the UI
    triesLeftElement.textContent = `Tries Left: ${triesLeft}`;
    feedbackMessageElement.textContent = '';
    feedbackMessageElement.className = ''; // Remove win/lose classes
    guessSlider.value = 5; // Reset slider position
    currentGuessValueElement.textContent = 5; // Reset displayed value
    submitGuessBtn.disabled = false; // Enable the submit button
}

// Function to handle a user's guess
function checkGuess() {
    if (gameOver) {
        return; // Do nothing if game is already over
    }

    const userGuess = parseInt(guessSlider.value); // Get slider value as a number
    triesLeft--; // Decrement tries

    // Update tries display
    triesLeftElement.textContent = `Tries Left: ${triesLeft}`;

    // Check the guess
    if (userGuess === targetNumber) {
        // Win condition
        feedbackMessageElement.textContent = `Congratulations! You guessed the number (${targetNumber})!`;
        feedbackMessageElement.className = 'win'; // Add win class for styling
        gameOver = true;
        submitGuessBtn.disabled = true; // Disable submit button after win
    } else if (triesLeft === 0) {
        // Lose condition after the last incorrect guess
        feedbackMessageElement.textContent = `Sorry, you ran out of tries! The number was ${targetNumber}.`;
        feedbackMessageElement.className = 'lose'; // Add lose class for styling
        gameOver = true;
        submitGuessBtn.disabled = true; // Disable submit button after loss

        // Automatically reset after a short delay so user can see the message
        setTimeout(initGame, 3000); // Reset after 3 seconds
    } else if (userGuess < targetNumber) {
        // Hint: Lesser
        feedbackMessageElement.textContent = 'The number is higher than your guess.';
        feedbackMessageElement.className = ''; // Reset class
    } else { // userGuess > targetNumber
        // Hint: Higher
        feedbackMessageElement.textContent = 'The number is lower than your guess.';
        feedbackMessageElement.className = ''; // Reset class
    }
}

// --- Event Listeners ---

// Update the displayed value as the slider moves
guessSlider.addEventListener('input', () => {
    currentGuessValueElement.textContent = guessSlider.value;
});

// Handle the submit button click
submitGuessBtn.addEventListener('click', checkGuess);

// Handle the restart button click
restartGameBtn.addEventListener('click', initGame);

// --- Initial Setup ---
// Start the game when the page loads
initGame();