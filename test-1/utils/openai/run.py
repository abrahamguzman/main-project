from config.openai import client_ai

def crear_run(thread_id, assistant_id, instructions=None):
    run = client_ai.beta.threads.runs.create_and_poll(
        thread_id=thread_id,
        assistant_id=assistant_id,
        instructions=instructions
    )
    
    return run.status == 'completed'