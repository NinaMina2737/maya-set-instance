#!/usr/bin/env python
# coding=utf-8

from __future__ import absolute_import, division, print_function, unicode_literals
import maya.cmds as cmds
import traceback

def set_instance():
    # get selected objects
    objects = cmds.ls(selection=True, long=True)
    if len(objects) < 2:
        cmds.warning("Please select 2 or more objects.")
        raise Exception("Please select 2 or more objects.")

    # get first selected object
    base_object = objects[0]

    # get shape of first selected object
    base_shape = cmds.listRelatives(base_object, shapes=True)[0]

    # share shape of first selected object to other selected objects
    other_objects = objects[1:]
    for other_object in other_objects:
        # get shape of other selected object
        other_object_shape = cmds.listRelatives(other_object, shapes=True)[0]
        # set instance
        cmds.parent(base_shape, other_object, add=True, shape=True)
        # delete other shapes
        cmds.delete(other_object_shape)

def execute():
    try:
        # Open an undo chunk
        cmds.undoInfo(openChunk=True)
        # Execute the script
        set_instance()
    except Exception as e:
        # Print the error message
        cmds.warning("An error occurred: {}".format(str(e)))
        # Print the traceback
        cmds.warning(traceback.format_exc())
    finally:
        # Close the undo chunk
        cmds.undoInfo(closeChunk=True)

if __name__ == '__main__':
    # Execute the script
    execute()
