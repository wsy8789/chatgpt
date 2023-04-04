import openai
import os

# 设置 OpenAI API 密钥
openai.api_key = os.environ.get("OPENAI_API_KEY")

# 发送消息给 ChatGPT，获取回复
def send_message_to_chatgpt(message):
    response = openai.Completion.create(
      engine="davinci",
      prompt=message,
      max_tokens=1024,
      n=1,
      stop=None,
      temperature=0.7,
    )

    message = response.choices[0].text.strip()
    return message

# 测试函数
if __name__ == "__main__":
    message = "你好，聊天机器人"
    reply = send_message_to_chatgpt(message)
    print(reply)
