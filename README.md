# transparent-png
Script for creating a transparent PNG of a specific size

docker build -t hjerpbakk/transparent-png .

docker run -v $(pwd):/app/image hjerpbakk/transparent-png 50 60