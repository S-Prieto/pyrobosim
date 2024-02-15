from openai import OpenAI
import time

# Initialize the OpenAI client with your API key
client = OpenAI(api_key='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')

# Create an assistant
assistant = client.beta.assistants.create(
    name="Test assistant",
    instructions="Provide a list of prime numbers until the indicated upper threshold",
    tools=[{"type": "code_interpreter"}],
    model="gpt-4"
)

# Create a thread
thread = client.beta.threads.create()

# Send a message to the thread
message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="The threshold is 100."
)

# Create a run with the assistant for the thread
run = client.beta.threads.runs.create(
    thread_id=thread.id,
    assistant_id=assistant.id
)

# Implementing a simple polling mechanism to wait for the assistant's response
timeout = 60  # Maximum time to wait in seconds
poll_interval = 3  # Interval to check for new messages in seconds
start_time = time.time()

while True:
    elapsed_time = time.time() - start_time
    if elapsed_time > timeout:
        print("Timeout waiting for assistant response.")
        break

    # Fetch messages from the thread
    messages = client.beta.threads.messages.list(
        thread_id=thread.id
    )

    # Assuming the first message is always the user's and any additional message is from the assistant
    if len(messages.data) > 1:
        # Assistant's response is available
        break

    time.sleep(poll_interval)

# Print all messages from the thread
for message in messages.data:
    # Check if 'content' list is not empty and then print the message
    if message.content and len(message.content) > 0:
        # Assuming 'text' is the correct way to access the message's text content
        # and it exists in every message's content you're interested in.
        print(f"{message.role} (TEST): {message.content[0].text.value}")
    else:
        print(f"{message.role} (TEST): No content available or content structure differs.")
