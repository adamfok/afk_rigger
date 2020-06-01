import maya.api.OpenMaya as om
import maya.cmds as cmds


def maya_useNewAPI():
    pass


def initializePlugin(plugin):
    vendor = "Chun Wai (Adam) Fok"
    version = "1.0.0"

    om.MFnPlugin(plugin, vendor, version)

    from eden.custom_menu import custom_menu
    custom_menu.CustomMenu().install()

    pass


def uninitializePlugin(plugin):
    from eden.custom_menu import custom_menu
    custom_menu.CustomMenu().remove()

    pass


if __name__ == "__main__":
    plugin_name = "eden.py"

    cmds.evalDeferred('if cmds.pluginInfo("{0}", q=True, loaded=True): cmds.unloadPlugin("{0}")'.format(plugin_name))
    cmds.evalDeferred('if not cmds.pluginInfo("{0}", q=True, loaded=True): cmds.loadPlugin("{0}")'.format(plugin_name))

    """
    plugin_name = "eden.py"
    
    if cmds.pluginInfo(plugin_name, q=True, loaded=True):
        cmds.unloadPlugin(plugin_name)
        
    cmds.loadPlugin(plugin_name)
    """
