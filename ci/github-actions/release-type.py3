#! /usr/bin/python3
from os import environ
import re

release_tag = environ.get('RELEASE_TAG', None)

if not release_tag:
  print('::error ::Missing mandatory environment variable RELEASE_TAG')
  exit(1)

tag_prefix = 'refs/tags/'
if release_tag.startswith(tag_prefix):
  release_tag = release_tag.replace(tag_prefix, '', 1)

def dict_path(source: dict, path: list) -> object:
  if not path: return source
  key, *next = path
  res = source.get(key)
  if res is None: return None
  if type(res) == dict: return dict_path(res, next)
  if next: return None
  return res

if re.match(r'^[0-9]+\.[0-9]+\.[0-9]+-.+$', release_tag):
  print('::set-output name=release_type::prerelease')
  print('::set-output name=is_release::true')
  print('::set-output name=is_prerelease::true')
  print(f'::set-output name=release_tag::{release_tag}')

elif re.match(r'^[0-9]+\.[0-9]+\.[0-9]+$', release_tag):
  print('::set-output name=release_type::official')
  print('::set-output name=is_release::true')
  print('::set-output name=is_prerelease::false')
  print(f'::set-output name=release_tag::{release_tag}')

else:
  print('::set-output name=release_type::none')
  print('::set-output name=is_release::false')
  print('::set-output name=is_prerelease::false')
  print(f'::set-output name=release_tag::{release_tag}')
