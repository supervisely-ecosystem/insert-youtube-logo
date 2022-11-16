import os
from PIL import Image
from dotenv import load_dotenv
import supervisely as sly

# load ENV variables for debug
# has no effect in production
load_dotenv(os.path.expanduser("~/supervisely.env"))
load_dotenv("local.env")


def paste_logo(bg_path, save_path, logo_path="src/ytlogo.png"):
    percentage = 0.15
    img = Image.open(bg_path)
    logo = Image.open(logo_path)
    w, h = img.size

    lw, lh = logo.size
    new_lw = int(w * percentage)
    new_lh = int(lh * (new_lw / lw))
    logo = logo.resize((new_lw, new_lh))
    img.paste(
        logo,
        (
            int(w * 0.5) - int(logo.size[0] / 2),
            int(h * 0.5) - int(logo.size[1] / 2),
        ),
        mask=logo,
    )
    img.save(save_path)


def main():
    api = sly.Api.from_env()
    team_id = sly.env.team_id()
    remote_dir = sly.env.folder()
    files_info = api.file.list2(team_id, remote_dir)

    for info in files_info:
        remote_path = info.path
        # remote_path = sly.env.file()

        local_path = os.path.join("src", sly.fs.get_file_name_with_ext(remote_path))
        api.file.download(team_id, remote_path, local_path)

        result_name = (
            sly.fs.get_file_name(local_path)
            + "_youtube"
            + sly.fs.get_file_ext(local_path)
        )
        local_result_path = os.path.join("src", result_name)
        paste_logo(local_path, local_result_path)

        remote_result_path = os.path.join(os.path.dirname(remote_path), result_name)
        if api.file.exists(team_id, remote_result_path) is True:
            api.file.remove(team_id, remote_result_path)
        api.file.upload(team_id, local_result_path, remote_result_path)


if __name__ == "__main__":
    main()
