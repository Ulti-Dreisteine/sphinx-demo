# -*- coding: utf-8 -*-
"""
Created on 2020/8/7 11:34 上午

@Project -> File: PyCaret-tutorial -> __init__.py

@Author: luolei

@Email: dreisteine262@163.com

@Describe: 初始化目录
"""

import sys

sys.path.append('../')

from mod.config.config_loader import config_loader

proj_dir, proj_cmap = config_loader.proj_dir, config_loader.proj_cmap

# 项目变量配置.
environ_config = config_loader.environ_config
model_config = config_loader.model_config
test_params = config_loader.test_params

# ============ 通用函数 ============

# ============ 环境变量 ============

# ============ 模型参数 ============

# ============ 测试参数 ============
