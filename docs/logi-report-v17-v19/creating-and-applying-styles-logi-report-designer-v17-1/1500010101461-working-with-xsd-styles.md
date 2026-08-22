---
title: "Working with XSD Styles"
id: 1500010101461
section: "Creating and Applying Styles - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010101461-Working-with-XSD-Styles
updated_at: 2021-07-23T19:16:52Z
---

# Working with XSD Styles

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010101441-Creating-and-Applying-Styles)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010062822-Working-with-CSS-Styles)

# Working with XSD Styles

An XSD style, that is a style group in a catalog, can hold a large amount of predefined object properties, giving you more control over the appearance and presentation of your report. You can nest the style groups, where the parent group is used as a container of other groups. The Style Group feature makes it easy to save and apply styles without repeatedly designing them each time. You can create various visual presentation sets from a single report, and change the visual presentation of your report at runtime in a dramatic way by applying different style groups. This topic describes how you can create and modify XSD styles in Designer, as well as edit the XSD style files outside Designer.

XSD styles are a Logi Report specific format and not an industry standard so you may want to use CSS styles which are an industry standard.

This topic contains the following sections:

* [Creating and Modifying XSD Styles in a Catalog](#XSD)
  + [Creating an XSD Style](#Create)
  + [Duplicating an XSD Style](#Duplicate)
  + [Editing an XSD Style](#EditGroup)
  + [Renaming an XSD Style](#RenameGroup)
  + [Editing the Properties of an XSD Style or a Style in an XSD Style](#Property)
  + [Editing a Style in an XSD Style](#EditStyle)
  + [Renaming a Style in an XSD Style](#RenameStyle)
  + [Removing a Style from an XSD Style](#RemoveStyle)
  + [Removing an XSD Style from a Catalog](#RemoveGroup)
* [Editing the XSD Style Files Outside Designer](#Edit)

## Creating and Modifying XSD Styles in a Catalog

Designer provides you with the Style Editor to manage XSD styles in a catalog (to display the editor, [open the catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500010056622-Creating-Opening-and-Saving-Catalogs#Open) to which you want to add the style groups, then on the Catalog Manager toolbar, select **Style**).

![Style Editor](https://devnet.logianalytics.com/hc/article_attachments/4404848388887/styledtr.gif)

The following shows how you can create and modify XSD styles in a catalog using the Style Editor:

### Creating an XSD Style

1. Do either of the following:
   1. Right-click any of the existing style groups (except the Default style group) or the root node **Style Groups** and select **New Style Group**  from the shortcut menu.
   2. Select the root node **Style Groups**, select **New Style Group** on the toolbar.Designer displays the New Style Group dialog box.

   ![New Style Group](https://devnet.logianalytics.com/hc/article_attachments/4404856814743/style_xsd_crt1.gif)
2. Specify the name and description of the group, then select **OK**. Designer adds a new style group to the tree.
3. Right-click the group and select **New Style**, or select the group and select **New Style** on the toolbar. Designer displays the New Style dialog box.

   ![New Style](https://devnet.logianalytics.com/hc/article_attachments/4404848390551/style_xsd_crt2.gif)
4. Specify the name, type, and description of the new style, then select **OK**.

   The style type indicates the application scope of a style, for example, you can apply a style with the "Label" type to label objects, and a style with the "DBField" to DBFields.
5. In the [Save Style dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010098981-Save-Style-Dialog-Box), add the properties you want to include in the style and change the property values as required.

   ![Save Style](https://devnet.logianalytics.com/hc/article_attachments/4404848390807/svstyl.gif)

   To add a property, select it in the **All Properties** box and select **![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848391191/btn_addarrow.gif)**; to add all the available properties to the style at a time, select ![Add All button](https://devnet.logianalytics.com/hc/article_attachments/4404848391575/btn_addall.gif).

   To edit the value of a property, select its value cell in the **Selected Properties** box, then type the new value and press **Enter** on the keyboard to confirm the change.

   To remove a property that you have added, select it in the Selected Properties box and select ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404848391831/btn_rmvarrow.gif); to remove all the added properties at a time, select ![Remove All button](https://devnet.logianalytics.com/hc/article_attachments/4404848392215/btn_rmvall.gif).
6. Select **Save** to add the style to the style group.
7. Repeat steps 3 to 6 to add more styles to the style group.

### Duplicating an XSD Style

You can duplicate an XSD style using either of the following methods:

* Right-click the style group and select **Copy Style Group** from the shortcut menu, then ight-click the node where you want to duplicate the style group, and select **Paste Style Group**.
* Select the style group and select **Copy** on the Style Editor toolbar, then select the node to place the style group and select **Paste** on the toolbar.

- Designer then duplicates a new group with all styles within it in the style group tree.

### Editing an XSD Style

1. Right-click the style group and select **Edit Group** from the shortcut menu, or select the style group and select **Edit** on the Style Editor toolbar. Designer displays the [Edit Style Group dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010058842-Edit-Style-Group-Dialog-Box).

   ![Edit Style Group](https://devnet.logianalytics.com/hc/article_attachments/4404848392471/edtstylgrp.gif)
2. In the **All Styles** box, select the styles that you want to include in the group, and then select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848391191/btn_addarrow.gif) to add them to the **Selected Styles** box; or you can remove some existing styles from the group by selecting them in the Selected Styles box and selecting ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404848391831/btn_rmvarrow.gif).
3. If you want to create a new style in the group, select the **New Style** button and specify the properties of the style as seen above.
4. Select **OK** to finish editing.

### Renaming an XSD Style

You can rename the style groups except for the Default style group.

1. Do any of the following:
   1. Select the style group and select **Rename** on the Style Editor toolbar.
   2. Right-click the style group and select **Rename** from the shortcut menu.
   3. Select on the name of the style group twice.
2. The name box becomes editable. Type the new name and select outside of the name box to accept the change.

### Editing the Properties of an XSD Style or a Style in an XSD Style

Select the style group, or expand a style group and select the style in it, then in the Properties sheet on the right, edit the property values as required.

You can make use of the search box to search for the desired properties (to display the search box, select the **Search** icon ![Search icon](https://devnet.logianalytics.com/hc/article_attachments/4404856807959/btn_srch.gif) at the upper right corner of the Properties sheet). To start searching, type the text you want to search for in the search box and Designer lists the properties containing the matched text. Designer closes the search box when you select another style group or style.

You can make use of the following options in the search box:

* ![More Search Option button](https://devnet.logianalytics.com/hc/article_attachments/4404848393111/btn_srchbox_adv.gif)**Drop-down icon**  
  Select to list more search options.
  + **Highlight All**   
    Select to highlight all matched text.
  + **Match Case**   
    Select to search for text that meets the case of the typed text.
  + **Match Whole Word**   
    Select to search for text that looks the same as the typed text.
* ![Close button](https://devnet.logianalytics.com/hc/article_attachments/4404856816535/btn_close1.gif)**Delete icon**  
  Select to close the search box and cancel the search.

### Editing a Style in an XSD Style

1. Expand the node of the style group, select the style in it, then select **Edit** on the Style Editor toolbar or right-click the style and select **Edit Style** from the shortcut menu.
2. In the Save Style dialog box, add more properties to the style or edit the existing properties of the style.
3. Select **OK** to apply the changes.

### Renaming a Style in an XSD Style

1. Expand the node of the style group, then do any of the following:
   1. Select the style and select **Rename** on the Style Editor toolbar.
   2. Right-click the style and select **Rename** from the shortcut menu.
   3. Select on the name of the style twice.
2. The name box becomes editable. Type the new name and select outside of the name box to accept the change.

### Removing a Style from an XSD Style

1. Expand the node of the style group, then do any of the following:
   1. Select the style and select **Delete** on the Style Editor toolbar.
   2. Right-click the style and select **Delete** from the shortcut menu.
   3. Select the style and press **Delete** on your keyboard.
2. Select **OK** in the warning message to confirm the removal.

### Removing an XSD Style from a Catalog

Except for the Default style group, you can delete the other style groups from the current catalog if you do not need them any more.

1. Do any of the following:
   1. Select the style group and select **Delete** on the Style Editor toolbar.
   2. Right-click the style group and select **Delete** from the shortcut menu.
   3. Select the style group and press **Delete** on your keyboard.
2. Select **OK** in the warning message to confirm the removal.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg)

* The root of the style group tree can only hold style groups. The styles must reside in the style groups. You cannot create a style directly in the style group tree root.
* You cannot create style groups in the Default style group.
* The name of each style group must be unique in the style group tree.
* You can create more than one style for a style type, and apply different styles to report objects of the same type. For example, suppose that you have a number of DBFields in your report, such as address fields, totals, and quantity fields. You probably do not want all the fields to look the same. You can create two or more styles, using the same style type - DBField, and then apply them separately to the fields that you want to distinguish.
* You can apply a default style to all the objects that hold the same type.

  In the Default style group, create a new style, making sure that the style name and style type are the same, for example, style name is Label and style type is Label. Then, modify the style properties. When you insert a new object of the specified type into a report, Designer applies the default style to the object automatically. You can see the difference only at runtime.

## Editing the XSD Style Files Outside Designer

In addition to editing the styles (style groups) in the Style Editor of Designer, you can also edit the XSD format styles (style groups) outside Designer.

When you save a catalog, Designer saves the style information to disk at the same time. Designer stores the related files as follows:

| File Name | File Description | Location |
| --- | --- | --- |
| CatalogName\_stl.xml | Style Group Structure in the Catalog | Catalog Folder (The directory where the catalog resides) |
| StyleGroupName\_stl.xsd | Group/Style information | `<install_root>\style` |

The file "CatalogName\_stl.xml" keeps the style group structure information. The following shows an example:

| Style Group Structure in the Catalog Manager | Corresponding Information in SampleReports\_stl.xml |
| --- | --- |
| Style Group Structure in Catalog Manager | `<?xml version="1.0" encoding="UTF-8"?>  <StyleGroup>  <StyleGroupname="Default">  </StyleGroup>  <StyleGroup name="ClassicBlue">  </StyleGroup>  <StyleGroup name="ClassicGreen">  </StyleGroup>  </StyleGroup>` |

The file "StyleGroupName\_stl.xsd" keeps the group/style information, which in the above sample is as follows:

| File Content of ClassicBlue\_stl.xsd |
| --- |
| Style Information |

As you can see in the above code sample, an XML style group file contains style group information, style information, and the style property entry information. You can edit the attributes of an element.

* To add a style entry, copy and paste the style information section, and then modify the attributes.
* To add a style property entry, copy and paste any element line, and then modify the attributes.
* To delete a style entry or style property entry, select the corresponding section, and delete it.
* To add a new style group, follow the steps below:
  1. Copy and paste an existing XML style group file.
  2. Rename it using the required name (Format: GroupName \_stl.xsd).
  3. Change the default attribute in the **GroupName** element line using the required group name. Make sure that the name is the same as the group name specified in the XML style group file name.
  4. Add a new line for this group in **CatalogName\_stl.xml**. For example, if the new group name is GroupA, you would then insert the following line to the file:

     `<StyleGroup name="GroupA"></StyleGroup>`
  5. Modify the XML style group file (GroupName\_stl.xsd).
  6. Open the catalog in Designer and you can see the changes.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg)

* The value you type for the default attribute must be consistent with other attributes in the element, and is recognized by Designer.

  For example, if you want to change the Font Face property, you must type a proper font name that Logi Report supports for the default attribute, such as Arial, Times New Roman, and Tahoma. You cannot type strings that Logi Report cannot recognize; otherwise, the element cannot take effect at runtime.
* Make sure that the GroupName attribute is consistent with the XML style group file name.

  For example, with GroupA in the XML file, the GroupName attribute is:

  `<xs:attribute name="GroupName" type="xs:string" default="GroupA"></xs:attribute>`

  The XML style group file name should then be GroupA\_stl.xsd.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010101441-Creating-and-Applying-Styles)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010062822-Working-with-CSS-Styles)
