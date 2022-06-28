import subprocess
import os

mdictonary = {
    "biap-app-ui-front": "main",
    "biap-client-node-js": "main",
    "ondc-mmi-service": "main",
    "py-ondc-protocol": "dev"
}

def check_for_latest_commit():
    """
    check if current latest commit is same with remote
    :return:
    """
    try:
        local_commit_id = subprocess.check_output(["git", "rev-parse", "HEAD"]).decode("utf-8").strip()
        remote_commit_id = subprocess.check_output(["git", "rev-parse", "origin/master"]).decode("utf-8").strip()
        if local_commit_id != remote_commit_id:
            print(f"local commit id {local_commit_id} is not same with remote commit id {remote_commit_id}")
            return False
        else:
            print(f"local commit id {local_commit_id} is same with remote commit id {remote_commit_id}")
            return True
    except Exception as e:
        print(f"error while checking commit id {e}")
        return False


def pull_new_and_build(branch_name):
    """
    pull new commit and build
    :return:
    """
    try:
        subprocess.check_output(["git", "pull", "origin", branch_name, "--rebase"])
    except Exception as e:
        print(f"error while pulling new commit and building {e}")


def build_docker_compose():
    """
    build docker compose
    :return:
    """
    try:
        subprocess.check_output(["docker-compose", "build"])
    except Exception as e:
        print(f"error while building docker compose {e}")


def run_docker_compose():
    """
    run docker compose
    :return:
    """
    try:
        subprocess.check_output(["docker-compose", "up", "-d"])
    except Exception as e:
        print(f"error while running docker compose {e}")


def pull_for_directory(dir):
    print(f"watching the dir {dir}")
    current_dir = os.getcwd()
    # get dir absolute path
    dir_path = os.path.abspath(dir)
    os.chdir(dir_path)
    if check_for_latest_commit():
        pull_new_and_build(mdictonary.get(dir))
        build_docker_compose()
        run_docker_compose()
    os.chdir(current_dir)


if __name__ == '__main__':
    dirs = mdictonary.keys()
    for dir in dirs:
        pull_for_directory(dir)








