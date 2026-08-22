---
title: "Creating Web Reports Using the Wizard"
id: 4405690684439
section: "Web Report Studio Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405690684439-Creating-Web-Reports-Using-the-Wizard
updated_at: 2022-01-27T07:59:52Z
---

# Creating Web Reports Using the Wizard

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690690711-Quick-Start-with-a-Table-Report)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405684047895-Creating-and-Using-Web-Report-Page-Templates)

# Creating Web Reports Using the Wizard

When you use the [traditional method](https://devnet.logianalytics.com/hc/en-us/articles/4405684031639-Web-Report-Studio-Server-v18#Way), you can create complex web reports with multiple components in a tabular style layout using the [Web Report Wizard](https://devnet.logianalytics.com/hc/en-us/articles/4405690615447-Web-Report-Wizard-Properties). This topic describes how you can create web reports using the wizard.

1. Choose a way to open the Web Report Wizard:
   * In the [Start Page](https://devnet.logianalytics.com/hc/en-us/articles/4405690636055-Accessing-Logi-Report-Server-via-a-Web-Browser#Start) of the Server Console, select **Web Report** in the **Create** category. Server displays a page. Select the folder in which you want to create the report, then the catalog that contains the required business view. Select **OK**.
   * On the Server Console, go to the **Resources** page, then:
     + Select **New** > **Web Report** on the task bar. Server displays a page. Select the folder in which to create the report, then the catalog that contains the required business view. Select **OK**.
     + Open a folder that contains catalogs, select a catalog for the new report from the **Catalog** button ![Catalog button](https://devnet.logianalytics.com/hc/article_attachments/4420447095191/btn_srv_catalog.gif) drop-down list, and then select **New** > **Web Report** on the task bar.
   * In the Web Report Studio, select **Menu** > **File** > **New Report** or the **New Report** button ![New Report button](https://devnet.logianalytics.com/hc/article_attachments/4420447051799/btn_newobj.gif) on the toolbar.

   Server displays the [Web Report Wizard](https://devnet.logianalytics.com/hc/en-us/articles/4405690615447-Web-Report-Wizard-Properties).
2. In the **Page** screen, choose a [page template](https://devnet.logianalytics.com/hc/en-us/articles/4405684047895-Creating-and-Using-Web-Report-Page-Templates) for the report. The built-in page templates contain information about Logi. You can customize the selected template as you want.

   ![Web Report Wizard - Page screen](https://devnet.logianalytics.com/hc/article_attachments/4420447095447/wbrptwzd_page.gif)
3. Select the ellipsis button ![Insert Image](https://devnet.logianalytics.com/hc/article_attachments/4420453393175/btn_chsr2.gif) to load your company logo.
4. Edit the text of the titles
5. Set the font properties for the titles using ![Font button](https://devnet.logianalytics.com/hc/article_attachments/4420461453847/btn_wbrpt_font.gif).
6. Select **Page Setup** if you want to set the [page properties](https://devnet.logianalytics.com/hc/en-us/articles/4405683867543-Page-Setup-Dialog-Box-Properties).

   If you are an administrator with the privilege of publishing resources, you can also [create a new page template](https://devnet.logianalytics.com/hc/en-us/articles/4405684047895-Creating-and-Using-Web-Report-Page-Templates) to save your customization.
7. Select **Next**.
8. In the **Layout** screen, select the layout with which you want to arrange the components in the report.

   ![Web Report Wizard - Layout screen](https://devnet.logianalytics.com/hc/article_attachments/4420461515543/wbrptwzd_layout.gif)
9. In the editing layout box, you can split a selected cell horizontally or vertically using the **Horizontal Split** or **Vertical Split** button, and merge adjacent cells by selecting them and using the **Merge** button.
10. Select **Click here to select component** and then choose a component type in each cell.
11. You can resize the cells by dragging the cell border.
12. By default, the built-in layouts only determine the absolute position of the components in the report. If you want to use a tabular to arrange the components in the report for more precise layout functionality, select **Use Tabular**. When you do this, you can further adjust the component position in a cell from left to center or right: select the cell, then select an item from the **Align** drop-down list.
13. Select **Next**.
14. In the **Bind Data** screen, define the specified components. For more information, see [Inserting Components in Web Report](https://devnet.logianalytics.com/hc/en-us/articles/4405684040855-Inserting-Components-in-Web-Report). You can create and use [dynamic resources](https://devnet.logianalytics.com/hc/en-us/articles/4405684037271-Using-Dynamic-Resources-and-Local-Parameters-in-Web-Report-) in the components. To switch between the components, make use of the **Back** and **Next** buttons.

    ![Web Report Wizard - Bind Data screen](https://devnet.logianalytics.com/hc/article_attachments/4420447096727/wbrptwzd_bnddt_table.gif)
15. In the **Style** screen, select a style you want to apply to the report.

    ![Web Report Wizard - Style screen](https://devnet.logianalytics.com/hc/article_attachments/4420461515927/wbrptwzd_style.gif)
16. Select **Save** if you want to save the report to the server resource tree. For more information, see [Saving a Web Report](https://devnet.logianalytics.com/hc/en-us/articles/4405684044439-Saving-a-Web-Report).
17. Select **Run** to run the report. If the report uses any parameter, Server displays the [Enter Parameter Values](https://devnet.logianalytics.com/hc/en-us/articles/4405683814423-Enter-Parameter-Values-Dialog-Box-Properties) dialog box for you to specify the parameter value, and then opens the report in Web Report Studio.

You can also use URL command to directly open the Web Report Wizard to [create a web report using the wizard](https://devnet.logianalytics.com/hc/en-us/articles/4405684052759-Creating-Reports-via-URL#Web).

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690690711-Quick-Start-with-a-Table-Report)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405684047895-Creating-and-Using-Web-Report-Page-Templates)
