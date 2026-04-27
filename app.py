from chains.chatbot_chain import get_chatbot, get_context
from memory.memory import clear_session_history

def get_role(role):
    if role == "teacher":
        return "You are a knowledgeable teacher who explains clearly with examples."
    elif role == "storyteller":
        return "You are a creative storyteller with engaging narration."
    elif role == "interviewer":
        return "You are an interviewer asking professional questions."
    else:
        return "You are a helpful AI assistant."

def main():
    chatbot = get_chatbot()
    session_id = "user_1"

    role_input = input("Select Role (teacher/storyteller/interviewer): ").strip().lower()
    print("\nCommands:")
    print(" - change role")
    print(" - reset")
    print(" - exit\n")

    while True:
        print(f"[Current Role: {role_input}]")
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Good Bye... 👋")
            break
        elif user_input.lower() == "change role":
            role_input = input("Select Role: ").strip().lower()
            clear_session_history(session_id)
            print("Role updated & history reset \n")
            continue
        elif user_input.lower() == "reset":
            clear_session_history(session_id)
            print("Memory Cleared")
            continue
        try:
            response = chatbot.invoke(
                {
                    "input": user_input,
                    "role": get_role(role_input),
                    "context": get_context(user_input)
                },
                config={"configurable": {"session_id": session_id}}
            )
            print("AI: ", response.content, "\n")
        except Exception as e:
            print("Error: ", e)

if __name__ == "__main__":
    main()