---
title: "Creating Web Reports Using Wizard"
id: 1500009724682
section: "Web and Page Report Studio and Dashboard Logi Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009724682-Creating-Web-Reports-Using-Wizard
updated_at: 2021-07-25T07:18:35Z
---

# Creating Web Reports Using Wizard

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009751621-Quick-Start-with-a-Table-Report)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009751601-Web-Report-Studio-Window-Elements)

# Creating Web Reports Using Wizard

When Web Report Studio is in the [traditional way](https://devnet.logianalytics.com/hc/en-us/articles/1500009724642-Web-Report-Studio#Way), you can create web reports using the wizard.

1. Choose an entry to open the Web Report Wizard:
   * In the [Logi Report Server Start Page](https://devnet.logianalytics.com/hc/en-us/articles/1500009749881-Accessing-Logi-Report-Server-via-a-Web-Browser#Start), select **Web Report** in the Create category. In the displayed page, specify the folder in which to create the report, then the catalog that contains the required business view. Select **OK**.
   * In the Logi Report Server console, go to the Resources page, then:
     + Select **New** > **Web Report** on the task bar. In the displayed page, specify the folder in which to create the report, then the catalog that contains the required business view. Select **OK**.
     + Open a folder that contains catalogs, select the catalog for the new report from the Catalog drop-down list, and then select **New** > **Web Report** on the task bar.
   * In Web Report Studio, select **File** > **New Report** or the **New Report** button ![New Report button](https://devnet.logianalytics.com/hc/article_attachments/4404936714519/btn_newobj.gif) on the toolbar.

   The [Web Report Wizard](https://devnet.logianalytics.com/hc/en-us/articles/1500009722522-Web-Report-Wizard) appears.
2. In the Page screen, choose a template for the report. The built-in templates contain information about Jinfonet. You can customize them to meet your own requirement. Use ![Insert Image](https://devnet.logianalytics.com/hc/article_attachments/4404942451479/btn_chsr2.gif) to load your company logo. Edit the text and set the font properties for company titles and report titles using ![Font button](https://devnet.logianalytics.com/hc/article_attachments/4404942454679/btn_wbrpt_font.gif). Select the **Page Setup** link to set the [page properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009749201-Page-Setup). If you are an administrator with the privilege of publishing resources, you can also [create a new template](#Template) to save your customization.

   ![Web Report Wizard - Page screen](https://devnet.logianalytics.com/hc/article_attachments/4404936751639/wbrptwzd_page.gif)
3. In the Layout screen, select the required layout with which you want to arrange the components in the report, then in the editing layout box select the **Click here to select component** link and select a component type in each cell. You can split a selected cell horizontally or vertically using the Horizontal Split or Vertical Split button, and merge adjacent cells by selecting them and using the Merge button. You can also resize the cells by dragging the cell border.

   By default the built-in layouts are only used to determine the absolute positions of the components in the report. If you want to use a tabular to arrange the components in the report which can provide more precise layout functionality, select the **Use Tabular** check box. When a layout applies a tabular, you can select a cell and use the Align drop-down list to adjust the position of the component in the cell: Left, Center or Right.

   ![Web Report Wizard - Layout screen](https://devnet.logianalytics.com/hc/article_attachments/4404936752151/wbrptwzd_layout.gif)
4. In the Bind Data screen, define the specified components (for details about how to define a table, crosstab, chart or banded object, refer to the specific topic in [Inserting Components](https://devnet.logianalytics.com/hc/en-us/articles/1500009751501-Inserting-Components). You can create [dynamic resources](https://devnet.logianalytics.com/hc/en-us/articles/1500009751461-Using-Dynamic-Resources-and-Local-Parameters-) and use them in the component. To switch between the components, make use of the Back and Next buttons.

   ![Web Report Wizard - Bind Data screen](https://devnet.logianalytics.com/hc/article_attachments/4404936752407/wbrptwzd_bnddt_table.gif)
5. In the Style screen, apply a style to the report.

   ![Web Report Wizard - Style screen](https://devnet.logianalytics.com/hc/article_attachments/4404942469527/wbrptwzd_style.gif)
6. Select **Save** to save the report to the server resource tree. For details, see [Saving the Report](https://devnet.logianalytics.com/hc/en-us/articles/1500009751541-Saving-the-Report).
7. Select **Run**. If any parameter is used in the report, Report Server displays the [Enter Parameter Values](https://devnet.logianalytics.com/hc/en-us/articles/1500009748321-Enter-Parameter-Values) dialog box for you to specify the parameter value, then the report is opened in Web Report Studio.

You can also use URL command to directly open the Web Report Wizard to [create a web report via standard wizard way](https://devnet.logianalytics.com/hc/en-us/articles/1500009751681-Creating-Reports#Web).

## Web Report Templates

When creating web reports using the Web Report Wizard, you need to choose a starting template. A web report template stores information on the header and footer as a starting point for a web report. If you are an administrator with the privilege of publishing resources, you can save report templates to include standard features such as a company logo, company name, privacy notices or any standard items and styles you want your users to start with.

The saved report templates will be added into `<install_root>\templates` of Logi Report Server, and will be automatically loaded onto the Page screen of the Web Report Wizard for use.

### Creating Web Report Templates

**To create a report template by customizing the built-in templates in the Web Report Wizard:**

The Web Report Wizard provides sample templates for you to define your own templates based on.

1. In the Page screen of the Web Report Wizard, make use of Template1 or Template2 to customize your own report templates. With Template1, you can add your company logo and report title. With Template2, you can add more items such as company name and title and report sub title. Use ![Insert Image](https://devnet.logianalytics.com/hc/article_attachments/4404942451479/btn_chsr2.gif) to load your company logo. You can set the font properties for company titles and report titles using ![Font button](https://devnet.logianalytics.com/hc/article_attachments/4404942454679/btn_wbrpt_font.gif).
2. Select the **Save** button.
3. In the Save As dialog box, choose the file type of **Web Report Template (\*.wsld)**, specify a name for the template in the File Name text box, then select **Save** to save the template.

**To create a report template by editing a report in Web Report Studio:**

1. Open a report in Web Report Studio.
2. Edit the header and footer of the report.

   The report header and footer are composed by two tabulars. You can split or merge the tabular cells by selecting the button ![Split button](https://devnet.logianalytics.com/hc/article_attachments/4404942447895/btn_wbrpt_split.gif) or ![Merge button](https://devnet.logianalytics.com/hc/article_attachments/4404942447639/btn_wbrpt_merge.gif) on the toolbar, then add objects from the Components panel into the tabular cells and format them to customize the header and footer.
3. Select **Menu** > **File** > **Save As** or the **Save As** button ![Save As button](https://devnet.logianalytics.com/hc/article_attachments/4404936715031/btn_saveas.gif) on the toolbar.
4. In the Save As dialog box, choose the file type **Web Report Template (\*.wsld)**, specify a name for the template in the File Name text box, then select **Save** to save the template.

### Dynamically Displaying the Company Logo

If the web report template used for creating a report contains company logo, you can make the logo display dynamically.

1. Select the company logo image in the report and then do either of the following:
   * Right-click the image and select **Properties** from the shortcut menu to display the [Image Properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009748861-Image-Properties) dialog box, then select ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404936732951/btn_wbrpt_fmla.gif) next to the Image Name option.
   * Select **Menu** > **View** > **Inspector** to display the Inspector panel, then in the Properties sheet select ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404936732951/btn_wbrpt_fmla.gif) in the value cell of the Image Name property.
2. Do either of the following to change the image name.
   * Select a formula that returns an image source from the drop-down list. By default, there will be no formula available in the list. If you want to use a formula to control the image source, you need to first bind a data source to the web report, then create formulas that return image sources in the Resources panel. For details, refer to [Using formulas to control showing or hiding components](https://devnet.logianalytics.com/hc/en-us/articles/1500009751521-Making-Simple-Modifications-to-Components#Formula).
   * Select **<Edit Expression>** from the drop-down list to open the [Formula Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500009748461-Formula-Editor) and edit an expression to control the image source.  

     Web Report Studio provides a built-in parameter named JRS\_P\_LOGOURL, which enables you to specify the image path easily. You can type *return @JRS\_P\_LOGOURL;* directly in the editing box of the Formula Editor to create the expression.
3. If you are in the Image Properties dialog box, select **OK** to accept the change.

   If the specified formula or expression returns an image, the image is changed. If the specified formula or expression uses parameters, the parameters are added to the [Parameters panel](https://devnet.logianalytics.com/hc/en-us/articles/1500009724862-Applying-Parameters). You can specify the parameter values in the panel to dynamically change the image.

If you are an administrator with the privilege of publishing resources, you can then select **Menu** > **File** > **Save As** or the **Save As** button ![Save As button](https://devnet.logianalytics.com/hc/article_attachments/4404936715031/btn_saveas.gif) on the toolbar to save the template as a new one for future use. However, if the company logo of a template is controlled by a formula, later when users use this template to create web reports, the web reports might not be created successfully, so Logi Report provides an option [**When web report template cannot work properly** Logi Report **should**](https://devnet.logianalytics.com/hc/en-us/articles/1500009724902-Customizing-Web-Report-Studio-Profile#Template) in the Web Report Studio profile for you to determine what you want Logi Report to do in this case.

### Renaming/Removing a Web Report Template

To rename or remove a web report template, go to `<install_root>\templates` on your server, then rename or delete the template file (.wsld). For each template file, there is an image file (.wsld.png) which is used to display in the templates box of the Page screen of the Web Report Wizard, as a representative of the template. You need to rename or delete the image file at the same time when you rename or delete the template file.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009751621-Quick-Start-with-a-Table-Report)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009751601-Web-Report-Studio-Window-Elements)
