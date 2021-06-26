import os
import io

import responder

from cartoonization import (
    load_img,
    Cartoonizer,
    save_img
)


env = os.environ
DEBUG = env['DEBUG'] in ['1', 'True', 'true']
IMAGE_FORMAT = env.get('IMAGE_FORMAT')

api = responder.API(debug=DEBUG)


@api.route("/")
async def index(req, resp):
    body = await req.content
    img = load_img(io.BytesIO(body))
    format_str = IMAGE_FORMAT if IMAGE_FORMAT else img.format
    cartoon_img = Cartoonizer.cartoonize(img)
    resp.content = save_img(cartoon_img, format_str=format_str)


if __name__ == "__main__":
    api.run()
