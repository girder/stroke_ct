import click
import os

__version__ = '0.1.0'


@click.command()
@click.argument('in-dir', type=click.Path(exists=True, file_okay=False))
@click.option('--mp4-out', type=click.Path(), help='output mp4 location')
@click.option('--gif-out', type=click.Path(), help='output image height (px)')
@click.version_option(version=__version__, prog_name='Generate timelapse videos from images')
def run(in_dir, mp4_out, gif_out):
    files = [os.path.join(in_dir, f) for f in sorted(os.listdir(in_dir))]
    import pprint
    print('Sorted files:')
    pprint.pprint(files)

    if mp4_out:
        with open(mp4_out, 'wb') as out, open('/test.mp4', 'rb') as mp4:
            out.write(mp4.read())

    if gif_out:
        with open(gif_out, 'wb') as out, open('/test.gif', 'rb') as gif:
            out.write(gif.read())

if __name__ == '__main__':
    run()
