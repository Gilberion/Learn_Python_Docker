import docker

client = docker.from_env()

cont_id = 'b2231e914a7ea8207e95bf7ff573e053f8c8a4b09b82a084ebc787a2534dcd20'
print(cont_id)

def start_cont(cont_id):
    container = client.containers.get(cont_id)
    container.start()

start_cont(cont_id)

