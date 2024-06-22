# WindowGen Documentation

Welcome to WindowGen

Procedural Window Generator for blender based on real life PVC window
profiles and furniture. In this documentation you can find how to use
the generator, future plans on development and updates.

Supported Blender versions: 3.6+

[**STARTING UP**](#starting-up)

> [How to add a generator to your scene
>](#how-to-add-a-generator-to-your-scene)

[**WORKING WITH THE GENERATOR**](#working-with-the-generator)

> [How to change parameters](#how-to-change-parameters)
>
> [Generator structure](#generator-structure)

[**PARAMETERS**](#parameters)

> [Profiles](#profile)
>
> [Size](#size)
>
> [Window Parameter](#window-parameters)
>
> [Origin in Center](#origin-in-center)
>
> [Frame Only](#frame-only)
>
> [Realize instances](#realize-instances)
>
> [Rotation Settings](#rotation-settings)
>
> [Turn Rotation](#turn-rotation)
>
> [Tilt Rotation](#tilt-rotation)
>
> [Left Turn Rotation](#left-turn-rotation)
>
> [Left Tilt Rotation](#left-tilt-rotation)
>
> [Handle Settings](#handle-settings)
>
> [Handle](#handle)
>
> [Custom Handle Height](#custom-handle-height)
>
> [Handle Height](#handle-height)
>
> [Handle Rotation](#handle-rotation)
>
> [Left Handle Rotation](#left-handle-rotation)
>
> [Glazing Settings](#glazing-settings)
>
> [Glazing](#glazing)
>
> [Impost Settings](#impost-settings)
>
> [Impost](#impost)
>
> [Left/Right Sash](#leftright-sash)
>
> [1/2 Sashes](#sashes)
>
> [Middle Section](#middle-section)
>
> [Impost Centered](#impost-centered)
>
> [Impost Frame Width](#impost-frame-width)
>
> [Stulp Settings](#stulp-settings)
>
> [Stulp](#stulp)
>
> [Right/Left](#rightleft)
>
> [Materials](#materials)

[**CUSTOMIZATION**](#customization)

> [How to add custom handle](#how-to-add-custom-handle)

[**FUTURE PLANS**](#future-plans)

#  

# STARTING UP

## How to add a generator to your scene

To incorporate a generator into your Blender scene, follow these steps:

1.  Click on "File" in the top left corner.

2.  Select "Append...".\
    <img src="media/image23.png" width="213" height="236" />

3.  Navigate to the folder where you saved the .blend file containing
    the generator and double-click on it.

4.  Within the file, navigate to the Collection folder.\
    <img src="media/image7.png" width="213" height="179" />

5.  Select "!GENERATOR (Append Me)" and click "Append" in the bottom
    right corner. <img src="media/image25.png" width="468" height="280" />

Your scene should now reflect the changes made by appending the
generator:\
<img src="media/image10.png" width="468" height="247" />

You can easily disable the "PROFILES" and "FURNITURE" collections as
they include the modeled geometry that is used in the generator such as
PVC profiles and furniture.

# WORKING WITH THE GENERATOR

## How to change parameters

The generator utilizes the geometry nodes modifier. To adjust
parameters, follow these steps:

1.  Select the "!Generator" object.

2.  Click on the wrench icon (Modifier Properties) on the right-hand
    side.\
    <img src="media/image22.png" width="213" height="224" />

## Generator structure

The generator is divided into the following sections:


<div dir="ltr" style="margin-left:0pt;" align="left"><table style="border:none;border-collapse:collapse;">
<colgroup><col width="165"><col width="469"></colgroup><tbody>
<tr style="height:18.75pt">
<td style="vertical-align:top;background-color:#f1f3f4;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:'Proxima Nova',sans-serif;color:#353744;background-color:transparent;font-weight:700;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Profile</span></p>
</td>
<td style="vertical-align:top;background-color:#f1f3f4;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:'Proxima Nova',sans-serif;color:#353744;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Choose from 5 build-in profiles.</span></p>
</td>
</tr>
<tr style="height:0pt">
<td style="vertical-align:top;background-color:#f1f3f4;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:'Proxima Nova',sans-serif;color:#353744;background-color:transparent;font-weight:700;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Size</span></p>
</td>
<td style="vertical-align:top;background-color:#f1f3f4;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:'Proxima Nova',sans-serif;color:#353744;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Adjust the size of your window.</span></p>
</td>
</tr>
<tr style="height:0pt">
<td style="vertical-align:top;background-color:#f1f3f4;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:'Proxima Nova',sans-serif;color:#353744;background-color:transparent;font-weight:700;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Window parameters</span></p>
</td>
<td style="vertical-align:top;background-color:#f1f3f4;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:'Proxima Nova',sans-serif;color:#353744;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Customize window features such as centering, sash disabling, and instance realization.</span></p>
</td>
</tr>
<tr style="height:0pt">
<td style="vertical-align:top;background-color:#f1f3f4;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:'Proxima Nova',sans-serif;color:#353744;background-color:transparent;font-weight:700;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Rotation settings</span></p>
</td>
<td style="vertical-align:top;background-color:#f1f3f4;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:'Proxima Nova',sans-serif;color:#353744;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Modify sash rotation.</span></p>
</td>
</tr>
<tr style="height:0pt">
<td style="vertical-align:top;background-color:#f1f3f4;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:'Proxima Nova',sans-serif;color:#353744;background-color:transparent;font-weight:700;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Handle settings</span></p>
</td>
<td style="vertical-align:top;background-color:#f1f3f4;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:'Proxima Nova',sans-serif;color:#353744;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Choose handle, position, and rotation.</span></p>
</td>
</tr>
<tr style="height:0pt">
<td style="vertical-align:top;background-color:#f1f3f4;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:'Proxima Nova',sans-serif;color:#353744;background-color:transparent;font-weight:700;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Glazing settings</span></p>
</td>
<td style="vertical-align:top;background-color:#f1f3f4;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:'Proxima Nova',sans-serif;color:#353744;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Select between double or triple glazing.</span></p>
</td>
</tr>
<tr style="height:0pt">
<td style="vertical-align:top;background-color:#f1f3f4;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:'Proxima Nova',sans-serif;color:#353744;background-color:transparent;font-weight:700;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Impost settings</span></p>
</td>
<td style="vertical-align:top;background-color:#f1f3f4;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:'Proxima Nova',sans-serif;color:#353744;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Control the presence and attributes of the impost.</span></p>
</td>
</tr>
<tr style="height:0pt">
<td style="vertical-align:top;background-color:#f1f3f4;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:'Proxima Nova',sans-serif;color:#353744;background-color:transparent;font-weight:700;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Stulp settings</span></p>
</td>
<td style="vertical-align:top;background-color:#f1f3f4;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:'Proxima Nova',sans-serif;color:#353744;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Configure settings for two-sash windows without impost.</span></p>
</td>
</tr>
<tr style="height:0pt">
<td style="vertical-align:top;background-color:#f1f3f4;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:'Proxima Nova',sans-serif;color:#353744;background-color:transparent;font-weight:700;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Materials</span></p>
</td>
<td style="vertical-align:top;background-color:#f1f3f4;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:'Proxima Nova',sans-serif;color:#353744;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Assign window materials.</span></p>
</td>
</tr>
</tbody>
</table>
</div>


# PARAMETERS

## Profile

This section features a single parameter **Profiles** (it was called
**System** in previous versions), which allows you to choose a window
profile. For that select profile from 0 to 4:

<img src="media/image32.gif" width="320" height="320" />

*Note that custom profiles aren't currently supported due to
dependencies on specific parameters for hinges, handles, and striker
plates. Feel free to contact us for specific profile requests.*

## Size

This section includes parameters **Width** and **Height** for adjusting
the width and height of the window.

##  

## Window Parameters

This section includes parameters for centering the window, enabling
frame-only window, and realizing instances.

### **Origin in Center**

Positions the window in the center of the geometry bounding box.

<img src="media/image2.gif" width="320" height="320" />

### **Frame Only**

Disables sashes, leaving only the frame with glass.

<img src="media/image5.gif" width="320" height="320" />

### **Realize instances**

Converts instances into real geometry.

<img src="media/image17.gif" width="320" height="320" />

## Rotation Settings

This section includes parameters for adjusting turn and tilt rotations
of the sash.

### **Turn Rotation**

Sets the turn angle of the sash.

*When the **Impost** is activated, it sets the turn angle of the right
sash.*

### **Tilt Rotation**

Sets the tilt angle of the sash. It is constrained to the size of the
scissors, automatically ignoring impossible values for the given window
size.

*When the **Impost** is activated, it sets the tilt angle of the right
sash.*

### **Left Turn Rotation**

Active when the **Impost** is turned on. Sets the turn angle of the left
sash.

### **Left Tilt Rotation**

Active when the **Impost** is turned on. Sets the tilt angle of the left
sash. Similar to **Tilt Rotation**, it is constrained to the size of the
scissors.

## Handle Settings

This section includes parameters for handle type, height, and rotation.

### **Handle**

Choose from different handle types or add a custom handle. More on that
[[here]{.underline}](#how-to-add-custom-handle).<img src="media/image14.gif" width="320" height="320" />

### **Custom Handle Height**

Allows to set the height position of the handle manually.

### **Handle Height**

Active when the **Custom Handle Height** is turned on. Adjust the
handle's height.<img src="media/image28.gif" width="320" height="320" />
### **Handle Rotation**

Sets the rotation of the handle. When the **Impost** is activated, it
sets the rotation of the right sash's handle.

### **Left Handle Rotation**

Active when **Impost** is turned on. Sets the rotation of the left
sash's handle.

## Glazing Settings

This section allows you to choose between double or triple glazing.

### **Glazing**

Choose between double glazed (0) and triple glazed (1)
windows:<img src="media/image27.gif" width="320" height="320" />

## Impost Settings

This section includes parameters for the impost (vertical post in the
window frame) and sashes.

### **Impost**

Activate or deactivate the impost.

<img src="media/image29.gif" width="320" height="320" />

### **Left/Right Sash**

Switch between left and right sashes. Only active when **1/2 Sashes** is
off.

<img src="media/image6.gif" width="320" height="320" />

###  

### **1/2 Sashes**

Switch between 1 or 2 sashes:

<img src="media/image15.gif" width="320" height="320" />

### **Middle Section**

Activate distance between 2 sashes:

<img src="media/image33.gif" width="320" height="320" />

###  

### **Impost Centered**

Automatically calculate even space for sashes and impost frame:

<img src="media/image18.gif" width="320" height="320" />

### **Impost Frame Width**

Sets the width of the impost frame (**Impost Centered** must be **turned
off**). This both works for 1 and 2 sashes window:

<img src="media/image20.gif" width="320" height="320" />

##  

## Stulp Settings

This section includes parameters for two-sash windows without an impost.

### **Stulp**

Activate two-sash window without an impost:

<img src="media/image3.gif" width="320" height="320" />

### **Right/Left**

Switch between right or left leading sash:

<img src="media/image12.gif" width="320" height="320" />

## Materials

This section allows you to assign materials to your window.

For the materials work correctly for Mapping choose **UV Map** node and
select UVMap (in some cases **Realize Instances** must be turned on in
the WindowGen Modifier):

<img src="media/image1.png" width="468" height="151" />


  **UVMaps:** The window includes necessary UVMaps, although there may be
  rotation issues at certain widths due to limitations in controlling UV
  unwrapping in geometry nodes.

  **Spacer Material:** If you wish to change the spacer material, it's
  recommended to adjust the existing material to your needs, as it
  contains a custom bump map for a realistic look and helps to reduce
  extra geometry for the spacer.

# CUSTOMIZATION

## How to add custom handle

To add custom handle, follow these steps:

1.  Temporarily disable Generator in the viewport. Activate "HANDLES"
    collection inside "FURNITURE" collection:

> <img src="media/image9.gif" width="320" height="320" />

2.  Import your custom handle to the "HANDLES" collection.\
    *Note that your custom handle must be comparable in sizes to the
    other handles in the collection*:\
    <img src="media/image26.gif" width="320" height="320" />

3.  Position your handle to the World Origin:\
    <img src="media/image31.gif" width="320" height="320" />

4.  Navigate to the Right orthographic view, for that press 3 on your
    Numpad or press ~ on your keyboard and choose **Right**, as it is
    shown below:\
    <img src="media/image30.gif" width="320" height="320" />\
    *Note that your handle must be oriented the same way as it is
    oriented in the example above. **Press Ctrl+A to apply Scale and
    Rotation**.*

5.  Origin of your handle must be at the beginning of the base geometry.
    Additionally, the rotation center of the handle should be
    appropriately set. Adhering to these guidelines is crucial for
    preventing clipping issues with window geometry and ensuring the
    correct rotation of the handle.\
    <img src="media/image8.png" width="320" height="320" />

6.  In cases where your handle and its base are joined into a single
    geometry, it is essential to separate them. This separation allows
    for independent rotation of the handle while ensuring that the base
    remains firmly attached to the sash:\
    <img src="media/image24.gif" width="320" height="320" />

7.  Unhide the Generator and select it.

8.  Navigate to the geometry nodes tab.

9.  Select **Handle Switch** node (it is located on the blue underlay)
    and press Tab to add your handle:\
    <img src="media/image11.gif" width="320" height="320" />

10. Change one of the current handles and its base to your custom
    handle:\
    <img src="media/image16.gif" width="320" height="320" />

#  

# FUTURE PLANS

Currently in the work and will be delivered with the next update:

-   Transom Window:\
    <img src="media/image4.png" width="283" height="244" />

-   Window Lites:\
    <img src="media/image13.png" width="283" height="283" />


  If you have ideas for new functionalities you'd like to see
  implemented or specific requirements tailored to your project, please
  don't hesitate to reach out to us. We value your feedback and are
  committed to enhancing WindowGen to better suit your needs. Contact us
  to discuss your suggestions or requirements further. We're here to
  help! i@mshevchenko.ru



# RELEASES

## Version 1.1

-   Initial release

## Version 1.2

-   Added lites

-   Added transom option (awning and hopper types)

-   Optimization. Average face count reduced by 10%

-   UI improvements for Blender 4.1. Added panels
