# Motion ![PRs Welcome](https://img.shields.io/badge/PRs-welcome-green.svg)

[MOTION](https://www.kapwing.com/motion) is an exploration of geometry, video, and machine learning. By using ML techniques, the tool generates shapes to fit the lines and colors of your image.

The project was inspired by [Primitive](https://github.com/fogleman/primitive) as well as [Geometrize](https://github.com/Tw1ddle/geometrize). The stitching of frames into GIFs is made possible by FFMPEG and ImageMagick.

This repo contains the code to be able to run Motion locally with python. You can also see the [online demo here](https://www.kapwing.com/motion).

## Quick overview

<p align='center'>
<img src='https://i.imgur.com/4FA6dDr.jpg' width='300' style='display:inline-block;margin-right: 10px;' alt='image preview' />
<img src='https://i.imgur.com/5nBce1A.gif' width='300' style='display:inline-block' alt='gif preview' />
</p>

We wanted to create a tool that could make short looping videos from still images, and the abstract effect created by geomatric shapes has always been a source of inspiration. With a unique hill-climbing algorithm, we were able to convert still photographs into beautiful, moving GIFs.

## Installation

Before running the script, you must first install [Primitive](https://github.com/fogleman/primitive) and ImageMagick.

To install Primitive, follow the instructions in the [primitive repo](https://github.com/fogleman/primitive).

```sh
go get -u github.com/fogleman/primitive
```

Then, install ImageMagick

```
brew install imagemagick
```

Now, clone the motion repo and install all dependencies:

```sh
git clone git@github.com:kapwing/motion.git
cd motion
pipenv install
pipenv run python3 motion.py your_input.jpg
```

## Acknowledgements

Credit is due to Michael Fogleman, the creator of Primitive on which this project is based

- [@fogleman](https://github.com/fogleman)

## License

Motion is open source software [licensed as MIT](https://github.com/kapwing/motion/blob/master/LICENSE).
