from openai import OpenAI
import time
# Assistant ID: asst_HfDyngILScONuxIKtehEhldW

client=OpenAI(api_key='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')

assistant = client.beta.assistants.create(
    name = "Test assistant",
    instructions = """ Provide a list of prime numbers until the indicated upper threshold""",
    tools = [{"type": "code_interpreter"}],
    model = "gpt-4"
)

# print(assistant)
# assistant = client.beta.assistants.create(
#     name = "Task scheduler",
#     instructions = """ Please respond with only the requested format, no introductory or explanatory text.

#     Each area  in the image is separated by D time units. A number i of robots start in the charging area (fully charged), 
#     and need to build a wall made out of N bricks in the build area. The bricks are in the storage area.  
#     The robots consume B percentage of battery per time unit. Negative values of battery are NOT accepted, 
#     the robots MUST go to the charging station whenever is needed to ensure that they won't run out of battery. 
#     The robots need to go back to the charging area once the job is finished. The robots are able to perform one action per time unit. 
#     Both robots are able to perform actions during the same time unit. The actions are: 

#         - Move (which requires to time units)
#         - Pick 1 unit of material
#         - Build 1 unit of material
#         - Charge (20% per time unit)
#         - Idle

#     The robots have the following characteristics:
#     - Cargo capacity of X material units
#     - Able to build Y material unit per time unit

#     Do not give any introduction to your logic, or write anything besides what's being asked. 
#     Provide a breakdown of all the actions to be taken per time unit with the specified format (per steps) in order to complete the task.  
#     Do not reply anything else, ONLY the code with the specified format. The different steps should be written down with the following format:

#     { STEP #, [CURRENT LOCATION_robot_1, CURRENT LOCATION_robot_i], [ACTION BEING PERFORMED_robot_1, ACTION BEING PERFORMED_robot_i], [INTERNAL CARGO_robot_1, INTERNAL CARGO_robot_i], PLACED BRICKS, [REMAINING BATTERY_robot_1, REMAINING BATTERY_robot_i]}

#     Where:

#     - Current location can be C, S, B or T (to indicate the robot is travelling)
#     - Action being performed can be MOVE_S, MOVE_B, MOVE_C, PICK, BUILD, IDLE
#     - Internal cargo can be an integer number
#     - Placed bricks can be an integer number,
#     - Remaining battery ranges from 0 to 100"
#     ) """,
#     tools = [{"type": "code_interpreter"}],
#     model = "gpt-4"
# )

thread = client.beta.threads.create()
# print(thread)

message = client.beta.threads.messages.create(
    thread_id = thread.id,
    role = "user",
    content = """The threshold is 100."""
)
# message = client.beta.threads.messages.create(
#     thread_id = thread.id,
#     role = "user",
#     content = """Provide a breakdown for an scenario with the following characteristics: only one robot, distance D between areas is 2 time units, 
#     the wall needs to be N=4 bricks,  the robot has a cargo of X=2 units, and the capacity to build Y=1 material per time unit. Do not take in consideration battery consumption."""
# )

# print(message)

run = client.beta.threads.runs.create(
    thread_id = thread.id,
    assistant_id= assistant.id
)
# print(run)

run = client.beta.threads.runs.retrieve(
    thread_id=thread.id,
    run_id = run.id
)

time.sleep(5)

messages = client.beta.threads.messages.list(
    thread_id = thread.id
)
print(messages)
time.sleep(5)

for message in reversed(messages.data):
    print(message.role + " (TEST): " + message.content[0].text.value)   
    