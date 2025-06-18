rm -rf *.egg-info build dist

python -m build

rm -rf *.egg-info build

twine check dist/*
