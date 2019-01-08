"""
Turns an image into a geometrized output (could be image or video)

"""
import os
import argparse
import tempfile
import shutil
import shlex
import subprocess

from pprint import pprint

primitive_path = 'primitive'


def create_primitive(input_file, output_file):
  # see all options in the primitive repo: https://github.com/fogleman/primitive
  mode = 1
  shapes_num = 200

  primitive_cmd = (
      '%s -i %s -o %s -n %s -m %s -v' % (
          primitive_path, input_file, output_file, shapes_num, mode))
  primitive_args = shlex.split(primitive_cmd)
  subprocess.call(primitive_args)


def make_motion(input_path):
  """
  Creates a motion from an input image

  this function uses imagemagick which should be possible to install using:
  brew install imagemagick
  """

  with tempfile.TemporaryDirectory() as temp_dir:
    print(temp_dir)

    gif_frames = []

    # first create all output filenames
    for x in range(4):
      frame_path = temp_dir + '/' + str(x) + '.png'
      gif_frames.append(frame_path)

    # now create all primitives
    print('Creating frames for your geometric gifs...')
    for frame_path in gif_frames:
      create_primitive(input_path, frame_path)

    # merge the images together with convert
    print('Merging frames together...')
    output = os.path.dirname(os.path.abspath(__file__)) + '/animation.gif'
    gif_cmd = (
        'convert -delay 10 -loop 0 *.png %s' % (output))

    gif_args = shlex.split(gif_cmd)
    process = subprocess.Popen(gif_args, cwd=temp_dir)
    process.wait()

    print('Your GIF is complete! Find it in animation.gif')
    return


def build_arg_parser():
  description = 'Create an animated, geometric GIF from an image'
  parser = argparse.ArgumentParser(description=description)

  parser.add_argument(
      'input_path', nargs='?', help='path to the input image', type=str
  )
  return parser


def validate_args(args):
  return args.input_path


if __name__ == '__main__':
  arg_parser = build_arg_parser()
  input_args = arg_parser.parse_args()

  if not validate_args(input_args):
    arg_parser.print_help()
  else:
    make_motion(**input_args.__dict__)
