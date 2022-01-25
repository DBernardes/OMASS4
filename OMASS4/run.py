#!/usr/bin/env python
# coding: utf-8
# 25/10/2019. Denis Varise Bernardes.

"""Script to run the optimization method."""

from Optimize_Camera import Optimize_Camera

opt_cam = Optimize_Camera(input_file_path="example")
opt_cam.optimize()
