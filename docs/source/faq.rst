FAQ
===

Q: I opened a file made with WindowGen 3. What do I do?
-----------------------------------------------------------

Press **Update WindowGen in This File** at the top of the *Add Window* panel.

WindowGen 3 linked its components from the add-on folder. Version 4 stores them in the file. The update:

- switches every window to the new components and keeps all of its settings;
- removes the link to ``WindowGen.blend``, the hidden *WindowGen Components* scene and the library overrides;
- leaves each window with a single smoothing modifier;
- replaces WindowGen library materials used on your own objects with local copies.

Blender may print "Data corruption ... library override reference" messages while opening such a file. They describe the overrides the old version left behind and disappear after the update.

Windows in a WindowGen 3 file can still be edited before updating, as long as the old library file is where the file expects it.

Files made with WindowGen 2 are converted the same way. Their windows keep every setting; the profiles and hardware are replaced by the current versions, so the mesh is not identical vertex for vertex.

Q: Blender crashes or freezes when I open an old WindowGen file.
----------------------------------------------------------------

This is a Blender problem with library overrides whose linked file cannot be found. It happens before any add-on runs, so WindowGen cannot prevent it. It was observed with:

- WindowGen 2 files opened in Blender 5.2 or newer, unless the WindowGen 2 library is still at its original location;
- WindowGen 3 files opened in Blender 5.1 or newer when ``WindowGen.blend`` is missing altogether.

Installing WindowGen 4 over WindowGen 3 does not cause it: WindowGen 3 files open normally in every supported version with the new library in place.

To recover such a file:

1. Open it in the Blender version it was last saved with (WindowGen 4 runs on Blender 4.2 and newer), or put the old ``WindowGen.blend`` back where the file expects it.
2. Press **Update WindowGen in This File** and save.

The saved file no longer links anything and opens in every supported Blender version.

Q: Window geometry disappeared although the object is still in the Outliner.
----------------------------------------------------------------------------

This was caused by several "Auto Smooth" modifiers stacked on one window in WindowGen 3 files. Press **Update WindowGen in This File**; each window is left with exactly one *WindowGen Smooth* modifier and one *Weighted Normal*.

Q: The parameters are empty or show errors in Blender 5.2 and newer.
--------------------------------------------------------------------

Blender 5.2 changed how geometry nodes modifier inputs are accessed, which broke WindowGen 3. WindowGen 4 supports Blender 4.2 to 5.3. Install version 4 and update the file as described above.

Q: In Blender 5.3 the locks and other sash hardware appear next to the window.
------------------------------------------------------------------------------

That happens with WindowGen 3 components in Blender 5.3. Update the file; the version 4 components place the hardware identically in every supported Blender version.

Q: Does the person I send my file to need WindowGen?
----------------------------------------------------

No. The file contains everything the windows need. Without the add-on the windows still render and can be adjusted through the modifier panel; with the add-on the recipient also gets the WindowGen panels.

Q: We keep assets on a network server. Can WindowGen load from there?
---------------------------------------------------------------------

Yes. See *Studio setup: one shared library* in :doc:`working_with_generator`. Because windows are appended, scenes never contain a path to the library, local or network.

Q: Blender is slow when I modify windows.
-------------------------------------------

Keep *Realize Instances* off while you work and switch it on only for export or when you need real geometry. Lower *Profile Resolution* for windows that are far from the camera.

Q: The previews in the galleries are missing.
---------------------------------------------

Press the refresh button next to the gallery.
