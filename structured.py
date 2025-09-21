from ollama import chat

def agent(system_prompt=None):
    messages = []

    if system_prompt:
        while True:
            try:
                messages.append({'role': 'system', 'content': system_prompt})
                response = chat(model='gpt-oss:20b', messages = messages)
                assistant_response = response['message']['content']
                print(f'Assistant: {assistant_response}')
                messages.append({'role': 'assistant', 'content': assistant_response})
                break
            except Exception as e:
                print(f"Error encountered: {e}")
                print("Retrying...")

    while True:
        user_input = input("You (enter 'done' to end chat): ")
        messages.append({'role': 'user', 'content': user_input})

        while True:
            try:
                response = chat(model='gpt-oss:20b', messages = messages)
                assistant_response = response['message']['content']
                if user_input.lower() == 'done':
                    return assistant_response 
                print(f'Assistant: {assistant_response}')
                messages.append({'role': 'assistant', 'content': assistant_response})
                break
            except Exception as e:
                print(f"Error encountered: {e}")
                print("Retrying...")


def main():
    print("----------Data Collection Stage----------")
    with open('./prompts/structured_stage_0.txt', "r") as file:
        system_prompt_0 = file.read()
    
    res_0 = agent(system_prompt_0)

    print("----------Recommendation Stage----------")
    with open('./prompts/structured_stage_1.txt', "r") as file:
        system_prompt_1 = file.read()

    system_prompt_1 = system_prompt_1.format(
        information=res_0
    )

    res_1 = agent(system_prompt_1)

    print("----------Explanation Stage----------")
    with open('./prompts/structured_stage_2.txt', "r") as file:
        system_prompt_2 = file.read()

    system_prompt_2 = system_prompt_2.format(
        information=res_0,
        recommendation=res_1
    )

    res_2 = agent(system_prompt_2)


if __name__ == '__main__':
    main()