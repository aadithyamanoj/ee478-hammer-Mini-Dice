'''
Hammer hooks for Mini_Dice cad flow

add this to ee478-hammer/py/
'''

import json
import os, stat
from tokenize import maybe

from hammer_vlsi.constraints import MMMCCornerType
import hammer_vlsi
from hammer_vlsi import CLIDriver, HammerToolHookAction, HierarchicalMode
import hammer_tech
from hammer_tech import Library, ExtraLibrary

from typing import Dict, Callable, Optional, List
from pathlib import Path


# Par hooks

def innovus_set_hold_target_slack(x: hammer_vlsi.HammerTool) -> bool:
    # sets target hold slack, can help innovus try a little harder. 
    # for post rout opt
    try:
        hold_slack = x.get_setting("par.innovus.opt_hold_target_slack")
    except KeyError:
        return True
    
    if hold_slack is None:
        return True

    x.verbose_append(f"set_db opt_hold_target_slack {hold_slack}")
    return True


