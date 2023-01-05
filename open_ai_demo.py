import openai
import config
import key


def guess(prompt):
    return openai.Completion.create(
        prompt=prompt,
        max_tokens=config.max_tokens,
        model=config.model,
        temperature=config.temperature
    )["choices"][0]["text"].strip()


if __name__ == '__main__':
    openai.api_key = key.OPEN_AI_KEY
    print("Type in 'quit' to end :)")
    while True:
        query = input()
        if query == 'quit':
            break
        print(guess(query))
