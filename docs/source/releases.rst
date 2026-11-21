Releases
========

Version 1.1
-----------

Initial release

Version 1.2
-----------

- Added lites
- Added transom option (awning and hopper types)
- Optimization. Average face count reduced by 10%
- UI improvements for Blender 4.1. Added panels

Version 2.0
-----------

- Standalone add-on release
- Better performance

Version 2.0.2
-------------

- Fixed a bug causing the Apply Modifier to not work and send an error.

Version 2.0.3
-------------

- Added opening option (inward and outward opening) in Rotation Settings

Version 2.0.4
-------------

- Fixed an issue where the Window Material was not updating

Version 2.0.5
-------------

- Corrected stulp position for window heights of 2.1m and above for Stulp Window.
- Resolved incorrect hinge orientation when "Realize Instances" is unchecked for Awning and Transom Windows.
- Fixed incorrect glass position when "Outward Opening" is selected for 3 Section Window.

Version 3.0
-------------

- Updated UI: progress is shown while appending and updating.
- Improved initial append performance.
- Added documentation links in the UI.
- New placement option: *Place at Selected Face*.
- Added profile resolution control.
- Added texel density control (scale UVs).
- Added new window types: Portal (lift & slide) and Sliding.
- Added update functionality to upgrade WindowGen components in existing projects.
- Added export functionality: prepare windows for export, set origins, and perform automatic export to selected formats.
- Added an asset library with multiple material presets.
- Fixed several bugs.

Version 3.0.2
-------------

- Fixed unexpected Lite behavior in Blender 4.5
- Fixed sliding window profiles not updating correctly
- Fixed incorrect sash scaling for Portal F and Portal C4 when changing window dimensions

Version 4.0.0
-------------

Complete rewrite. Requires Blender 4.2 or newer; tested up to Blender 5.3.

- Works in Blender 5.2 and 5.3 (parameters were not shown in 5.2; sash hardware was misplaced in 5.3).
- Windows are appended instead of linked. Files are self-contained and can be shared without relinking.
- No "Append WindowGen" step: components load automatically with the first window.
- Only the window appears in the Outliner; no hidden scene, no helper collections.
- Fixed disappearing geometry caused by duplicated Auto Smooth modifiers.
- One-click update of existing files, including files made with WindowGen 3.
- Custom library folder (preference or ``WINDOWGEN_LIBRARY`` environment variable) for studios with shared storage.
- Material library split into its own asset file; the generator file went from 109 MB to 7 MB.
- Handle, glazing and other choices are stored per window (portal and sliding handles used to be shared by the whole scene).
- Face placement works directly from Edit Mode; cutting the opening is optional.
- Many windows at once: a window on every selected face, optional random window types within the chosen category, editing all selected windows together, copying settings from the active window and randomizing type, side and opening of existing windows.
- "Add Window" is a button, so the same preset can be added several times in a row and the action can be undone.
- Export rewritten: OBJ export works again, parts get correct origins and hierarchy at any object scale, the original window is never modified.
- Removed Windows-only file paths that broke the add-on on macOS and Linux.

Version 4.1.0
-------------

- Interior: rooms behind the glass for facades seen from outside. One built-in material with eight furnished rooms, Day / Night, Lights On, Lit Windows and Room Variation. It adds almost no geometry and works the same with *Realize Instances* on or off.
- Level of Detail: windows far from the camera are drawn more simply, by themselves, when the camera stops moving. Choose what low detail does (profile resolution 1, hide hinges, hide locks and strikers); set *Detail* per window to Auto, Full or Low. Renders and animations are always up to date; export always uses full detail.
- Hinges and Locks and Strikers can be turned off per window.
- Shading is now identical with *Realize Instances* on and off.
- Reorganized sidebar: *Opening* replaces *Rotation* and *Slide*; *Hardware* holds the handle, hinges and locks; Glazing moved into *Profile*; Pivot moved into *Size*; new *Interior* and *Performance* panels; the *Options* panel is gone.
- *Apply Modifier* is now **Convert to Mesh…** in the *Export* panel and asks before converting.
- Level of Detail shows its status in the panel header; the Library panel shows whether the file is up to date and holds *Reload Previews*.
- Shorter labels that are no longer cut off; Randomize shows the window type list inline.
