# pylint: skip-file

# standard libraries
# append on demand

# third-party dependencies
import openai
from gpt4all import GPT4All

# local dependencies
# append on demand


class OpenAiChef:
    def __init__(self, api_key, system_role, limit=10):
        self.client = openai.OpenAI(api_key=api_key)
        self.system_role = system_role
        self.messages = [{"role": "system", "content": self.system_role}]
        self.recipes = 0
        self.limit = limit

    def reset_messages(self):
        self.messages = [{"role": "system", "content": self.system_role}]

    def generate_recipe(self, model, region, ingredients):
        if self.recipes % self.limit == 0:  # avoid exhaustion
            self.reset_messages()

        question = f"Generate a recipe for {region} cuisine using the following ingredients:\n{ingredients}"
        self.messages.append({"role": "user", "content": question})

        try:
            response = self.client.chat.completions.create(
                model=model,  # model id
                messages=self.messages,  # list of messages
            )
        except Exception as e:
            raise e

        answer = response.choices[0].message.content
        self.messages.append({"role": "assistant", "content": answer})
        self.recipes += 1

        return answer


class Gpt4AllChef:
    def __init__(self, model_name, model_path, system_role, device="cpu"):
        self.client = GPT4All(
            model_name=model_name,  # full model name with .gguf extension
            model_path=model_path,  # path to model directory
            device=device,  # device to run model on, only "cpu" is supported
            n_ctx=2048,  # context window size
            allow_download=False,  # disallow, must be pre-downloaded
        )
        self.system_role = system_role

    def generate_recipe(self, region, ingredients):
        question = f"Generate a recipe for {region} cuisine using the following ingredients:\n{ingredients}"
        prompt = f"{self.system_role}\n{question}"
        answer = self.client.generate(prompt)
        return answer
