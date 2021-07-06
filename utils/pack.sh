#!/usr/bin/env bash

rm ../dist/geodata_cz_sk_0.3.zip

cd ..

find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf

mkdir -p dist/czech_slovak_freegeodata/data
cp data/README.md dist/czech_slovak_freegeodata/data/
mkdir -p dist/czech_slovak_freegeodata/data_sources
cp -r data_sources/* dist/czech_slovak_freegeodata/data_sources/
mkdir -p dist/czech_slovak_freegeodata/doc
cp -r doc/* dist/czech_slovak_freegeodata/doc/
mkdir -p dist/czech_slovak_freegeodata/i18n
cp -r i18n/* dist/czech_slovak_freegeodata/i18n/
mkdir -p dist/czech_slovak_freegeodata/icons
cp icons/* dist/czech_slovak_freegeodata/icons/
mkdir -p dist/czech_slovak_freegeodata/help
cp -r help dist/czech_slovak_freegeodata/
mkdir -p dist/czech_slovak_freegeodata/crs_trans
cp -r crs_trans dist/czech_slovak_freegeodata/
cp * dist/cp * dist/czech_slovak_freegeodata/

cd dist
zip -r geodata_cz_sk_0.3.zip czech_slovak_freegeodata/
