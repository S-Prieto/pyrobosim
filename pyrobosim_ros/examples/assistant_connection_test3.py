from openai import OpenAI
import time

# Initialize the OpenAI client with your API key
client = OpenAI(api_key='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')

# Use the existing assistant's ID
assistant_id_ = 'asst_qh4jdWvZ8prgFDy7iL0PHc89'

# Create a thread
thread = client.beta.threads.create()

# Send a message to the thread
message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="Provide a breakdown for an scenario with the following characteristics: only one robot, distance D between areas is 2 time units, the wall needs to be N=4 bricks, the robot has a cargo of X=2 units, and the capacity to build Y=1 material per time unit. Do not take in consideration battery consumption."
)

# Create a run with the existing assistant for the thread
run = client.beta.threads.runs.create(
    thread_id=thread.id,
    assistant_id=assistant_id_  # Use the existing assistant ID here
)
# print(run)

# Implementing a simple polling mechanism to wait for the assistant's response
timeout = 180  # Maximum time to wait in seconds
poll_interval = 5  # Interval to check for new messages in seconds
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
    # if len(messages.data) > 1:
    #     # Assistant's response is available
    #     break

    # Print all messages from the thread
    for message in messages.data:
        # Check if 'content' list is not empty and then print the message
        print("(DEBUG) Size of messages.data: ", len(messages.data))
        if message.content and len(message.content) > 0:
            # Assuming 'text' is the correct way to access the message's text content
            # and it exists in every message's content you're interested in.
            print(f"{message.role} (TEST): {message.content[0].text.value}")
        else:
            print(f"{message.role} (TEST): No content available or content structure differs.")
    
    time.sleep(poll_interval)
