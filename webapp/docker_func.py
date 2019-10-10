import docker

client = docker.from_env()

inf_b_treat = client.containers.list(all)
for inf_w_treat in inf_b_treat:
    int_temp=inf_b_treat['Container']
    print(client.containers.get(int_temp).attrs['Name'])