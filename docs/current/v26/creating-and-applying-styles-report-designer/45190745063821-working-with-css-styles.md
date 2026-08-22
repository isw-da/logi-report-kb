---
title: "Working with CSS Styles"
id: 45190745063821
section: "Creating and Applying Styles - Report Designer"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45190745063821-Working-with-CSS-Styles
updated_at: 2026-04-30T15:16:10Z
source_host: logi-report-v26.insightsoftware.com
---
# Working with CSS Styles

Report CSS styles enable you to create various visual presentation sets from a single report, and change the visual presentation of your report. A CSS style file is like a style group, which contains a set of styles with many predefined properties. Report supports the CSS style file that is defined according to the W3C CSS 2.1 standard. You can control the properties of all the components in a report  by a CSS file. You can customize, edit, and save a CSS style with visible UI of the CSS Editor in Designer, and can also compile and save a CSS file manually according to the W3C standard. After that, you can import these CSS style files to apply to a component. This topic describes how you can create and manage CSS styles in Designer.

This topic contains the following sections:

- Creating CSS Styles

- Managing CSS Styles

## 
Creating CSS Styles

Report supports some of the W3C CSS 2.1 standard properties at present, which are background-color, border-style/border-top-style/border-bottom-style/border-left-style/border-right-style, color, font-size, height, padding/padding-top/padding-bottom/padding-left/padding-right, text-align, and width.

To create a CSS style in Designer

- Right-click an object in the design area and select Save Style from the shortcut menu. Designer displays the New CSS Style dialog box.
    

- 
Define the type of the CSS style.
    
- To create a custom style that you can apply as a class attribute to a range or block of text, select the Class option and type a name for the style in the Selector Name combo box.
           Class names must begin with a period and can contain any combination of letters and numbers (for example, .myhead1). If you do not type the beginning period, Designer automatically adds it for you.

- To redefine the default formatting of a specific tag, select the Tag option and then select a tag from the Selector Name combo box.

- To define the formatting for a particular combination of tags or for all tags that contain a specific ID attribute, select the Advanced option and then type one or more tags in the Selector Name combo box or select one from the box. If the object is in a crosstab, when you select this option, the following advanced selector names are available in the Selector Name drop-down list according to the current object name.

| Object Name | CSS Tag Name | Advanced Selector Name Example |
| --- | --- | --- |
| Aggregation Title | CrosstabLabelField | CrosstabLabelField[Depth=] |
| Aggregation Field | CrosstabAggregationField | CrosstabAggregationField[XDepth=][YDepth=] CrosstabAggregationField[XDepth=] CrosstabAggregationField[YDepth=] |
| Special Aggregation Field | CrosstabAggregationSpecialField | CrosstabAggregationSpecialField[XDepth=][YDepth=] CrosstabAggregationSpecialField[XDepth=] CrosstabAggregationSpecialField[YDepth=] |
| Label of Column/Row Field | CrosstabDBTitleField | CrosstabDBTitleField[Depth=][IsXHeader=] CrosstabDBTitleField[Depth=] CrosstabDBTitleField[IsXHeader=] |
| Column/Row Field | CrosstabDBField | CrosstabDBField[Depth=][IsXHeader=] CrosstabDBField[Depth=] CrosstabDBField[IsXHeader=] |
| Total Label | CrosstabTextField | CrosstabTextField[Depth=][IsXHeader=] CrosstabTextField[Depth=] CrosstabTextField[IsXHeader=] |

The following image illustrates the four selector attributes in a crosstab: Depth, XDepth, YDepth, and IsXHeader. IsXHeader is a Boolean type attribute which specifies whether it is a column header. 

The four attributes are not String in the crosstab definition, so Designer needs to convert them to String to meet the CSS definition, for example: 

- CrosstabTextField[Depth="1"]

- CrosstabTextField[IsXHeader="false"]

Depth, XDepth, and YDepth can use the JR-MAX dynamic value to represent the maximum value in the parallel-setting or summary area they belong to, for example, CrosstabTextField[Depth=JR-MAX]. In this case, Designer also lists the JR-MAX conditions  in the Selector Name drop-down list.

- From the Add Selector to Style drop-down list, select the location to define the style.
    
- If you want to create an external style file, select New Style Sheet File and select OK. Then,
          
- In the Save CSS As dialog box, specify the name of the new CSS file.
                

- Select Save to save the file. Designer then displays the CSS Style Definition dialog box.
              

- Add the properties you want to contain in the style, specify values for the properties, and select if the properties are important or not.

- Select Save to apply the settings.

- If you want to embed the style in an existing CSS file, select any of the existing styles and select OK. In the CSS Style Definition dialog box, define properties of the style and select Save to save the file.

 

## 
Managing CSS Styles

You can manage CSS styles using the CSS Editor dialog box in Designer. However, you might find it easier to use a third party CSS editor such as Dreamweaver that enables you to use all CSS classes at one time.

To access the CSS Editor dialog box, navigate to Home > CSS Editor.

You can perform the following management tasks in the CSS Editor dialog box:

- 
Creating a CSS style
- Select New.

- In the New CSS Style dialog box, define the style.

- 
Importing a CSS style
- Select Import.

- In the Import CSS File dialog box, select the CSS style you want to import and select Open.

 In the imported CSS styles, only the valid property names, which match with those in Designer, can take effect.

- 
Duplicating a CSS style
- Select the CSS style in the CSS File box.

- Select Duplicate.

- 
Exporting a CSS style
- In the CSS File box, select the CSS style you want to output.

- Select Export.

- In the Save As dialog box, specify the directory to locate the CSS style.

- Select Save to save the CSS style to the specified directory.

- 
Removing a CSS style
- Select the CSS style in the CSS File box.

- Select Remove to remove it.

- 
Editing the style sheets in a CSS style
- Select the CSS style  in the CSS File box. Designer lists all style sheets in the style file  in the Styles box.

-  Select the style sheet you want to edit and select Edit. 

- In the CSS Style Definition dialog box, edit properties for the style sheet.

- Select Save to accept the changes.

- 
Creating a style sheet in a CSS style
- In the CSS File box, select the CSS style to which you want to add new style sheet.

- Select New.

- If you have selected a built-in CSS style to add the style sheet, Designer displays a warning message. Make a choice.

- In the New CSS Style dialog box, specify the Selector Name and Selector Type of the style as seen earlier in this topic. Select OK.

- In the CSS Style Definition dialog box, define properties of the style sheet.

- Select Save to create the style sheet.

- 
Removing a style sheet from a CSS style
- Select the CSS style in the CSS File box.

- In the Styles box, select the style sheet you want to remove.

- Select Remove.
