from ollama import chat

def agent(system_prompt=None):
    messages = []

    if system_prompt:
        messages.append({'role': 'system', 'content': system_prompt})
        response = chat(model='gpt-oss:20b', messages = messages)
        assistant_response = response['message']['content']
        print(f'Assistant: {assistant_response}')
        messages.append({'role': 'assistant', 'content': assistant_response})

    while True:
        user_input = input("You (enter 'done' to end chat): ")
        messages.append({'role': 'user', 'content': user_input})

        response = chat(model='gpt-oss:20b', messages = messages)
        assistant_response = response['message']['content']
        print(f'Assistant: {assistant_response}')

        if user_input.lower() == 'done':
            return assistant_response

        messages.append({'role': 'assistant', 'content': assistant_response})
    
def main():
    with open('./prompts/direct_stage_0.txt', "r") as file:
        system_prompt_0 = file.read()

    agent(system_prompt_0)

if __name__ == '__main__':
    main()