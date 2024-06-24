Customization
=============

How to add a custom handle
--------------------------

To add a custom handle, follow these steps:

1. Temporarily disable Generator in the viewport. Activate "HANDLES" collection inside "FURNITURE" collection.
    
    .. image:: images/04_customization_disable.gif
        :width: 75%

2. Import your custom handle to the "HANDLES" collection.
    
    .. image:: images/04_customization_import.gif
        :width: 75%

    .. important::
        Your custom handle must be comparable in size to the other handles in the collection.
            
3. Position your handle to the World Origin.
    
    .. image:: images/04_customization_worl_origin.gif
        :width: 75%

4. Navigate to the Right orthographic view (press 3 on your Numpad or press ~ on your keyboard and choose Right).
    
    .. image:: images/04_customization_right_view.gif
        :width: 75%

    .. important::
        Ensure your handle is oriented the same way as in the example provided. **Press Ctrl+A to apply Scale and Rotation**.

5. The origin of your handle must be at the beginning of the base geometry. The rotation center of the handle should be appropriately set to prevent clipping issues and ensure correct rotation.
   
    .. image:: images/04_customization_origin.png
        :width: 75%

6. If your handle and its base are joined into a single geometry, separate them to allow independent rotation of the handle while ensuring the base remains attached to the sash.
   
    .. image:: images/04_customization_handle_and_base.gif
        :width: 75%

7. Unhide the Generator and select it.
8. Navigate to the geometry nodes tab.
9. Select **Handle Switch** node (located on the blue underlay) and press Tab to add your handle.
   
    .. image:: images/04_customization_handle_node.gif
        :width: 75%

10. Change one of the current handles and its base to your custom handle.
   
    .. image:: images/04_customization_handle _change.gif
        :width: 75%
