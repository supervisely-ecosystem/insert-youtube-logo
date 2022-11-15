import os
from PIL import Image
from dotenv import load_dotenv
import supervisely as sly

# load ENV variables for debug
# has no effect in production
load_dotenv(os.path.expanduser("~/supervisely.env"))
load_dotenv("local.env")
api = sly.Api.from_env()


def main():
    percentage = 0.15
    img = Image.open(r"src/thumb2.jpg")
    logo = Image.open(r"src/ytlogo.png")
    w, h = img.size
    print(w, h)

    lw, lh = logo.size
    new_lw = int(w * percentage)
    new_lh = int(lh * (new_lw / lw))
    logo = logo.resize((new_lw, new_lh))
    print("img: ", img.size)
    print("logo: ", logo.size)
    # calculate logo landing spot
    img.paste(
        logo,
        (
            int(w * 0.5) - int(logo.size[0] / 2),
            int(h * 0.5) - int(logo.size[1] / 2),
        ),
        mask=logo,
    )
    # Image.Image.paste(img1, resized_img2, (50, 125))
    # img1.show()
    img.save("src/result.png")


if __name__ == "__main__":
    main()
