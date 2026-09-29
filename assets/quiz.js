/**
 * Quiz Widget — reusable across all lessons
 * 
 * Usage in HTML:
 *   <div class="quiz" data-quiz="q1">
 *     <h3>Pergunta aqui?</h3>
 *     <ul class="quiz-options">
 *       <li data-correct>Resposta correta</li>
 *       <li>Distrator 1</li>
 *       <li>Distrator 2</li>
 *       <li>Distrator 3</li>
 *     </ul>
 *     <div class="quiz-feedback correct">✅ Explicação do acerto</div>
 *     <div class="quiz-feedback wrong">❌ Explicação do erro</div>
 *   </div>
 */

document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('.quiz').forEach(quiz => {
    const options = quiz.querySelectorAll('.quiz-options li');
    const feedbackCorrect = quiz.querySelector('.quiz-feedback.correct');
    const feedbackWrong = quiz.querySelector('.quiz-feedback.wrong');
    let answered = false;

    // Shuffle options for retrieval practice (no formatting clues)
    const optionsList = quiz.querySelector('.quiz-options');
    const items = Array.from(options);
    for (let i = items.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      optionsList.appendChild(items[j]);
    }

    options.forEach(option => {
      option.addEventListener('click', () => {
        if (answered) return;
        answered = true;

        const isCorrect = option.hasAttribute('data-correct');

        if (isCorrect) {
          option.classList.add('correct');
          if (feedbackCorrect) {
            feedbackCorrect.classList.add('show');
          }
        } else {
          option.classList.add('wrong');
          // Highlight the correct one
          options.forEach(o => {
            if (o.hasAttribute('data-correct')) o.classList.add('correct');
          });
          if (feedbackWrong) {
            feedbackWrong.classList.add('show');
          }
        }

        // Disable all options
        options.forEach(o => { o.style.pointerEvents = 'none'; });
      });
    });
  });
});
