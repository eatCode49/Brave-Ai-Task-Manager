from openai import OpenAI

# Calling the api key
with open("Api_calls/apiKey.txt") as Key:
    content = Key.read()
    client = OpenAI(api_key=content, base_url="https://openrouter.ai/api/v1")

# Getting the task from the json task
with open ("Api_calls/task.txt") as jsread:
    contents = jsread.read()

def apiCalls(user_input):
    # Give this comments
    while True:
        try:
            response = client.chat.completions.create(
                model = "deepseek/deepseek-r1-0528:free",
                messages=[
                {"role": "system", "content":f"""You are Brave, my smart ai task assistant. Your job is to give me tasks every day and help me if I get stuck. You must remember all the tasks I give you and manage them wisely.
                                Always do the following:
                                - Assign daily tasks and suggest improvements when needed.
                                - If I fail to do a task, update the deadline smartly and guide me.
                                - Set automatic deadlines and remind me 24 hours before, 1 hour before, and after the deadline if it's overdue.
                                - Only give code if I ask for it. Otherwise, just guide me on how to do the task.
                                - Always be flexible with my schedule.
                                - Keep your replies short and helpful — don't talk too much.

                                Always respond in this format:
                                **Task | Deadline | Priority | Status | Next Step**

                                Here are the tasks from my task file:
                                {contents}"""},
                {"role":"user","content": user_input},
            ])
            if response and response.choices and len(response.choices) > 0:
                return response.choices[0].message.content
            else:
                return "Api call succed but no response returned"
        except Exception as e:
            return "Error Ocured during api call"

