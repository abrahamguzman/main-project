from config.openai import client

def crear_run(thread_id, assistant_id, instructions=None):
    run = client.beta.threads.runs.create_and_poll(
        thread_id=thread_id,
        assistant_id=assistant_id,
        instructions=instructions
    )
    
    return run.status == 'completed'