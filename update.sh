#!/usr/bin/env bash
hugo -D
rm -rf ../chimez-website/*
cp -a public/* ../chimez-website/
