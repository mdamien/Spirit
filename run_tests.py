#-*- coding: utf-8 -*-

import os
import sys
import django

os.environ['DJANGO_SETTINGS_MODULE'] = 'example.settings_test_runner'

from django.test.runner import DiscoverRunner


def run_tests():
    django.setup()
    test_runner = DiscoverRunner()
    failures = test_runner.run_tests(["spirit", ])
    sys.exit(failures)


if __name__ == "__main__":
    run_tests()
