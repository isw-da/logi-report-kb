---
title: "Standard Way of Report Creation Using Wizard"
id: 1500009675141
section: "Web Report Studio Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009675141-Standard-Way-of-Report-Creation-Using-Wizard
updated_at: 2021-07-24T20:53:37Z
---

# Standard Way of Report Creation Using Wizard

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009675381-Quick-Start-with-a-Table-Report)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009675341-Web-Report-Studio-Window-Elements)

# Standard Way of Report Creation Using Wizard

When Web Report Studio is in the [standard way](https://devnet.logianalytics.com/hc/en-us/articles/1500009675101-Web-Report-Studio#Way), you can create web reports using the wizard.

1. Choose an entry to open the Web Report Wizard:
   * On the [Logi JReport Server Start Page](https://devnet.logianalytics.com/hc/en-us/articles/1500009648602-Accessing-Logi-JReport-Server-Guide-v15-Server-via-a-Web-Browser#Local), select **Web Reports** in the Create category. Next specify a folder and a catalog in the folder.
   * On the Logi JReport Console > Resources page, browse to a folder that contains catalogs, select the catalog for the new web report from the Catalog drop-down list, and then select **New** > **Web Report** on the task bar.
   * In Web Report Studio, select **File** > **New Report** or the **New Report** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920357527/btn_newobj.gif) on the toolbar.

   The [Web Report Wizard](https://devnet.logianalytics.com/hc/en-us/articles/1500009648042-Web-Report-Wizard) appears.
2. In the Page screen, choose a template for the report. The built-in templates contain information about Jinfonet. You can customize them to meet your own requirement. Use ![](https://devnet.logianalytics.com/hc/article_attachments/4404920402327/btn_chsr2_29x20.gif) to load your company logo. Edit the text and set the font properties for company titles and report titles using ![](https://devnet.logianalytics.com/hc/article_attachments/4404920373527/btn_wbrpt_font.gif). Select the **Page Setup** link to set the [page properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009672341-Page-Setup). If you are an administrator with the privilege of publishing resources, you can also [create a new template](#Template) to save your customization.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404920402583/wbrptwzd_page.gif)
3. In the Layout screen, select the required layout with which you want to create the report. Then, in the edit layout area, select a tabular cell and select the component you want to display in the cell. Select the **Align** drop-down list to set the component to the left, center or right of the cell. Repeat this to add component to the other cells.

   If required, you can split the selected cell horizontally or vertically by selecting the **Horizontal Split** or **Vertical Split** button, merge adjacent cells by selecting them and selecting **Merge**. You can also resize the tabular cells by dragging the cell border.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404920402839/wbrptwzd_layout.gif)
4. In the Bind Data screen, define the specified components (for details about how to define a component, refer to the specific topic in [Inserting Components](https://devnet.logianalytics.com/hc/en-us/articles/1500009675221-Inserting-Components)).
   You can use the Back and Next buttons to switch between the components.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404920403095/wbrptwzd_bnddt_table.gif)
5. In the Style screen, apply a style to the report.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404920403607/wbrptwzd_style.gif)
6. Select **Save** to save the report to the server resource tree. For details, see [Saving the Report](https://devnet.logianalytics.com/hc/en-us/articles/1500009650362-Saving-the-Report).
7. Select **Run**. If any parameter is used in the report, the [Report Parameters](https://devnet.logianalytics.com/hc/en-us/articles/1500009647742-Report-Parameters) dialog appears for you to specify the parameter value, then the report is opened in Web Report Studio.

You can also use URL command to directly open the Web Report Wizard to [create a web report via standard wizard way](https://devnet.logianalytics.com/hc/en-us/articles/1500009650402-Creating-Reports#Web).

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Web Report Templates

When creating web reports using the Web Report Wizard, you need to choose a starting template. A web report template stores information on the header and footer as a starting point for a web report. If you are an administrator with the privilege of publishing resources, you can save report templates to include standard features such as a company logo, company name, privacy notices or any standard items and styles you want your users to start with.

The saved report templates will be added into `<install_root>\templates` of Logi JReport Server, and will be automatically loaded onto the Page screen of the Web Report Wizard for use.

### Creating Web Report Templates

**To create a report template by customizing the built-in templates in the Web Report Wizard:**

The Web Report Wizard provides sample templates for you to define your own templates based on.

1. In the Page screen of the Web Report Wizard, make use of Template1 or Template2 to customize your own report templates. With Template1, you can add your company logo and report title. With Template2, you can add more items such as company name and title and report sub title. Use ![](https://devnet.logianalytics.com/hc/article_attachments/4404920370839/btn_chsr2.gif) to load your company logo. You can set the font properties for company titles and report titles using ![](https://devnet.logianalytics.com/hc/article_attachments/4404920373527/btn_wbrpt_font.gif).
2. Select the **Save** button.
3. In the Save As dialog, choose the file type of **Web Report Template (\*.wsld)**, specify a name for the template in the File Name text field, then select **Save** to save the template.

**To create a report template by editing a report in Web Report Studio:**

1. Open a report in Web Report Studio.
2. Edit the header and footer of the report.

   The report header and footer are composed by two tabulars. You can split or merge the tabular cells by selecting the button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920363287/btn_wbrpt_split.gif) or ![](https://devnet.logianalytics.com/hc/article_attachments/4404920363031/btn_wbrpt_merge.gif) on the toolbar, then add objects from the Components panel into the tabular cells and format them to customize the header and footer.
3. Select **Menu** > **File** > **Save As** or the **Save As** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920358039/btn_saveas.gif) on the toolbar.
4. In the Save As dialog, choose the file type **Web Report Template (\*.wsld)**, specify a name for the template in the File Name text field, then select **Save** to save the template.

### Dynamically Displaying the Company Logo

If the web report template used for creating a report contains company logo, you can make the logo display dynamically.

1. Select the company logo image in the report and then do either of the following:
   * Right-select the image and select **Properties** from the shortcut menu to display the [Image Properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009647522-Image-Properties) dialog, then select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920382743/btn_wbrpt_fmla.gif) next to the Image Name option.
   * Select **Menu** > **View** > **Inspector** to display the Inspector panel, then in the Properties sheet select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920382743/btn_wbrpt_fmla.gif) in the value cell of the Image Name property.
2. Do either of the following to change the image name.
   * Select a formula that returns an image source from the drop-down list. By default, there will be no formula available in the list. If you want to use a formula to control the image source, you need to first bind a data source to the web report, then create formulas that return image sources in the Resources panel. For details, refer to [Using formulas to control showing or hiding components](https://devnet.logianalytics.com/hc/en-us/articles/1500009675241-Making-Simple-Modifications-to-Components#Formula).
   * Select **<Edit Expression>** from the drop-down list to open the [Formula Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500009671841-Formula-Editor) and edit an expression to control the image source.  
       
     Logi JReport provides a built-in parameter named JRS\_P\_LOGOURL, which enables you to specify the image path easily. You can enter return *@JRS\_P\_LOGOURL;* directly in the editing box of the Formula Editor to create the expression.
3. If you are in the Image Properties dialog, select **OK** to accept the change.

   If the specified formula or expression returns an image, the image is changed. If the specified formula or expression uses parameters, the parameters are added to the [Parameters panel](https://devnet.logianalytics.com/hc/en-us/articles/1500009650342-Applying-Parameters#Panel). You can specify the parameter values in the panel to dynamically change the image.

If you are an administrator with the privilege of publishing resources, you can then select **Menu** > **File** > **Save As** or the **Save As** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920358039/btn_saveas.gif) on the toolbar to save the template as a new one for future use. However, if the company logo of a template is controlled by a formula, later when users use this template to create web reports, the web reports might not be created successfully, so Logi JReport provides [an option](https://devnet.logianalytics.com/hc/en-us/articles/1500009675361-Customizing-Web-Report-Studio-Profile#Template) in the Web Report Studio profile for you to determine what you want Logi JReport to do in this case.

### Renaming/Removing a Web Report Template

To rename or remove a web report template, go to `<install_root>\templates` on your server, then rename or delete the template file (.wsld). For each template file, there is an image file (.wsld.png) which is used to display in the templates box of the Page screen of the Web Report Wizard, as a representative of the template. You need to rename or delete the image file at the same time when you rename or delete the template file.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009675381-Quick-Start-with-a-Table-Report)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009675341-Web-Report-Studio-Window-Elements)
