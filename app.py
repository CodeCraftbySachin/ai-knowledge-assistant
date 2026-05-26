from chains.chatbot_chain import get_chatbot, get_context
from memory.memory import clear_session_history

# ANSI Color Codes
GREEN = "\033[92m"
BLUE = "\033[94m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
BOLD = "\033[1m"
RESET = "\033[0m"

def get_role_config(role):
    roles = {
        "teacher": {
            "prompt": "You are a knowledgeable teacher who explains clearly with examples.",
            "message": "Class is in session! 🎓 I'm here to help you learn."
        },
        "storyteller": {
            "prompt": "You are a creative storyteller with engaging narration.",
            "message": "Gather 'round! 📖 Let me weave a tale for you."
        },
        "interviewer": {
            "prompt": "You are an interviewer asking professional questions.",
            "message": "Welcome to the interview. 👔 Let's begin the evaluation."
        }
    }

    config = roles.get(role.lower())
    if config:
        return config["prompt"], f"{GREEN}{config['message']}{RESET}"
    else:
        return "You are a helpful AI assistant.", f"{YELLOW}Using default role: Helpful Assistant 🤖{RESET}"

def main():
    print(f"\n{BLUE}{BOLD}{'='*50}")
    print(f"{'🧠 AI KNOWLEDGE ASSISTANT':^50}")
    print(f"{'='*50}{RESET}\n")

    chatbot = get_chatbot()
    session_id = "user_1"

    print(f"{CYAN}Available Roles: teacher, storyteller, interviewer{RESET}")
    role_input = input(f"{BOLD}Select Role:{RESET} ").strip().lower()
    role_prompt, role_msg = get_role_config(role_input)
    print(f"\n{role_msg}")

    print(f"\n{YELLOW}Commands:{RESET}")
    print(f" {CYAN}•{RESET} change role")
    print(f" {CYAN}•{RESET} reset")
    print(f" {CYAN}•{RESET} exit\n")

    while True:
        print(f"{BLUE}──────────────────────────────────────────────────{RESET}")
        user_input = input(f"{BOLD}{GREEN}You:{RESET} ")

        if user_input.lower() == "exit":
            print(f"\n{BLUE}Good Bye... 👋{RESET}\n")
            break
        elif user_input.lower() == "change role":
            role_input = input(f"{BOLD}Select Role:{RESET} ").strip().lower()
            role_prompt, role_msg = get_role_config(role_input)
            clear_session_history(session_id)
            print(f"\n{role_msg}")
            print(f"{YELLOW}Role updated & history reset{RESET}\n")
            continue
        elif user_input.lower() == "reset":
            clear_session_history(session_id)
            print(f"{YELLOW}Memory Cleared{RESET}\n")
            continue

        if not user_input.strip():
            continue

        try:
            print(f"{CYAN}Thinking...{RESET}", end="\r")
            response = chatbot.invoke(
                {
                    "input": user_input,
                    "role": role_prompt,
                    "context": get_context(user_input)
                },
                config={"configurable": {"session_id": session_id}}
            )
            # Clear "Thinking..." line
            print(" " * 20, end="\r")
            print(f"{BOLD}{BLUE}AI:{RESET} {response.content}\n")
        except Exception as e:
            # Clear "Thinking..." line
            print(" " * 20, end="\r")
            print(f"{YELLOW}Error:{RESET} {e}")

if __name__ == "__main__":
    main()