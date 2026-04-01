#!/usr/bin/env python3
"""OpenAI terminal chatbot demo."""

import os
import sys

try:
    import openai
except ImportError:
    print("Missing dependency: install via 'pip install openai'")
    sys.exit(1)

MODEL = "gpt-3.5-turbo"
EXIT_WORDS = {"exit", "quit", "bye"}


def init_openai_api() -> None:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise EnvironmentError(
            "OPENAI_API_KEY environment variable not set."
            " Set it with: export OPENAI_API_KEY='your_key'"
        )
    openai.api_key = api_key


def get_response(messages):
    response = openai.ChatCompletion.create(
        model=MODEL,
        messages=messages,
        temperature=0.7,
        max_tokens=500,
    )
    return response.choices[0].message.content.strip()


def run_chatbot() -> None:
    try:
        init_openai_api()
    except EnvironmentError as err:
        print(f"Error: {err}")
        sys.exit(1)

    print("===== OpenAI Terminal Chatbot =====")
    print("Type 'exit', 'quit', or 'bye' to end.")

    conversation = [
        {"role": "system", "content": "You are a helpful assistant."},
    ]

    while True:
        try:
            user_input = input("You: ")
        except (KeyboardInterrupt, EOFError):
            print("\nChatbot: Goodbye!")
            break

        if not user_input.strip():
            continue

        lower = user_input.strip().lower()
        if lower in EXIT_WORDS:
            print("Chatbot: Goodbye! Have a great day.")
            break

        conversation.append({"role": "user", "content": user_input})
        try:
            answer = get_response(conversation)
        except Exception as e:
            print(f"Chatbot: Error while contacting OpenAI: {e}")
            continue

        conversation.append({"role": "assistant", "content": answer})
        print(f"Chatbot: {answer}")


if __name__ == "__main__":
    run_chatbot()



# #!/usr/bin/env python3
# """Simple terminal chatbot demo (rule-based)."""

# import re

# RESPONSES = {
#     r"hi|hello|hey": "Hello! I am a sample chatbot. Ask me anything.",
#     r"how are you\??": "I am a bot, I always feel binary! 😄",
#     r"your name": "I am Chatbot v1.0 built by Python.",
#     r"what can you do": "I can answer simple questions and demonstrate an interactive terminal chat loop.",
#     r"time|date": "Sorry, I can't access real time, but you can use Python datetime in your own code.",
#     r"help": "Type a question, or type 'exit' or 'quit' to end the chat.",
#     r"thanks|thank you": "You're welcome!",
# }

# DEFAULT_RESPONSE = "I don't know that yet. Try asking something else, or type 'help'."


# def get_response(user_input: str) -> str:
#     text = user_input.strip().lower()
#     if not text:
#         return "Please ask something."

#     for pattern, response in RESPONSES.items():
#         if re.search(pattern, text):
#             return response

#     # simple keyword expansions
#     if "python" in text:
#         return "Python is a powerful programming language used for automation, web, data science, etc."

#     if "chatbot" in text:
#         return "I am a simple rule-based chatbot running in your terminal."

#     return DEFAULT_RESPONSE


# def run_chatbot() -> None:
#     print("===== Simple Terminal Chatbot =====")
#     print("Type 'exit', 'quit', or 'bye' to end the conversation.")
#     print("Type 'help' for basic guidance.")

#     while True:
#         try:
#             user_input = input("You: ")
#         except (KeyboardInterrupt, EOFError):
#             print("\nChatbot: Goodbye!")
#             break

#         if not user_input:
#             continue

#         lower = user_input.strip().lower()
#         if lower in {"exit", "quit", "bye"}:
#             print("Chatbot: Goodbye! Have a great day.")
#             break

#         answer = get_response(user_input)
#         print(f"Chatbot: {answer}")


# if __name__ == "__main__":
#     run_chatbot()
