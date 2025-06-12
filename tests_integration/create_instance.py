import logging
import os
from time import sleep

import docker
import requests
from docker.errors import DockerException, ImageNotFound, ContainerError
from tqdm import tqdm

client = docker.from_env()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

CONTAINER_NAME = 'jellyfin_integration_test'


def create_instance():
    script_dir = os.path.dirname(os.path.abspath(__file__))

    config_dir = os.path.join(script_dir, 'config')
    media_dir = os.path.join(script_dir, 'media')

    assert os.path.exists(config_dir), "Config directory does not exist, check out from git again."
    assert os.path.exists(media_dir), "Media directory does not exist, check out from git again."

    try:
        all_containers = client.containers.list(all=True)
        container_exists = any(container.name == CONTAINER_NAME for container in all_containers)

        if os.getenv('KEEP_JELLYFIN') and container_exists:
            container = client.containers.get(CONTAINER_NAME)
            if container.status == 'running':
                logger.info("Keeping Jellyfin from last run.")
                return


        # Pull the Jellyfin image
        logger.info("Pulling Jellyfin image...")
        client.images.pull("jellyfin/jellyfin")

        # Run the Jellyfin container
        logger.info("Running Jellyfin container...")
        container = client.containers.run(
            "jellyfin/jellyfin",
            name=CONTAINER_NAME,
            ports={'8096/tcp': 11111},
            volumes={
                config_dir: {'bind': '/config', 'mode': 'rw'},
                media_dir: {'bind': '/media', 'mode': 'ro'},
            },
            detach=True
        )
        logger.info(f"Running Jellyfin container with id {container.id}")
        logger.info("Waiting up to 60 seconds for Jellyfin container...")
        for i  in tqdm(range(60)):
            sleep(1)
            if i < 10: # ten-second grace period for docker to do its magic
                continue
            if requests.get("http://localhost:11111/System/Info/Public").status_code < 300:
                break
    except ImageNotFound as e:
        logger.error(f"Docker image not found: {e}")
    except ContainerError as e:
        logger.error(f"Container error occurred: {e}")
    except DockerException as e:
        logger.error(f"An dokcer error occurred: {e}")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")


def cleanup_instance():
    if os.getenv('KEEP_JELLYFIN'):
        return

    try:
        container = client.containers.get("jellyfin")
        container.stop()
        logger.info("Jellyfin container stopped.")

        # Remove the container
        container.remove()
        logger.info("Jellyfin container removed.")
    except DockerException as e:
        logger.info(f"An error occurred: {e}")
