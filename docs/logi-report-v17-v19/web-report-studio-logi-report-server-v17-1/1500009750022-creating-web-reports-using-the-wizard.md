---
title: "Creating Web Reports Using the Wizard"
id: 1500009750022
section: "Web Report Studio Logi Report Server v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009750022-Creating-Web-Reports-Using-the-Wizard
updated_at: 2021-07-24T00:47:32Z
---

# Creating Web Reports Using the Wizard

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009778861-Quick-Start-with-a-Table-Report)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009778841-Web-Report-Studio-Window-Elements)

# Creating Web Reports Using the Wizard

When you use the Web Report Studio in the [traditional way](https://devnet.logianalytics.com/hc/en-us/articles/1500009778701-Web-Report-Studio#Way), you can create web reports using the wizard. This topic describes how you can create web reports using Web Report Wizard and customize web report page templates.

1. Choose an entry to open the Web Report Wizard:
   * In the [Start Page](https://devnet.logianalytics.com/hc/en-us/articles/1500009777061-Accessing-Logi-Report-Server-via-a-Web-Browser#Start) of the Server Console, select **Web Report** in the **Create** category. Server displays a page. Select the folder in which to create the report, then the catalog that contains the required business view. Select **OK**.
   * In the Server Console, go to the **Resources** page, then:
     + Select **New** > **Web Report** on the task bar. Server displays a page. Select the folder in which to create the report, then the catalog that contains the required business view. Select **OK**.
     + Open a folder that contains catalogs, select the catalog for the new report from the **Catalog** drop-down list, and then select **New** > **Web Report** on the task bar.
   * In Web Report Studio, select **File** > **New Report** or the **New Report** button ![New Report button](https://devnet.logianalytics.com/hc/article_attachments/4404885307031/btn_newobj.gif) on the toolbar.

   Server displays the [Web Report Wizard](https://devnet.logianalytics.com/hc/en-us/articles/1500009776601-Web-Report-Wizard-Properties).
2. In the **Page** screen, choose a page template for the report. The built-in templates contain information about Logi. You can customize them to meet your own requirement.

   ![Web Report Wizard - Page screen](https://devnet.logianalytics.com/hc/article_attachments/4404880197655/wbrptwzd_page.gif)
3. Use ![Insert Image](https://devnet.logianalytics.com/hc/article_attachments/4404880145687/btn_chsr2.gif) to load your company logo.
4. Edit the text and set the font properties for company titles and report titles using ![Font button](https://devnet.logianalytics.com/hc/article_attachments/4404885319959/btn_wbrpt_font.gif).
5. Select **Page Setup** to set the [page properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009747842-Page-Setup-Dialog-Box-Properties). If you are an administrator with the privilege of publishing resources, you can also [create a new page template](#Template) to save your customization.
6. In the **Layout** screen, select the layout with which you want to arrange the components in the report,

   ![Web Report Wizard - Layout screen](https://devnet.logianalytics.com/hc/article_attachments/4404885344407/wbrptwzd_layout.gif)
7. In the editing layout box, select **Click here to select component** and select a component type in each cell.
8. You can split a selected cell horizontally or vertically using the **Horizontal Split** or **Vertical Split** button, and merge adjacent cells by selecting them and using the **Merge** button.
9. You can also resize the cells by dragging the cell border.
10. By default, the built-in layouts are only used to determine the absolute positions of the components in the report. If you want to use a tabular to arrange the components in the report which can provide more precise layout functionality, select the **Use Tabular** check box. When a layout applies a tabular, you can select a cell and use the **Align** drop-down list to adjust the position of the component in the cell: Left, Center, or Right.
11. In the **Bind Data** screen, define the specified components. For more information, see [Inserting Components in Web Report](https://devnet.logianalytics.com/hc/en-us/articles/1500009750122-Inserting-Components-in-Web-Report). You can create and use [dynamic resources](https://devnet.logianalytics.com/hc/en-us/articles/1500009750082-Using-Dynamic-Resources-and-Local-Parameters-in-Web-Report-) in the component. To switch between the components, make use of the **Back** and **Next** buttons.

    ![Web Report Wizard - Bind Data screen](https://devnet.logianalytics.com/hc/article_attachments/4404880198039/wbrptwzd_bnddt_table.gif)
12. In the **Style** screen, apply a style to the report.

    ![Web Report Wizard - Style screen](https://devnet.logianalytics.com/hc/article_attachments/4404880198295/wbrptwzd_style.gif)
13. Select **Save** to save the report to the server resource tree. For more information, see [Saving a Web Report](https://devnet.logianalytics.com/hc/en-us/articles/1500009750182-Saving-a-Web-Report).
14. Select **Run**. If the report uses any parameter, Server displays the [Enter Parameter Values](https://devnet.logianalytics.com/hc/en-us/articles/1500009775221-Enter-Parameter-Values-Dialog-Box-Properties) dialog box for you to specify the parameter value and then opens the report in Web Report Studio.

You can also use URL command to directly open the Web Report Wizard to [create a web report in the traditional wizard way](https://devnet.logianalytics.com/hc/en-us/articles/1500009750322-Creating-Reports-via-URL#Web).

## Web Report Page Templates

When creating web reports using the Web Report Wizard, you need to choose a starting page template. A web report page template stores information on the header and footer as a starting point for a web report. If you are an administrator with the privilege of publishing resources, you can save page templates to include standard features such as a company logo, company name, privacy notices, or any standard items and styles you want your people to start with.

Logi Report Server adds the page templates that you saved into `<install_root>\templates`, and automatically loads them onto the Page screen of the Web Report Wizard for use.

### Creating Web Report Page Templates

**To create a page template by customizing the built-in templates in the Web Report Wizard:**

The Web Report Wizard provides sample page templates for you to define your own templates based on.

1. In the Page screen of the Web Report Wizard, make use of **Template1** or **Template2** to customize your own report templates. With Template1, you can add your company logo and report title. With Template2, you can add more items such as company name, title, and report subtitle. Use ![Insert Image](https://devnet.logianalytics.com/hc/article_attachments/4404880145687/btn_chsr2.gif) to load your company logo. You can set the font properties for company titles and report titles using ![Font button](https://devnet.logianalytics.com/hc/article_attachments/4404885319959/btn_wbrpt_font.gif).
2. Select the **Save** button. Server displays the Save As dialog box.
3. Choose the file type of **Web Report Template (\*.wsld).**
4. Type a name for the template in the **File Name** text box.
5. Select **Save** to save the template.

**To create a page template by editing a report in Web Report Studio:**

1. Open a report in Web Report Studio.
2. Edit the header and footer of the report.
   The report header and footer are composed by two tabulars. You can split or merge the tabular cells by selecting the button ![Split button](https://devnet.logianalytics.com/hc/article_attachments/4404885310615/btn_wbrpt_split.gif) or ![Merge button](https://devnet.logianalytics.com/hc/article_attachments/4404880140567/btn_wbrpt_merge.gif) on the toolbar, then add objects from the **Components** panel into the tabular cells and format them to customize the header and footer.
3. Select **Menu** > **File** > **Save As** or the **Save As** button ![Save As button](https://devnet.logianalytics.com/hc/article_attachments/4404880136727/btn_saveas.gif) on the toolbar. Server displays the Save As dialog box.
4. Choose the file type **Web Report Template (\*.wsld)**.
5. Type a name for the template in the **File Name** text box.
6. Select **Save** to save the template.

### Dynamically Displaying the Company Logo

If the web report page template used for creating a report contains a company logo, you can make the logo display dynamically.

1. Select the company logo image in the report and then do either of the following:
   * Right-click the image and select **Properties** from the shortcut menu. Server displays the [Image Properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009775901-Image-Properties) dialog box. Select ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404880159895/btn_wbrpt_fmla.gif) next to the **Image Name** option.
   * Select **Menu** > **View** > **Inspector**. Server displays the **Inspector** panel. In the Properties sheet select ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404880159895/btn_wbrpt_fmla.gif) in the value cell of the **Image Name** property.
2. Do either of the following to change the image name.
   * Select a formula that returns an image source from the drop-down list. By default, there is no formula available in the list. If you want to use a formula to control the image source, you need to first bind a data source to the web report, then create a formula in the Resources panel to return an image source. For more information, see [Using formulas to control showing or hiding components](https://devnet.logianalytics.com/hc/en-us/articles/1500009778821-Making-Simple-Modifications-to-Web-Report-Components#Formula).
   * Select **<Edit Expression>** from the drop-down list to open the [Formula Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500009775341-Formula-Editor-Properties) and edit an expression to control the image source.  

     Web Report Studio provides a built-in parameter named JRS\_P\_LOGOURL, which enables you to specify the image path easily. You can type *return @JRS\_P\_LOGOURL;* directly in the editing box of the Formula Editor to create the expression.
3. If you are in the Image Properties dialog box, select **OK** to accept the change.

   If the specified formula or expression uses parameters, Server adds the parameters to the [Parameters panel](https://devnet.logianalytics.com/hc/en-us/articles/1500009750162-Applying-Parameters-to-Web-Report). You can specify the parameter values in the panel to dynamically change the image.

If you are an administrator with the privilege of publishing resources, you can then select **Menu** > **File** > **Save As** or the **Save As** button ![Save As button](https://devnet.logianalytics.com/hc/article_attachments/4404880136727/btn_saveas.gif) on the toolbar to save the page template as a new one for future use. However, if you control the company logo of a page template by a formula, later when you use this template to create web reports, the web reports might not be created successfully, so Logi Report provides an option [**When web report template cannot work properly** Logi Report **should**](https://devnet.logianalytics.com/hc/en-us/articles/1500009750242-Customizing-Web-Report-Studio-Profile#Template) in the Web Report Studio profile for you to determine what you want Logi Report to do in this case.

### Renaming/Removing a Web Report Page Template

To rename or remove a web report page template, go to `<install_root>\templates` on your server, then rename or delete the template file (.wsld). For each template file, there is an image file (.wsld.png) which is used to display in the templates box of the Page screen of the Web Report Wizard, as a representative of the template. You need to rename or delete the image file at the same time when you rename or delete the template file.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009778861-Quick-Start-with-a-Table-Report)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009778841-Web-Report-Studio-Window-Elements)
