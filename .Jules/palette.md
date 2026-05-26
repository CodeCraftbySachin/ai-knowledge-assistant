## 2024-05-22 - [CLI Visual Polish & Feedback]
**Learning:** For terminal-based applications, visual hierarchy is often neglected. Using ANSI colors and ASCII dividers significantly improves readability. Additionally, providing immediate feedback like "Thinking..." during async operations (LLM calls) prevents the user from feeling like the app has frozen.
**Action:** Always include a visual status indicator for operations exceeding 500ms and use distinct colors for user vs system output.
