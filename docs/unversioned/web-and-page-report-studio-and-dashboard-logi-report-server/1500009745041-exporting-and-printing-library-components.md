---
title: "Exporting and Printing Library Components"
id: 1500009745041
section: "Web and Page Report Studio and Dashboard Logi Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009745041-Exporting-and-Printing-Library-Components
updated_at: 2021-07-25T07:20:14Z
---

# Exporting and Printing Library Components

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009718942-Specifying-Parameter-Values-for-a-Dashboard)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009745121-Running-and-Editing-Reports-in-JDashboard)

# Exporting and Printing the Library Components in a Dashboard

Library components visible in the page panel can be exported and printed, for example, library components that were created using Logi Report Designer and inserted into dashboards via the Resources panel.

When you export or print the library components in a dashboard, you choose whether to use system layout or customize the layout by yourself. In the system layout, Logi Report will calculate the positions of the library components in the dashboard following defined rule. If you are not satisfied with the system layout, you can customize the layout by yourself to determine the position of each library component and specify whether to export or print all the data of a table/crosstab or just the current page of the table/crosstab displayed in the dashboard. The customized layout can be saved for all users who can access the dashboard.

Select the following links to view the topics:

* [Exporting the Library Components](#Export)
* [Printing the Library Components](#Print)

## Exporting the Library Components

To export the library components in a dashboard, select the **Export** button ![Export button](https://devnet.logianalytics.com/hc/article_attachments/4404936715287/btn_expt.gif) on the toolbar, or select the **Options** button ![Options button](https://devnet.logianalytics.com/hc/article_attachments/4404936890647/btn_dshbrd_optn.gif) on the toolbar and select **Export** from the option list to open the [Export](https://devnet.logianalytics.com/hc/en-us/articles/1500009720102-Export#Dashboard) dialog box, then:

### Exporting Using the System Layout

**To export using system layout:**

1. In the Export dialog box, the **System Layout** item is selected as the layout by default.

   ![Export dialog - System Layout](https://devnet.logianalytics.com/hc/article_attachments/4404936956055/expt_dshbd_sys.gif)

   JDashboard displays the preview of the layout in the preview panel on the right. Sometimes you may find that the layout is a little different from what you see in the dashboard.
2. In the Resources box, select the library components you want to export. By default all exportable library components are listed and selected.
3. The order of the library components in the Resources box determines the order in which they will be exported. You can select ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404936729239/btn_mvdown.gif) and ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404942457495/btn_mvup.gif) to adjust the exporting order.
4. Select the **Show Component Title** option if you want to show the library component titles in the exported result.
5. Select the page navigation buttons on the toolbar of the preview panel to browse the pages if you want.
6. Select the **Page Setup** button ![Page Setup button](https://devnet.logianalytics.com/hc/article_attachments/4404942570391/btn_dshbrd_pgstup.gif) on the toolbar to set the page properties of the exported result file such as page size and margins in the [Page Setup](https://devnet.logianalytics.com/hc/en-us/articles/1500009720222-Page-Setup#Export) dialog box. You can either define the page properties generally for all export formats or customize the page properties for each export format as you want.
7. Select ![Export button](https://devnet.logianalytics.com/hc/article_attachments/4404936715287/btn_expt.gif) to do the last setting and then export.
   1. From the Export File Format drop-down list, select the format to which the library components will be exported. For a format other than XML, all the selected library components will be exported into one single file. For XML, each library component will be exported to a separate XML file. When the exported result contains more than one file, all the files will be zipped.
   2. In the File Name text box, specify the name of the exported result file, which could be either a single file or a zipped package name.
   3. Select **Run Linked Report** if you need to include linked report in the exported result file.
   4. Select **OK** to start exporting.

### Exporting Using a Customized Layout

**To export using customized layout:**

1. In the Export dialog box, select **Customize Layout** from the Layout drop-down list. You can also select an existing customized layout to modify it.

   ![Export dialog - Customize Layout](https://devnet.logianalytics.com/hc/article_attachments/4404936900119/expt_dshbd.gif)
2. Select the **Show Component Title** option if you want to show the library component titles in the exported result.
3. Select the **Page Setup** button ![Page Setup button](https://devnet.logianalytics.com/hc/article_attachments/4404942570391/btn_dshbrd_pgstup.gif) on the toolbar to set the page properties of the exported result file such as page size and margins in the [Page Setup](https://devnet.logianalytics.com/hc/en-us/articles/1500009720222-Page-Setup#Export) dialog box.
4. In the Design tab, customize the layout of the library components by making use of the following operations.
   The library components are arranged using a tabular with each cell holding one component.
   * Split or merge cells using the toolbar options: **![Horizontal Split button](https://devnet.logianalytics.com/hc/article_attachments/4404942570135/btn_dshbrd_splth.gif)**, **![Merge button](https://devnet.logianalytics.com/hc/article_attachments/4404936893975/btn_dshbrd_merge.gif)**, and **![Vertical Split button](https://devnet.logianalytics.com/hc/article_attachments/4404936894231/btn_dshbrd_spltv.gif)**.
   * Drag a library component from the Resources box into a blank cell in the Design tab. A cell can hold only one library component.
   * Delete a library component from a tabular cell using the shortcut menu option **Remove**.
   * For a table or crosstab, only its current view of data as displayed in the dashboard will be exported by default. If you want its full data to be exported, right-click on the table or crosstab and select **Filter** from the drop-down list. Then in the Filter dialog box, switch from Current View to **All** and select **OK**.
5. Select the **View** tab to preview the layout. You can browse the pages and zoom in/out by selecting the corresponding toolbar buttons.

   If you are satisfied with the layout and want to save it for future use, select ![Save button](https://devnet.logianalytics.com/hc/article_attachments/4404942445847/btn_save.gif) or **![Save As button](https://devnet.logianalytics.com/hc/article_attachments/4404936715031/btn_saveas.gif)** on the toolbar, then in the Save As dialog box, provide a name for the layout and select **OK**. The saved customized layouts will be available in the Layout drop-down list to all users who can access the dashboard. For each of them, you can edit its name or delete it using the two buttons - Rename and Delete - appearing on the right when the mouse hovers over the layout item in the drop-down list.

   ![Layout Drop-down List](https://devnet.logianalytics.com/hc/article_attachments/4404936893719/dshbrd_expt_layout.gif)
6. Select**![Export button](https://devnet.logianalytics.com/hc/article_attachments/4404936715287/btn_expt.gif)**, then in the Export dialog box, [do the last setting and start exporting](#Export).

**Tip:** If you just want to export a single library component, there is a more convenient way.

1. Select ![Options Icon](https://devnet.logianalytics.com/hc/article_attachments/4404942444951/btn_dshbrd_more.gif) on the [component title bar](https://devnet.logianalytics.com/hc/en-us/articles/1500009745081-General-Operations-in-JDashboard#TitleBar) and select **Export** from the drop-down menu. Report Server displays the Export dialog box.

   ![Export dialog](https://devnet.logianalytics.com/hc/article_attachments/4404936899863/expt_lc.gif)
2. In the dialog box, choose the format to which you want to export the library component, then select **OK**.

However, using this way, if the library component is linked with other reports, you cannot control whether to generate the linked reports while exporting. The linked reports will not be included in the exported result.

## Printing the Library Components

To print the library components in a dashboard, select the ****Print**** button **![Print button](https://devnet.logianalytics.com/hc/article_attachments/4404936715543/btn_print.gif)** on the toolbar, or select the **Options** button ![Options button](https://devnet.logianalytics.com/hc/article_attachments/4404936890647/btn_dshbrd_optn.gif) on the toolbar and select **Print** from the option list to open the [Print](https://devnet.logianalytics.com/hc/en-us/articles/1500009746981-Print) dialog box, then:

**To print using system layout:**

1. In the Print dialog box, select **System Layout** from the Layout drop-down list.

   ![Print dialog - System Layout](https://devnet.logianalytics.com/hc/article_attachments/4404936956311/prnt_sys.gif)

   The preview of the layout appears in the preview panel on the right. Sometimes you may find that the layout is a little different from what you see in the dashboard.
2. In the Resources box, select the library components you want to print. By default all printable library components are listed and selected.
3. The order of the library components in the Resources box determines the order in which they will be printed. You can select ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404936729239/btn_mvdown.gif) and ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404942457495/btn_mvup.gif) to adjust the printing order.
4. Select the **Show Component Title** option if you want to show the library component titles in the printed result.
5. From the Printer drop-down list, select the printer to use to print the library component result. All the printers the web browser can access will be listed here. If you want to download the result to a PDF or HTML file and then use your local printer to print the file, select **Save as PDF** or **Save as HTML**.
6. If a printer is selected, select the **Properties** link to specify the printing properties in the [Printer Properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009720242-Printer-Properties) dialog box.
7. Define the number of copies you want to print accordingly.
8. Specify the page orientation and paper type for the printed result file. You can select the **More Settings**  link to set more page properties such as paper size and margins in the [Page Setup](https://devnet.logianalytics.com/hc/en-us/articles/1500009720222-Page-Setup#Print) dialog box.
9. Select the page navigation buttons on the toolbar of the preview panel to browse the pages if you want.
10. Select ![Print button](https://devnet.logianalytics.com/hc/article_attachments/4404936715543/btn_print.gif) on the toolbar to start printing. If Save as PDF or Save as HTML is selected in the Printer drop-down list, the result file of the library components is then opened in an associated program with which you can print the result to a printer.

**To print using customized layout:**

1. In the Print dialog box, select **Customize Layout** from the Layout drop-down list. You can also select an existing customized layout to modify it.

   ![Print dialog - Customize Layout](https://devnet.logianalytics.com/hc/article_attachments/4404936893463/prnt.gif)
2. Do the same as described in steps 4 to 8 of the above system layout procedure.
3. In the Design tab, customize the layout of the library components, then preview it in the View tab. For how to customize the layout, see [Exporting Using a Customized Layout](#Layout).
4. Select ![Print button](https://devnet.logianalytics.com/hc/article_attachments/4404936715543/btn_print.gif) on the toolbar to start printing. If Save as PDF or Save as HTML is selected in the Printer drop-down list, the result file of the library components is then opened in an associated program with which you can print the result to a printer.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009718942-Specifying-Parameter-Values-for-a-Dashboard)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009745121-Running-and-Editing-Reports-in-JDashboard)
