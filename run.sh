#!/bin/sh

rm -rf build
rm -rf dist
rm -rf odoo_helper.egg-info

python -m pip install --user --upgrade setuptools wheel
python setup.py sdist bdist_wheel
pip install -e .
python -m pip install --user --upgrade twine
python -m twine check dist/* && python -m twine upload dist/*