#!/usr/bin/env bash

rm dist/geodata_cz_sk_0.1.zip

cd ..
mkdir -p dist/data
cp data/README.md dist/data/
mkdir -p dist/data_sources
cp -r data_sources/* dist/data_sources/
mkdir -p dist/doc
cp -r doc/* dist/doc/
mkdir -p dist/i18n
cp -r i18n/* dist/i18n/
mkdir -p dist/icons
cp icons/* dist/icons/
cp * dist

cd dist
zip -r geodata_cz_sk_0.1.zip *
