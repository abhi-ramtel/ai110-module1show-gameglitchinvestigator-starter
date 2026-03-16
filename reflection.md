# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

When I first ran the app, it looked functional, but the game behavior was inconsistent and unfair. I confirmed that Easy mode could still reveal secrets above 20 after resets, because the New Game logic regenerated the secret in 1 to 100 instead of using the selected difficulty range. I also saw attempt counting issues because attempts started at 1 and were incremented before input validation, so the attempts-left display felt off. Another major bug was that guess hints were logically reversed, and an alternating type conversion on the secret could cause misleading comparisons.
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I used GitHub Copilot (GPT-5.3-Codex) as a debugging teammate to inspect game state flow, identify risky logic, and propose testable refactors. One correct suggestion was to move reusable logic into `logic_utils.py` and have `app.py` import those helpers, which reduced duplicated logic and made unit testing direct; I verified this by running pytest and seeing all logic tests pass. Another correct suggestion was to reset full session state on New Game (secret, attempts, score, status, history, input) and also reset on difficulty change, which directly fixed the Easy-mode range bug. One initially misleading AI-style pattern in the original code was coercing the secret to string every other attempt; I rejected that approach because it introduced type-based comparison bugs and removed it, then verified normal integer comparisons with tests and manual reasoning.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I treated a bug as fixed only if the behavior was corrected in code and covered by an automated test. I ran pytest after refactoring and confirmed `9 passed`, including tests for difficulty ranges, hint direction, parsing behavior, and score updates. For example, the test asserting Easy is `(1, 20)` and Hard has a larger max than Normal verified that the difficulty design now matches expectations. AI helped by proposing targeted edge-case tests (blank input, float-like input, win-score floor) and I kept only the cases that clearly mapped to observed bugs or game rules.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

The secret number felt unstable because key values were being reinitialized in ways that did not consistently respect the selected difficulty or a complete reset flow. In Streamlit, almost the whole script reruns on each interaction, so local variables are recalculated unless you store durable values in `st.session_state`. I would explain reruns as "the script restarts on every click, but session state is your memory between runs." The fix that stabilized game behavior was centralizing reset logic in one function and always creating the secret with the current difficulty range, plus resetting when the user changes difficulty.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

One habit I want to reuse is turning every discovered bug into a focused pytest case before moving on, so fixes are locked in and regressions are obvious. Next time, I would ask AI for smaller, verifiable patches earlier instead of trusting broad generated logic, especially around stateful UI code. This project changed my view of AI-generated code from "fast solution" to "first draft that must be validated." AI was most useful when I used it to generate hypotheses and tests, then applied human judgment to accept, modify, or reject each change.
