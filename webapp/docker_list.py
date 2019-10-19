import docker

client = docker.from_env()

def get_list():
    inf_b_treat = client.containers.list(all)
    docker_list = []

    for inf_w_treat in inf_b_treat:
        transf = str(inf_w_treat).replace('<Container: ', '')
        cont_id = (transf.replace('>', ''))
        c_id = client.containers.get(cont_id).attrs['Id']
        c_name = client.containers.get(cont_id).attrs['Name']
        c_status = (client.containers.get(cont_id).status)
        c_image = client.containers.get(cont_id).attrs['Config']['Image']
        c_labels = client.containers.get(cont_id).attrs['Config']['Labels']
        c_volumes = client.containers.get(cont_id).attrs['Config']['Volumes']
        try:
            c_ports = client.containers.get(cont_id).attrs['Config']['ExposedPorts']
        except:
            c_ports = 'Порт не определен'

        docker_dict = {
            'id': c_id,
            'name': c_name,
            'status': c_status,
            'image': c_image,
            'labels': c_labels,
            'volumes': c_volumes,
            'ports': c_ports
        }
        docker_list.append(docker_dict)

    return(docker_list)
