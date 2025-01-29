import openai

openai.api_key = '###'
a=input('Enter the text: ')
a=f'{a} (Write down the emotions in this text in ration)'
response = openai.Completion.create(
  model="text-davinci-003",
  prompt=a,
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
print(response["choices"][0]["text"])
