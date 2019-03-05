# Transparent PNG

`transparent_png` is a simple Python script for creating a transparent PNG of a given size.

## Usage

```bash
python transparent_png.py [OPTION] [X] [Y]
```

### Options

| Option | description                                                           |
|--------|-----------------------------------------------------------------------|
| -o     | Optimizes the created image using ImageOptim, if available, or PNGOUT |

### Examples

```bash
python transparent_png.py 42 1337
```

Creates an image with a width of 42 and a height of 1337, with the name `42x1337.png` and saves it to the current directory.

```bash
python transparent_png.py -o 100 50
```

Creates an image of size 100x50 with the name `100x50.png`, optimizes it using [ImageOptim](https://imageoptim.com/mac) (if available on macOS) or [PNGOUT](http://www.jonof.id.au/kenutils) (*nix or Windows) and saves the image to the current directory.

## Running through Docker

Instead of having Python installed on your machine, make Docker do the heavy lifting for you.

### Example running with the image from Docker Hub

A Docker image is [available on Docker Hub](https://hub.docker.com/r/hjerpbakk/transparent-png).

```bash
docker run -v $(pwd):/app/image hjerpbakk/transparent-png 42 1337
```

The above command creates an image of size 42x1337 with the name `42x1337.png` and saves it to the current directory.

Using Docker, the same options are available as before. Thus, the following command creates an image of size 100x50 with the name `100x50.png`, optimizes it using PNGOUT and saves the image to the current directory.

```bash
docker run -v $(pwd):/app/image hjerpbakk/transparent-png -o 100 50
```

### Building the image locally

If you want to build the image yourself, use the following command:

```bash
docker build -t hjerpbakk/transparent-png .
```